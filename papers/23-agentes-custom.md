---
title: "Agentes Custom"
module: 23
duration: "50 min"
prerequisites: "Módulo 22 - Agentes Primarios y Subagentes"
---

# Clase 23: Agentes Custom

## Resumen Ejecutivo

OpenCode permite crear agentes personalizados (custom agents) que se adaptan a las necesidades específicas de cada proyecto o flujo de trabajo. Estos agentes se definen mediante archivos Markdown con frontmatter YAML en el directorio `.opencode/agents/` y se pueden configurar opciones avanzadas como modelo, temperatura, herramientas disponibles y permisos. Los agentes custom complementan los agentes primarios build y plan, ofreciendo flexibilidad total para crear roles especializados como revisores de código, generadores de documentación, o asistentes de testing.

La configuración de agentes custom se integra completamente con el sistema existente, permitiendo establecer un agente custom como predeterminado, configurar permisos granulares, y definir prompts específicos que guíen el comportamiento del agente.

## Objetivos de Aprendizaje
- Crear agentes personalizados en `.opencode/agents/` con frontmatter YAML
- Configurar propiedades avanzadas: modelo, temperatura, herramientas, permisos
- Distinguir entre modo primary y subagent para agentes custom
- Establecer un agente custom como predeterminado
- Gestionar permisos granulares por herramienta

## Conceptos Clave

### Estructura de un Archivo de Agente Custom

Los agentes custom se definen como archivos Markdown en el directorio `.opencode/agents/`. Cada archivo contiene frontmatter YAML con la configuración del agente y el cuerpo del archivo define el prompt del agente.

```markdown
---
description: "Agente especializado en revisión de código"
model: "anthropic/claude-sonnet-4-20250514"
temperature: 0.3
tools:
  - read
  - edit
  - grep
  - glob
  - bash
permission:
  edit: true
  bash: true
  webfetch: false
mode: primary
---

Eres un agente especializado en revisión de código. Tu tarea es:

1. Analizar el código fuente en busca de problemas
2. Identificar malas prácticas y sugerir mejoras
3. Verificar la adherencia a estándares de codificación
4. Reportar hallazgos de forma clara y concisa

Al revisar código, sigue estos principios:
- Prioriza la legibilidad sobre la complejidad
- Verifica la seguridad en operaciones sensibles
- Sugiere alternativas cuando sea apropiado
- Proporiona ejemplos de código corregido
```

### Campos Disponibles en el Frontmatter

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `description` | string | Descripción breve del agente | `"Revisor de código"` |
| `model` | string | Modelo de IA a utilizar | `"anthropic/claude-sonnet-4-20250514"` |
| `temperature` | number | Temperatura de generación (0-1) | `0.3` |
| `tools` | array | Herramientas disponibles | `["read", "edit", "grep"]` |
| `permission` | object | Permisos por herramienta | `{"edit": true, "bash": true}` |
| `mode` | string | Modo de operación | `"primary"` o `"subagent"` |

### Modo Primary vs Subagent

Los agentes custom pueden operar en dos modos:

#### Modo Primary
Un agente en modo primary puede ser seleccionado como agente principal de trabajo. El usuario puede cambiar a este agente usando Tab o `switch_agent`. Los agentes en modo primary tienen acceso completo a las herramientas según sus permisos configurados.

```yaml
mode: primary
```

#### Modo Subagent
Un agente en modo subagent solo puede ser invocado como subagente, ya sea automáticamente por otro agente o manualmente mediante @mention. No puede seleccionarse como agente principal.

```yaml
mode: subagent
```

### Configuración del Agente por Defecto

Para establecer un agente custom como predeterminado, se configura en `opencode.json`:

```json
{
  "agent": {
    "default": "mi-agente-custom"
  }
}
```

El nombre del agente corresponde al nombre del archivo sin extensión. Por ejemplo, un archivo `revisor.md` se referencia como `revisor`.

### Configuración en opencode.json

Además de los archivos Markdown, se puede configurar agentes directamente en `opencode.json` bajo la clave `agent`:

```json
{
  "agent": {
    "default": "build",
    "custom": {
      "mi-agente": {
        "description": "Agente personalizado",
        "model": "anthropic/claude-sonnet-4-20250514",
        "temperature": 0.5
      }
    }
  }
}
```

### Gestión de Permisos

Los permisos controlan qué herramientas puede usar un agente. Se pueden configurar permisos a nivel global y por herramienta específica:

```yaml
permission:
  # Permisos globales
  edit: true
  bash: true
  read: true
  
  # Permisos específicos
  webfetch: false
  websearch: false
  
  # Permisos de bash con restricciones
  bash:
    allowed_commands:
      - "npm run test"
      - "npm run lint"
      - "git status"
```

### Configuración de Modelo y Temperatura

El modelo y la temperatura determinan el comportamiento de generación del agente:

```yaml
# Modelo específico
model: "anthropic/claude-sonnet-4-20250514"

# Temperatura baja para tareas precisas (0.0 - 0.3)
temperature: 0.2

# Temperatura media para tareas equilibradas (0.4 - 0.6)
temperature: 0.5

# Temperatura alta para tareas creativas (0.7 - 1.0)
temperature: 0.8
```

## Guía Paso a Paso

### Paso 1: Crear el Directorio de Agentes

```bash
# Crear el directorio si no existe
mkdir -p .opencode/agents
```

### Paso 2: Crear un Archivo de Agente Custom

```markdown
<!-- .opencode/agents/testing-assistant.md -->
---
description: "Asistente especializado en testing y QA"
model: "anthropic/claude-sonnet-4-20250514"
temperature: 0.3
tools:
  - read
  - edit
  - grep
  - glob
  - bash
permission:
  edit: true
  bash: true
  webfetch: false
mode: subagent
---

Eres un asistente especializado en testing y aseguramiento de calidad.

## Tu rol
- Crear pruebas unitarias y de integración
- Analizar cobertura de código
- Identificar casos edge faltantes
- Sugiere mejoras en la estrategia de testing

## Herramientas disponibles
- Lee archivos de código fuente
- Escribe archivos de prueba
- Ejecuta comandos de testing
- Busca patrones en el código

## Estándares
- Usa el framework de testing existente del proyecto
- Sigue las convenciones de nombrado de archivos
- Incluye describe/it blocks descriptivos
- Mockea dependencias externas appropriately
```

### Paso 3: Configurar el Agente como Predeterminado

```json
// opencode.json
{
  "agent": {
    "default": "testing-assistant"
  }
}
```

### Paso 4: Verificar la Carga del Agente

```bash
# Reiniciar OpenCode para cargar los cambios
# El agente debería aparecer en la lista de agentes disponibles
opencode
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `.opencode/agents/*.md` | Archivos de agentes custom | `revisor.md` |
| `agent.default` | Agente predeterminado | `"mi-agente"` |
| `mode: primary` | Agente puede ser principal | En frontmatter |
| `mode: subagent` | Agente solo es invocable | En frontmatter |
| `model` | Modelo de IA a usar | `"anthropic/claude-sonnet-4-20250514"` |
| `temperature` | Control de creatividad | `0.3` |
| `tools` | Herramientas disponibles | `["read", "edit"]` |
| `permission` | Control de acceso | `{"edit": true}` |

## Ejercicios Guiados

### Ejercicio 1: Crear un Agente de Revisión de Código
**Objetivo:** Crear un agente custom especializado en revisión de código con permisos específicos.

**Instrucciones:**
1. Crea el directorio `.opencode/agents/` si no existe
2. Crea un archivo `code-reviewer.md` con el frontmatter apropiado
3. Define las herramientas necesarias para revisión (read, grep, glob)
4. Configura permisos para permitir solo lectura (edit: false)
5. Establece un prompt que guíe al agente en la revisión

**Solución Esperada:**
```markdown
---
description: "Revisor de código especializado"
model: "anthropic/claude-sonnet-4-20250514"
temperature: 0.2
tools:
  - read
  - grep
  - glob
permission:
  edit: false
  bash: false
  read: true
mode: subagent
---

Eres un revisor de código experto. Tu tarea es analizar el código fuente y proporcionar retroalimentación constructiva.

## Áreas de revisión
- Legibilidad y mantenibilidad
- Seguridad
- Rendimiento
- Patrones de diseño
- Manejo de errores

## Formato de reporte
Para cada hallazgo, incluye:
1. Ubicación exacta (archivo:línea)
2. Descripción del problema
3. Impacto potencial
4. Sugerencia de mejora con código de ejemplo
```

### Ejercicio 2: Configurar un Agente como Predeterminado
**Objetivo:** Establecer un agente custom como el agente principal de trabajo.

**Instrucciones:**
1. Crea un agente custom llamado `daily-dev.md` en `.opencode/agents/`
2. Configúralo en modo primary
3. Define herramientas completas para desarrollo diario
4. Establece el agente como predeterminado en `opencode.json`
5. Verifica que el agente se carga correctamente al iniciar OpenCode

**Solución Esperada:**
```markdown
---
description: "Agente de desarrollo diario"
model: "anthropic/claude-sonnet-4-20250514"
temperature: 0.4
tools:
  - read
  - edit
  - grep
  - glob
  - bash
permission:
  edit: true
  bash: true
  webfetch: true
mode: primary
---

Eres un asistente de desarrollo diario. Ayudas con:
- Tareas de codificación rutinarias
- Ejecución de comandos de build y test
- Gestión de Git
- Resolución de problemas comunes
```

```json
// opencode.json
{
  "agent": {
    "default": "daily-dev"
  }
}
```

### Ejercicio 3: Crear un Agente con Restricciones de Bash
**Objetivo:** Configurar un agente con permisos de bash restringidos a comandos específicos.

**Instrucciones:**
1. Crea un agente `safe-runner.md` que solo pueda ejecutar comandos de testing
2. Configura permisos de bash con lista blanca de comandos
3. Incluye herramientas de lectura para analizar resultados
4. Verifica que el agente no puede ejecutar comandos no autorizados

**Solución Esperada:**
```markdown
---
description: "Ejecutor seguro de comandos de testing"
model: "anthropic/claude-sonnet-4-20250514"
temperature: 0.1
tools:
  - read
  - grep
  - bash
permission:
  edit: false
  bash:
    allowed_commands:
      - "npm run test"
      - "npm run test:coverage"
      - "npm run lint"
      - "pytest"
      - "cargo test"
  webfetch: false
mode: subagent
---

Eres un ejecutor seguro de comandos de testing.

## Comandos permitidos
Solo puedes ejecutar:
- npm run test
- npm run test:coverage
- npm run lint
- pytest
- cargo test

## Procedimiento
1. Antes de ejecutar, verifica que el comando esté en la lista blanca
2. Ejecuta el comando y captura la salida
3. Analiza los resultados
4. Reporta éxitos y fallos de forma clara
```

## Ejercicio Desafío

**Reto:** Crea un sistema de agentes custom para un proyecto completo. Diseña:
1. Un agente `architect` (modo primary) para diseño de arquitectura
2. Un agente `implementer` (modo subagent) para implementar cambios
3. Un agente `reviewer` (modo subagent) para revisar código
4. Un agente `documenter` (modo subagent) para generar documentación

Cada agente debe tener permisos y herramientas apropiadas para su rol. Configura el architect como predeterminado y verifica que puede invocar a los demás agentes como subagentes.

**Pistas:**
- El architect necesita permisos de lectura pero no de escritura directa
- El implementer necesita permisos completos de edición
- El reviewer solo necesita permisos de lectura
- El documenter necesita acceso a webfetch para referencias
- Usa `subagent_depth: 2` para permitir que el architect cree subagentes

## Recursos Adicionales
- [Documentación oficial de OpenCode - Agentes Custom](https://opencode.ai/docs/agents/custom)
- [Referencia de configuración de agentes](https://opencode.ai/docs/configuration/agents)
- [Guía de permisos de agentes](https://opencode.ai/docs/agents/permissions)

## Autoevaluación
- [ ] Puedo crear un archivo de agente custom con frontmatter YAML válido
- [ ] Entiendo la diferencia entre modo primary y subagent
- [ ] Sé configurar modelo, temperatura y herramientas para un agente
- [ ] Puedo establecer un agente custom como predeterminado
- [ ] Sé configurar permisos granulares por herramienta
- [ ] Puedo crear agentes con restricciones de bash específicas
