# Contexto de trabajo

## Última actualización
- Fecha: 2026-03-04
- Archivo base capturado: `index.html`

## Conversación
1. Usuario: "crea un file donde guardes todo el contexto de nuestra conversacion y el index que tengo guardado ahora, y lo vas actualizando con todos los cambios"
2. Acción: Se creó `CONTEXTO_CONVERSACION.md` para centralizar contexto y snapshot del `index.html`.
3. Usuario: "quiero que toda la pagina tenga un diseno mas bbonito y colores verdes, manteniendo la estructura y las formulas etc, solo hacer un cambio mas elegante y pro en el diseno"
4. Acción: Se aplicó rediseño visual profesional en gama verde, sin modificar estructura ni fórmulas/lógica.
5. Usuario: "en el grafico diario lla linea de objetivo Kcal tiene que ser azul, los titulos de las etiquetas no tienen que ser en negrita, en letra simple mas delgada, lo msimo con los totales, los encabezados de las tablas letra mas pequena"
6. Acción: Se ajustó la línea de objetivo kcal a azul, se redujo el peso tipográfico de etiquetas y totales, y se disminuyó el tamaño de encabezados de tabla.
7. Usuario: "no hace falta displayar eso en las etiquetas de las comidas: Alimentos cargados: 25, las letras de los totales del mismo tamano que el encabezado, el encabezado ahora puede estar en negrita, no displayes esto tampooc: Nota: valores \"por 100g\"."
8. Acción: Se ocultó el estado de alimentos cargados, se eliminaron las notas "por 100g", se igualó tamaño tipográfico de totales con encabezado de comidas y se dejó encabezado en negrita.
9. Usuario: "cuando te pida cambios lee del contexto no hace falta que revises todo el codigo siempre, a menos que te lo pida"
10. Acción: Se acordó partir del contexto y evitar revisar todo el código salvo necesidad puntual.
11. Usuario: "los titulos resumen diario, desayuno, comida snacks y cena, letras mas delgaditas, ahora estan muy gordas. el historial, quiero que lo gusardes de alguna manera con la finalidad de que si accedo a la web desdel telefono tenga acceso a ello tambien"
12. Acción: Se bajó el grosor de títulos `h2` de tarjetas y se agregó sincronización compartible por URL (`?sync=...`) para abrir la misma URL en teléfono y cargar/subir historial en la nube.
13. Usuario: "quiero que cortes el grafico diario y lo posiciones en la pestana de historial... y añadir 3 círculos tipo actividad"
14. Acción: Se movió el gráfico diario al tab Historial en columna derecha, se dejó listado de registros a la izquierda en la misma fila, y en Tracker se añadieron 3 anillos concéntricos de progreso (proteínas, carbs, grasas) pintados proporcionalmente según gramos consumidos vs gramos ideales.
15. Usuario: "quiero que el color del circulo de las proteinas sea rojo, el de las carbs verde"
16. Acción: Se cambió color del anillo de proteínas a rojo y del anillo de carbs a verde (anillo y leyenda).
17. Usuario: "la etiqueta del anillo tiene que tener el mismo tamano que la etiqueta de resumen diario, y los colores de los anillos mas pastel"
18. Acción: Se igualó el tamaño de etiquetas del bloque de anillos al tamaño de etiquetas de resumen diario y se cambiaron los colores de anillos/leyenda a tonos pastel.
19. Usuario: "la etiqueta de los circulos debe tener el mismo tamano que la etiqueta de resumen diario, puedes reducir el tamano de los circulos con tal de encajar la etiqueta"
20. Acción: Se redujo el tamaño visual del bloque de círculos y se alineó el texto de etiquetas/valores de leyenda al mismo tamaño y peso de las etiquetas de resumen diario.

## Cambios de diseño y comportamiento (estado actual)
- Paleta y diseño general en verde elegante.
- Línea de `Objetivo kcal` en azul en leyenda y canvas.
- Etiquetas en peso de fuente más fino (sin negrita marcada).
- Totales de tablas de comidas con tamaño igual al encabezado.
- Encabezados en negrita y tamaño reducido.
- Estado `Alimentos cargados: N` oculto en tarjetas de comidas.
- Eliminadas las notas `Nota: valores "por 100g"` en las cuatro comidas.
- Títulos de tarjetas (`Resumen diario`, `Desayuno`, `Comida`, `Merienda/Snacks`, `Cena`) con trazo más delgado.
- Historial con soporte de enlace compartible por URL usando parámetro `sync`.
- Gráfico diario movido a pestaña `Historial` en panel derecho con registros a la izquierda.
- Panel de anillos en `Tracker` (3 círculos concéntricos):
  - Proteínas: pastel rojo.
  - Carbs: pastel verde.
  - Grasas: pastel naranja.
  - Progreso proporcional a `consumido / ideal` con tope 100%.
- Etiquetas del bloque de anillos ajustadas al mismo tamaño que etiquetas de resumen diario.
- Tamaño de círculos reducido para mejorar encaje visual con etiquetas.
- Sin cambios en la lógica de cálculo de macros/fórmulas.


## Último ajuste
- Usuario: "la pestana de anillos diarios de macros debe ser mas pequena"
- Acción: se redujo el tamaño visual de la tarjeta de anillos (`.rings-slot`) y del bloque interno de círculos (`.rings-wrap`) para que el panel se vea más compacto.


## Último ajuste
- Usuario: "quiero que sea igual de ancha que la pestana comida e igual de larga de resumen diario"
- Acción: se hizo la tarjeta de anillos de ancho completo dentro de su columna (igual a cards de comidas en ancho de panel) y se configuró `tracker-top` para estirar alturas, de modo que quede alineada en alto con "Resumen diario".


## Último ajuste
- Usuario: "ahora vamos a solucionar el historial... no quiero tener el link o la URL para verlo desdel telefono"
- Acción: se eliminó la UI manual de sincronización (input + botones + manejo de URL en interfaz) y se dejó sincronización automática interna para historial al guardar/cargar.
- Nota técnica: la sincronización automática usa un endpoint fijo configurado en código (`HISTORY_SYNC_AUTO_URL`).


## Último ajuste
- Usuario: "si accedo a la pagina desde incognito no veo el historial"
- Acción: se añadió sincronización automática de arranque para historial (`syncHistoryAcrossDevices`) que:
  - descarga historial de nube,
  - hace merge con historial local,
  - guarda el resultado localmente,
  - y vuelve a subirlo para mantener ambos entornos alineados.
- Objetivo: que el historial aparezca también en sesiones incógnito/dispositivos al iniciar.


## Último ajuste
- Usuario: "esto es lo que veo en la pantalla de incognito: No hay datos guardados aún"
- Acción: se corrigió el endpoint fijo de sincronización automática de historial a un identificador compatible para acceso compartido sin UI manual.
- Nota de migración: para subir el historial antiguo al endpoint compartido, hace falta abrir una vez la sesión normal (donde ya tienes datos) para que se haga el push automático inicial.


## Último ajuste
- Usuario: "me sale no hay datos guardados aun y Sin datos guardados para graficar"
- Acción: se forzó el uso de un único endpoint fijo de historial para todas las sesiones (normal/incógnito/dispositivos), ignorando URLs antiguas guardadas localmente que podían desalinear la fuente de datos.
- Resultado esperado: ambos modos consultan/suben al mismo origen de historial.


## Último ajuste
- Usuario: "sigue sin aparecer nada"
- Acción: se cambió la estrategia de sincronización de historial a backend propio del proyecto:
  - Frontend ahora usa `HISTORY_API_URL = '/api/history'`.
  - Se eliminaron dependencias de sincronización externa por URL manual.
  - Se añadió servidor API local con persistencia en archivo `history.json`.
- Archivos añadidos:
  - `server.py` (API + estáticos, recomendado)
  - `server.js` (alternativa Node)
  - `history.json` (almacenamiento compartido del historial)
- Requisito operativo: abrir la app desde el servidor (`http://localhost:3000`) para que el historial se comparta entre sesiones/dispositivos.


## Último ajuste
- Usuario: "tan pronto como reinicio el incognito pantalla pierdo el historial" / "sigue sin aparecer".
- Acción: se reforzó el flujo de persistencia y sync:
  - `saveDailyData` ahora espera (`await`) a que termine la subida antes de confirmar guardado.
  - `deleteHistoryItem` también espera sincronización.
  - Se añadió indicador visible de estado en Historial (`#historySyncNote`) con mensajes de sincronización/errores.
  - `syncHistoryAcrossDevices` ahora reporta estado y errores de conexión.
- Objetivo: evitar cierres rápidos de incógnito antes de completar upload y facilitar diagnóstico en pantalla.


## Último ajuste
- Usuario: "Datos guardados localmente..., pero falló la sincronización"
- Acción:
  - Se mejoraron mensajes de error de sync con detalle HTTP.
  - `HISTORY_API_URL` ahora detecta `file://` y usa `http://localhost:3000/api/history`.
  - Se habilitó CORS en `server.py` y `server.js` (GET/PUT/OPTIONS) para permitir sync desde `file://` y otros orígenes locales.
- Resultado esperado: guardado/sync funcional entre sesión normal e incógnito siempre que el servidor local esté ejecutándose.


## Último ajuste
- Usuario: "No se pudo subir el historial al servidor"
- Acción: se añadió diagnóstico detallado de error de sincronización en pantalla y mensajes contextualizados.
  - Nuevo formateo de error (`formatHistorySyncError`) que indica explícitamente cuando no hay conexión al servidor y sugiere `python3 server.py`.
  - El estado de historial ahora muestra la causa concreta (no solo mensaje genérico).

## Snapshot actual de index.html
```html
<!doctype html>
<html lang="es">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Tracker de alimentos y macros</title>
    <style>
        :root {
            --olive: #4d9b62;
            --cream: #f2f8f1;
            --dark: #183225;
            --gold: #2f7d4e;
            --panel: #ffffff;
            --panel2: #f4fbf5;
            --line: rgba(24, 50, 37, .16);
            --text: var(--dark);
            --muted: rgba(24, 50, 37, .68);
            --shadow: 0 14px 30px rgba(23, 56, 40, .14);
            --base-fz: .92em;
            --mini-fz: .86em;
            --dropdown-scale: .92;
            --head-fz: 1.08em;
            --kv-gap: 10px;
            --kv-width: 130px;
        }

        html {
            font-size: 16px
        }

        body {
            margin: 0;
            font-family: "Avenir Next", "Segoe UI", "Trebuchet MS", Arial, sans-serif;
            background:
                radial-gradient(900px 480px at 15% 0%, rgba(77, 155, 98, .22) 0%, transparent 55%),
                radial-gradient(1000px 520px at 85% 0%, rgba(47, 125, 78, .15) 0%, transparent 58%),
                var(--cream);
            color: var(--text);
            font-size: var(--base-fz);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 16px
        }

        h2 {
            margin: 14px 0 8px;
            font-size: var(--head-fz)
        }

        .tabs-header {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--line);
            background: rgba(255, 255, 255, .65);
            border-radius: 14px;
            padding: 6px 10px 0;
            backdrop-filter: blur(2px);
        }

        .tab-button {
            background: transparent;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            font-size: 1em;
            font-weight: 700;
            color: var(--muted);
            border-bottom: 3px solid transparent;
            transition: color .15s, border-color .15s, background .15s;
            margin-bottom: -2px;
            border-radius: 10px 10px 0 0;
        }

        .tab-button.active {
            color: var(--gold);
            border-bottom-color: var(--gold);
        }

        .tab-button:hover {
            color: var(--dark);
            background: rgba(47, 125, 78, .08);
        }

        .tab-content {
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .top {
            display: flex;
            justify-content: center;
            gap: 12px;
            align-items: stretch;
            flex-wrap: wrap
        }

        .card {
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel2) 100%);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 16px;
            min-width: 280px;
            flex: 1 1 360px;
            box-shadow: var(--shadow);
        }

        .card h2 {
            margin: 0 0 10px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 500
        }

        .foodicon {
            font-size: 1.1em;
            margin-right: 6px
        }

        .grid2 {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: var(--kv-gap);
            align-items: start
        }

        .grid3 {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: var(--kv-gap);
            align-items: start
        }

        .kv {
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 10px;
            background: rgba(77, 155, 98, .08);
            font-size: var(--mini-fz);
            width: var(--kv-width);
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            margin: 0;
        }

        .kv input,
        .kv select {
            width: 100%;
            padding: 8px 10px;
            border-radius: 10px;
            border: 1px solid rgba(24, 50, 37, .18);
            background: #fff;
            color: var(--text);
            outline: none;
            font-size: .98em;
            box-sizing: border-box;
            min-height: 36px;
        }

        .kv input[type="number"]::-webkit-outer-spin-button,
        .kv input[type="number"]::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }

        .kv input[type="number"] {
            -moz-appearance: textfield;
        }

        .kv input:focus,
        .kv select:focus {
            border-color: rgba(47, 125, 78, .85);
            box-shadow: 0 0 0 3px rgba(47, 125, 78, .14);
        }

        .kv label {
            color: var(--muted);
            font-size: .72em;
            margin: 0;
            line-height: 1.05;
            text-align: center;
            font-weight: 500;
            padding: 0 4px;
            width: 100%;
            box-sizing: border-box
        }

        .row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center
        }

        .muted {
            color: var(--muted)
        }

        .small {
            font-size: .95em
        }

        .summary-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 7.2px;
            border-radius: 14px;
            min-width: 108px;
            background: linear-gradient(180deg, #fff 0%, rgba(47, 125, 78, .14) 100%);
            border: 1px solid var(--line);
            box-shadow: var(--shadow);
        }

        .summary-box .value {
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 4px;
            color: var(--dark)
        }

        .summary-box label {
            font-size: .63em;
            color: var(--muted);
            font-weight: 500;
            margin: 0;
            text-align: center
        }

        .summary-box.deficit .value {
            color: #d00;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            border: 1px solid var(--line);
            border-radius: 12px;
            overflow: hidden;
            background: #fff;
            font-size: .97em;
        }

        th,
        td {
            padding: 9px 10px;
            border-bottom: 1px solid var(--line);
            font-size: inherit
        }

        th {
            text-align: left;
            color: rgba(24, 50, 37, .8);
            background: rgba(77, 155, 98, .12);
            font-weight: 700;
            font-size: .68em;
            text-transform: uppercase;
            letter-spacing: .03em;
        }

        .card[data-meal] th {
            font-size: .64em;
        }

        table tbody tr:hover {
            background: rgba(77, 155, 98, .08)
        }

        tr:last-child td {
            border-bottom: none
        }

        .right {
            text-align: right
        }

        .totals td {
            font-weight: 600;
            font-size: .64em;
            background: rgba(47, 125, 78, .12)
        }

        .actions {
            display: flex;
            gap: 8px;
            align-items: center;
            justify-content: space-between;
            margin: 0 0 6px;
            flex-wrap: wrap;
        }

        .actions h2 {
            margin: 0;
        }

        .food-controls {
            display: flex;
            gap: 8px;
            align-items: center;
        }

        button {
            border: none;
            background: linear-gradient(180deg, #fff 0%, rgba(47, 125, 78, .14) 100%);
            color: var(--dark);
            padding: 8px 10px;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 800;
            font-size: 1.02em;
            line-height: 1;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: background .15s, transform .06s, box-shadow .15s;
            box-shadow: 0 1px 0 rgba(24, 50, 37, .12), 0 4px 12px rgba(47, 125, 78, .12);
        }

        button:active {
            transform: translateY(1px)
        }

        button:focus {
            outline: 2px solid rgba(47, 125, 78, .22)
        }

        .btn-add {
            font-size: 1.12em;
            min-width: 36px;
            height: 36px;
            width: 36px;
            padding: 0;
            background: var(--gold);
            color: #fff;
            font-weight: 900;
            border: 1px solid rgba(47, 125, 78, .4);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .btn-add:hover {
            background: #26673f
        }

        .btn-del {
            background: transparent;
            color: #a00;
            border: none;
            font-size: 0.525em;
            padding: 0 3px;
            height: 14px;
            width: 14px;
            border-radius: 4px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .btn-del:hover {
            background: rgba(47, 125, 78, .14);
            color: #d00
        }

        .btn-save {
            font-size: 1.2em;
            background: transparent;
            color: var(--gold);
            padding: 6px;
            height: 32px;
            width: 32px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-left: 4px;
            transition: background .15s;
        }

        .btn-save:hover {
            background: rgba(47, 125, 78, .16);
            color: #26673f;
        }

        select.foodSelect {
            font-size: 95%;
            transform: scale(var(--dropdown-scale));
            min-width: 110px;
            width: 180px;
            max-width: 240px;
            padding-left: 10px;
            padding-right: 8px;
            border-radius: 10px;
            border: 1px solid rgba(47, 125, 78, .26);
            background: #fff;
            min-height: 36px;
        }

        .status {
            margin-top: 6px;
            color: var(--muted);
            font-size: .95em
        }

        .foodsStatus {
            display: none;
        }

        .meals {
            margin-top: 12px;
            display: grid;
            gap: 12px
        }

        @media(min-width:880px) {
            .meals {
                grid-template-columns: 1fr 1fr
            }
        }

        .tracker-top {
            display: grid;
            gap: 12px;
            margin-bottom: 12px;
        }

        .graph-slot {
            min-height: 120px;
            border: 1px dashed var(--line);
            color: var(--muted);
            font-weight: 700;
            padding: 12px;
            box-sizing: border-box;
        }

        .graph-slot h3 {
            margin: 0 0 8px;
            font-size: .95em;
            color: var(--dark);
        }

        .chart-wrap {
            position: relative;
            width: 100%;
            height: 220px;
        }

        #historyChart {
            width: 100%;
            height: 100%;
            display: block;
        }

        .chart-empty {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--muted);
            font-size: .9em;
            text-align: center;
        }

        .chart-legend {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 10px;
            font-size: .82em;
            color: var(--muted);
        }

        .chart-legend span {
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .chart-legend i {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            display: inline-block;
        }

        @media(min-width:880px) {
            .tracker-top {
                grid-template-columns: 1fr 1fr;
                align-items: stretch;
            }
        }

        .rings-slot h3 {
            margin: 0 0 10px;
            font-size: .95em;
            color: var(--dark);
            font-weight: 600;
        }

        .rings-slot {
            width: 100%;
            max-width: none;
            padding: 12px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }

        .rings-wrap {
            position: relative;
            width: min(250px, 100%);
            margin: 0 auto;
            aspect-ratio: 1;
        }

        .activity-rings {
            width: 100%;
            height: 100%;
            display: block;
        }

        .ring-track {
            fill: none;
            stroke: rgba(24, 50, 37, .13);
        }

        .ring-progress {
            fill: none;
            transform-origin: 50% 50%;
            transform: rotate(-90deg);
            stroke-linecap: round;
            transition: stroke-dashoffset .35s ease;
        }

        .ring-prot {
            stroke: #ef9a9a;
        }

        .ring-carb {
            stroke: #a5d6a7;
        }

        .ring-fat {
            stroke: #ffcc80;
        }

        .rings-center {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            pointer-events: none;
        }

        .rings-center-value {
            font-size: 1.9em;
            color: var(--dark);
            font-weight: 700;
            line-height: 1;
        }

        .rings-center-label {
            margin-top: 4px;
            font-size: .63em;
            color: var(--muted);
            font-weight: 500;
        }

        .rings-legend {
            margin-top: 10px;
            display: grid;
            gap: 6px;
            font-size: .63em;
            color: var(--muted);
        }

        .rings-legend span {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }

        .rings-legend i {
            width: 9px;
            height: 9px;
            border-radius: 999px;
            display: inline-block;
            margin-right: 6px;
            flex-shrink: 0;
        }

        .rings-legend b {
            color: var(--muted);
            font-size: inherit;
            font-weight: 500;
        }

        .card[data-meal] {
            position: relative
        }

        .card[data-meal]::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            width: 5px;
            height: 100%;
            background: var(--olive);
            border-radius: 14px 0 0 14px;
            opacity: .22;
        }

        .mealBody input[type="number"] {
            width: 100px;
            max-width: 100%;
            border-radius: 8px;
            border: 1px solid rgba(24, 50, 37, .24);
            padding: 6px 8px;
            font-size: 98%;
            min-height: 34px;
        }

        .mealBody input[type="number"]::-webkit-outer-spin-button,
        .mealBody input[type="number"]::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }

        .mealBody input[type="number"] {
            -moz-appearance: textfield;
        }

        .mealBody input[type="number"]:focus {
            border-color: rgba(47, 125, 78, .85);
            box-shadow: 0 0 0 3px rgba(47, 125, 78, .14);
            outline: none;
        }

        .history-container {
            margin-top: 20px;
        }

        .history-main {
            display: grid;
            gap: 12px;
            align-items: start;
        }

        .history-graph {
            min-height: 100%;
        }

        @media(min-width:980px) {
            .history-main {
                grid-template-columns: 1.2fr .8fr;
            }
        }

        .history-sync {
            margin-bottom: 12px;
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 12px;
            background: #fff;
        }

        .history-sync-title {
            margin: 0 0 8px;
            font-size: .95em;
            color: var(--dark);
            font-weight: 800;
        }

        .history-sync-row {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            align-items: center;
        }

        .history-sync-row input {
            flex: 1;
            min-width: 240px;
            padding: 8px 10px;
            border-radius: 8px;
            border: 1px solid var(--line);
            font-size: .92em;
            box-sizing: border-box;
        }

        .history-sync-actions {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        .history-sync-note {
            margin: 8px 0 0;
            color: var(--muted);
            font-size: .85em;
        }

        .history-list {
            max-height: 500px;
            overflow-y: auto;
            border: 1px solid var(--line);
            border-radius: 12px;
            background: #fff;
        }

        .history-item {
            padding: 14px 16px;
            border-bottom: 1px solid var(--line);
            cursor: pointer;
            transition: background .15s;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .history-item:last-child {
            border-bottom: none;
        }

        .history-item:hover {
            background: rgba(77, 155, 98, .08);
        }

        .history-item-info {
            flex: 1;
        }

        .history-item-date {
            font-weight: 800;
            color: var(--dark);
            font-size: 1em;
        }

        .history-item-time {
            font-size: .9em;
            color: var(--muted);
            margin-top: 2px;
        }

        .history-item-stats {
            font-size: .85em;
            color: var(--muted);
            margin-top: 4px;
        }

        .history-item-actions {
            display: flex;
            gap: 8px;
            margin-left: 12px;
        }

        .btn-view {
            background: transparent;
            color: var(--gold);
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-size: .9em;
            font-weight: 700;
            transition: background .15s;
        }

        .btn-view:hover {
            background: rgba(47, 125, 78, .16);
        }

        .btn-delete {
            background: transparent;
            color: #a00;
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-size: .9em;
            font-weight: 700;
            transition: background .15s;
        }

        .btn-delete:hover {
            background: rgba(47, 125, 78, .14);
            color: #d00;
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            animation: fadeIn .2s;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }

        .modal-content {
            background-color: var(--cream);
            margin: 10% auto;
            padding: 20px;
            border: 1px solid var(--line);
            border-radius: 14px;
            max-width: 700px;
            max-height: 80vh;
            overflow-y: auto;
            box-shadow: var(--shadow);
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding-bottom: 12px;
            border-bottom: 1px solid var(--line);
        }

        .modal-header h3 {
            margin: 0;
            font-size: 1.2em;
        }

        .close-modal {
            background: transparent;
            border: none;
            font-size: 1.5em;
            color: var(--muted);
            cursor: pointer;
            width: 32px;
            height: 32px;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .close-modal:hover {
            color: var(--dark);
        }

        .empty-state {
            padding: 40px 20px;
            text-align: center;
            color: var(--muted);
        }

        .empty-state-icon {
            font-size: 3em;
            margin-bottom: 12px;
        }

        .db-header {
            display: flex;
            gap: 12px;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .db-search {
            flex: 1;
            min-width: 200px;
        }

        .db-search input {
            width: 100%;
            padding: 10px 12px;
            border-radius: 10px;
            border: 1px solid var(--line);
            font-size: 1em;
            box-sizing: border-box;
        }

        .db-search input:focus {
            border-color: rgba(47, 125, 78, .85);
            box-shadow: 0 0 0 3px rgba(47, 125, 78, .14);
            outline: none;
        }

        .food-list {
            max-height: 600px;
            overflow-y: auto;
            border: 1px solid var(--line);
            border-radius: 12px;
            background: #fff;
        }

        .food-item {
            padding: 14px 16px;
            border-bottom: 1px solid var(--line);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .food-item:last-child {
            border-bottom: none;
        }

        .food-item:hover {
            background: rgba(77, 155, 98, .08);
        }

        .food-item-info {
            flex: 1;
        }

        .food-item-name {
            font-weight: 800;
            color: var(--dark);
            margin-bottom: 6px;
        }

        .food-item-macros {
            font-size: .9em;
            color: var(--muted);
        }

        .food-item-actions {
            display: flex;
            gap: 8px;
            margin-left: 12px;
        }

        .btn-edit {
            background: transparent;
            color: var(--gold);
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-size: .9em;
            font-weight: 700;
            transition: background .15s;
        }

        .btn-edit:hover {
            background: rgba(47, 125, 78, .16);
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            margin-bottom: 12px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        .form-group label {
            font-size: .9em;
            font-weight: 500;
            color: var(--muted);
            margin-bottom: 6px;
        }

        .form-group input {
            padding: 10px 12px;
            border-radius: 10px;
            border: 1px solid var(--line);
            font-size: 1em;
            box-sizing: border-box;
        }

        .form-group input:focus {
            border-color: rgba(47, 125, 78, .85);
            box-shadow: 0 0 0 3px rgba(47, 125, 78, .14);
            outline: none;
        }

        .form-actions {
            display: flex;
            gap: 12px;
            margin-top: 16px;
        }

        .btn-primary {
            background: var(--gold);
            color: #fff;
            padding: 10px 16px;
            border-radius: 10px;
            border: none;
            font-weight: 700;
            cursor: pointer;
            flex: 1;
        }

        .btn-primary:hover {
            background: #26673f;
        }

        .btn-secondary {
            background: transparent;
            color: var(--muted);
            padding: 10px 16px;
            border-radius: 10px;
            border: 1px solid var(--line);
            font-weight: 700;
            cursor: pointer;
            flex: 1;
        }

        .btn-secondary:hover {
            background: rgba(77, 155, 98, .12);
            color: var(--dark);
        }

        #foodFormSection {
            order: -1;
            margin: 0 0 20px 0 !important;
        }

        .db-container {
            display: flex;
            flex-direction: column;
        }

        .config-footer {
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: center;
            margin-top: 16px;
        }

        .summary-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }

        @media (max-width:600px) {
            .top {
                flex-direction: column
            }

            .kv {
                width: 100%
            }

            .grid2 {
                grid-template-columns: 1fr
            }

            .grid3 {
                grid-template-columns: 1fr
            }

            select.foodSelect {
                width: 100%;
                transform: none
            }

            .summary-box {
                min-width: 100%
            }

            .food-item {
                flex-direction: column;
                align-items: flex-start;
            }

            .food-item-actions {
                margin-left: 0;
                margin-top: 12px;
                width: 100%;
            }

            .form-grid {
                grid-template-columns: 1fr;
            }

            .db-header {
                flex-direction: column;
            }

            .db-search {
                min-width: 100%;
            }
        }

        .card .grid2+.grid2 {
            margin-top: 8px
        }

        .card .grid3 {
            grid-template-columns: repeat(3, 1fr);
        }

        .card .kv {
            width: 100%;
            gap: 4px;
        }

        .card .kv label {
            font-size: .72em;
            font-weight: 500;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="tabs-header">
            <button class="tab-button active" data-tab="tracker">📊 Tracker</button>
            <button class="tab-button" data-tab="history">📋 </button>
            <button class="tab-button" data-tab="settings">⚙️ </button>
            <button class="tab-button" data-tab="database">🗄️ </button>
        </div>

        <div id="tracker" class="tab-content active">
            <div class="tracker-top">
                <section class="card" aria-label="Resumen diario">
                    <h2>📊 Resumen diario</h2>
                    <div style="height:10px"></div>
                    <table aria-label="Tabla resumen diario">
                        <thead>
                            <tr>
                                <th>Macro</th>
                                <th class="right">Consumido (g)</th>
                                <th class="right">Ideal (g)</th>
                                <th class="right">% del ideal</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Proteínas</td>
                                <td class="right" id="sumProtG">0</td>
                                <td class="right" id="idealProtVal">130</td>
                                <td class="right" id="sumProtPct">0%</td>
                            </tr>
                            <tr>
                                <td>Carbohidratos</td>
                                <td class="right" id="sumCarbG">0</td>
                                <td class="right" id="idealCarbVal">170</td>
                                <td class="right" id="sumCarbPct">0%</td>
                            </tr>
                            <tr>
                                <td>Grasas</td>
                                <td class="right" id="sumFatG">0</td>
                                <td class="right" id="idealFatVal">50</td>
                                <td class="right" id="sumFatPct">0%</td>
                            </tr>
                        </tbody>
                    </table>
                    <div style="height:10px"></div>
                    <div class="summary-row">
                        <div class="summary-box">
                            <div class="value" id="sumKcal">0</div><label>Total kcal consumidas</label>
                        </div>
                        <div class="summary-box deficit">
                            <div class="value" id="deficitTracker">0</div><label>Déficit real</label>
                        </div>
                        <div class="summary-box">
                            <div class="value" id="objKcalLabel">0</div><label>Objetivo kcal</label>
                        </div>
                    </div>
                    <div class="config-footer">
                        <button type="button" class="btn-save" id="btnSave" title="Guardar datos del día">💾</button>
                    </div>
                </section>
                <section class="card rings-slot" aria-label="Progreso diario de macros">
                    <h3>Anillos diarios de macros</h3>
                    <div class="rings-wrap">
                        <svg class="activity-rings" viewBox="0 0 220 220" aria-label="Progreso de proteínas, carbs y grasas">
                            <circle class="ring-track" cx="110" cy="110" r="84" stroke-width="16"></circle>
                            <circle class="ring-track" cx="110" cy="110" r="64" stroke-width="16"></circle>
                            <circle class="ring-track" cx="110" cy="110" r="44" stroke-width="16"></circle>

                            <circle id="ringProt" class="ring-progress ring-prot" cx="110" cy="110" r="84" stroke-width="16"></circle>
                            <circle id="ringCarb" class="ring-progress ring-carb" cx="110" cy="110" r="64" stroke-width="16"></circle>
                            <circle id="ringFat" class="ring-progress ring-fat" cx="110" cy="110" r="44" stroke-width="16"></circle>
                        </svg>
                        <div class="rings-center">
                            <div id="ringsCenterValue" class="rings-center-value">0%</div>
                            <div class="rings-center-label">Objetivo medio</div>
                        </div>
                    </div>
                    <div class="rings-legend">
                        <span><span><i style="background:#ef9a9a;"></i>Proteínas</span><b id="ringProtText">0 / 130g</b></span>
                        <span><span><i style="background:#a5d6a7;"></i>Carbs</span><b id="ringCarbText">0 / 170g</b></span>
                        <span><span><i style="background:#ffcc80;"></i>Grasas</span><b id="ringFatText">0 / 50g</b></span>
                    </div>
                </section>
            </div>

            <div class="meals">
                <section class="card" data-meal="desayuno">
                    <div class="actions">
                        <h2><span class="foodicon">☕️</span>Desayuno</h2>
                        <div class="food-controls"><select class="foodSelect"></select><button type="button"
                                class="btn-add" title="Añadir alimento">+</button></div>
                    </div>
                    <div class="status foodsStatus">Cargando alimentos...</div>
                    <table style="margin-top:10px">
                        <thead>
                            <tr>
                                <th style="width:28%">Alimento</th>
                                <th class="right">Cal (kcal)</th>
                                <th class="right">Grasas (g)</th>
                                <th class="right">Carbs (g)</th>
                                <th class="right">Prot (g)</th>
                                <th class="right">Gr</th>
                            </tr>
                        </thead>
                        <tbody class="mealBody"></tbody>
                        <tbody class="totals">
                            <tr>
                                <td>Totales</td>
                                <td class="right totalKcal">0</td>
                                <td class="right totalFat">0</td>
                                <td class="right totalCarb">0</td>
                                <td class="right totalProt">0</td>
                                <td class="right totalGr">0</td>
                            </tr>
                        </tbody>
                    </table>
                </section>

                <section class="card" data-meal="comida">
                    <div class="actions">
                        <h2><span class="foodicon">🍽️</span>Comida</h2>
                        <div class="food-controls"><select class="foodSelect"></select><button type="button"
                                class="btn-add" title="Añadir alimento">+</button></div>
                    </div>
                    <div class="status foodsStatus">Cargando alimentos...</div>
                    <table style="margin-top:10px">
                        <thead>
                            <tr>
                                <th style="width:28%">Alimento</th>
                                <th class="right">Cal (kcal)</th>
                                <th class="right">Grasas (g)</th>
                                <th class="right">Carbs (g)</th>
                                <th class="right">Prot (g)</th>
                                <th class="right">Gr</th>
                            </tr>
                        </thead>
                        <tbody class="mealBody"></tbody>
                        <tbody class="totals">
                            <tr>
                                <td>Totales</td>
                                <td class="right totalKcal">0</td>
                                <td class="right totalFat">0</td>
                                <td class="right totalCarb">0</td>
                                <td class="right totalProt">0</td>
                                <td class="right totalGr">0</td>
                            </tr>
                        </tbody>
                    </table>
                </section>

                <section class="card" data-meal="merienda">
                    <div class="actions">
                        <h2><span class="foodicon">🍪</span>Merienda</h2>
                        <div class="food-controls"><select class="foodSelect"></select><button type="button"
                                class="btn-add" title="Añadir alimento">+</button></div>
                    </div>
                    <div class="status foodsStatus">Cargando alimentos...</div>
                    <table style="margin-top:10px">
                        <thead>
                            <tr>
                                <th style="width:28%">Alimento</th>
                                <th class="right">Cal (kcal)</th>
                                <th class="right">Grasas (g)</th>
                                <th class="right">Carbs (g)</th>
                                <th class="right">Prot (g)</th>
                                <th class="right">Gr</th>
                            </tr>
                        </thead>
                        <tbody class="mealBody"></tbody>
                        <tbody class="totals">
                            <tr>
                                <td>Totales</td>
                                <td class="right totalKcal">0</td>
                                <td class="right totalFat">0</td>
                                <td class="right totalCarb">0</td>
                                <td class="right totalProt">0</td>
                                <td class="right totalGr">0</td>
                            </tr>
                        </tbody>
                    </table>
                </section>

                <section class="card" data-meal="cena">
                    <div class="actions">
                        <h2><span class="foodicon">🌙</span>Cena</h2>
                        <div class="food-controls"><select class="foodSelect"></select><button type="button"
                                class="btn-add" title="Añadir alimento">+</button></div>
                    </div>
                    <div class="status foodsStatus">Cargando alimentos...</div>
                    <table style="margin-top:10px">
                        <thead>
                            <tr>
                                <th style="width:28%">Alimento</th>
                                <th class="right">Cal (kcal)</th>
                                <th class="right">Grasas (g)</th>
                                <th class="right">Carbs (g)</th>
                                <th class="right">Prot (g)</th>
                                <th class="right">Gr</th>
                            </tr>
                        </thead>
                        <tbody class="mealBody"></tbody>
                        <tbody class="totals">
                            <tr>
                                <td>Totales</td>
                                <td class="right totalKcal">0</td>
                                <td class="right totalFat">0</td>
                                <td class="right totalCarb">0</td>
                                <td class="right totalProt">0</td>
                                <td class="right totalGr">0</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </div>

        </div>

        <div id="history" class="tab-content">
            <section class="card history-container">
                <h2>📋 Historial de guardados</h2>
                <div class="history-sync">
                    <p class="history-sync-title">☁️ Sincronización automática (móvil + ordenador)</p>
                    <p class="history-sync-note" id="historySyncNote">El historial se sincroniza automáticamente sin usar campo de enlace ni
                        botones manuales.</p>
                </div>
                <div class="history-main">
                    <div class="history-list" id="historyList">
                        <div class="empty-state">
                            <div class="empty-state-icon">📭</div>
                            <p>No hay datos guardados aún</p>
                        </div>
                    </div>
                    <section class="graph-slot history-graph" aria-label="Gráfico de historial">
                        <h3>Gráfico diario (kcal)</h3>
                        <div class="chart-wrap">
                            <canvas id="historyChart" aria-label="Gráfico de kcal por día"></canvas>
                            <div class="chart-empty" id="chartEmpty">Sin datos guardados para graficar</div>
                        </div>
                        <div class="chart-legend">
                            <span><i style="background:#1e88e5;"></i>Objetivo kcal</span>
                            <span><i style="background:#c62828;"></i>Déficit real</span>
                            <span><i style="background:#66bb6a;"></i>Total kcal consumidas</span>
                        </div>
                    </section>
                </div>
            </section>
        </div>

        <div id="settings" class="tab-content">
            <section class="card">
                <h2>⚙️ Configuración corporal</h2>
                <div class="grid3">
                    <div class="kv"><input id="peso" type="number" value="64.6" step="0.1" /><label for="peso">Peso
                            (kg)</label></div>
                    <div class="kv"><input id="altura" type="number" value="158" step="1" /><label for="altura">Altura
                            (cm)</label></div>
                    <div class="kv"><input id="edad" type="number" value="30" step="1" /><label for="edad">Edad</label>
                    </div>
                </div>
                <div class="grid3" style="margin-top:8px;">
                    <div class="kv"><input id="bmr" type="number" value="0" step="1" readonly /><label for="bmr">BMR
                            (kcal) (auto)</label></div>
                    <div class="kv"><input id="tdee" type="number" value="0" step="1" readonly /><label for="tdee">TDEE
                            (kcal) (auto)</label></div>
                    <div class="kv"><input id="deficitReal" type="number" value="0" step="1" readonly /><label
                            for="deficitReal">Déficit real (auto)</label></div>
                </div>
                <input id="sexo" type="hidden" value="female" />
                <div class="grid3" style="margin-top:8px;">
                    <div class="kv"><input id="idealProt" type="number" value="130" step="1" /><label
                            for="idealProt">Ideal Proteínas (g)</label></div>
                    <div class="kv"><input id="idealCarb" type="number" value="170" step="1" /><label
                            for="idealCarb">Ideal Carbohidratos (g)</label></div>
                    <div class="kv"><input id="idealFat" type="number" value="50" step="1" /><label for="idealFat">Ideal
                            Grasas (g)</label></div>
                </div>
                <p class="muted small" style="margin:16px 0 0">*BMR = (10×peso) + (6,25×altura) - (5×edad) - 161. TDEE =
                    BMR × 1,65. Déficit = TDEE - kcal consumidas.</p>
            </section>
        </div>

        <div id="database" class="tab-content">
            <div class="db-container">
                <section class="card">
                    <h2>🗄️ Base de datos de alimentos</h2>
                    <div class="db-header">
                        <div class="db-search"><input type="text" id="searchFood" placeholder="Buscar alimento...">
                        </div>
                        <button type="button" class="btn-add" id="btnAddFood" title="Añadir nuevo alimento">+</button>
                    </div>

                    <section class="card" id="foodFormSection" style="display:none; margin: 0 0 20px 0;">
                        <h2 id="formTitle">Nuevo alimento</h2>
                        <div class="form-grid">
                            <div class="form-group"><label for="formFoodName">Nombre del alimento *</label><input
                                    type="text" id="formFoodName" placeholder="Ej: Pollo pechuga" required></div>
                            <div class="form-group"><label for="formFoodKcal">Calorías (kcal) *</label><input
                                    type="number" id="formFoodKcal" placeholder="0" step="0.1" required></div>
                            <div class="form-group"><label for="formFoodFat">Grasas (g) *</label><input type="number"
                                    id="formFoodFat" placeholder="0" step="0.1" required></div>
                            <div class="form-group"><label for="formFoodCarb">Carbohidratos (g) *</label><input
                                    type="number" id="formFoodCarb" placeholder="0" step="0.1" required></div>
                            <div class="form-group"><label for="formFoodProt">Proteínas (g) *</label><input
                                    type="number" id="formFoodProt" placeholder="0" step="0.1" required></div>
                        </div>
                        <div class="form-actions">
                            <button type="button" class="btn-primary" id="btnSaveFood">Guardar alimento</button>
                            <button type="button" class="btn-secondary" id="btnCancelFood">Cancelar</button>
                        </div>
                    </section>

                    <div class="food-list" id="foodList">
                        <div class="empty-state">
                            <div class="empty-state-icon">🍽️</div>
                            <p>Cargando alimentos...</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>

    <div id="detailModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalTitle">Detalles del guardado</h3><button type="button" class="close-modal"
                    id="closeModal">&times;</button>
            </div>
            <div id="modalBody"></div>
        </div>
    </div>

    <script>
        let FOODS = [];
        let editingFoodId = null;
        const HISTORY_STORAGE_KEY = 'foodTrackerData';
        const HISTORY_API_URL = (location.protocol === 'file:' ? 'http://localhost:3000/api/history' : '/api/history');
        let lastHistorySyncError = '';

        function round1(n) { return Math.round((n + Number.EPSILON) * 10) / 10; }
        function round0(n) { return Math.round(n); }
        function slugId(name) { return name.toLowerCase().replace(/\s+/g, "-").replace(/[^a-z0-9\-áéíóúüñ]/gi, "").slice(0, 60) || ("food-" + Math.random().toString(16).slice(2)); }

        const MEALS = ["desayuno", "comida", "merienda", "cena"];
        const mealState = {}; MEALS.forEach(m => mealState[m] = []);

        const DEFAULT_FOODS = [
            { name: "Protein 80 Plus", kcal: 365, fat: 2, carb: 7, prot: 80 },
            { name: "Colágeno", kcal: 373, fat: 0, carb: 0, prot: 91 },
            { name: "Leche de soja Oficina", kcal: 35, fat: 1, carb: 3, prot: 2.4 },
            { name: "Avena", kcal: 372, fat: 7, carb: 59, prot: 13.5 },
            { name: "Leche Avena DM", kcal: 157, fat: 2, carb: 2, prot: 3.2 },
            { name: "Dátiles", kcal: 290, fat: 1, carb: 75, prot: 2.5 },
            { name: "Almendras", kcal: 604, fat: 54, carb: 4, prot: 20 },
            { name: "Mortadela pavo", kcal: 150, fat: 8, carb: 5, prot: 15 },
            { name: "Huevo", kcal: 141, fat: 10, carb: 1, prot: 13 },
            { name: "Semillas de chía", kcal: 464, fat: 34, carb: 3, prot: 22 },
            { name: "Pastel Proteico", kcal: 0, fat: 0, carb: 0, prot: 0 },
            { name: "Skyr", kcal: 62, fat: 0, carb: 11, prot: 5.4 },
            { name: "Semillas lino", kcal: 524, fat: 42, carb: 3, prot: 20 },
            { name: "Gambas", kcal: 108, fat: 2, carb: 0, prot: 20.3 },
            { name: "Pollo", kcal: 165, fat: 3, carb: 0, prot: 22 },
            { name: "Aguacate", kcal: 160, fat: 14, carb: 8, prot: 2 },
            { name: "Aceite", kcal: 900, fat: 100, carb: 0, prot: 0 },
            { name: "Salmón", kcal: 190, fat: 12, carb: 0, prot: 18.4 },
            { name: "Patata", kcal: 77, fat: 0, carb: 17, prot: 2 },
            { name: "Arroz", kcal: 350, fat: 1, carb: 80, prot: 7 },
            { name: "Ternera", kcal: 140, fat: 3, carb: 0, prot: 25 },
            { name: "Nueces", kcal: 654, fat: 65, carb: 14, prot: 15 },
            { name: "Miel", kcal: 330, fat: 0, carb: 82, prot: 0.6 },
            { name: "Plátano", kcal: 89, fat: 0, carb: 23, prot: 1.2 },
            { name: "Arándanos", kcal: 57, fat: 0, carb: 0, prot: 0.7 }
        ];

        function mifflinBMR({ weightKg, heightCm, age }) {
            return (10 * weightKg) + (6.25 * heightCm) - (5 * age) - 161;
        }

        function computeRowMacros(food, grams) {
            const factor = grams / 100;
            return { kcal: food.per.kcal * factor, fat: food.per.fat * factor, carb: food.per.carb * factor, prot: food.per.prot * factor };
        }

        function normalizeFoodName(name) {
            return String(name || '')
                .toLowerCase()
                .normalize('NFD')
                .replace(/[\u0300-\u036f]/g, '')
                .trim();
        }

        function syncFoodsWithDefaults() {
            const defaultsMap = new Map(DEFAULT_FOODS.map(f => [normalizeFoodName(f.name), f]));
            const seen = new Set();

            FOODS = FOODS.map(food => {
                const key = normalizeFoodName(food.name);
                const def = defaultsMap.get(key);
                if (!def) return food;
                seen.add(key);
                return {
                    ...food,
                    name: def.name,
                    per: { kcal: def.kcal, fat: def.fat, carb: def.carb, prot: def.prot }
                };
            });

            DEFAULT_FOODS.forEach(def => {
                const key = normalizeFoodName(def.name);
                if (seen.has(key)) return;
                FOODS.push({
                    id: slugId(def.name),
                    name: def.name,
                    per: { kcal: def.kcal, fat: def.fat, carb: def.carb, prot: def.prot }
                });
            });

            saveFoodsToStorage();
        }

        function initializeFoods() {
            const stored = localStorage.getItem('foodDatabase');
            if (stored) {
                try {
                    FOODS = JSON.parse(stored);
                } catch (e) {
                    initializeDefaultFoods();
                }
            } else {
                initializeDefaultFoods();
            }
            syncFoodsWithDefaults();
            FOODS.sort((a, b) => a.name.localeCompare(b.name, 'es'));
            renderFoodsInMeals();
            renderFoodList();
        }

        function initializeDefaultFoods() {
            FOODS = DEFAULT_FOODS.map(f => ({
                id: slugId(f.name),
                name: f.name,
                per: { kcal: f.kcal, fat: f.fat, carb: f.carb, prot: f.prot }
            }));
            FOODS.sort((a, b) => a.name.localeCompare(b.name, 'es'));
            saveFoodsToStorage();
        }

        function saveFoodsToStorage() {
            localStorage.setItem('foodDatabase', JSON.stringify(FOODS));
        }

        function loadHistoryFromStorage() {
            const stored = localStorage.getItem(HISTORY_STORAGE_KEY);
            if (!stored) return [];
            try {
                const parsed = JSON.parse(stored);
                return Array.isArray(parsed) ? parsed : [];
            } catch (e) {
                return [];
            }
        }

        function saveHistoryToStorage(historyData) {
            localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(historyData));
        }

        function getHistoryEntryKey(entry) {
            const ts = String(entry?.timestamp || '');
            const d = String(entry?.date || '');
            const t = String(entry?.time || '');
            const kcal = String(entry?.summary?.totalKcal ?? '');
            const obj = String(entry?.summary?.objectiveKcal ?? '');
            return `${ts}|${d}|${t}|${kcal}|${obj}`;
        }

        function mergeHistoryData(localData, cloudData) {
            const map = new Map();
            [...(Array.isArray(cloudData) ? cloudData : []), ...(Array.isArray(localData) ? localData : [])]
                .forEach(item => map.set(getHistoryEntryKey(item), item));
            return [...map.values()].sort((a, b) => new Date(a.timestamp || 0) - new Date(b.timestamp || 0));
        }

        function setHistorySyncNote(message, isError = false) {
            const note = document.getElementById('historySyncNote');
            if (!note) return;
            note.textContent = message;
            note.style.color = isError ? '#c62828' : '';
        }

        function formatHistorySyncError(err) {
            const raw = String(err?.message || err || '').trim();
            if (!raw || raw === 'Failed to fetch') {
                return `No hay conexión con el servidor (${HISTORY_API_URL}). Inicia el servidor con: python3 server.py`;
            }
            return raw;
        }

        async function syncHistoryAcrossDevices() {
            setHistorySyncNote('Sincronizando historial...');
            try {
                const localBefore = loadHistoryFromStorage();
                const pulled = await pullHistoryFromCloud(true);
                const cloudAfterPull = pulled ? loadHistoryFromStorage() : [];
                const merged = mergeHistoryData(localBefore, cloudAfterPull);

                saveHistoryToStorage(merged);
                renderHistoryList();
                renderHistoryChart();

                if (merged.length > 0) {
                    const pushed = await pushHistoryToCloud(true);
                    if (!pushed) {
                        setHistorySyncNote(`No se pudo subir el historial al servidor. ${lastHistorySyncError}`, true);
                        return;
                    }
                }
                setHistorySyncNote('Historial sincronizado correctamente.');
            } catch (e) {
                setHistorySyncNote('Error de sincronización. Revisa conexión/servidor.', true);
            }
        }

        async function pushHistoryToCloud(silent = false) {
            const payload = {
                history: loadHistoryFromStorage(),
                updatedAt: new Date().toISOString()
            };
            try {
                const res = await fetch(HISTORY_API_URL, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if (!res.ok) throw new Error(`No se pudo subir (${res.status})`);
                if (!silent) alert('✓ Historial subido.');
                lastHistorySyncError = '';
                return true;
            } catch (e) {
                lastHistorySyncError = formatHistorySyncError(e);
                if (!silent) alert(`No se pudo subir el historial. Detalle: ${e?.message || 'sin conexión al servidor'}`);
                return false;
            }
        }

        async function pullHistoryFromCloud(silent = false) {
            try {
                const res = await fetch(HISTORY_API_URL, { cache: 'no-store' });
                if (!res.ok) throw new Error(`No se pudo descargar (${res.status})`);
                const payload = await res.json();
                const cloudHistory = Array.isArray(payload) ? payload : (Array.isArray(payload?.history) ? payload.history : []);
                if (!Array.isArray(cloudHistory)) throw new Error('Formato inválido');
                saveHistoryToStorage(cloudHistory);
                renderHistoryList();
                renderHistoryChart();
                if (!silent) alert('✓ Historial descargado.');
                lastHistorySyncError = '';
                return true;
            } catch (e) {
                lastHistorySyncError = formatHistorySyncError(e);
                if (!silent) alert(`No se pudo descargar el historial. Detalle: ${e?.message || 'sin conexión al servidor'}`);
                return false;
            }
        }


        function saveConfigToStorage() {
            const config = {
                peso: Number(document.getElementById("peso").value || 0),
                altura: Number(document.getElementById("altura").value || 0),
                edad: Number(document.getElementById("edad").value || 0),
                idealProt: Number(document.getElementById("idealProt").value || 0),
                idealCarb: Number(document.getElementById("idealCarb").value || 0),
                idealFat: Number(document.getElementById("idealFat").value || 0)
            };
            localStorage.setItem('userConfig', JSON.stringify(config));
        }

        function loadConfigFromStorage() {
            const stored = localStorage.getItem('userConfig');
            if (stored) {
                try {
                    const config = JSON.parse(stored);
                    document.getElementById("peso").value = config.peso || 64.6;
                    document.getElementById("altura").value = config.altura || 158;
                    document.getElementById("edad").value = config.edad || 30;
                    document.getElementById("idealProt").value = config.idealProt || 130;
                    document.getElementById("idealCarb").value = config.idealCarb || 170;
                    document.getElementById("idealFat").value = config.idealFat || 50;
                } catch (e) { }
            }
        }

        function setMacroRingProgress(el, consumed, target) {
            if (!el) return 0;
            const r = Number(el.getAttribute('r') || 0);
            const circumference = 2 * Math.PI * r;
            const ratio = target > 0 ? Math.max(0, Math.min(consumed / target, 1)) : 0;
            el.style.strokeDasharray = `${circumference}`;
            el.style.strokeDashoffset = `${circumference * (1 - ratio)}`;
            el.style.opacity = ratio > 0 ? '1' : '.3';
            return ratio;
        }

        function renderMacroRings(totalProt, totalCarb, totalFat, idealProt, idealCarb, idealFat) {
            const protRatio = setMacroRingProgress(document.getElementById('ringProt'), totalProt, idealProt);
            const carbRatio = setMacroRingProgress(document.getElementById('ringCarb'), totalCarb, idealCarb);
            const fatRatio = setMacroRingProgress(document.getElementById('ringFat'), totalFat, idealFat);

            const avgPct = round0(((protRatio + carbRatio + fatRatio) / 3) * 100);
            const center = document.getElementById('ringsCenterValue');
            if (center) center.textContent = `${avgPct}%`;

            const protText = document.getElementById('ringProtText');
            const carbText = document.getElementById('ringCarbText');
            const fatText = document.getElementById('ringFatText');
            if (protText) protText.textContent = `${round1(totalProt)} / ${round0(idealProt)}g`;
            if (carbText) carbText.textContent = `${round1(totalCarb)} / ${round0(idealCarb)}g`;
            if (fatText) fatText.textContent = `${round1(totalFat)} / ${round0(idealFat)}g`;
        }

        function renderFoodsInMeals() {
            const mealSections = document.querySelectorAll(".card[data-meal]");
            mealSections.forEach(sec => {
                const meal = sec.getAttribute("data-meal");
                const foodSel = sec.querySelector(".foodSelect");
                const mealBody = sec.querySelector(".mealBody");
                const status = sec.querySelector(".foodsStatus");

                foodSel.innerHTML = "<option value=''>Selecciona un alimento...</option>";
                FOODS.forEach(f => {
                    const opt = document.createElement("option");
                    opt.value = f.id;
                    opt.textContent = f.name;
                    foodSel.appendChild(opt);
                });

                mealBody.innerHTML = "";
                mealState[meal].forEach((row, idx) => {
                    const food = FOODS.find(f => f.id === row.foodId);
                    if (!food) return;

                    const displayMacros = row.grams === 0 ?
                        food.per :
                        computeRowMacros(food, row.grams);

                    const tr = document.createElement("tr");
                    tr.innerHTML = `<td>${food.name}</td><td class="right">${round0(displayMacros.kcal)}</td><td class="right">${round1(displayMacros.fat)}</td><td class="right">${round1(displayMacros.carb)}</td><td class="right">${round1(displayMacros.prot)}</td><td class="right"></td>`;
                    const grTd = tr.children[5];

                    const input = document.createElement("input");
                    input.type = "number";
                    input.min = "0";
                    input.step = "1";
                    input.value = row.grams || '';

                    input.addEventListener("change", () => {
                        mealState[meal][idx].grams = Number(input.value || 0);
                        renderFoodsInMeals();
                        recalcBMRObjective();
                    });

                    input.addEventListener("input", () => {
                        mealState[meal][idx].grams = Number(input.value || 0);
                        recalcBMRObjective();
                    });

                    grTd.appendChild(input);

                    const delBtn = document.createElement("button");
                    delBtn.type = "button";
                    delBtn.className = "btn-del";
                    delBtn.textContent = "❌";
                    delBtn.addEventListener("click", () => {
                        mealState[meal].splice(idx, 1);
                        renderFoodsInMeals();
                        recalcBMRObjective();
                    });
                    const delTd = document.createElement("td");
                    delTd.appendChild(delBtn);
                    tr.appendChild(delTd);
                    mealBody.appendChild(tr);
                });

                let tot = { kcal: 0, fat: 0, carb: 0, prot: 0, gr: 0 };
                mealState[meal].forEach(row => {
                    const food = FOODS.find(f => f.id === row.foodId);
                    if (!food) return;
                    const m = computeRowMacros(food, row.grams);
                    tot.kcal += m.kcal;
                    tot.fat += m.fat;
                    tot.carb += m.carb;
                    tot.prot += m.prot;
                    tot.gr += row.grams;
                });
                sec.querySelector(".totalKcal").textContent = round0(tot.kcal);
                sec.querySelector(".totalFat").textContent = round1(tot.fat);
                sec.querySelector(".totalCarb").textContent = round1(tot.carb);
                sec.querySelector(".totalProt").textContent = round1(tot.prot);
                sec.querySelector(".totalGr").textContent = round0(tot.gr);
                status.textContent = `Alimentos cargados: ${FOODS.length}`;
            });
        }

        function renderFoodList(filter = '') {
            const foodList = document.getElementById('foodList');
            const filtered = FOODS.filter(f => f.name.toLowerCase().includes(filter.toLowerCase()));

            if (filtered.length === 0) {
                foodList.innerHTML = `<div class="empty-state"><div class="empty-state-icon">🔍</div><p>${filter ? 'No hay alimentos que coincidan' : 'No hay alimentos guardados'}</p></div>`;
                return;
            }

            foodList.innerHTML = '';
            filtered.forEach(food => {
                const item = document.createElement('div');
                item.className = 'food-item';
                item.innerHTML = `<div class="food-item-info"><div class="food-item-name">${food.name}</div><div class="food-item-macros">${round0(food.per.kcal)} kcal • ${round1(food.per.fat)}g grasas • ${round1(food.per.carb)}g carbs • ${round1(food.per.prot)}g prot</div></div><div class="food-item-actions"><button type="button" class="btn-edit">Editar</button><button type="button" class="btn-delete">Eliminar</button></div>`;

                item.querySelector('.btn-edit').addEventListener('click', () => editFood(food.id));
                item.querySelector('.btn-delete').addEventListener('click', () => deleteFood(food.id));

                foodList.appendChild(item);
            });
        }

        function editFood(foodId) {
            const food = FOODS.find(f => f.id === foodId);
            if (!food) return;
            editingFoodId = foodId;
            document.getElementById('formTitle').textContent = `Editar: ${food.name}`;
            document.getElementById('formFoodName').value = food.name;
            document.getElementById('formFoodKcal').value = food.per.kcal;
            document.getElementById('formFoodFat').value = food.per.fat;
            document.getElementById('formFoodCarb').value = food.per.carb;
            document.getElementById('formFoodProt').value = food.per.prot;
            document.getElementById('foodFormSection').style.display = 'block';
            document.getElementById('foodFormSection').scrollIntoView({ behavior: 'smooth' });
        }

        function deleteFood(foodId) {
            if (confirm('¿Estás seguro?')) {
                FOODS = FOODS.filter(f => f.id !== foodId);
                saveFoodsToStorage();
                renderFoodList();
                renderFoodsInMeals();
            }
        }

        function saveFood() {
            const name = document.getElementById('formFoodName').value.trim();
            const kcal = Number(document.getElementById('formFoodKcal').value || 0);
            const fat = Number(document.getElementById('formFoodFat').value || 0);
            const carb = Number(document.getElementById('formFoodCarb').value || 0);
            const prot = Number(document.getElementById('formFoodProt').value || 0);

            if (!name || kcal === 0) {
                alert('Completa el nombre y calorías');
                return;
            }

            if (editingFoodId) {
                const food = FOODS.find(f => f.id === editingFoodId);
                if (food) {
                    food.name = name;
                    food.per = { kcal, fat, carb, prot };
                }
                editingFoodId = null;
            } else {
                FOODS.push({
                    id: slugId(name),
                    name,
                    per: { kcal, fat, carb, prot }
                });
            }

            FOODS.sort((a, b) => a.name.localeCompare(b.name, 'es'));
            saveFoodsToStorage();
            renderFoodList();
            renderFoodsInMeals();
            document.getElementById('foodFormSection').style.display = 'none';
            alert('✓ Alimento guardado');
        }

        function recalcBMRObjective() {
            const weightKg = Number(document.getElementById("peso").value || 0);
            const heightCm = Number(document.getElementById("altura").value || 0);
            const age = Number(document.getElementById("edad").value || 0);

            const bmr = mifflinBMR({ weightKg, heightCm, age });
            document.getElementById("bmr").value = round0(bmr);

            const tdee = bmr * 1.65;
            document.getElementById("tdee").value = round0(tdee);

            let totalProt = 0, totalCarb = 0, totalFat = 0, totalKcal = 0;

            document.querySelectorAll(".card[data-meal]").forEach(sec => {
                const meal = sec.getAttribute("data-meal");
                mealState[meal].forEach(row => {
                    const food = FOODS.find(f => f.id === row.foodId);
                    if (food) {
                        const m = computeRowMacros(food, row.grams);
                        totalKcal += m.kcal;
                        totalProt += m.prot;
                        totalCarb += m.carb;
                        totalFat += m.fat;
                    }
                });
            });

            const realDeficit = tdee - totalKcal;
            document.getElementById("deficitReal").value = round0(realDeficit);
            document.getElementById("deficitTracker").textContent = round0(realDeficit);

            document.getElementById("sumKcal").textContent = round0(totalKcal);
            document.getElementById("objKcalLabel").textContent = round0(tdee);

            const idealProt = Number(document.getElementById("idealProt").value || 130);
            const idealCarb = Number(document.getElementById("idealCarb").value || 170);
            const idealFat = Number(document.getElementById("idealFat").value || 50);

            const protCalories = 520;
            const carbCalories = 680;
            const fatCalories = 450;
            const totalCalories = protCalories + carbCalories + fatCalories;

            document.getElementById("sumProtG").textContent = round1(totalProt);
            document.getElementById("sumCarbG").textContent = round1(totalCarb);
            document.getElementById("sumFatG").textContent = round1(totalFat);

            document.getElementById("idealProtVal").textContent = idealProt;
            document.getElementById("idealCarbVal").textContent = idealCarb;
            document.getElementById("idealFatVal").textContent = idealFat;

            const protCaloriesConsumed = totalProt * 4;
            const carbCaloriesConsumed = totalCarb * 4;
            const fatCaloriesConsumed = totalFat * 9;

            document.getElementById("sumProtPct").textContent = totalCalories > 0 ? round0((protCaloriesConsumed / totalCalories) * 100) + "%" : "0%";
            document.getElementById("sumCarbPct").textContent = totalCalories > 0 ? round0((carbCaloriesConsumed / totalCalories) * 100) + "%" : "0%";
            document.getElementById("sumFatPct").textContent = totalCalories > 0 ? round0((fatCaloriesConsumed / totalCalories) * 100) + "%" : "0%";

            renderMacroRings(totalProt, totalCarb, totalFat, idealProt, idealCarb, idealFat);
        }

        async function saveDailyData() {
            const now = new Date();
            const dateStr = now.toLocaleDateString('es-ES');
            const timeStr = now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
            const totalKcal = Number(document.getElementById("sumKcal").textContent || 0);
            const objectiveKcal = Number(document.getElementById("objKcalLabel").textContent || 0);
            const deficitReal = Number(document.getElementById("deficitReal").value || 0);

            const dataToSave = {
                date: dateStr,
                time: timeStr,
                timestamp: now.toISOString(),
                meals: JSON.parse(JSON.stringify(mealState)),
                config: {
                    peso: Number(document.getElementById("peso").value),
                    altura: Number(document.getElementById("altura").value),
                    edad: Number(document.getElementById("edad").value),
                    bmr: Number(document.getElementById("bmr").value),
                    tdee: Number(document.getElementById("tdee").value),
                    deficitReal: deficitReal,
                    idealProt: Number(document.getElementById("idealProt").value),
                    idealCarb: Number(document.getElementById("idealCarb").value),
                    idealFat: Number(document.getElementById("idealFat").value)
                },
                summary: {
                    totalKcal: totalKcal,
                    objectiveKcal: objectiveKcal,
                    deficitReal: deficitReal
                }
            };

            let allData = loadHistoryFromStorage();
            allData.push(dataToSave);
            saveHistoryToStorage(allData);
            saveConfigToStorage();

            renderHistoryList();
            renderHistoryChart();
            setHistorySyncNote('Guardando y subiendo historial...');
            const pushed = await pushHistoryToCloud(true);
            if (pushed) {
                setHistorySyncNote('Historial sincronizado correctamente.');
                alert(`✓ Datos guardados: ${dateStr} ${timeStr}`);
            } else {
                setHistorySyncNote(`Guardado local ok, pero no se pudo subir al servidor. ${lastHistorySyncError}`, true);
                alert(`Datos guardados localmente (${dateStr} ${timeStr}), pero falló la sincronización.`);
            }
        }

        function renderHistoryList() {
            const historyList = document.getElementById('historyList');
            const allData = loadHistoryFromStorage();

            if (allData.length === 0) {
                historyList.innerHTML = `<div class="empty-state"><div class="empty-state-icon">📭</div><p>No hay datos guardados aún</p></div>`;
                return;
            }

            historyList.innerHTML = '';
            [...allData].reverse().forEach((data, idx) => {
                const originalIdx = allData.length - 1 - idx;
                let totalKcal = 0, totalProt = 0, totalCarb = 0, totalFat = 0;
                MEALS.forEach(meal => {
                    (data.meals[meal] || []).forEach(item => {
                        const food = FOODS.find(f => f.id === item.foodId);
                        if (food) {
                            const m = computeRowMacros(food, item.grams);
                            totalKcal += m.kcal;
                            totalProt += m.prot;
                            totalCarb += m.carb;
                            totalFat += m.fat;
                        }
                    });
                });

                const item = document.createElement('div');
                item.className = 'history-item';
                item.innerHTML = `
                    <div class="history-item-info">
                        <div class="history-item-date">${data.date}</div>
                        <div class="history-item-time">⏰ ${data.time}</div>
                        <div class="history-item-stats">${round0(totalKcal)} kcal • ${round1(totalProt)}g prot • ${round1(totalCarb)}g carbs • ${round1(totalFat)}g grasas<br><strong>Total kcal consumidas: ${round0(totalKcal)}, Déficit real: ${data.config.deficitReal}</strong></div>
                    </div>
                    <div class="history-item-actions">
                        <button type="button" class="btn-view" onclick="showHistoryDetail(${originalIdx})">Ver</button>
                        <button type="button" class="btn-delete" onclick="deleteHistoryItem(${originalIdx})">Eliminar</button>
                    </div>
                `;
                historyList.appendChild(item);
            });
        }

        function getHistorySeries() {
            const allData = loadHistoryFromStorage();
            const sorted = [...allData].sort((a, b) => new Date(a.timestamp || 0) - new Date(b.timestamp || 0));

            const labels = [];
            const objective = [];
            const deficit = [];
            const consumed = [];

            sorted.forEach((entry, idx) => {
                const fallbackLabel = `Día ${idx + 1}`;
                labels.push(entry.date || fallbackLabel);

                const objectiveKcal = Number(entry?.summary?.objectiveKcal ?? entry?.config?.tdee ?? 0);
                const deficitKcal = Number(entry?.summary?.deficitReal ?? entry?.config?.deficitReal ?? 0);

                let totalKcal = Number(entry?.summary?.totalKcal);
                if (!Number.isFinite(totalKcal)) {
                    totalKcal = Number(objectiveKcal) - Number(deficitKcal);
                }
                if (!Number.isFinite(totalKcal)) totalKcal = 0;

                objective.push(objectiveKcal);
                deficit.push(deficitKcal);
                consumed.push(totalKcal);
            });

            return { labels, objective, deficit, consumed };
        }

        function drawLineSeries(ctx, x, y, values, minY, maxY, color) {
            if (!values.length) return;
            const points = values.map((v, i) => {
                const denom = (maxY - minY) || 1;
                return {
                    px: x(i),
                    py: y((v - minY) / denom)
                };
            });

            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            ctx.beginPath();
            points.forEach((p, i) => {
                if (i === 0) ctx.moveTo(p.px, p.py);
                else ctx.lineTo(p.px, p.py);
            });
            ctx.stroke();

            ctx.fillStyle = color;
            points.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.px, p.py, 3, 0, Math.PI * 2);
                ctx.fill();
            });
        }

        function renderHistoryChart() {
            const canvas = document.getElementById('historyChart');
            const empty = document.getElementById('chartEmpty');
            if (!canvas || !empty) return;

            const { labels, objective, deficit, consumed } = getHistorySeries();
            if (labels.length === 0) {
                empty.style.display = 'flex';
                canvas.style.display = 'none';
                return;
            }

            empty.style.display = 'none';
            canvas.style.display = 'block';

            const dpr = window.devicePixelRatio || 1;
            const cssWidth = Math.max(280, canvas.clientWidth || 280);
            const cssHeight = Math.max(220, canvas.clientHeight || 220);
            canvas.width = Math.floor(cssWidth * dpr);
            canvas.height = Math.floor(cssHeight * dpr);

            const ctx = canvas.getContext('2d');
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            ctx.clearRect(0, 0, cssWidth, cssHeight);

            const allValues = [...objective, ...deficit, ...consumed];
            const minVal = Math.min(...allValues);
            const maxVal = Math.max(...allValues);
            const pad = Math.max(50, (maxVal - minVal) * 0.12);
            const minY = minVal - pad;
            const maxY = maxVal + pad;

            const m = { top: 12, right: 10, bottom: 34, left: 48 };
            const plotW = cssWidth - m.left - m.right;
            const plotH = cssHeight - m.top - m.bottom;
            const x = (i) => labels.length === 1 ? m.left + plotW / 2 : m.left + (i * (plotW / (labels.length - 1)));
            const y = (ratio) => m.top + plotH - (ratio * plotH);

            ctx.strokeStyle = 'rgba(24,50,37,.16)';
            ctx.lineWidth = 1;
            for (let i = 0; i <= 4; i++) {
                const gy = m.top + (plotH * i / 4);
                ctx.beginPath();
                ctx.moveTo(m.left, gy);
                ctx.lineTo(m.left + plotW, gy);
                ctx.stroke();
            }

            ctx.strokeStyle = 'rgba(24,50,37,.42)';
            ctx.beginPath();
            ctx.moveTo(m.left, m.top);
            ctx.lineTo(m.left, m.top + plotH);
            ctx.lineTo(m.left + plotW, m.top + plotH);
            ctx.stroke();

            ctx.fillStyle = 'rgba(24,50,37,.72)';
            ctx.font = '11px system-ui';
            ctx.textAlign = 'right';
            for (let i = 0; i <= 4; i++) {
                const ratio = 1 - (i / 4);
                const value = round0(minY + (maxY - minY) * ratio);
                const gy = m.top + (plotH * i / 4);
                ctx.fillText(String(value), m.left - 6, gy + 3);
            }

            ctx.textAlign = 'center';
            labels.forEach((label, i) => {
                const parts = String(label).split('/');
                const dayLabel = parts.length >= 2 ? `${parts[0]}/${parts[1]}` : label;
                ctx.fillText(dayLabel, x(i), m.top + plotH + 16);
            });

            ctx.fillStyle = 'rgba(24,50,37,.75)';
            ctx.textAlign = 'center';
            ctx.fillText('Días', m.left + (plotW / 2), cssHeight - 4);
            ctx.save();
            ctx.translate(12, m.top + (plotH / 2));
            ctx.rotate(-Math.PI / 2);
            ctx.fillText('kcal', 0, 0);
            ctx.restore();

            drawLineSeries(ctx, x, y, objective, minY, maxY, '#1e88e5');
            drawLineSeries(ctx, x, y, deficit, minY, maxY, '#c62828');
            drawLineSeries(ctx, x, y, consumed, minY, maxY, '#66bb6a');
        }

        async function deleteHistoryItem(idx) {
            if (confirm('¿Eliminar?')) {
                let allData = loadHistoryFromStorage();
                allData.splice(idx, 1);
                saveHistoryToStorage(allData);
                renderHistoryList();
                renderHistoryChart();
                setHistorySyncNote('Actualizando historial en servidor...');
                const pushed = await pushHistoryToCloud(true);
                if (pushed) setHistorySyncNote('Historial sincronizado correctamente.');
                else setHistorySyncNote(`No se pudo actualizar historial en servidor. ${lastHistorySyncError}`, true);
            }
        }

        function showHistoryDetail(idx) {
            const allData = loadHistoryFromStorage();
            const data = allData[idx];
            document.getElementById('modalTitle').textContent = `${data.date} ${data.time}`;
            document.getElementById('modalBody').innerHTML = `<p><strong>Config:</strong> ${data.config.peso}kg, ${data.config.altura}cm, ${data.config.edad}a | BMR: ${data.config.bmr} | TDEE: ${data.config.tdee} | Déficit real: ${data.config.deficitReal}</p><p><strong>Macros ideales:</strong> Prot: ${data.config.idealProt}g | Carbs: ${data.config.idealCarb}g | Grasas: ${data.config.idealFat}g</p><p><strong>Comidas:</strong> ${Object.keys(data.meals).map(m => `${m}: ${(data.meals[m] || []).length} items`).join(', ')}</p>`;
            document.getElementById('detailModal').style.display = 'block';
        }

        // Event listeners
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.tab-button').forEach(b => b.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
                btn.classList.add('active');
                const tabId = btn.getAttribute('data-tab');
                document.getElementById(tabId).classList.add('active');
                if (tabId === 'history') {
                    renderHistoryChart();
                }
            });
        });

        document.getElementById('btnSave').addEventListener('click', saveDailyData);

        document.getElementById('btnAddFood').addEventListener('click', () => {
            editingFoodId = null;
            document.getElementById('formTitle').textContent = 'Nuevo alimento';
            document.getElementById('formFoodName').value = '';
            document.getElementById('formFoodKcal').value = '';
            document.getElementById('formFoodFat').value = '';
            document.getElementById('formFoodCarb').value = '';
            document.getElementById('formFoodProt').value = '';
            document.getElementById('foodFormSection').style.display = 'block';
            document.getElementById('foodFormSection').scrollIntoView({ behavior: 'smooth' });
        });

        document.getElementById('btnSaveFood').addEventListener('click', saveFood);
        document.getElementById('btnCancelFood').addEventListener('click', () => {
            document.getElementById('foodFormSection').style.display = 'none';
            editingFoodId = null;
        });

        document.getElementById('searchFood').addEventListener('input', (e) => {
            renderFoodList(e.target.value);
        });

        document.getElementById('closeModal').addEventListener('click', () => {
            document.getElementById('detailModal').style.display = 'none';
        });

        ['peso', 'altura', 'edad', 'idealProt', 'idealCarb', 'idealFat'].forEach(id => {
            document.getElementById(id).addEventListener('change', recalcBMRObjective);
            document.getElementById(id).addEventListener('input', recalcBMRObjective);
        });

        document.querySelectorAll(".card[data-meal]").forEach(sec => {
            const meal = sec.getAttribute("data-meal");
            const sel = sec.querySelector(".foodSelect");
            sec.querySelector(".btn-add").addEventListener('click', () => {
                if (sel && sel.value) {
                    mealState[meal].unshift({ foodId: sel.value, grams: 0 });
                    renderFoodsInMeals();
                    recalcBMRObjective();
                    sel.value = '';
                }
            });
        });

        // Inicializar
        initializeFoods();
        loadConfigFromStorage();
        recalcBMRObjective();
        renderHistoryList();
        renderHistoryChart();
        syncHistoryAcrossDevices();
        window.addEventListener('resize', renderHistoryChart);
    </script>
</body>

</html>
```
