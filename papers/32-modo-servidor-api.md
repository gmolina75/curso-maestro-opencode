---
title: "Clase 32: Modo Servidor y API"
module: 32
duration: "1 hora"
prerequisites: "Módulo 31 - Clase 31: Troubleshooting y Recursos"
---

# Clase 32: Modo Servidor y API

> **Actualizado a OpenCode v2.** En v2 la arquitectura cambió: ya no se ejecuta `opencode server` como comando independiente. En su lugar, OpenCode mantiene un **servidor compartido en segundo plano** que descubre o inicia automáticamente, y todos los clientes locales (TUI, CLI, desktop) se conectan a él. El modo headless se hace con `opencode run`.

## Resumen Ejecutivo

Esta clase cubre la arquitectura de servidor de OpenCode v2 y cómo integrarlo con herramientas externas. El servidor es el dueño de las sesiones, la configuración, los permisos y la ejecución de herramientas; los clientes son interfaces que se conectan a él. Esto permite compartir estado entre la terminal, scripts de CI/CD, la app de escritorio y aplicaciones web propias.

A lo largo de la sesión se exploran los siguientes temas: qué es el servidor compartido y cómo administrarlo con `opencode service`, los endpoints principales de la API HTTP (sesiones, mensajes, compactación, fork), el modo no interactivo con `opencode run` para automatización y CI/CD, y la interfaz mínima `opencode mini`. Al finalizar, el estudiante podrá levantar, inspeccionar y consumir el servidor de OpenCode desde sus propios programas.

## Objetivos de Aprendizaje

- Explicar la arquitectura servidor/cliente de OpenCode v2 y el rol del servidor compartido.
- Administrar el servicio con `opencode service` (iniciar, detener, deshabilitar).
- Conectarse a un servidor específico con `--server` o trabajar aislado con `--standalone`.
- Ejecutar tareas sin interfaz usando `opencode run` y consumir la API HTTP REST.
- Integrar OpenCode en pipelines de CI/CD y scripts programáticos.

## Conceptos Clave

### El servidor compartido de OpenCode v2

Por defecto, OpenCode descubre o inicia **un servidor de fondo compartido por usuario**. Todos los clientes locales se conectan a ese servidor, que es quien posee las sesiones, la configuración, las integraciones, los permisos y la ejecución de herramientas. Ventajas clave:

- **Estado persistente compartido**: la TUI, la app de escritorio y los scripts ven las mismas sesiones.
- **Un solo proceso gestiona los proyectos**: las sesiones no mueren al cerrar la terminal.
- **API HTTP estable**: otros programas pueden crear sesiones, enviar mensajes y leer resultados.

```bash
# Trabajar con un servidor privado aislado (sin el servicio compartido)
opencode --standalone

# Conectarse a un servidor específico (por defecto escucha en el puerto 4096)
opencode --server http://localhost:4096
```

### Administración del servicio: `opencode service`

El servicio compartido se controla explícitamente con el subcomando `service`:

```bash
# Iniciar el servicio compartido explícitamente
opencode service start

# Hacer que los comandos del CLI NO inicien el servicio automáticamente
opencode service set disabled true

# Volver al comportamiento automático
opencode service unset disabled
```

Notas importantes:

- Deshabilitar el servicio **detiene el servidor en ejecución**; `--server` sigue pudiendo conectarse a un servidor explícito, y `opencode service start` puede reiniciarlo.
- El **emparejamiento (pairing)** —flujo con código de corta duración para conectar clientes— requiere el servicio compartido y no está disponible mientras está deshabilitado.

### API HTTP del servidor

El servidor expone una API REST (documentada en `opencode.ai/docs/server`). Algunos endpoints representativos:

| Endpoint | Método | Propósito |
|----------|--------|-----------|
| `/api/info` | GET | Identidad del servidor, URLs de conexión y estado de preparación |
| `/api/session` | GET/POST | Listar o crear sesiones (soporta `parentID`, filtros, paginación por cursor) |
| `/api/session/{id}/prompt` | POST | Enviar un mensaje y arrancar el agente (encola; no espera a que termine) |
| `/api/session/{id}/message` | GET | Leer los mensajes de la sesión |
| `/api/session/{id}/compact` | POST | Compactar el historial de la sesión |
| `/api/session/{id}/fork` | POST | Crear una sesión hija con el historial hasta cierto mensaje |
| `/api/session/{id}/interrupt` | POST | Detener la ejecución del agente |
| `/api/session/active` | GET | Listar sesiones con el agente corriendo ahora mismo |
| `/api/experimental/session/stats` | GET | Estadísticas de uso: actividad, tokens y fiabilidad de herramientas |

Flujo típico de automatización:

```bash
# 1. Crear sesión
curl -s -X POST http://localhost:4096/api/session \
  -H "Content-Type: application/json" \
  -d '{"directory": "/home/user/proyecto"}'

# 2. Enviar un mensaje (devuelve cuando el mensaje fue encolado, no al terminar)
curl -s -X POST http://localhost:4096/api/session/<ID>/prompt \
  -H "Content-Type: application/json" \
  -d '{"parts": [{"type": "text", "text": "Resume este repositorio"}]}'

# 3. Esperar a que el agente termine y leer la respuesta
curl -s -X POST http://localhost:4096/api/experimental/session/<ID>/wait
curl -s "http://localhost:4096/api/session/<ID>/message?type=assistant"
```

### Modo headless: `opencode run`

Para scripts y CI/CD no hace falta la API: el subcomando `opencode run` envía un prompt sin abrir la interfaz interactiva y devuelve el resultado por stdout.

```bash
# Pregunta única sin interfaz
opencode run "Explain this repository"

# Interfaz mínima interactiva (alternativa ligera a la TUI completa)
opencode mini
```

Ideal para: pipelines, cron jobs, hooks de git, generación de documentación programática. Requiere que la configuración del proveedor (API keys, modelo por defecto) ya esté resuelta en archivos de configuración o variables de entorno.

### Inspección y depuración

```bash
# Ver rutas internas (base de datos, config, logs, caché)
opencode debug paths

# Ruta concreta para usar con otras herramientas
sqlite3 "$(opencode debug paths db)"
```

## Guía Paso a Paso

### Paso 1: Levantar y verificar el servidor

```bash
opencode service start
curl -s http://localhost:4096/api/info | head
```

Comprueba que la respuesta incluya la identidad del servidor y las URLs de conexión. Si el servicio estaba deshabilitado, primero ejecuta `opencode service unset disabled`.

### Paso 2: Conectar un cliente TUI al servidor

```bash
opencode --server http://localhost:4096
```

Abre la interfaz completa conectada al servidor compartido. Crea una sesión de prueba y envía un mensaje; luego cierra la TUI y verifica con `curl` que la sesión sigue viva en `/api/session`.

### Paso 3: Automatizar con `opencode run`

```bash
opencode run "Lista los 3 archivos más importantes de src/ y explica por qué"
```

Integra este comando en un script shell y captura su salida. Para CI, asegúrate de exportar las variables de entorno del proveedor (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) antes de invocarlo.

### Paso 4: Crear una sesión y consumir la API

1. Crea una sesión con `POST /api/session` en el directorio de tu proyecto.
2. Envía un mensaje con `POST /api/session/{id}/prompt`.
3. Espera con `POST /api/session/{id}/wait` (endpoint experimental).
4. Lee la respuesta del asistente con `GET /api/session/{id}/message?type=assistant`.

### Paso 5: Integración con GitHub Actions

```yaml
name: resumen-diario
on:
  schedule:
    - cron: "0 7 * * *"
jobs:
  opencode:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Instalar OpenCode
        run: curl -fsSL https://opencode.ai/install | bash
      - name: Generar resumen
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: opencode run "Resume los cambios del último día y crea un reporte breve" > resumen.md
      - uses: actions/upload-artifact@v4
        with:
          name: resumen
          path: resumen.md
```

## Referencia Rápida

| Comando / Endpoint | Descripción | Ejemplo |
|-------------------|-------------|---------|
| `opencode service start` | Inicia el servidor compartido | `opencode service start` |
| `opencode service set disabled true` | Desactiva el servicio automático | — |
| `opencode --standalone` | Servidor privado aislado | — |
| `opencode --server <url>` | Conecta a un servidor concreto | `opencode --server http://localhost:4096` |
| `opencode run "<prompt>"` | Ejecuta sin interfaz | `opencode run "Explain this repo"` |
| `opencode mini` | Interfaz mínima interactiva | `opencode mini` |
| `opencode debug paths` | Muestra rutas internas | `opencode debug paths db` |
| `GET /api/info` | Estado del servidor | `curl localhost:4096/api/info` |
| `POST /api/session/{id}/prompt` | Enviar mensaje a una sesión | ver Paso 4 |
| `POST /api/session/{id}/compact` | Compactar historial | — |
| `POST /api/session/{id}/fork` | Ramificar sesión | — |

## Ejercicios Guiados

1. **Servidor y persistencia:** inicia el servicio, crea una sesión desde la TUI, cierra la terminal y lista las sesiones con `curl http://localhost:4096/api/session`. Explica por qué la sesión sobrevive al cierre del cliente.
2. **Script headless:** escribe un script bash que reciba un directorio como argumento y genere un `README.md` automático con `opencode run`, verificando el resultado antes de sobreescribir el archivo.
3. **Cliente API mínimo:** implementa en Python o Node un pequeño cliente que cree una sesión, envíe un mensaje, espere con `/wait` y devuelva solo el texto del último mensaje del asistente.

## Ejercicio Desafío

Diseña un servicio de "revisor nocturno": un pipeline (GitHub Actions, cron o servicio propio) que, cada noche, recorra los repositorios configurados, use `opencode run` o la API para generar un resumen de los commits del día, detecte archivos sin tests tocados recientemente y deje un issue o comentario con los hallazgos. Documenta la configuración del servidor (autenticación, puerto, permisos) y justifica la elección entre `opencode run` y la API REST.

## Recursos Adicionales

- [Documentación oficial de OpenCode — CLI](https://opencode.ai/docs/cli)
- [Referencia de la API del servidor](https://opencode.ai/docs/server)
- Presentación de la clase: `presentaciones/nuevas-clases/32-modo-servidor-api.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/32-modo-servidor-api.pptx`

## Autoevaluación

- [ ] Puedo explicar la diferencia entre el servidor compartido y `--standalone`.
- [ ] Sé administrar el servicio con `opencode service` en sus tres variantes.
- [ ] Puedo crear una sesión y enviarle un mensaje usando solo `curl`.
- [ ] Entiendo la diferencia entre "el mensaje fue encolado" y "el agente terminó" en la API.
- [ ] Puedo escribir un workflow de CI que use `opencode run`.
- [ ] Sé inspeccionar las rutas internas con `opencode debug paths`.
