---
title: "Clase 41: Migración desde Otros Agentes"
module: 41
duration: "1 hora"
prerequisites: "Módulo 40 - Clase 40: Testing y Calidad de Código"
---

# Clase 41: Migración desde Otros Agentes

> **Actualizado a OpenCode v2.** En v2 los puntos clave de migración son: archivos de instrucciones `AGENTS.md` (equivale a `CLAUDE.md` y a `.cursorrules`), agentes en Markdown bajo `.opencode/agents/` (con `mode`, `permissions`, `model`, sin campos legacy de v1), configuración central en `opencode.jsonc`, servidor compartido en lugar de proceso por terminal, y `opencode run` como reemplazo de los flujos headless de otros agentes.

## Resumen Ejecutivo

Esta clase cubre cómo migrar a OpenCode v2 desde otros agentes de código (Claude Code, Cursor, GitHub Copilot, Aider y la propia v1 de OpenCode): mapeo de conceptos equivalentes, traducción de reglas y configuraciones, y una estrategia de transición de bajo riesgo que empieza en modo plan y valida cada capacidad antes de confiar el flujo completo.

A lo largo de la sesión se exploran los siguientes temas: mapeo de funcionalidades entre agentes, migración desde Claude Code y desde Cursor, adaptación de configuraciones de v1, y tips prácticos de transición. Al finalizar, el estudiante podrá ejecutar una migración ordenada con un plan de rollback.

## Objetivos de Aprendizaje

- Mapear las funcionalidades de Claude Code, Cursor y v1 a sus equivalentes de OpenCode v2.
- Traducir archivos de reglas (CLAUDE.md, .cursorrules, rules de Copilot) a `AGENTS.md`.
- Convertir configuraciones de v1 eliminando campos deprecados.
- Diseñar una transición de bajo riesgo con el agente `plan` y validación por fases.
- Documentar una equivalencia de comandos para el equipo.

## Conceptos Clave

### Mapeo de funcionalidades

| Concepto | Claude Code | Cursor | OpenCode v2 |
|----------|-------------|--------|-------------|
| Archivo de reglas del proyecto | `CLAUDE.md` | `.cursorrules` / reglas | `AGENTS.md` (+ `instructions` en config) |
| Comandos personalizados | slash commands | rules/commands | `commands` en config o `.opencode/commands/` |
| Subagentes | Task/subagents | Composer/Agent | `agents` con `mode: subagent` |
| Modo plan | plan mode | Plan previo | Agente `plan` (primary, no edita) |
| Headless / CI | `claude -p` | — | `opencode run` |
| Configuración central | settings | settings.json | `opencode.jsonc` (global → proyecto → sistema) |
| Permisos | permission modes | — | `permissions` + `policies` |
| Servidor persistente | — | — | Servidor compartido (`opencode service`) |

### De Claude Code a OpenCode

- **CLAUDE.md → AGENTS.md**: mismo propósito (instrucciones de proyecto), formato equivalente (Markdown). Copia el contenido y ajusta referencias a herramientas específicas.
- **Slash commands**: muchos se traducen 1:1 a entradas `commands` en `opencode.jsonc` con plantillas.
- **Plan mode**: el agente `plan` de v2 es un agente primary independiente; además, cualquier sesión puede arrancar en modo exploración sin editar usando `plan`.
- **Proveedores**: OpenCode soporta múltiples proveedores nativamente; la configuración del modelo es `proveedor/modelo` con variantes opcionales.
- **Subagentes con @mention**: en v2 los subagentes se lanzan vía herramienta `subagent` (el modelo elige cuál según `description`) o mención directa en la sesión.

### De Cursor a OpenCode

- **.cursorrules → AGENTS.md**: las reglas globales van a `AGENTS.md`; las reglas por ruta pueden expresarse como entradas en `instructions` (globs) o en los system de agentes especializados.
- **Composer/Agent →** sesiones con el agente `build`; para trabajo no destructivo primero, usa `plan`.
- **Chat → Plan mode**: el agente `plan` es solo lectura; ideal para familiarizarse sin riesgo.
- **@symbols de archivos**: equivalentes en la sesión (referenciar rutas en el prompt).
- **Multi-proveedor**: OpenCode es open source y multi-proveedor por diseño; no quedas atado a un solo modelo.

### De OpenCode v1 a v2

Campos deprecados a eliminar en agentes y config: `prompt`, `tools`, `permission`, `maxSteps`, `temperature`, `top_p`, `disable`. Sus reemplazos:

| v1 (deprecado) | v2 |
|----------------|-----|
| `prompt` | cuerpo del `.md` del agente o campo `system` |
| `tools` / `disable` | `permissions` con efectos allow/deny |
| `maxSteps` | `steps` (frontmatter o config) |
| `temperature`/`top_p` | `request.body` del agente |
| `opencode server` | `opencode service` / servidor compartido automático |
| `--headless --prompt` | `opencode run "..."` |

### Estrategia de transición de bajo riesgo

1. **Semana 1 — familiarización**: usa el agente `plan` en proyectos reales. Cero ediciones, aprendes prompts y límites.
2. **Semana 2 — reglas**: migra `CLAUDE.md`/`.cursorrules` a `AGENTS.md`; añade comandos de tu flujo anterior.
3. **Semana 3 — paralelo**: ejecuta la misma tarea en ambos agentes (el antiguo y OpenCode) y compara.
4. **Semana 4 — producción**: migras el flujo principal; configuras permisos (`ask` en operaciones sensibles) y dejas el agente anterior como respaldo.

Comandos útiles durante la transición:

```bash
opencode run "Resume lo que hace este módulo"   # equivalente headless
opencode --standalone                             # aislar pruebas del servicio compartido
opencode debug paths                              # conocer dónde vive la data en v2
```

## Guía Paso a Paso

### Paso 1: Inventario

Lista todo lo que usas del agente anterior: archivos de reglas, comandos personalizados, subagentes, hooks, integraciones CI. Marca cada uno con su equivalente v2 del mapeo.

### Paso 2: Traducir reglas

Copia `CLAUDE.md` (o `.cursorrules`) a `AGENTS.md`; traduce referencias a herramientas específicas; añade `instructions` para fuentes extra. Verifica en una sesión `plan` que las instrucciones se cargan.

### Paso 3: Recrear comandos y subagentes

Convierte tus slash commands a entradas `commands`; tus subagentes a archivos `.opencode/agents/*.md` con `description`, `mode`, `permissions` y `model` adecuados.

### Paso 4: Configurar proveedores y permisos

Define el modelo por defecto, externaliza secretos con `{env:}`/`{file:}` (ver Clase 38), configura `ask` en operaciones sensibles del agente `build`.

### Paso 5: Validación paralela

Ejecuta 3 tareas reales en ambos sistemas. Compara: calidad del resultado, tiempo, costo, número de intervenciones tuyas. Documenta la decisión final con datos.

## Referencia Rápida

| Origen | Destino v2 | Nota |
|--------|-----------|------|
| `CLAUDE.md` | `AGENTS.md` | copiar y ajustar |
| `.cursorrules` | `AGENTS.md` + agentes | reglas por ruta → `instructions` |
| `claude -p "..."` | `opencode run "..."` | headless/CI |
| slash commands | `commands` en config | plantillas |
| subagentes | `.opencode/agents/*.md` | `mode: subagent` |
| `prompt` (v1) | cuerpo del `.md` / `system` | — |
| `maxSteps` (v1) | `steps` | — |
| plan mode | agente `plan` | primary, solo lectura |
| — | `opencode service` | servidor compartido de v2 |

## Ejercicios Guiados

1. **Traducción:** migra tu `CLAUDE.md` o `.cursorrules` real a `AGENTS.md` y verifica en una sesión `plan` que las instrucciones se cargan correctamente.
2. **Comandos:** recrea tus 3 comandos más usados del agente anterior como `commands` de v2 y documenta las diferencias de sintaxis.
3. **Comparativa paralela:** ejecuta la misma tarea de refactor en tu agente anterior y en OpenCode; presenta una tabla de calidad/tiempo/costo e indica qué hiciste con las diferencias.

## Ejercicio Desafío

Ejecuta la migración completa de un proyecto real a OpenCode v2: inventario, AGENTS.md, comandos, agentes, permisos, validación paralela de 5 tareas y plan de rollback. Entregable: un documento de migración con el mapeo usado, evidencia de la validación paralela y la checklist que dejarías para el próximo proyecto que migre tu equipo.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs) (guías de config, agentes, CLI)
- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (equivalentes de subagentes)
- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (sustitución de campos legacy, `instructions`)
- Presentación de la clase: `presentaciones/nuevas-clases/41-migracion-agentes.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/41-migracion-agentes.pptx`

## Autoevaluación

- [ ] Puedo mapear las funcionalidades de Claude Code y Cursor a sus equivalentes v2.
- [ ] Sé traducir CLAUDE.md y .cursorrules a AGENTS.md.
- [ ] Puedo identificar y reemplazar los campos legacy de v1.
- [ ] Sé usar `opencode run` como reemplazo de flujos headless.
- [ ] Puedo diseñar una transición de 4 semanas con validación paralela.
- [ ] Tengo un plan de rollback documentado.
