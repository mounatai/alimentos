#!/usr/bin/env python3
import base64
import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, cast
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
HISTORY_PATH = ROOT / 'history.json'
FOODS_PATH = ROOT / 'alimentos.json'
HOST = '0.0.0.0'
PORT = 3001

GITHUB_REPO = os.getenv('GITHUB_REPO', '').strip()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '').strip()
GITHUB_BRANCH = os.getenv('GITHUB_BRANCH', 'main').strip() or 'main'
GITHUB_HISTORY_PATH = os.getenv(
    'GITHUB_HISTORY_PATH', 'history.json').strip() or 'history.json'
GITHUB_FOODS_PATH = os.getenv(
    'GITHUB_FOODS_PATH', 'alimentos.json').strip() or 'alimentos.json'

MIME = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.ico': 'image/x-icon',
}

JsonList = List[Any]


def ensure_json_file(path: Path) -> None:
    if not path.exists():
        path.write_text('[]\n', encoding='utf-8')


def read_local_items(path: Path) -> JsonList:
    ensure_json_file(path)
    try:
        parsed = json.loads(path.read_text(encoding='utf-8'))
        return cast(JsonList, parsed) if isinstance(parsed, list) else []
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return []


def write_local_items(path: Path, items: JsonList) -> None:
    safe = items
    path.write_text(json.dumps(safe, ensure_ascii=False,
                    indent=2) + '\n', encoding='utf-8')


def github_enabled() -> bool:
    return bool(GITHUB_REPO)


def github_write_enabled() -> bool:
    return bool(GITHUB_REPO and GITHUB_TOKEN)


def github_headers() -> Dict[str, str]:
    headers = {
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'alimentos-server',
    }
    if GITHUB_TOKEN:
        headers['Authorization'] = f'Bearer {GITHUB_TOKEN}'
    return headers


def github_api_url(path_in_repo: str) -> str:
    encoded = quote(path_in_repo.strip('/'))
    return f'https://api.github.com/repos/{GITHUB_REPO}/contents/{encoded}'


def github_get_file(path_in_repo: str) -> Tuple[Optional[JsonList], str, Optional[str]]:
    if not github_enabled():
        return None, 'github-disabled', None
    url = f"{github_api_url(path_in_repo)}?ref={quote(GITHUB_BRANCH)}"
    req = Request(url, headers=github_headers(), method='GET')
    try:
        with urlopen(req, timeout=15) as res:
            payload = json.loads(res.read().decode('utf-8'))
            content = payload.get('content', '')
            decoded = base64.b64decode(content).decode(
                'utf-8') if content else '[]'
            parsed = json.loads(decoded or '[]')
            return (cast(JsonList, parsed) if isinstance(parsed, list) else []), '', payload.get('sha')
    except HTTPError as e:
        if e.code == 404:
            return None, 'github-file-not-found', None
        return None, f'github-http-{e.code}', None
    except URLError:
        return None, 'github-unreachable', None
    except (TypeError, ValueError, OSError, json.JSONDecodeError):
        return None, 'github-invalid-content', None


def github_put_file(path_in_repo: str, items: JsonList, message: str) -> Tuple[bool, str]:
    if not github_write_enabled():
        return False, 'github-write-disabled'

    _existing_items, err, sha = github_get_file(path_in_repo)
    if err and err not in ('github-file-not-found', ''):
        return False, err

    safe = items
    content = json.dumps(safe, ensure_ascii=False, indent=2) + '\n'
    payload = {
        'message': message,
        'content': base64.b64encode(content.encode('utf-8')).decode('ascii'),
        'branch': GITHUB_BRANCH,
    }
    if sha:
        payload['sha'] = sha

    body = json.dumps(payload).encode('utf-8')
    req = Request(
        github_api_url(path_in_repo),
        data=body,
        headers={**github_headers(), 'Content-Type': 'application/json'},
        method='PUT'
    )
    try:
        with urlopen(req, timeout=20) as res:
            if res.status in (200, 201):
                return True, ''
            return False, f'github-http-{res.status}'
    except HTTPError as e:
        return False, f'github-http-{e.code}'
    except URLError:
        return False, 'github-unreachable'
    except (TypeError, ValueError, OSError, json.JSONDecodeError):
        return False, 'github-write-failed'


def read_items(local_path: Path, repo_path: str) -> Tuple[JsonList, str, str]:
    cloud_items, err, _ = github_get_file(repo_path)
    if cloud_items is not None:
        # Keep local snapshot in sync when cloud is available.
        write_local_items(local_path, cloud_items)
        return cloud_items, 'github', ''
    return read_local_items(local_path), 'local', err


def write_items(local_path: Path, repo_path: str, items: JsonList, commit_message: str) -> Tuple[bool, str, str]:
    write_local_items(local_path, items)
    if not github_enabled():
        return True, 'local', 'github-disabled'

    ok, err = github_put_file(repo_path, items, commit_message)
    if ok:
        return True, 'github', ''
    return True, 'local', err


class Handler(BaseHTTPRequestHandler):
    def _set_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, PUT, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _send_json(self, status: int, payload: Dict[str, Any]) -> None:
        body = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self._set_cors()
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_file(self, path: str) -> None:
        if path == '/':
            path = '/index.html'

        candidate = (ROOT / unquote(path).lstrip('/')).resolve()
        if ROOT not in candidate.parents and candidate != ROOT:
            self.send_error(403, 'Forbidden')
            return

        if not candidate.exists() or not candidate.is_file():
            self.send_error(404, 'Not found')
            return

        data = candidate.read_bytes()
        ctype = MIME.get(candidate.suffix.lower(), 'application/octet-stream')
        self.send_response(200)
        self.send_header('Content-Type', ctype)
        self._set_cors()
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_json_payload(self) -> Tuple[Optional[Any], str]:
        try:
            length = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if length > 0 else b''
        try:
            return json.loads(raw.decode('utf-8') or '{}'), ''
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
            return None, 'Invalid JSON payload'

    def do_OPTIONS(self):
        self.send_response(204)
        self._set_cors()
        self.end_headers()

    def do_GET(self):
        pathname = urlparse(self.path).path
        if pathname == '/api/history':
            items, source, sync_error = read_items(
                HISTORY_PATH, GITHUB_HISTORY_PATH)
            return self._send_json(200, {
                'history': items,
                'updatedAt': datetime.now(timezone.utc).isoformat(),
                'source': source,
                'syncError': sync_error,
            })

        if pathname == '/api/foods':
            items, source, sync_error = read_items(
                FOODS_PATH, GITHUB_FOODS_PATH)
            return self._send_json(200, {
                'foods': items,
                'updatedAt': datetime.now(timezone.utc).isoformat(),
                'source': source,
                'syncError': sync_error,
            })

        return self._serve_file(pathname)

    def do_PUT(self):
        pathname = urlparse(self.path).path
        if pathname not in ('/api/history', '/api/foods'):
            return self._send_json(405, {'ok': False, 'error': 'Method not allowed'})

        parsed, err = self._read_json_payload()
        if err:
            return self._send_json(400, {'ok': False, 'error': err})
        data: Dict[str, Any] = cast(
            Dict[str, Any], parsed) if isinstance(parsed, dict) else {}

        if pathname == '/api/history':
            items_any: Any = cast(Any, parsed) if isinstance(
                parsed, list) else data.get('history', [])
            if not isinstance(items_any, list):
                return self._send_json(400, {'ok': False, 'error': 'history must be an array'})
            items: JsonList = cast(JsonList, items_any)
            ok, source, sync_error = write_items(
                HISTORY_PATH, GITHUB_HISTORY_PATH, items, 'Update history.json from alimentos app')
            return self._send_json(200, {
                'ok': ok,
                'count': len(items),
                'source': source,
                'syncError': sync_error,
            })

        items_any: Any = cast(Any, parsed) if isinstance(
            parsed, list) else data.get('foods', [])
        if not isinstance(items_any, list):
            return self._send_json(400, {'ok': False, 'error': 'foods must be an array'})
        items = cast(JsonList, items_any)
        ok, source, sync_error = write_items(
            FOODS_PATH, GITHUB_FOODS_PATH, items, 'Update alimentos.json from alimentos app')
        return self._send_json(200, {
            'ok': ok,
            'count': len(items),
            'source': source,
            'syncError': sync_error,
        })

    def do_POST(self):
        return self.do_PUT()


if __name__ == '__main__':
    ensure_json_file(HISTORY_PATH)
    ensure_json_file(FOODS_PATH)
    server = HTTPServer((HOST, PORT), Handler)
    print(f'Alimentos server running on http://localhost:{PORT}')
    print('GitHub repo sync enabled:' + (' yes' if github_enabled() else ' no'))
    if github_enabled() and not github_write_enabled():
        print('Warning: GITHUB_TOKEN not set. Reads may work, writes will stay local only.')
    server.serve_forever()
