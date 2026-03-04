#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
HISTORY_PATH = ROOT / 'history.json'
HOST = '0.0.0.0'
PORT = 3000

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


def ensure_history_file():
    if not HISTORY_PATH.exists():
        HISTORY_PATH.write_text('[]\n', encoding='utf-8')


def read_history():
    ensure_history_file()
    try:
        parsed = json.loads(HISTORY_PATH.read_text(encoding='utf-8'))
        return parsed if isinstance(parsed, list) else []
    except Exception:
        return []


def write_history(items):
    safe = items if isinstance(items, list) else []
    HISTORY_PATH.write_text(json.dumps(safe, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


class Handler(BaseHTTPRequestHandler):
    def _set_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self._set_cors()
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_file(self, path):
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

    def do_OPTIONS(self):
        self.send_response(204)
        self._set_cors()
        self.end_headers()

    def do_GET(self):
        pathname = urlparse(self.path).path
        if pathname == '/api/history':
            return self._send_json(200, {
                'history': read_history(),
                'updatedAt': datetime.now(timezone.utc).isoformat(),
            })

        return self._serve_file(pathname)

    def do_PUT(self):
        pathname = urlparse(self.path).path
        if pathname != '/api/history':
            return self._send_json(405, {'ok': False, 'error': 'Method not allowed'})

        try:
            length = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if length > 0 else b''

        try:
            parsed = json.loads(raw.decode('utf-8') or '{}')
        except Exception:
            return self._send_json(400, {'ok': False, 'error': 'Invalid JSON payload'})

        items = parsed if isinstance(parsed, list) else parsed.get('history', [])
        write_history(items)
        return self._send_json(200, {'ok': True, 'count': len(items) if isinstance(items, list) else 0})

    def do_POST(self):
        return self.do_PUT()


if __name__ == '__main__':
    ensure_history_file()
    server = HTTPServer((HOST, PORT), Handler)
    print(f'Alimentos server running on http://localhost:{PORT}')
    server.serve_forever()
