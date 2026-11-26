---
title: "Clase 40: Testing y Calidad de Código"
module: 40
duration: "1 hora"
prerequisites: "Módulo 39 - Clase 39: System Prompts"
---

# Clase 40: Testing y Calidad de Código

> **Actualizado a OpenCode v2.** En v2 el trabajo de calidad se apoya en: el agente `plan` (explora sin editar), subagentes especializados (`reviewer` de solo lectura, `explore` para mapear código), comandos personalizados (`commands` en config o `.opencode/commands/`), pasos limitados (`steps`), formatter automático (`formatter: true`) y las herramientas de seguridad del ciclo de trabajo (snapshots, revert por etapas, diffs por turno).

## Resumen Ejecutivo

Esta clase cubre cómo usar OpenCode para elevar la calidad del código: generación de tests asistida, revisión sistemática con subagentes de solo lectura, verificación de cambios con diffs por turno y construcción de una rutina de calidad repetible mediante comandos personalizados. El principio rector: el agente propone y ejecuta; los tests y la revisión son la red de seguridad que tú controlas.

A lo largo de la sesión se exploran los siguientes temas: estrategia de testing con OpenCode, revisión de código con subagentes, comandos personalizados para rutinas de calidad, verificación de cambios (diff por turno, revert) y métricas de calidad. Al finalizar, el estudiante tendrá un pipeline de calidad integrado en su flujo de trabajo diario.

## Objetivos de Aprendizaje

- Diseñar una estrategia de testing donde OpenCode genera tests y tú defines cobertura y criterios.
- Crear y usar subagentes revisores de solo lectura con permisos restrictivos.
- Definir comandos personalizados (slash commands) para rutinas repetibles de calidad.
- Verificar los cambios del agente con diff por turno y revert por etapas antes de aceptarlos.
- Configurar formato automático de archivos modificados.

## Conceptos Clave

### Estrategia de testing asistido

Flujo recomendado:

1. **Explorar** (agente `plan` o subagente `explore`): mapear el módulo y los tests existentes sin editar nada.
2. **Plan de tests**: pedir una lista de casos (normales, límite, error) ordenados por riesgo.
3. **Generar**: implementar los tests de a uno, ejecutando tras cada uno.
4. **Verificar**: correr la suite completa y revisar el diff por turno.
5. **Refinar**: pedir mutaciones dirigidas (¿qué assertions faltan?).

```bash
# Ejecutar tests dentro de la sesión (el agente puede hacerlo con su herramienta shell)
npm test
# o dejar que sea parte del prompt: "Implementa X y ejecuta los tests hasta que pasen"
```

### Revisión con subagentes de solo lectura

```markdown
<!-- .opencode/agents/reviewer.md -->
---
description: Reviews changes for correctness, security and missing tests
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
Check: correctness, security, missing tests, error handling. Never modify files.
```

Patrones de uso:

- Antes de cada commit: "Use the reviewer subagent on my current changes."
- Con modelo de alta variante si la criticidad lo merece: `model: "...#high"`.
- Con `steps: 8` para que resuma en texto si se alarga.

### Comandos personalizados (slash commands)

Definición en config o archivos en `.opencode/commands/`:

```jsonc
{
  "commands": {
    "test-coverage": {
      "description": "Analiza cobertura y propone tests faltantes",
      "template": "Analiza la cobertura de tests de {{args}}. Lista los casos faltantes por riesgo e implementa el más importante."
    }
  }
}
```

Úsalo en la TUI con `/test-coverage src/auth/`. Los comandos son plantillas de prompt versionables en el repo: la rutina de calidad queda documentada y repetible.

### Verificación de cambios del agente

Antes de aceptar el trabajo del agente:

```bash
# Diff estructurado de lo que cambió en el último turno
curl -s "http://localhost:4096/api/session/<ID>/diff"

# Revert preparado hasta un mensaje concreto si algo no convence
curl -X POST http://localhost:4096/api/session/<ID>/revert/stage \
  -H "Content-Type: application/json" -d '{"messageID": "<id>"}'
```

Complementos: `snapshots` habilitan deshacer/rehacer en la UI; `formatter: true` formatea tras write/edit/patch; `tool_output` limitado evita que salidas enormes de tests contaminen el contexto (ver Clase 33).

### Métricas y gates de calidad

- Define gates explícitos en `AGENTS.md`: "los tests deben pasar antes de commitear", "cobertura mínima del 80% en src/".
- Usa `/api/experimental/session/stats` para auditar fiabilidad de herramientas (¿fallan los runs de tests con frecuencia?).
- Registra hallazgos del revisor en issues antes de que el contexto de la sesión se compacte.

## Guía Paso a Paso

### Paso 1: Baseline

En un proyecto con tests existentes, pide a OpenCode que mapee la cobertura actual y los puntos débiles (subagente `explore`).

### Paso 2: Generación guiada

Pide los 5 tests de mayor impacto para el módulo objetivo. Implementa el primero, ejecútalo, revisa el diff por turno; repite. Rechaza (revert) cualquier test que no falle por las razones correctas.

### Paso 3: Comando de rutina

Crea el comando `test-coverage` y úsalo sobre un módulo distinto; ajusta la plantilla según lo que falte (mutaciones, casos límite, tests de error).

### Paso 4: Revisión sistemática

Antes del commit, lanza el subagente `reviewer` con el modelo de variante alta; convierte cada hallazgo en una tarea concreta y repite hasta cero hallazgos de severidad alta.

### Paso 5: Auditoría

Semanalmente, revisa `/api/experimental/session/stats?tools=detail` para detectar herramientas con fallos recurrentes (tests que fallan intermitentes, comandos mal formados) y ajusta prompts o configuración.

## Referencia Rápida

| Elemento | Descripción | Ejemplo |
|----------|-------------|---------|
| Agente `plan` | Explora y planea sin editar | selección en la sesión |
| Subagente `reviewer` | Revisor de solo lectura | ver Conceptos |
| `commands` | Slash commands de rutina | `/test-coverage src/` |
| `GET /api/session/{id}/diff` | Cambios del turno | verificación previa |
| `POST .../revert/stage` | Revert preparado | deshacer un turno |
| `formatter: true` | Formatea tras editar | config |
| `steps: N` | Tope de pasos del agente | 8 |
| `/api/experimental/session/stats` | Fiabilidad de herramientas | auditoría |

## Ejercicios Guiados

1. **TDD asistido:** implementa una función nueva con el flujo explorar → plan de tests → generación uno a uno → suite completa; registra cuántos tests rechazaste y por qué.
2. **Revisor en acción:** introduce a propósito 3 bugs sutiles en una rama y verifica que el subagente `reviewer` los detecta; ajusta su system prompt si algo se escapa.
3. **Comando de equipo:** define un comando `/quality-check` que revise diff, corra tests y formatee; úsalo durante 3 días y mejora su plantilla con lo aprendido.

## Ejercicio Desafío

Construye el "gate de calidad" pre-merge de tu equipo: subagente revisor obligatorio, suite de tests con umbral de cobertura, comando `/pre-merge` que lo orquesta, y auditoría semanal automática de fiabilidad de herramientas. Preséntalo con evidencia: antes/después de un PR real (hallazgos detectados, tiempo de revisión, cobertura).

## Recursos Adicionales

- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (`plan`, subagentes, `steps`)
- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (`commands`, `formatter`, `tool_output`)
- [Referencia de la API del servidor](https://opencode.ai/docs/server) (`diff`, `revert`, `stats`)
- Presentación de la clase: `presentaciones/nuevas-clases/40-testing-calidad.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/40-testing-calidad.pptx`

## Autoevaluación

- [ ] Puedo ejecutar un ciclo completo de testing asistido (explorar → tests → verificación).
- [ ] Sé crear un revisor de solo lectura con permisos deny.
- [ ] Puedo definir y usar un slash command de rutina de calidad.
- [ ] Sé verificar un turno del agente con diff y revertirlo si no convence.
- [ ] Puedo auditar la fiabilidad de herramientas con `/session/stats`.
- [ ] Tengo gates de calidad documentados en `AGENTS.md`.
