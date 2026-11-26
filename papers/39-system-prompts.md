---
title: "Clase 39: System Prompts"
module: 39
duration: "1 hora"
prerequisites: "Módulo 38 - Clase 38: Seguridad Avanzada"
---

# Clase 39: System Prompts

> **Actualizado a OpenCode v2.** En v2 los system prompts se construyen por capas: el system del agente (campo `system` en config o cuerpo del `.md` en `.opencode/agents/`), las instrucciones de proyecto (`AGENTS.md` y la lista `instructions` del config), skills, referencias y ajustes por request (`request.headers`/`body`). Los campos legacy de v1 (`prompt`, `temperature`, `tools`, `maxSteps`, etc.) están deprecados.

## Resumen Ejecutivo

Esta clase cubre cómo se compone y personaliza el comportamiento del agente mediante system prompts: la jerarquía de instrucciones que OpenCode ensambla en cada llamada al modelo, cómo definir agentes con identidad propia (propósito, tono, límites), cómo inyectar instrucciones de proyecto sin tocar el prompt del agente, y cómo afinar parámetros de generación por agente.

A lo largo de la sesión se exploran los siguientes temas: la anatomía del system prompt en v2, agentes Markdown con frontmatter, AGENTS.md y la lista `instructions`, override de agentes built-in y ajustes por request. Al finalizar, el estudiante podrá diseñar agentes especializados consistentes y mantenibles para su equipo.

## Objetivos de Aprendizaje

- Explicar las capas que componen el system prompt final en una sesión v2.
- Crear agentes en Markdown (`.opencode/agents/*.md`) con frontmatter completo.
- Usar `AGENTS.md` e `instructions` para instrucciones de proyecto independientes del agente.
- Sobreescribir agentes built-in (`build`, `plan`) sin perder sus capacidades.
- Ajustar temperatura y headers por agente con el campo `request`.

## Conceptos Clave

### Anatomía del system prompt en v2

El prompt de sistema que recibe el modelo es una composición de capas (las fuentes de instrucción del proyecto se añaden siempre, aunque el agente defina `system`):

1. **System del agente**: campo `system` en la entrada `agents.<id>` del config, o el cuerpo del archivo Markdown del agente. Un valor no vacío **reemplaza** el prompt base del proveedor para ese agente.
2. **Instrucciones de proyecto**: `AGENTS.md` descubierto en el proyecto, más los archivos/globs/URLs listados en `instructions`.
3. **Skills**: documentación de skills activas disponibles para el modelo.
4. **Referencias**: contexto de apoyo nombrado (`references` en config).
5. **Ajustes de request**: headers y body por agente (`request.headers`, `request.body`).

Consecuencia práctica: no necesitas repetir las reglas del proyecto en cada agente; viven en `AGENTS.md` y aplican a todos.

### Agentes en Markdown

```markdown
<!-- .opencode/agents/reviewer.md -->
---
description: Reviews database migrations for safety
mode: subagent
model: anthropic/claude-sonnet-5-5#high
permissions:
  - action: edit
    resource: "*"
    effect: deny
  - action: shell
    resource: "*"
    effect: deny
steps: 8
color: "#ff6b6b"
---

Review the current changes. List findings in severity order with file and line references.
Focus on correctness, security and missing tests. Never modify files.
```

- El frontmatter acepta los mismos campos que una entrada `agents` del config; el cuerpo del documento es el `system` del agente.
- Guardado global (`~/.config/opencode/agents/`) o por proyecto (`.opencode/agents/`); una ruta anidada forma parte del ID: `team/reviewer`.
- Campos útiles: `description` (la ve el modelo que elige subagentes), `mode` (`primary`/`subagent`/`all`), `model`, `permissions`, `steps` (tope de pasos; en el último paso quita herramientas y pide resumen en texto), `hidden`, `color`, `disabled`, `request`.
- Los campos de frontmatter de v1 están deprecados; los archivos antiguos siguen leyéndose, pero no uses `prompt`, `tools`, `maxSteps`, etc., en configs nuevas.

### AGENTS.md e instructions

`AGENTS.md` en la raíz del proyecto es el archivo de instrucciones por defecto (convenciones de código, comandos de test, estilo de commits). Para añadir más fuentes sin renombrar nada:

```jsonc
{
  "instructions": ["CONTRIBUTING.md", "docs/guidelines/*.md", "https://ejemplo.com/reglas.md"]
}
```

Las instrucciones son la capa más estable del system prompt: no se pierden al compactar y aplican a todos los agentes.

### Override de agentes built-in

Usar el mismo ID reemplaza la configuración del built-in (las reglas de permisos se anexan a las globales):

```jsonc
{
  "agents": {
    "build": {
      "permissions": [
        { "action": "shell", "resource": "git push *", "effect": "ask" }
      ]
    },
    "plan": { "disabled": true }
  }
}
```

Los agentes visibles built-in son: `build` (primary, codificación por defecto), `plan` (primary, explora y planea sin editar), `general` (subagente, investigación de varios pasos) y `explore` (subagente, búsqueda y lectura sin editar). Los agentes ocultos `compaction`, `title` y `summary` hacen mantenimiento y no se pueden seleccionar.

### Ajustes por request

```jsonc
{
  "agents": {
    "creativo": {
      "request": {
        "headers": { "x-agent": "creativo" },
        "body": { "temperature": 0.7 }
      }
    }
  }
}
```

Útil para enrutado en proxies corporativos, observabilidad por agente o comportamiento determinista en revisores (`temperature: 0.1`).

## Guía Paso a Paso

### Paso 1: Leer la composición actual

Crea una sesión y pide: "Enumera las instrucciones de proyecto que tienes cargadas". Verifica que `AGENTS.md` aparece y que no está duplicado en el system del agente.

### Paso 2: Agente Markdown especializado

Crea `.opencode/agents/doc-writer.md` con descripción, modo subagente, permisos de solo escritura en `docs/**` y un system con tono y formato. Invócalo: "Use the doc-writer subagent to document the auth module".

### Paso 3: Instrucciones de proyecto

Escribe `AGENTS.md` con: comandos de test, convenciones de commits, estructura del repo. Añade una segunda fuente con `instructions` y verifica que ambas se cargan.

### Paso 4: Override de built-in

Configura `build` para pedir confirmación en `git push` y desactiva `plan` si no lo usas. Prueba que el comportamiento cambió sin romper el resto.

### Paso 5: Afinado por request

Añade `request.body.temperature` bajo a un revisor y `request.headers` de enrutado a otro; compara consistencia de salidas entre ambos en la misma tarea.

## Referencia Rápida

| Elemento | Dónde | Qué define |
|----------|-------|-----------|
| Cuerpo de `.opencode/agents/<id>.md` | proyecto o global | system del agente |
| `system` en `agents.<id>` | `opencode.jsonc` | system del agente (reemplaza base del proveedor) |
| `AGENTS.md` | raíz del proyecto | instrucciones de proyecto |
| `instructions: [...]` | `opencode.jsonc` | fuentes extra de instrucciones |
| `description` | frontmatter/agente | propósito (lo lee el modelo) |
| `mode` | frontmatter/agente | `primary` / `subagent` / `all` |
| `steps` | frontmatter/agente | tope de pasos del agente |
| `request.body` | agente | ajustes como `temperature` |
| Override por ID | `agents.<id-built-in>` | reemplaza/amplía el built-in |

## Ejercicios Guiados

1. **Descomposición:** dado un agente genérico con todo el comportamiento en el system, extrae las reglas de proyecto a `AGENTS.md` y deja en el agente solo lo específico de su rol.
2. **Tres especialistas:** crea `explorador`, `implementador` y `revisor` con modos, permisos y modelos distintos; orquesta una tarea real que los use en secuencia.
3. **Override seguro:** personaliza `build` con un permiso `ask` y un header de observabilidad, verificando que las capacidades por defecto se conservan.

## Ejercicio Desafío

Diseña el "sistema de agentes" de tu organización: catálogo de agentes (ID, propósito, modo, modelo, permisos, steps), qué vive en `AGENTS.md` vs. en cada system, convenciones de `description` para que el modelo elija bien los subagentes, y un proceso de revisión trimestral de prompts. Documenta un caso donde un prompt mal diseñado causó un comportamiento indeseado y cómo lo corregiste con esta estructura.

## Recursos Adicionales

- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (frontmatter, modos, override, `request`)
- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (`agents`, `instructions`, `references`)
- Presentación de la clase: `presentaciones/nuevas-clases/39-system-prompts.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/39-system-prompts.pptx`

## Autoevaluación

- [ ] Puedo enumerar las capas del system prompt final en v2.
- [ ] Sé crear un agente Markdown con frontmatter completo.
- [ ] Puedo separar instrucciones de proyecto (AGENTS.md) de las del agente.
- [ ] Sé sobreescribir un built-in conservando sus capacidades.
- [ ] Puedo ajustar `temperature` y headers por agente.
- [ ] Conozco los campos legacy de v1 y sé evitarlos.
