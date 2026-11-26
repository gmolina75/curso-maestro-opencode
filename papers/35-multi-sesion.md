---
title: "Clase 35: Multi-Sesión"
module: 35
duration: "1 hora"
prerequisites: "Módulo 34 - Clase 34: Flujo Git"
---

# Clase 35: Multi-Sesión

> **Actualizado a OpenCode v2.** En v2 las sesiones son objetos de primera clase gestionados por el servidor: tienen API completa (crear, listar con filtros y paginación, archivar, mover entre proyectos), soportan jerarquía padre/hijo (los subagentes corren en sesiones hijas), fork con historial parcial, y estado compartido entre todos los clientes conectados al mismo servidor.

## Resumen Ejecutivo

Esta clase cubre el trabajo con múltiples sesiones simultáneas: qué es una sesión en OpenCode v2, cómo se relacionan entre sí (padre/hijo, forks), cómo gestionarlas desde la API y desde la TUI, y qué patrones de uso aprovechan el paralelismo sin caer en caos de contexto.

A lo largo de la sesión se exploran los siguientes temas: el modelo de sesiones del servidor, sesiones padre/hijo y subagentes, trabajo en paralelo con sesiones múltiples, gestión del ciclo de vida (archivar, mover, eliminar, interrumpir) y casos de uso reales. Al finalizar, el estudiante podrá orquestar varias sesiones coordinadas sobre uno o varios proyectos.

## Objetivos de Aprendizaje

- Explicar el modelo de sesiones de OpenCode v2 y su persistencia en el servidor.
- Crear y gestionar sesiones desde la API (listar con filtros, archivar, mover, eliminar).
- Usar sesiones padre/hijo y fork para ramificar trabajos sin perder historial.
- Coordinar sesiones paralelas sobre proyectos diferentes o worktrees del mismo proyecto.
- Interrumpir y reanudar trabajo en sesiones activas de forma segura.

## Conceptos Clave

### El modelo de sesiones en v2

- Cada sesión pertenece a un **proyecto** (directorio) y tiene un ID único.
- El servidor las persiste: cerrar la TUI no destruye nada.
- Los clientes (TUI, desktop, scripts) ven el mismo conjunto de sesiones porque hablan con el mismo servidor.
- Una sesión puede estar **activa** (el agente está corriendo), **archivada** o **hija** de otra sesión.

Endpoints principales:

```bash
# Listar sesiones (filtros: búsqueda por título, directorio, padre, archivadas, paginación)
curl -s "http://localhost:4096/api/session?search=auth&order=desc"

# Crear sesión en un directorio (parentID crea una sesión hija vinculada)
curl -s -X POST http://localhost:4096/api/session \
  -H "Content-Type: application/json" \
  -d '{"directory": "/home/user/proyecto", "parentID": null}'

# Sesiones corriendo ahora mismo
curl -s http://localhost:4096/api/session/active

# Archivar / actualizar / eliminar
curl -X PATCH http://localhost:4096/api/session/<ID> -H "Content-Type: application/json" -d '{"archived": true}'
curl -X DELETE http://localhost:4096/api/session/<ID>   # elimina también las hijas
```

### Padre/hijo: subagentes en sesiones hijas

Cuando el agente principal lanza un subagente (herramienta `subagent`), este corre en una **sesión hija con contexto fresco**:

- El padre recibe un reporte cuando la hija queda idle y tras cada ronda posterior de trabajo.
- La profundidad de anidación se controla con `experimental.subagent_depth` (por defecto 1: un subagente no puede lanzar otro).

```jsonc
{
  "experimental": {
    "subagent_depth": 2
  }
}
```

### Fork: ramificar historial sin duplicar sesiones

`POST /api/session/{id}/fork` crea una sesión hija con el historial de la original hasta un mensaje dado (sin `before`, copia todo el historial). Usos típicos:

- Probar dos soluciones alternativas al mismo problema desde el mismo punto.
- Convertir una sesión de exploración en una de implementación conservando el contexto.

### Trabajo en paralelo

Patrones recomendados:

| Patrón | Cuándo usarlo |
|--------|---------------|
| Sesiones en proyectos distintos | Tareas independientes sin relación |
| Worktrees + sesiones | Mismo repo, tareas paralelas (ver Clase 34) |
| Subagentes dentro de una sesión | Subtareas acotadas (investigación, revisión) que reportan al padre |
| Fork + dos sesiones | Comparar soluciones alternativas desde un punto común |

Regla de oro: **una sesión = un objetivo**. Evita mezclar tareas en la misma conversación; el contexto se degrada y los costos suben.

### Ciclo de vida e interrupción

```bash
# Interrumpir al agente (con resume=true reanuda items pendientes: steering, compactación, movimientos)
curl -X POST "http://localhost:4096/api/session/<ID>/interrupt?resume=false"

# Mover una sesión a otro directorio de proyecto
curl -X POST http://localhost:4096/api/session/<ID>/move \
  -H "Content-Type: application/json" \
  -d '{"directory": "/home/user/otro-proyecto"}'
```

También existen endpoints para enviar mensajes sintéticos (notificaciones que el modelo lee como entrada del usuario), ejecutar comandos shell en el directorio de la sesión y consultar la bandeja de entrada (inbox) con items aún no entregados al agente — incluida la **entrada de control**: se puede cambiar el modo de entrega de un mensaje encolado (steering) o cancelarlo antes de que llegue al modelo.

## Guía Paso a Paso

### Paso 1: Explorar el estado de sesiones

```bash
curl -s "http://localhost:4096/api/session?order=desc&limit=10" | jq '.sessions[] | {id, title, directory, archived}'
```

Identifica título, proyecto y estado de archivado de las sesiones recientes.

### Paso 2: Crear dos sesiones coordinadas

Crea una sesión "exploración" y otra "implementación" en el mismo proyecto. Trabaja contexto en la primera y, cuando tengas claro el plan, abre la segunda con un prompt que incluya el resumen — o usa fork si parten del mismo historial.

### Paso 3: Ramificar con fork

Desde una sesión con historial relevante:

```bash
curl -s -X POST http://localhost:4096/api/session/<ID>/fork \
  -H "Content-Type: application/json" \
  -d '{"before": "<messageID>"}'
```

Continúa las dos ramas con estrategias distintas y compara resultados.

### Paso 4: Paralelismo real con worktrees

Combina con lo aprendido en la Clase 34: dos sesiones, dos worktrees, un solo repositorio. Verifica desde cada sesión que `git branch --show-current` apunta a su worktree.

### Paso 5: Orquestar subagentes

En una sesión principal, pide: "Lanza el subagente explore para mapear X y luego el reviewer para evaluar el diff". Observa en la API las sesiones hijas (`parentID` filtra las raíces con `parentID=null`).

### Paso 6: Limpieza

Archiva las sesiones concluidas, elimina las experimentales fallidas (recuerda: eliminar un padre elimina a sus hijas) e interrumpe cualquier sesión activa que ya no necesites.

## Referencia Rápida

| Endpoint / Comando | Descripción | Ejemplo |
|--------------------|-------------|---------|
| `GET /api/session` | Lista con filtros y paginación | `?search=auth&archived=false` |
| `POST /api/session` | Crear sesión (opcional `parentID`) | ver Conceptos |
| `POST /api/session/{id}/fork` | Ramificar historial | `{ "before": "<msg>" }` |
| `POST /api/session/{id}/interrupt` | Detener el agente | `?resume=false` |
| `PATCH /api/session/{id}` | Actualizar (archivar, título) | `{ "archived": true }` |
| `POST /api/session/{id}/move` | Mover a otro proyecto | ver Paso 6 |
| `DELETE /api/session/{id}` | Eliminar sesión y sus hijas | — |
| `GET /api/session/active` | Sesiones corriendo ahora | — |
| `experimental.subagent_depth` | Anidación de subagentes | `2` |

## Ejercicios Guiados

1. **Inventario:** lista todas tus sesiones con la API, clasifícalas (activas/archivadas, con/sin hijas) y archiva las concluidas. Escribe un comando `jq` que agrupe por proyecto.
2. **Fork comparativo:** toma una sesión de decisión técnica, haz fork antes del mensaje clave y desarrolla la opción A en una rama y la B en otra; presenta una tabla comparativa.
3. **Paralelismo:** con dos worktrees del mismo repo, ejecuta dos sesiones simultáneas resolviendo issues distintos; documenta cómo evitaste interferencias y qué hiciste al llegar al merge.

## Ejercicio Desafío

Construye un "panel de orquestación": un script (Python/Node) que usando la API muestre en una tabla las sesiones activas de todos tus proyectos, permita interrumpir una sesión con un solo comando, archivar las terminadas y alerte cuando una sesión lleve más de N minutos activa (posible bucle). Bonus: que liste las sesiones hijas bajo cada padre.

## Recursos Adicionales

- [Documentación oficial de OpenCode — CLI](https://opencode.ai/docs/cli) (servidor compartido y sesiones)
- [Referencia de la API del servidor](https://opencode.ai/docs/server) (rutas de sesión)
- Presentación de la clase: `presentaciones/nuevas-clases/35-multi-sesion.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/35-multi-sesion.pptx`

## Autoevaluación

- [ ] Puedo listar, filtrar y paginar sesiones desde la API.
- [ ] Sé crear sesiones padre/hijo y explicar cómo corren los subagentes.
- [ ] Puedo hacer fork de una sesión hasta un mensaje concreto.
- [ ] Sé interrumpir una sesión y decidir si reanuda items pendientes.
- [ ] Puedo mover y archivar sesiones sin perder historial.
- [ ] Tengo clara la regla "una sesión = un objetivo" y cuándo usar worktrees.
