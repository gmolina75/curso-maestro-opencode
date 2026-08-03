# Glosario Completo del Curso Maestro de OpenCode

## Referencia de Términos, Conceptos y Comandos

---

## A

### ACI (Agent Communication Interface)
Protocolo de comunicación que permite la interacción entre agentes en OpenCode. Ver [ACP Support](#acp-agent-communication-protocol) en la documentación oficial.

### ACP (Agent Communication Protocol)
Protocolo para comunicación entre agentes de IA. OpenCode soporta ACP para interoperabilidad entre diferentes sistemas de agentes.

### AGENTS.md
Archivo de contexto del proyecto que OpenCode genera automáticamente con el comando `/init`. Contiene información sobre la estructura del proyecto, convenciones de código, patrones de arquitectura y guías de desarrollo. Se carga automáticamente al iniciar OpenCode y persiste entre sesiones.

**Ubicación:** Raíz del proyecto  
**Propósito:** Proporcionar contexto persistente a los agentes de IA  
**Ejemplo de contenido:**
```markdown
# Project Structure
- src/ - Source code
- tests/ - Test files
- docs/ - Documentation

# Conventions
- Use TypeScript
- Follow ESLint rules
- Commit messages: conventional commits
```

### API Key
Clave de autenticación proporcionada por un proveedor de LLM (como Anthropic, OpenAI, etc.) para acceder a sus servicios. Se almacenan en `~/.local/share/opencode/auth.json` y se configuran con el comando `/connect`.

**Ejemplo de configuración:**
```json
{
  "provider": {
    "anthropic": {
      "options": {
        "apiKey": "{env:ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

### Autoupdate
Función que permite a OpenCode actualizarse automáticamente cuando se inicia. Se configura en `opencode.json`.

**Valores:**
- `true` - Actualizar automáticamente (default)
- `false` - No actualizar
- `"notify"` - Solo notificar cuando haya actualizaciones disponibles

**Configuración:**
```json
{
  "autoupdate": true
}
```

---

## B

### bash (Tool)
Herramienta integrada de OpenCode que permite ejecutar comandos del shell directamente desde el agente de IA. Es una de las herramientas más utilizadas para instalar paquetes, ejecutar scripts, verificar estado de git, etc.

**Permisos:** Se controla con el permiso `bash` en configuración  
**Uso típico:**
- `npm install` - Instalar dependencias
- `git status` - Ver estado del repositorio
- `npm test` - Ejecutar tests
- `ls -la` - Listar archivos

**Configuración de permisos:**
```json
{
  "permission": {
    "bash": "ask"
  }
}
```

### Blacklist (de modelos)
Lista de modelos que se excluyen del selector de modelos `/models`. Útil para ocultar modelos que no se desean usar o que no están disponibles.

**Configuración:**
```json
{
  "provider": {
    "anthropic": {
      "blacklist": ["claude-opus-4-20250514"]
    }
  }
}
```

### Build Mode
Modo de operación por defecto de OpenCode que permite al agente realizar cambios en el sistema de archivos. Tiene acceso completo a todas las herramientas: bash, edit, write, read, grep, glob, etc.

**Características:**
- Acceso completo a tools de escritura
- Ejecución de comandos shell
- Creación y modificación de archivos
- Ideal para implementación de features y bug fixing

**Activación:** Por defecto al iniciar OpenCode, o con `Tab`

---

## C

### CLI (Command Line Interface)
Interfaz de línea de comandos que permite ejecutar OpenCode de forma no interactiva. Útil para scripts, automatización y CI/CD.

**Comandos principales:**
```bash
opencode                          # Lanzar TUI
opencode run "prompt"             # Ejecutar prompt no-interactivo
opencode run "prompt" -f json     # Output JSON
opencode run "prompt" -q          # Modo quiet (sin spinner)
opencode --continue               # Continuar sesión previa
opencode --attach http://server   # Conectar a backend remoto
```

### Cloudflare AI Gateway
Gateway unificado de Cloudflare que permite acceder a múltiples proveedores de IA (OpenAI, Anthropic, Workers AI) a través de un endpoint único. Soporta Unified Billing para simplificar la facturación.

**Configuración:**
```json
{
  "provider": {
    "cloudflare-ai-gateway": {
      "models": {
        "openai/gpt-4o": {},
        "anthropic/claude-sonnet-4": {}
      }
    }
  }
}
```

### Compact / Summarize
Comando slash `/compact` o `/summarize` que reduce el contexto de la sesión actual para liberar tokens. Útil cuando la conversación se vuelve muy larga y se acerca al límite de contexto del modelo.

**Uso:** `/compact` o `/summarize`  
**Configuración de auto-compactación:**
```json
{
  "compaction": {
    "auto": true,
    "prune": false,
    "reserved": 10000
  }
}
```

### Config (opencode.json)
Archivo de configuración principal de OpenCode. Puede estar en formato JSON o JSONC (JSON con comentarios). Define la configuración del servidor, modelos, permisos, herramientas, agentes y más.

**Ubicaciones (por precedencia):**
1. Remote config (`.well-known/opencode`)
2. Global config (`~/.config/opencode/opencode.json`)
3. Custom config (`OPENCODE_CONFIG` env var)
4. Project config (`opencode.json` en raíz)

**Schema:** `https://opencode.ai/config.json`

### Context Window / Context Limit
Ventana de contexto del modelo de IA que determina cuánta información puede procesar en una sola interacción. OpenCode gestiona esto automáticamente con compactación cuando se acerca al límite.

**Configuración de compactación:**
```json
{
  "compaction": {
    "auto": true,
    "reserved": 10000
  }
}
```

### Custom Command
Comandos personalizados definidos por el usuario para tareas repetitivas. Se configuran en `opencode.json` o en archivos markdown en `.opencode/commands/`.

**Ejemplo en config:**
```json
{
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report.",
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5"
    }
  }
}
```

**Ejemplo en archivo .md:**
```markdown
---
description: Explain code in detail
---
Please provide a detailed explanation of: @$ARGUMENTS
```

### Custom Tool
Herramienta personalizada definida por el usuario que el agente de IA puede ejecutar. Se definen en el archivo de configuración y permiten ejecutar código arbitrario.

---

## D

### Default Agent
Agente primario que se utiliza cuando no se especifica uno explícito. Se configura con `default_agent` en `opencode.json`. Aplica a TUI, CLI, desktop app y GitHub Action.

**Configuración:**
```json
{
  "default_agent": "plan"
}
```

**Valores permitidos:** Agentes primarios (built-in o custom), no subagentes.

### Deny
Nivel de permiso que bloquea completamente una herramienta o acción. Cuando un tool tiene permiso `deny`, el agente no puede usarlo bajo ninguna circunstancia.

**Ejemplo:**
```json
{
  "permission": {
    "write": "deny"
  }
}
```

### Diff Style
Estilo de visualización de diferencias en la TUI. Se configura en `tui.json`.

**Valores:**
- `"auto"` - Automático según el contexto
- `"unified"` - Diferencias unificadas
- `"split"` - Diferencias lado a lado

**Configuración:**
```json
{
  "diff_style": "auto"
}
```

---

## E

### Edit (Tool)
Herramienta principal de OpenCode para modificar archivos existentes mediante reemplazos de texto exactos. Realiza ediciones quirúrgicas sin rewrite completo del archivo.

**Características:**
- Reemplazo de texto exacto (oldString → newString)
- Edición precisa sin rewrite completo
- Controlada por permiso `edit`
- Soporte para `replaceAll` para renombrar variables

**Ejemplo:**
```
oldString: "function calculateTotal(items)"
newString: "function computeTotal(items)"
```

### Environment Variable
Variable de entorno del sistema que OpenCode puede usar para configuración. Se referencian en `opencode.json` con la sintaxis `{env:VARIABLE_NAME}`.

**Variables principales:**
- `OPENCODE_CONFIG` - Ruta custom de config
- `OPENCODE_CONFIG_DIR` - Directorio custom
- `OPENCODE_TUI_CONFIG` - Ruta de TUI config
- `OPENCODE_DISABLE_AUTOUPDATE` - Desactivar auto-updates
- `OPENCODE_EXPERIMENTAL` - Habilitar features experimentales
- `OPENCODE_ENABLE_EXA` - Habilitar websearch

**Ejemplo en config:**
```json
{
  "model": "{env:OPENCODE_MODEL}"
}
```

### Export
Comando slash `/export` que exporta la conversación actual a formato Markdown. Útil para documentar sesiones de trabajo o compartir resultados.

**Uso:** `/export`

---

## F

### File Reference
Mecanismo para referenciar archivos específicos dentro de las conversaciones de OpenCode. Se usa el símbolo `@` seguido del nombre o ruta del archivo.

**Sintaxis:**
- `@nombre-archivo` - Búsqueda fuzzy
- `@src/components/Button.tsx` - Ruta específica
- `@src/index.ts#L10-20` - Líneas específicas

**Uso:** Permite al agente entender qué archivo se está discutiendo y trabajar con él directamente.

### Formatter
Herramienta de formateo de código que OpenCode puede ejecutar después de modificaciones para asegurar consistencia de estilo. Soporta Prettier, rustfmt, y formateadores personalizados.

**Configuración:**
```json
{
  "formatter": true
}
```

**Configuración detallada:**
```json
{
  "formatter": {
    "prettier": { "disabled": true },
    "custom-prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    }
  }
}
```

---

## G

### GitHub Actions
Plataforma de automatización de GitHub que OpenCode integra para ejecutar tareas en issues y pull requests. Se configura con el comando `opencode github install`.

**Eventos soportados:**
- `issue_comment` - Comentarios en issues/PRs
- `pull_request_review_comment` - Comentarios en código específico
- `issues` - Issues abiertos/editados
- `pull_request` - PRs abiertos/actualizados
- `schedule` - Tareas programadas (cron)
- `workflow_dispatch` - Trigger manual

**Workflow mínimo:**
```yaml
name: opencode
on:
  issue_comment:
    types: [created]
jobs:
  opencode:
    if: contains(github.event.comment.body, '/oc')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: anomalyco/opencode/github@latest
```

### GitLab Duo
Plataforma de agentes AI de GitLab que OpenCode integra. Requiere suscripción Premium o Ultimate. Soporta OAuth y Personal Access Token.

**Modelos disponibles:**
- `duo-chat-haiku-4-5` - Rápido
- `duo-chat-sonnet-4-5` - Balanceado
- `duo-chat-opus-4-5` - Más capaz

**Configuración:**
```json
{
  "provider": {
    "gitlab": {
      "options": {
        "instanceUrl": "https://gitlab.com"
      }
    }
  }
}
```

### Glob (Tool)
Herramienta de búsqueda de archivos por patrón. Utiliza sintaxis de glob patterns como `**/*.js` o `src/**/*.ts`. Retorna archivos ordenados por fecha de modificación.

**Sintaxis:**
- `**/*.js` - Todos los archivos .js recursivamente
- `src/**/*.ts` - Archivos .ts en src y subdirectorios
- `*.json` - Archivos .json en directorio actual

**Internals:** Usa ripgrep bajo el capó.

---

## H

### Helicone
Plataforma de observabilidad de LLM que proporciona logging, monitoreo y analíticas. OpenCode soporta Helicone como proveedor y tiene plugin para tracking de sesiones.

**Plugin:**
```bash
npm install -g opencode-helicone-session
```

**Configuración:**
```json
{
  "plugin": ["opencode-helicone-session"]
}
```

---

## I

### IDE Integration
Integración de OpenCode con editores de código como VS Code, Cursor, Windsurf y VSCodium. Permite abrir OpenCode directamente desde el editor con atajos de teclado.

**IDEs soportados:**
- VS Code
- Cursor
- Windsurf
- VSCodium
- Cualquiera con terminal integrado

**Atajos:**
- `Cmd/Ctrl+Esc` - Abrir/focus OpenCode
- `Cmd/Ctrl+Shift+Esc` - Nueva sesión
- `Cmd/Ctrl+Option+K` - Insertar referencia de archivo

### Image Attachment
Soporte para adjuntar imágenes en las conversaciones de OpenCode. Se pueden arrastrar y soltar imágenes al terminal para que el agente las analice.

**Configuración:**
```json
{
  "attachment": {
    "image": {
      "auto_resize": true,
      "max_width": 2000,
      "max_height": 2000,
      "max_base64_bytes": 5242880
    }
  }
}
```

### Init (Comando)
Comando slash `/init` que analiza el proyecto actual y crea o actualiza el archivo `AGENTS.md` con información sobre la estructura del proyecto, patrones de código y convenciones.

**Uso:** `/init`  
**Resultado:** Crea `AGENTS.md` en la raíz del proyecto  
**Recomendación:** Commitear `AGENTS.md` a Git

### Init-deep
Variante del comando `/init` que realiza una inicialización profunda, analizando subdirectorios y creando múltiples archivos AGENTS.md en diferentes niveles del proyecto.

### Instructions
Campo en `opencode.json` que permite especificar archivos de instrucciones adicionales que se cargan junto con `AGENTS.md`. Soporta paths y glob patterns.

**Configuración:**
```json
{
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines.md",
    ".cursor/rules/*.md"
  ]
}
```

---

## K

### Keybinds (Atajos de Teclado)
Configuración de atajos de teclado para la TUI de OpenCode. Se define en `tui.json` y se mergea con los defaults.

**Leader key:** `Ctrl+X` (por defecto)

**Atajos principales:**
- `Ctrl+X N` - Nueva sesión
- `Ctrl+X L` - Listar sesiones
- `Ctrl+X C` - Compactar
- `Ctrl+X S` - Compartir
- `Ctrl+X X` - Exportar
- `Ctrl+X U` - Deshacer
- `Ctrl+X R` - Rehacer
- `Ctrl+X M` - Modelos
- `Ctrl+X E` - Editor
- `Ctrl+X I` - Init
- `Ctrl+X D` - Detalles
- `Ctrl+X Q` - Salir
- `Ctrl+P` - Paleta de comandos
- `Tab` - Cambiar modo Build/Plan

**Configuración:**
```json
{
  "keybinds": {
    "command_list": "ctrl+p"
  }
}
```

---

## L

### Leader Key
Tecla principal (leader key) que se presiona antes de otros atajos de teclado en la TUI. Por defecto es `Ctrl+X`. Todos los atajos de OpenCode comienzan con esta tecla seguida de otra letra.

### LLM (Large Language Model)
Modelo de lenguaje grande. Se refiere a los modelos de IA como Claude, GPT, Gemini, etc. que OpenCode utiliza para procesar código y generar respuestas.

### LSP (Language Server Protocol)
Protocolo que permite a OpenCode obtener inteligencia de código como definiciones, referencias, hover info y diagnósticos. Se integra automáticamente con los servidores LSP del proyecto.

**Operaciones disponibles:**
- `goToDefinition` - Ir a definición
- `findReferences` - Encontrar referencias
- `hover` - Información hover
- `documentSymbol` - Símbolos del documento
- `workspaceSymbol` - Símbolos del workspace
- `goToImplementation` - Ir a implementación
- `prepareCallHierarchy` - Jerarquía de llamadas
- `incomingCalls` - Llamadas entrantes
- `outgoingCalls` - Llamadas salientes

**Habilitar:**
```json
{
  "lsp": true
}
```

**Tool experimental:**
```bash
OPENCODE_EXPERIMENTAL_LSP_TOOL=true opencode
```

---

## M

### Managed Settings
Configuración forzada por administradores de TI que los usuarios no pueden override. Se carga en la prioridad más alta.

**Plataformas:**
- macOS: `/Library/Application Support/opencode/`
- Linux: `/etc/opencode/`
- Windows: `%ProgramData%\opencode`

**macOS MDM:** Se despliega vía `.mobileconfig` con el tipo `ai.opencode.managed`

### MCP (Model Context Protocol)
Protocolo para integrar herramientas externas con modelos de IA. OpenCode soporta MCP local y remoto, permitiendo agregar funcionalidades como acceso a Sentry, Context7, etc.

**Tipos:**
- **Local:** Se ejecuta como proceso local
- **Remoto:** Se conecta a un servidor HTTP

**Configuración local:**
```json
{
  "mcp": {
    "my-mcp": {
      "type": "local",
      "command": ["npx", "-y", "my-mcp-command"],
      "enabled": true
    }
  }
}
```

**Configuración remota:**
```json
{
  "mcp": {
    "my-remote-mcp": {
      "type": "remote",
      "url": "https://my-mcp-server.com",
      "enabled": true
    }
  }
}
```

**Comandos de gestión:**
- `opencode mcp auth <server>` - Autenticar
- `opencode mcp list` - Listar servidores
- `opencode mcp logout <server>` - Cerrar sesión
- `opencode mcp debug <server>` - Debug

### Model
Configuración del modelo principal de IA que OpenCode utiliza. Se especifica en formato `proveedor/modelo`.

**Configuración:**
```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5"
}
```

**Cambio en TUI:** `/models`

### Multi-session
Capacidad de OpenCode de ejecutar múltiples agentes en paralelo en el mismo proyecto. Cada sesión tiene su propio contexto y historial.

**Gestión:**
- `/sessions` - Listar sesiones
- `/new` - Nueva sesión
- Navegación: `Leader+Down` (child), `Right/Left` (ciclar), `Up` (parent)

---

## N

### New (Comando)
Comando slash `/new` o `/clear` que inicia una nueva sesión de conversación, limpiando el contexto anterior.

**Uso:** `/new` o `/clear`  
**Atajo:** `Ctrl+X N`

---

## O

### OAuth
Protocolo de autorización que OpenCode utiliza para autenticarse con proveedores como Anthropic, OpenAI, GitHub Copilot, etc. Permite usar suscripciones existentes sin necesidad de API keys separadas.

**Proveedores con OAuth:**
- Anthropic (Claude Pro/Max)
- OpenAI (ChatGPT Plus/Pro)
- GitHub Copilot
- GitLab Duo
- DigitalOcean

### OpenCode
Agente de IA de código abierto para coding. Disponible como terminal TUI, desktop app y extensión de IDE. Soporta 75+ proveedores de LLM y permite modelos locales.

**Estadísticas:**
- 160K+ GitHub Stars
- 900+ contribuidores
- 7.5M desarrolladores mensuales

**Repositorio:** github.com/anomalyco/opencode  
**Docs:** opencode.ai/docs

### OpenCode Go
Plan de suscripción de bajo costo que proporciona acceso a modelos de código abierto populares verificados por el equipo de OpenCode.

### OpenCode Zen
Lista curada de modelos proporcionada por el equipo de OpenCode que han sido probados y verificados para funcionar bien con OpenCode. Modelo de pago pay-as-you-go ($20 saldo, auto top-up).

**Configuración:**
1. `/connect` → Seleccionar OpenCode Zen
2. Ir a opencode.ai/auth
3. Iniciar sesión y agregar datos de facturación
4. Copiar API key

### OpenRouter
Proveedor que agrega acceso a múltiples proveedores de LLM a través de una API unificada. Soporta routing inteligente y fallbacks.

---

## P

### Permission (Permiso)
Nivel de acceso que tiene el agente a diferentes herramientas y acciones. OpenCode soporta tres niveles: `allow`, `ask` y `deny`.

**Niveles:**
- `allow` - Permitir sin preguntar
- `ask` - Requiere aprobación del usuario
- `deny` - Bloquear completamente

**Configuración:**
```json
{
  "permission": {
    "bash": "ask",
    "edit": "allow",
    "write": "deny"
  }
}
```

**Patrones glob:**
```json
{
  "permission": {
    "mymcp_*": "ask"
  }
}
```

### Plan Mode
Modo de solo lectura de OpenCode que analiza código y propone cambios sin modificar nada. Ideal para explorar codebases unfamiliar y planificar features complejas.

**Características:**
- Sin capacidad de modificar archivos
- Análisis y propuestas de cambios
- Seguro para exploración
- Activación con `Tab`

### Plugin
Extensión de OpenCode que agrega herramientas, hooks o integraciones. Se carga desde npm o desde directorios locales.

**Ubicaciones:**
- `.opencode/plugins/`
- `~/.config/opencode/plugins/`
- npm packages

**Configuración:**
```json
{
  "plugin": ["opencode-helicone-session"]
}
```

### Precedence (de configuración)
Orden en que se cargan y mergean las diferentes fuentes de configuración de OpenCode. Fuentes posteriores override las anteriores para claves conflictivas.

**Orden (de menor a mayor prioridad):**
1. Remote config
2. Global config
3. Custom config
4. Project config
5. `.opencode` directories
6. Inline config
7. Managed settings
8. macOS managed preferences (MDM)

### Provider
Proveedor de servicios de LLM (como Anthropic, OpenAI, Google, etc.) que OpenCode utiliza para acceder a modelos de IA.

**Proveedores soportados (75+):**
- Anthropic (Claude)
- OpenAI (GPT)
- Google Vertex AI (Gemini)
- GitHub Copilot
- GitLab Duo
- Amazon Bedrock
- Azure OpenAI
- Ollama (local)
- LM Studio (local)
- Y muchos más...

**Configuración con `/connect`:**
```
/connect
# Seleccionar proveedor
# Ingresar API key o autenticar OAuth
```

---

## Q

### Question (Tool)
Herramienta que permite al agente hacer preguntas al usuario durante la ejecución de una tarea. Útil para clarificar instrucciones o obtener decisiones.

**Características:**
- Opciones predefinidas
- Respuestas custom
- Múltiples preguntas
- Navegación entre preguntas

---

## R

### Read (Tool)
Herramienta que lee el contenido de archivos del sistema de archivos. Soporta rangos de líneas para archivos grandes.

**Uso típico:**
- Analizar código existente
- Entender estructura de archivos
- Revisar configuraciones

### Redo
Comando slash `/redo` que rehace un mensaje que fue deshecho con `/undo`. Requiere que el proyecto esté en un repositorio git.

**Uso:** `/redo`  
**Atajo:** `Ctrl+X R`

### Remote Config
Configuración organizacional que se sirve desde el endpoint `.well-known/opencode`. Se carga primero y puede ser override por configuración local.

**Ejemplo de uso:**
- Servidores MCP deshabilitados por defecto
- Providers aprobados por la organización
- Políticas de seguridad

### Rules
Archivos de reglas e instrucciones que OpenCode carga para guiar el comportamiento del agente. Se configuran con `instructions` en `opencode.json`.

---

## S

### Schedule (GitHub Actions)
Evento de GitHub Actions que permite ejecutar OpenCode en un horario programado usando cron. Útil para tareas automatizadas como review periódico de código.

**Ejemplo:**
```yaml
on:
  schedule:
    - cron: "0 9 * * 1"  # Cada lunes a las 9am UTC
```

### Share
Función que permite compartir conversaciones de OpenCode con otros mediante un enlace público.

**Comando:** `/share`  
**Formato de enlace:** `opncd.ai/s/<id>`

**Configuración:**
```json
{
  "share": "manual"  // "manual" | "auto" | "disabled"
}
```

### SKILL.md
Archivo de definición de habilidades (skills) que contiene instrucciones reutilizables para agentes. Se carga on-demand via la herramienta `skill`.

**Estructura:**
```markdown
---
name: git-release
description: Create consistent releases
license: MIT
---

## What I do
- Draft release notes
- Propose version bumps
```

**Ubicaciones:**
- `.opencode/skills/<name>/SKILL.md`
- `~/.config/opencode/skills/<name>/SKILL.md`
- `.claude/skills/<name>/SKILL.md`
- `.agents/skills/<name>/SKILL.md`

### Skill (Tool)
Herramienta que carga el contenido de un archivo SKILL.md y lo retorna en la conversación. Se usa para proporcionar instrucciones especializadas al agente.

### Snapshot
Sistema de tracking de cambios que OpenCode utiliza para permitir undo/redo. Usa un repositorio git interno para rastrear todas las modificaciones.

**Configuración:**
```json
{
  "snapshot": false  // Deshabilitar para repos grandes
}
```

### Small Model
Modelo ligero configurado para tareas menores como generación de títulos. Se diferencia del modelo principal (`model`) que se usa para tareas principales.

**Configuración:**
```json
{
  "small_model": "anthropic/claude-haiku-4-5"
}
```

### Subagent
Agente secundario que ejecuta tareas especializadas en sesiones child. Puede ser invocado automáticamente por agentes primarios o manualmente con `@mention`.

**Invocación manual:**
```
@general help me search for this function
```

**Navegación:**
- `Leader+Down` - Entrar a child session
- `Right/Left` - Ciclar entre children
- `Up` - Volver a parent

**Profundidad:** Controlada con `subagent_depth` (default: 1)

---

## T

### Tab (Tecla)
Tecla utilizada para cambiar entre Build mode y Plan mode en la TUI de OpenCode.

**Función:** Alternar entre modos  
**Indicador:** Esquina inferior derecha de la TUI

### Temperature
Parámetro de configuración de modelos de IA que controla la aleatoriedad de las respuestas. Valores más bajos = más determinístico, valores más altos = más creativo.

**Rango:** 0.0 - 1.0  
**Uso en agentes:**
```json
{
  "agent": {
    "my-agent": {
      "temperature": 0.1
    }
  }
}
```

### Theme
Tema de color de la TUI de OpenCode. Se configura en `tui.json` o se cambia con `/themes`.

**Cambio:** `/themes`  
**Configuración:**
```json
{
  "theme": "tokyonight"
}
```

### Timeout
Tiempo máximo de espera para operaciones de red. Se configura por proveedor.

**Configuración:**
```json
{
  "provider": {
    "anthropic": {
      "options": {
        "timeout": 600000,
        "chunkTimeout": 30000
      }
    }
  }
}
```

### TLI (Terminal User Interface)
Interfaz de usuario de terminal que OpenCode utiliza como su modo principal de interacción. Proporciona una experiencia rica con colores, formatos y atajos de teclado.

---

## U

### Undo
Comando slash `/undo` que deshace el último mensaje o cambio realizado. Requiere que el proyecto esté en un repositorio git para funcionar.

**Uso:** `/undo`  
**Atajo:** `Ctrl+X U`  
**Múltiples:** Se puede ejecutar múltiples veces

### Whitelist (de modelos)
Lista de modelos que se muestran exclusivamente en el selector. A diferencia de blacklist que oculta modelos, whitelist muestra solo los especificados.

**Configuración:**
```json
{
  "provider": {
    "anthropic": {
      "whitelist": ["claude-sonnet-4-20250514"]
    }
  }
}
```

---

## W

### Watcher
Sistema de monitoreo de archivos que detecta cambios en el sistema de archivos. Se puede configurar para ignorar ciertos patrones.

**Configuración:**
```json
{
  "watcher": {
    "ignore": ["node_modules/**", "dist/**", ".git/**"]
  }
}
```

### Web (Modo)
Modo de interfaz web de OpenCode. Se ejecuta con `opencode web` y proporciona una interfaz basada en navegador.

### Webfetch (Tool)
Herramienta que permite al agente obtener y leer contenido de páginas web. Útil para consultar documentación o investigar recursos online.

**Uso típico:**
- Consultar documentación oficial
- Investigar APIs
- Leer artículos técnicos

### Websearch (Tool)
Herramienta de búsqueda en la web que utiliza Exa AI. Disponible cuando se usa el proveedor de OpenCode o se habilita `OPENCODE_ENABLE_EXA`.

**Habilitar:**
```bash
OPENCODE_ENABLE_EXA=1 opencode
```

---

## Z

### Zen (OpenCode Zen)
Ver [OpenCode Zen](#opencode-zen)

### ZenMux
Proveedor que permite múltiples rutas de acceso a modelos, proporcionando fallbacks y optimización de costos.

---

## Símbolos y Caracteres Especiales

### @ (Arroba)
Símbolo utilizado en OpenCode para referenciar archivos en las conversaciones. Se escribe `@` seguido del nombre o ruta del archivo para que el agente lo identifique.

**Ejemplos:**
- `@package.json`
- `@src/components/Button.tsx`
- `@src/index.ts#L10-20`

### / (Barra)
Prefijo para comandos slash en la TUI de OpenCode. Se escribe `/` seguido del nombre del comando para ejecutarlo.

**Ejemplos:**
- `/init`
- `/connect`
- `/models`

### Tab (Tecla)
Tecla para cambiar entre Build mode y Plan mode.

### Ctrl+X
Leader key (tecla principal) por defecto en la TUI. Se presiona seguida de otra tecla para ejecutar atajos.

---

## Acrónimos

| Acrónimo | Significado |
|----------|-------------|
| **ACP** | Agent Communication Protocol |
| **API** | Application Programming Interface |
| **AWS** | Amazon Web Services |
| **CLI** | Command Line Interface |
| **CORS** | Cross-Origin Resource Sharing |
| **DAP** | Duo Agent Platform (GitLab) |
| **EOF** | End of File |
| **GCP** | Google Cloud Platform |
| **GH** | GitHub |
| **GLM** | General Language Model |
| **IDE** | Integrated Development Environment |
| **JSON** | JavaScript Object Notation |
| **JSONC** | JSON with Comments |
| **LLM** | Large Language Model |
| **LSP** | Language Server Protocol |
| **MDM** | Mobile Device Management |
| **MCP** | Model Context Protocol |
| **NIM** | NVIDIA Inference Microservice |
| **OAuth** | Open Authorization |
| **PAT** | Personal Access Token |
| **PR** | Pull Request |
| **SDK** | Software Development Kit |
| **TUI** | Terminal User Interface |
| **URL** | Uniform Resource Locator |
| **VPC** | Virtual Private Cloud |
| **WSL** | Windows Subsystem for Linux |

---

## Versiones y Releases

### OpenCode 1.3.0+
- Última versión estable
- Plugins de Claude Pro/Max removidos
- Soporte mejorado para MCP

### Versiones Recomendadas
- **Producción:** Última versión estable
- **Desarrollo:** Latest release candidate
- **Enterprise:** Versión validada por el equipo

---

## Configuración Rápida de Referencia

### Inicio Rápido
```bash
# Instalar
curl -fsSL https://opencode.ai/install | bash

# Lanzar
cd /path/to/project
opencode

# Configurar proveedor
/connect

# Inicializar proyecto
/init

# Seleccionar modelo
/models
```

### Configuración Mínima
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5"
}
```

### Configuración Recomendada
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "small_model": "anthropic/claude-haiku-4-5",
  "permission": {
    "bash": "ask",
    "edit": "allow"
  },
  "lsp": true,
  "formatter": true,
  "autoupdate": true
}
```

---

## Recursos de Referencia

| Recurso | URL |
|---------|-----|
| Documentación oficial | opencode.ai/docs |
| GitHub | github.com/anomalyco/opencode |
| Discord | opencode.ai/discord |
| Changelog | opencode.ai/changelog |
| Config Schema | opencode.ai/config.json |
| TUI Schema | opencode.ai/tui.json |

---

*Última actualización: Agosto 2026*  
*Total de términos: 150+*
