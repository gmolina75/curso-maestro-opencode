---
title: "Clase 34: Flujo Git"
module: 34
duration: "1 hora"
prerequisites: "Módulo 33 - Clase 33: Gestión de Contexto y Tokens"
---

# Clase 34: Flujo Git

> **Actualizado a OpenCode v2.** En v2 Git sigue siendo el control de versiones por defecto y OpenCode añade herramientas propias encima: worktrees configurables (`worktree.directory`), snapshots para deshacer/revertir, y endpoints de API para diffs por turno y revert por etapas. El trabajo en ramas y la revisión de PRs se apoya en los agentes `build` y `plan`.

## Resumen Ejecutivo

Esta clase cubre cómo integrar OpenCode en un flujo de trabajo Git profesional: ramas por tarea, commits asistidos, trabajo paralelo con worktrees, uso seguro de la función de deshacer de OpenCode (snapshots) y revisión de cambios con subagentes de solo lectura. El objetivo es que el agente colabore dentro de las reglas del equipo, no al margen de ellas.

A lo largo de la sesión se exploran los siguientes temas: Git como estrategia de control en OpenCode, creación de ramas y commits asistidos, gestión de conflictos, pull requests con revisión asistida por agentes, y worktrees para sesiones paralelas. Al finalizar, el estudiante tendrá un flujo completo y seguro para trabajar con OpenCode en repositorios reales.

## Objetivos de Aprendizaje

- Diseñar un flujo de ramas que integre el trabajo del agente sin comprometer `main`.
- Usar commits asistidos por OpenCode manteniendo el control sobre el mensaje y el contenido.
- Aplicar worktrees para trabajar en paralelo sobre varias tareas del mismo repositorio.
- Usar snapshots, revert por etapas y diffs por turno para auditar y deshacer cambios.
- Configurar permisos para que operaciones sensibles (`git push`, etc.) pidan aprobación.

## Conceptos Clave

### OpenCode y Git: roles claros

OpenCode ejecuta comandos git como herramientas shell dentro del repositorio, pero el desarrollador conserva el control mediante permisos:

```jsonc
{
  "permissions": [
    { "action": "shell", "resource": "git push *", "effect": "ask" },
    { "action": "shell", "resource": "git commit *", "effect": "allow" }
  ]
}
```

Las reglas se evalúan en orden y **gana la última regla que coincide**. Esto permite, por ejemplo, permitir commits libres pero exigir confirmación para pushes.

### Flujo de ramas recomendado

```bash
# 1. Rama dedicada por tarea (nunca trabajar directo en main)
git checkout -b feature/auth-refactor

# 2. Trabajar con OpenCode en la rama
opencode "Refactoriza la lógica de autenticación hacia src/auth/"

# 3. Revisar el diff del turno antes de commitear (ver API abajo)

# 4. Commit: tú decides el mensaje
git add .
git commit -m "refactor: extract auth logic"

# 5. Push solo con aprobación (si configuraste el permiso ask)
git push -u origin feature/auth-refactor
```

Buenas prácticas:

- Pide a OpenCode que trabaje en pasos pequeños y commiteables.
- Usa el agente `plan` antes de tocar ramas compartidas: explora y planea sin editar.
- Revisa siempre `git status` y `git diff` antes de aceptar un commit propuesto.

### Worktrees: paralelismo sin conflictos

OpenCode v2 soporta worktrees de Git para tener varias copias de trabajo del mismo repo:

```jsonc
{
  "worktree": {
    "directory": "../worktrees"   // base para los worktrees nuevos
  }
}
```

Las rutas relativas se resuelven contra el checkout canónico del proyecto; `~/` se resuelve contra el home del usuario. Sin esta configuración, los worktrees se crean bajo el directorio de datos del servidor (`worktree/<prefijo-ID-proyecto>`). La creación y actualización de worktrees carga la configuración desde el checkout canónico del proyecto.

Caso de uso típico: sesión A arregla un hotfix en `main` mientras la sesión B implementa la feature en su propio worktree, sin interferencias.

### Snapshots, revert y diffs por turno

- **Snapshots**: OpenCode toma snapshots del sistema de archivos que habilitan deshacer/rehacer (`snapshots: false` en config los desactiva).
- **Revert por etapas** (API): `POST /api/session/{id}/revert/stage` marca un límite reversible y opcionalmente aplica sus cambios de archivos; `POST .../revert/commit` confirma y `DELETE .../revert` limpia el revert preparado.
- **Diff por turno**: `GET /api/session/{id}/diff?from=<messageID>` devuelve diffs estructurados por archivo de lo que cambió un turno (desde el primer prompt tras el último estado idle hasta el siguiente).

```bash
# Diff de lo que el agente cambió en su último turno
curl -s "http://localhost:4096/api/session/<ID>/diff" | jq .
```

### Conflictos y resolución

Cuando un worktree o rama choca con `main`:

1. Sincroniza: `git fetch origin && git rebase origin/main` (o merge).
2. Pide a OpenCode que explique los conflictos: pega los bloques `<<<<<<<` o pide que lea los archivos afectados.
3. Resuelve con criterio: el agente propone, tú decides — especialmente en cambios de API públicas o lógica de negocio.
4. Verifica con tests antes de continuar el rebase.

### Pull requests con revisión asistida

Crea un subagente revisor de solo lectura y úsalo antes de abrir el PR:

```markdown
<!-- .opencode/agents/reviewer.md -->
---
description: Reviews changes for correctness and regressions
mode: subagent
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: shell
    resource: "*"
    effect: deny
---

Review the current changes. List findings in severity order with file and line references.
```

```bash
git push -u origin feature/auth-refactor
gh pr create --fill
# En la sesión de OpenCode: "Use the reviewer subagent to review my current changes."
```

## Guía Paso a Paso

### Paso 1: Preparar el repositorio y los permisos

Configura en `opencode.jsonc`: `git commit` permitido, `git push` con `ask`. Verifica que `.gitignore` excluye artefactos del agente si aplica.

### Paso 2: Crear la rama y planear

```bash
git checkout -b feature/mejora-cache
opencode  # y en la sesión: "Explora el código de caché y propone un plan"
```

Usa el agente `plan` (de solo lectura) para que la exploración no modifique archivos.

### Paso 3: Implementar en pasos pequeños

Pide cambios incrementales; tras cada uno, revisa el diff por turno:

```bash
curl -s "http://localhost:4096/api/session/<ID>/diff"
```

### Paso 4: Revertir si algo salió mal

```bash
# Prepara un revert hasta un mensaje concreto
curl -X POST http://localhost:4096/api/session/<ID>/revert/stage \
  -H "Content-Type: application/json" \
  -d '{"messageID": "<id-mensaje>"}'

# Confirma o descarta
curl -X POST http://localhost:4096/api/session/<ID>/revert/commit
```

### Paso 5: Commit, push y PR

Revisa `git status`, haz commit con mensaje propio, push (con aprobación si lo configuraste) y abre el PR tras la revisión del subagente `reviewer`.

### Paso 6: Paralelismo con worktrees

Configura `worktree.directory`, crea una segunda sesión en un worktree nuevo y trabaja dos tareas simultáneas; verifica que cada sesión ve solo su copia de archivos.

## Referencia Rápida

| Comando / Endpoint | Descripción | Ejemplo |
|--------------------|-------------|---------|
| `git checkout -b <rama>` | Rama nueva por tarea | `git checkout -b feature/x` |
| `GET /api/session/{id}/diff` | Diff por turno del agente | `curl ".../diff?from=<msg>"` |
| `POST .../revert/stage` | Prepara revert a un mensaje | ver Paso 4 |
| `POST .../revert/commit` | Confirma el revert | — |
| `worktree.directory` | Base de worktrees en config | `"../worktrees"` |
| `snapshots: false` | Desactiva snapshots (config) | — |
| `permissions` ask en `git push` | Push con aprobación | ver Conceptos |
| `gh pr create --fill` | Abre PR con el diff | — |

## Ejercicios Guiados

1. **Flujo básico:** en un repo de práctica, ejecuta los pasos 1–5 completos: rama → plan → implementación con revisión de diff por turno → commit → PR con revisor.
2. **Conflicto guiado:** crea el mismo cambio en dos ramas, provoca el conflicto al hacer rebase y resuélvelo con ayuda de OpenCode, documentando qué aceptaste o rechazaste de su propuesta.
3. **Worktrees:** configura `worktree.directory` y trabaja dos tareas en paralelo sobre el mismo repo; demuestra que los cambios de una sesión no aparecen en la otra hasta el merge.

## Ejercicio Desafío

Diseña el "Git workflow del curso" para tu equipo: convención de ramas y mensajes, política de permisos (qué pide `ask`), cuándo usar worktrees, cuándo activar/desactivar snapshots, y una checklist de revisión con el subagente `reviewer` antes de cada PR. Aplícalo en un repositorio real durante una semana y ajusta lo que falle.

## Recursos Adicionales

- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (`permissions`, `worktree`, `snapshots`)
- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (subagente de revisión)
- Presentación de la clase: `presentaciones/nuevas-clases/34-flujo-git.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/34-flujo-git.pptx`

## Autoevaluación

- [ ] Puedo configurar permisos para que `git push` pida aprobación y `git commit` no.
- [ ] Sé obtener el diff exacto de lo que cambió el agente en un turno.
- [ ] Puedo preparar, confirmar y descartar un revert por etapas vía API.
- [ ] Sé configurar y usar worktrees para trabajo en paralelo.
- [ ] Puedo crear y usar un subagente revisor de solo lectura antes de un PR.
- [ ] Tengo clara la regla de resolución de conflictos: el agente propone, yo decido.
