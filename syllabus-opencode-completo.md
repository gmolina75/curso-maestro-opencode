# Syllabus Completo: Curso Maestro de OpenCode

## El Agente de IA de Código Abierto para Terminal, Escritorio y IDE

---

## MÓDULO 1: Introducción y Fundamentos

### 1.1 ¿Qué es OpenCode?
- Definición: Agente de IA de código abierto para coding
- Arquitectura: Terminal TUI, Desktop App, IDE Extension
- Comparativa con otros agentes (Claude Code, Cursor, Codex, Gemini CLI)
- Ventajas: open source, multi-provider, privacy-first, 75+ proveedores
- Estadísticas: 160K+ GitHub Stars, 900+ contribuidores, 7.5M desarrolladores mensuales

### 1.2 Requisitos Previos
- Terminal moderno: WezTerm, Alacritty, Ghostty, Kitty
- API keys de proveedores LLM (o usar OpenCode Zen)
- Conocimientos básicos de línea de comandos
- Git (recomendado)

### 1.3 Instalación
- **Método principal (recomendado):**
  ```bash
  curl -fsSL https://opencode.ai/install | bash
  ```
- **Node.js:**
  ```bash
  npm install -g opencode-ai
  bun install -g opencode-ai
  pnpm install -g opencode-ai
  yarn global add opencode-ai
  ```
- **Homebrew (macOS/Linux):**
  ```bash
  brew install anomalyco/tap/opencode
  ```
- **Arch Linux:**
  ```bash
  sudo pacman -S opencode
  paru -S opencode-bin
  ```
- **Windows:**
  - Chocolatey: `choco install opencode`
  - Scoop: `scoop install opencode`
  - Mise: `mise use -g github:anomalyco/opencode`
  - Docker: `docker run -it --rm ghcr.io/anomalyco/opencode`
  - WSL (recomendado para mejor experiencia)
- **Verificación de instalación:**
  ```bash
  opencode --version
  ```

---

## MÓDULO 2: Configuración de Proveedores y Modelos

### 2.1 OpenCode Zen (Recomendado para principiantes)
- ¿Qué es Zen? Lista curada de modelos verificados por el equipo de OpenCode
- Modelo de pago: pay-as-you-go ($20 saldo, auto top-up)
- Sin markup en inferencia, límites de gasto disponibles
- Configuración:
  1. Ejecutar `/connect` en TUI
  2. Seleccionar "OpenCode Zen"
  3. Ir a opencode.ai/auth
  4. Iniciar sesión, agregar datos de facturación
  5. Copiar API key y pegarla

### 2.2 OpenCode Go
- Plan de suscripción de bajo costo
- Modelos de código abierto populares
- Mismo proceso de configuración que Zen

### 2.3 Proveedores Principales
- **Anthropic (Claude):**
  - Soporte para Claude Pro/Max (OAuth)
  - Modelos: Claude Opus, Sonnet, Haiku
- **OpenAI:**
  - Soporte para ChatGPT Plus/Pro (OAuth)
  - Modelos: GPT-4o, GPT-5, o1, o3
- **GitHub Copilot:**
  - Autenticación OAuth
  - Acceso a modelos de GitHub
- **GitLab Duo:**
  - OAuth o Personal Access Token
  - Modelos Claude-based: haiku-4-5, sonnet-4-5, opus-4-5
- **Google Vertex AI:**
  - Configuración con Google Cloud
  - Modelos Gemini

### 2.4 Proveedores Cloud
- Amazon Bedrock (AWS)
- Azure OpenAI / Azure Cognitive Services
- Cloudflare AI Gateway / Workers AI
- DigitalOcean Inference
- Fireworks AI
- Groq
- Hugging Face
- NVIDIA NIM
- OpenRouter
- Together AI
- xAI
- Z.AI (GLM-5.2)

### 2.5 Modelos Locales
- **Ollama:**
  ```json
  {
    "provider": {
      "ollama": {
        "npm": "@ai-sdk/openai-compatible",
        "name": "Ollama (local)",
        "options": { "baseURL": "http://localhost:11434/v1" },
        "models": { "llama2": { "name": "Llama 2" } }
      }
    }
  }
  ```
- **LM Studio:** endpoint local en puerto 1234
- **llama.cpp:** endpoint local en puerto 8080
- **Atomic Chat:** endpoint local en puerto 1337

### 2.6 Proveedor Custom
- Configuración de `baseURL` personalizado
- Soporte para proxies y endpoints personalizados
- Paquetes npm compatibles: `@ai-sdk/openai-compatible`

### 2.7 Gestión de Modelos
- `/models` - Selector de modelos en TUI
- `model` - Modelo principal en config
- `small_model` - Modelo ligero para tareas menores (títulos)
- `blacklist` / `whitelist` - Filtrar modelos visibles
- Configuración de timeout y chunk timeout

---

## MÓDULO 3: Configuración Avanzada

### 3.1 Formato de Configuración
- Soporte JSON y JSONC (JSON con comentarios)
- Schema: `https://opencode.ai/config.json`
- Autocompletado y validación en editores

### 3.2 Ubicaciones de Configuración (Precedencia)
1. **Remote config** (`.well-known/opencode`) - defaults organizacionales
2. **Global config** (`~/.config/opencode/opencode.json`) - preferencias usuario
3. **Custom config** (`OPENCODE_CONFIG` env var) - overrides custom
4. **Project config** (`opencode.json` en raíz del proyecto) - específica del proyecto
5. **`.opencode` directorios** - agents, commands, plugins
6. **Inline config** (`OPENCODE_CONFIG_CONTENT` env var) - runtime overrides
7. **Managed settings** (macOS: `/Library/Application Support/opencode/`, Linux: `/etc/opencode/`, Windows: `%ProgramData%\opencode`)
8. **macOS managed preferences** (`.mobileconfig` vía MDM)

### 3.3 Variables de Entorno
- `OPENCODE_CONFIG` - Ruta custom de config
- `OPENCODE_CONFIG_DIR` - Directorio custom de config
- `OPENCODE_TUI_CONFIG` - Ruta custom de TUI config
- `OPENCODE_DISABLE_AUTOUPDATE` - Desactivar auto-updates
- `OPENCODE_EXPERIMENTAL` - Habilitar features experimentales
- `OPENCODE_ENABLE_EXA` - Habilitar websearch

### 3.4 Sustitución de Variables
- **Environment variables:** `{env:VARIABLE_NAME}`
- **File contents:** `{file:path/to/file}`
- Útiles para: API keys sensibles, instrucciones grandes, snippets compartidos

### 3.5 Gestión Remota (Enterprise)
- Endpoint `.well-known/opencode` para defaults organizacionales
- Override de defaults remotos en config local
- Managed settings con MDM (Jamf, Kandji, FleetDM)
- Mobileconfig para macOS
- Prioridad máxima: managed settings

---

## MÓDULO 4: Interfaz de Usuario TUI

### 4.1 Navegación Básica
- Lanzamiento: `opencode` desde directorio del proyecto
- Leader key: `Ctrl+X` (por defecto)
- Modos: Build (default) y Plan
- Cambio de modo: `Tab`

### 4.2 Slash Commands Completos
- **Sesión:**
  - `/new` (`/clear`) - Nueva sesión
  - `/sessions` (`/resume`, `/continue`) - Listar/cambiar sesiones
  - `/compact` (`/summarize`) - Compactar sesión
  - `/share` - Compartir conversación
  - `/unshare` - Revocar enlace
  - `/export` - Exportar a Markdown
  - `/undo` - Deshacer último mensaje
  - `/redo` - Rehacer mensaje deshecho
- **Proveedor y Modelo:**
  - `/connect` - Agregar/actualizar credenciales
  - `/models` - Cambiar modelo activo
- **Inicialización:**
  - `/init` - Crear/actualizar AGENTS.md
  - `/init-deep` - Inicialización profunda con subdirectorios
- **Navegación:**
  - `/help` - Mostrar ayuda
  - `/details` (`/detail`) - Toggle detalles de ejecución
  - `/thinking` - Toggle proceso de razonamiento
  - `/themes` - Listar temas
  - `/editor` - Abrir editor externo
- **Control:**
  - `/exit` (`/quit`, `/q`) - Salir

### 4.3 Atajos de Teclado Principales
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
- `Tab` - Cambiar entre Build/Plan mode

### 4.4 Atajos de Archivo
- `@` - Búsqueda fuzzy de archivos
- `@File#L37-42` - Referencia a líneas específicas
- Drag and drop de imágenes al terminal

### 4.5 Personalización del TUI
- Archivo `tui.json` dedicado
- `scroll_speed` - Velocidad de scroll
- `scroll_acceleration` - Aceleración de scroll
- `diff_style` - Estilo de diff ("auto", "unified", "split")
- `mouse` - Habilitar soporte de mouse
- `attention` - Notificaciones y sonidos
- `theme` - Tema de color
- `keybinds` - Atajos personalizados

---

## MÓDULO 5: Herramientas Integradas (Tools)

### 5.1 Tools Principales
- **bash** - Ejecutar comandos shell
- **edit** - Modificar archivos con reemplazo exacto
- **write** - Crear/sobrescribir archivos
- **read** - Leer contenido de archivos
- **grep** - Búsqueda por regex en contenido
- **glob** - Búsqueda de archivos por patrón
- **apply_patch** - Aplicar parches a archivos
- **skill** - Cargar SKILL.md
- **todowrite** - Gestionar listas de tareas
- **webfetch** - Obtener contenido web
- **websearch** - Buscar en la web (vía Exa AI)
- **question** - Preguntar al usuario durante ejecución
- **lsp** (experimental) - Interacción con LSP servers

### 5.2 Configuración de Permisos por Tool
```json
{
  "permission": {
    "bash": "allow",
    "edit": "ask",
    "write": "deny",
    "webfetch": "allow"
  }
}
```
- `allow` - Permitir sin preguntar
- `ask` - Requiere aprobación
- `deny` - Bloquear completamente
- Patrones glob: `"mymcp_*": "ask"`

### 5.3 Internals
- Uso de ripgrep para grep/glob
- Respeto de `.gitignore`
- Archivo `.ignore` para incluir paths ignorados

---

## MÓDULO 6: Modos de Trabajo (Build vs Plan)

### 6.1 Build Mode (Default)
- Acceso completo a tools
- Lectura, escritura, edición de archivos
- Ejecución de comandos shell
- Búsqueda en codebase
- Desarrollo de features y refactoring

### 6.2 Plan Mode
- Solo lectura (sin modificaciones)
- Análisis de código
- Propuesta de cambios
- Revisión de sugerencias
- Ideal para explorar codebase unfamiliar
- Activación con `Tab`

### 6.3 Flujo de Trabajo Plan → Build
1. Activar Plan mode con `Tab`
2. Describir feature deseada con detalle
3. Iterar sobre el plan con OpenCode
4. Cambiar a Build mode con `Tab`
5. Ejecutar: "Go ahead and make the changes"

### 6.4 Edición Directa
- Para cambios directos sin plan
- Referenciar archivos con `@`
- Proporcionar contexto suficiente
- Ejemplo: "We need auth on /settings — mirror @path/notes.ts in @path/settings.ts"

---

## MÓDULO 7: Agentes

### 7.1 Agentes Primarios
- **build** (default) - Acceso completo a tools
- **plan** - Solo lectura, análisis
- Cambio con `Tab` o keybind `switch_agent`
- Configuración en `opencode.json` bajo `agent`

### 7.2 Subagentes
- Ejecución en sesiones child
- Invocación automática por agentes primarios
- Invocación manual con `@mention`: `@general help me search`
- Profundidad configurable: `subagent_depth` (default: 1)
- Navegación: `Leader+Down` (child), `Right/Left` (ciclar), `Up` (parent)

### 7.3 Agentes Custom
- Definición en `.opencode/agents/*.md` con YAML frontmatter
- Configuración en `opencode.json` bajo `agent`
- Campos disponibles:
  - `description` - Descripción del agente
  - `model` - Modelo específico
  - `prompt` - Prompt del sistema
  - `temperature` - Temperatura
  - `tools` - Habilitar/deshabilitar tools
  - `permission` - Permisos específicos
  - `mode` - "primary" o "subagent"

### 7.4 Ejemplo de Agente Custom
```json
{
  "agent": {
    "code-reviewer": {
      "description": "Reviews code for best practices",
      "model": "anthropic/claude-sonnet-4-5",
      "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

### 7.5 Agente por Defecto
- Configuración: `default_agent` en opencode.json
- Aplica a: TUI, CLI, desktop app, GitHub Action
- Fallback a "build" si el agente no existe

---

## MÓDULO 8: Agent Skills (SKILL.md)

### 8.1 ¿Qué son las Skills?
- Instrucciones reutilizables descubiertas por agentes
- Carga on-demand via tool `skill`
- Definidos en archivos `SKILL.md`

### 8.2 Ubicación de Archivos
- **Proyecto:** `.opencode/skills/<name>/SKILL.md`
- **Global:** `~/.config/opencode/skills/<name>/SKILL.md`
- **Claude-compatible:** `.claude/skills/<name>/SKILL.md`
- **Agent-compatible:** `.agents/skills/<name>/SKILL.md`

### 8.3 Estructura del SKILL.md
```markdown
---
name: git-release
description: Create consistent releases and changelogs
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: github
---

## What I do
- Draft release notes from merged PRs
- Propose semantic version bumps

## When to use me
Use this when preparing tagged releases.
```

### 8.4 Permisos de Skills
```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

### 8.5 Override por Agente
- Custom agent: en frontmatter YAML
- Built-in agent: en `opencode.json`

### 8.6 Deshabilitar Skills
- Por agente: `tools: { skill: false }`
- Global: no aplica (siempre disponible)

### 8.7 Troubleshooting
1. Verificar `SKILL.md` en MAYÚSCULAS
2. Frontmatter con `name` y `description` requeridos
3. Nombres únicos entre todas las ubicaciones
4. Verificar permisos

---

## MÓDULO 9: AGENTS.md (Contexto del Proyecto)

### 9.1 ¿Qué es AGENTS.md?
- Archivo de contexto del proyecto para agentes
- Creado con `/init`
- Analiza estructura, patrones y convenciones
- Se recomienda commitear a Git

### 9.2 Contenido Típico
- Estructura del proyecto
- Convenciones de naming
- Patrones de arquitectura
- Comandos disponibles
- Guías de coding
- Instrucciones para el agente

### 9.3 Uso de AGENTS.md
- Se carga automáticamente al inicio
- Persiste entre sesiones
- Proporciona contexto sin re-explicar
- Se puede editar manualmente

### 9.4 Instrucciones Adicionales
- Campo `instructions` en config: array de paths/globs
- Ejemplo: `["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]`
- Se cargan junto con AGENTS.md

---

## MÓDULO 10: MCP Servers (Model Context Protocol)

### 10.1 ¿Qué es MCP?
- Protocolo para integrar herramientas externas
- Soporte local y remoto
- Tools disponibles junto con tools integrados

### 10.2 MCP Local
```json
{
  "mcp": {
    "my-local-mcp": {
      "type": "local",
      "command": ["npx", "-y", "my-mcp-command"],
      "enabled": true,
      "environment": { "MY_ENV_VAR": "value" }
    }
  }
}
```

### 10.3 MCP Remoto
```json
{
  "mcp": {
    "my-remote-mcp": {
      "type": "remote",
      "url": "https://my-mcp-server.com",
      "enabled": true,
      "headers": { "Authorization": "Bearer TOKEN" }
    }
  }
}
```

### 10.4 OAuth para MCP Remoto
- Detección automática de 401
- Dynamic Client Registration (RFC 7591)
- Tokens almacenados en `~/.local/share/opencode/mcp-auth.json`
- Comandos:
  ```bash
  opencode mcp auth <server-name>
  opencode mcp list
  opencode mcp logout <server-name>
  opencode mcp debug <server-name>
  ```

### 10.5 Gestión de MCP
- Habilitar/deshabilitar globalmente
- Por agente específico
- Patrones glob: `"my-mcp*": false`
- Caveat: MCP servers añaden tokens al contexto

### 10.6 Ejemplos Populares
- **Sentry:** `https://mcp.sentry.dev/mcp`
- **Context7:** `https://mcp.context7.com/mcp`
- **Grep by Vercel:** `https://mcp.grep.app`

---

## MÓDULO 11: Custom Tools

### 11.1 ¿Qué son?
- Funciones definidas por el usuario
- Ejecución de código arbitrario
- Definidos en config file

### 11.2 Configuración
- Definición en `opencode.json` bajo `tools`
- Disponibles para el LLM junto con tools integrados
- Control de permisos igual que tools nativas

---

## MÓDULO 12: Plugins

### 12.1 ¿Qué son?
- Extienden OpenCode con tools, hooks e integraciones
- Ubicación: `.opencode/plugins/` o `~/.config/opencode/plugins/`
- Carga desde npm

### 12.2 Configuración
```json
{
  "plugin": ["opencode-helicone-session", "@my-org/custom-plugin"]
}
```

### 12.3 Ejemplos
- `opencode-helicone-session` - Tracking de sesiones en Helicone
- `opencode-gitlab-plugin` - Herramientas GitLab

---

## MÓDULO 13: Permissions y Policies

### 13.1 Permisos de Tools
- Por tool individual: `bash`, `edit`, `write`, etc.
- Patrones glob: `"mymcp_*": "ask"`
- Valores: `allow`, `deny`, `ask`

### 13.2 Permisos de Skills
- Por skill: `"pr-review": "allow"`
- Patrones: `"internal-*": "deny"`
- Por agente: override en agent config

### 13.3 Policies (Experimental)
```json
{
  "experimental": {
    "policies": [
      {
        "effect": "deny",
        "action": "provider.use",
        "resource": "openai"
      }
    ]
  }
}
```
- Control de providers permitidos/denegados

### 13.4 Por Defecto
- Todas las operaciones permitidas sin aprobación
- Cambiar con `permission` en config

---

## MÓDULO 14: LSP Servers

### 14.1 ¿Qué son?
- Language Server Protocol
- Inteligencia de código: definiciones, referencias, hover, diagnósticos
- Carga automática por OpenCode

### 14.2 Configuración
```json
{
  "lsp": true
}
```
- Lenguajes soportados: Rust, TypeScript, Python, Swift, y más
- Configuración por lenguaje:
```json
{
  "lsp": {
    "typescript": { "disabled": true }
  }
}
```

### 14.3 Herramienta LSP (Experimental)
- Habilitar: `OPENCODE_EXPERIMENTAL_LSP_TOOL=true`
- Operaciones: goToDefinition, findReferences, hover, documentSymbol, workspaceSymbol, goToImplementation, prepareCallHierarchy, incomingCalls, outgoingCalls

---

## MÓDULO 15: Formatters

### 15.1 Configuración
```json
{
  "formatter": true
}
```
- Formateadores built-in: Prettier, rustfmt, etc.
- Configuración detallada:
```json
{
  "formatter": {
    "prettier": { "disabled": true },
    "custom-prettier": {
      "command": ["npx", "prettier", "--write", "$FILE"],
      "environment": { "NODE_ENV": "development" },
      "extensions": [".js", ".ts", ".jsx", ".tsx"]
    }
  }
}
```

---

## MÓDULO 16: Temas y Personalización Visual

### 16.1 Temas
- `/themes` para listar temas disponibles
- Configuración en `tui.json`:
```json
{
  "theme": "tokyonight"
}
```

### 16.2 Atajos de Teclado
- Configuración en `tui.json` bajo `keybinds`
- Merge con defaults
- Solo configurar los que se quieran cambiar

---

## MÓDULO 17: Comandos Custom

### 17.1 Definición en Config
```json
{
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report.",
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-haiku-4-5"
    },
    "component": {
      "template": "Create a new React component named $ARGUMENTS.",
      "description": "Create a new component"
    }
  }
}
```

### 17.2 Definición en Archivos Markdown
- Ubicación: `~/.config/opencode/commands/` o `.opencode/commands/`
- Formato: YAML frontmatter + prompt
- Variables: `$ARGUMENTS`

---

## MÓDULO 18: Integración IDE

### 18.1 VS Code / Cursor / Windsurf / VSCodium
- Instalación automática al ejecutar `opencode` en terminal integrada
- Instalación manual: buscar "OpenCode" en Extension Marketplace
- Atajos:
  - `Cmd/Ctrl+Esc` - Abrir OpenCode en split terminal
  - `Cmd/Ctrl+Shift+Esc` - Nueva sesión OpenCode
  - `Cmd/Ctrl+Option/Alt+K` - Insertar referencia de archivo
- Context awareness: comparte selección o tab actual
- Configuración de editor: `export EDITOR="code --wait"`

---

## MÓDULO 19: Integración GitHub

### 19.1 GitHub Actions
- Instalación: `opencode github install`
- App: `github.com/apps/opencode-agent`
- Workflow: `.github/workflows/opencode.yml`

### 19.2 Eventos Soportados
- `issue_comment` - Comentarios en issues/PRs
- `pull_request_review_comment` - Comentarios en código específico
- `issues` - Issues abiertos/editados
- `pull_request` - PRs abiertos/actualizados
- `schedule` - Tareas programadas (cron)
- `workflow_dispatch` - Trigger manual

### 19.3 Uso
- `/opencode explain this issue` - Explicar issue
- `/opencode fix this` - Fix automático con PR
- `/oc delete attachment` - Cambios directos en PR
- Review de PRs con commentarios específicos de líneas

### 19.4 Configuración del Action
```yaml
- uses: anomalyco/opencode/github@latest
  with:
    model: anthropic/claude-sonnet-4-5
    agent: build
    share: true
    prompt: |
      Review this pull request...
```

---

## MÓDULO 20: Integración GitLab

### 20.1 GitLab Duo Agent Platform
- Requiere suscripción Premium o Ultimate
- OAuth o Personal Access Token
- Modelos: duo-chat-haiku-4-5, duo-chat-sonnet-4-5, duo-chat-opus-4-5

### 20.2 Self-Hosted GitLab
```bash
export GITLAB_INSTANCE_URL=https://gitlab.company.com
export GITLAB_TOKEN=glpat-...
export GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
```

### 20.3 Plugin GitLab
```json
{
  "plugin": ["opencode-gitlab-plugin"]
}
```
- MR reviews, issue tracking, pipeline monitoring, CI/CD

---

## MÓDULO 21: Share y Colaboración

### 21.1 Compartir Sesiones
- `/share` - Generar enlace público (`opncd.ai/s/<id>`)
- `/unshare` - Revocar enlace
- Configuración: `"share": "manual" | "auto" | "disabled"`

### 21.2 Exportar
- `/export` - Exportar conversación a Markdown

### 21.3 Multi-Sesión
- Múltiples agentes en paralelo en el mismo proyecto
- Navegación entre sesiones: `/sessions`

---

## MÓDULO 22: Gestión de Cambios (Undo/Redo)

### 22.1 Snapshots
- Tracking de cambios del agente via git interno
- Habilitado por default
- Deshabilitar: `"snapshot": false`
- Caveat: para repos grandes puede ser lento

### 22.2 Undo/Redo
- `/undo` - Deshacer cambios (requiere git)
- `/redo` - Rehacer cambios
- Múltiples undo/redo soportados

---

## MÓDULO 23: Compaction y Contexto

### 23.1 Compaction
- `/compact` - Compactar sesión manualmente
- Configuración:
```json
{
  "compaction": {
    "auto": true,
    "prune": false,
    "reserved": 10000
  }
}
```
- `auto` - Compactar automáticamente cuando contexto lleno
- `prune` - Eliminar outputs de tools antiguos
- `reserved` - Buffer de tokens para evitar overflow

---

## MÓDULO 24: Watcher

### 24.1 Configuración
```json
{
  "watcher": {
    "ignore": ["node_modules/**", "dist/**", ".git/**"]
  }
}
```
- Patrones glob para excluir directorios ruidosos

---

## MÓDULO 25: Imágenes y Adjuntos

### 25.1 Soporte de Imágenes
- Drag and drop al terminal
- Escaneo automático por OpenCode
- Normalización antes de enviar al modelo

### 25.2 Configuración
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

---

## MÓDULO 26: CLI y Modo Headless

### 26.1 Comandos CLI Principales
- `opencode` - Lanzar TUI
- `opencode run "prompt"` - Ejecutar prompt no-interactivo
- `opencode run "prompt" -f json` - Output JSON
- `opencode run "prompt" -q` - Modo quiet (sin spinner)
- `opencode run "prompt" --model openai/gpt-4o` - Modelo específico
- `opencode --continue` - Continuar sesión previa
- `opencode --attach http://server:4242` - Conectar a backend remoto

### 26.2 Uso en Scripts
- Automatización y CI/CD
- Output JSON para procesamiento
- Flags: `-f json`, `-q`, `--model`

---

## MÓDULO 27: Red y Proxy

### 27.1 Configuración de Proxy
- Soporte para proxies corporativos
- Configuración en config o variables de entorno

### 27.2 CORS
```json
{
  "server": {
    "cors": ["http://localhost:5173"]
  }
}
```

---

## MÓDULO 28: Enterprise

### 28.1 OpenCode Go
- Plan de suscripción para equipos
- Modelos de código abierto verificados

### 28.2 Enterprise Features
- Managed settings (MDM)
- Políticas organizacionales
- Configuración remota via `.well-known/opencode`
- Control de providers permitidos
- Deshabilitar sharing

### 28.3 Deployment
- WSL para Windows
- Docker support
- Server mode: `opencode serve`
- mDNS para descubrimiento en red

---

## MÓDULO 29: Desarrollo y Extensibilidad

### 29.1 SDK
- API para integración programática
- Documentación en opencode.ai/docs/sdk

### 29.2 Server Mode
```json
{
  "server": {
    "port": 4096,
    "hostname": "0.0.0.0",
    "mdns": true,
    "mdnsDomain": "myproject.local"
  }
}
```
- `opencode serve` - Ejecutar como servidor
- `opencode web` - Interfaz web

### 29.3 Ecosistema
- Plugins disponibles
- Integración con herramientas existentes
- Contribución al proyecto open source

---

## MÓDULO 30: Best Practices y Casos de Uso

### 30.1 Flujo de Trabajo Recomendado
1. Instalar OpenCode
2. Configurar proveedor (Zen recomendado para empezar)
3. Navegar al proyecto
4. Ejecutar `/init` para crear AGENTS.md
5. Commitear AGENTS.md a Git
6. Usar Plan mode para features complejas
7. Usar Build mode para implementación directa
8. Compartir sesiones con equipo

### 30.2 Consejos de Prompting
- Dar suficiente contexto
- Referenciar archivos con `@`
- Hablar como a un junior developer
- Incluir ejemplos cuando sea posible
- Usar imágenes como referencia

### 30.3 Casos de Uso
- Exploración de codebase unfamiliar
- Refactoring seguro con Plan mode
- Code review automatizado
- Creación de features completas
- Bug fixing con contexto
- Documentación automática
- Testing y validación
- Integración con CI/CD vía GitHub Actions

### 30.4 Seguridad
- API keys en `~/.local/share/opencode/auth.json`
- Nunca commitear credenciales
- Permisos granulares por tool y agente
- Políticas para controlar providers
- Managed settings para enterprise

---

## MÓDULO 31: Troubleshooting

### 31.1 Problemas Comunes
- Instalación fallida en Windows: usar WSL
- MCP server no carga: verificar permisos
- Skill no aparece: verificar nombre MAYÚSCULAS y frontmatter
- LSP no funciona: habilitar experimental
- Imágenes no se cargan: verificar límites de tamaño

### 31.2 Debug
```bash
opencode debug config
opencode mcp auth list
opencode mcp debug <server>
```

### 31.3 Recursos
- Docs oficiales: opencode.ai/docs
- GitHub: github.com/anomalyco/opencode
- Discord: opencode.ai/discord
- Changelog: opencode.ai/changelog

---

## MÓDULO 32: Modo Servidor y API

### 32.1 Server Mode
- `opencode serve` - Ejecutar como servidor HTTP
- Configuración de puerto, hostname y CORS
- Descubrimiento mDNS en red local

### 32.2 API Programática
- SDK de OpenCode
- Integración con aplicaciones externas
- Uso de `opencode web` para interfaz en navegador

### 32.3 Casos de Uso Avanzados
- Backend de agentes para microservicios
- Integración con pipelines de datos
- Automatización remota

---

## MÓDULO 33: Gestión de Contexto y Tokens

### 33.1 Context Window
- Ventana de contexto del modelo
- Límites y estrategias de manejo

### 33.2 Compactación Avanzada
- Configuración `auto`, `prune`, `reserved`
- Buffer de tokens para evitar overflow

### 33.3 Estrategias de Optimización
- Uso de `small_model` para tareas ligeras
- División de prompts largos
- Reutilización de contexto con AGENTS.md

---

## MÓDULO 34: Flujo de Trabajo con Git

### 34.1 Snapshots y Git Interno
- Tracking automático de cambios
- Undo/redo con `/undo` y `/redo`

### 34.2 Workflow Git + OpenCode
- Crear features en ramas
- Code review automatizado
- Merge y resolución de conflictos

### 34.3 Buenas Prácticas
- Commits atómicos con contexto del agente
- Documentación automática de cambios

---

## MÓDULO 35: Multi-Sesión y Trabajo Paralelo

### 35.1 Gestión de Sesiones
- `/sessions`, `/new`, `/resume`
- Navegación entre sesiones activas

### 35.2 Subagentes en Paralelo
- Invocación con `@mention`
- `subagent_depth` y jerarquía de sesiones
- Navegación: `Leader+Down`, `Right/Left`, `Up`

### 35.3 Casos de Uso
- Revisión de código paralela
- Investigación multi-archivo
- Testing y implementación simultáneos

---

## MÓDULO 36: Desktop App

### 36.1 OpenCode Desktop
- Aplicación nativa vs TUI
- Instalación y configuración

### 36.2 Integración con el Sistema
- Atajos globales
- Notificaciones
- Drag and drop de archivos

### 36.3 Comparativa Desktop vs Terminal
- Cuándo usar cada modo
- Sincronización de configuración

---

## MÓDULO 37: Optimización de Costos

### 37.1 Gestión de Proveedores
- Comparativa de precios por token
- Selección dinámica de modelos

### 37.2 Configuraciones de Ahorro
- `small_model` para tareas simples
- Blacklist/whitelist de modelos caros
- Límites de gasto en OpenCode Zen

### 37.3 Monitoreo
- Tracking de uso con Helicone
- Análisis de costos por proyecto

---

## MÓDULO 38: Seguridad Avanzada

### 38.1 Protección de Credenciales
- Almacenamiento en `~/.local/share/opencode/auth.json`
- Uso de `{env:VARIABLE}` en configuración
- Nunca commitear API keys

### 38.2 Permisos Granulares
- Permisos por tool: `allow`, `ask`, `deny`
- Permisos por skill y agente
- Policies experimentales

### 38.3 Enterprise Security
- Managed settings con MDM
- Configuración remota via `.well-known/opencode`
- Control de providers permitidos

---

## MÓDULO 39: Personalización de System Prompts

### 39.1 System Prompts
- Definición en agentes custom
- YAML frontmatter en `.opencode/agents/`
- Override de comportamiento por proyecto

### 39.2 Instrucciones Adicionales
- Campo `instructions` en `opencode.json`
- Carga de reglas desde archivos markdown
- Compatibilidad con `.cursor/rules/`

### 39.3 Casos de Uso
- Agentes especializados por tecnología
- Reglas de estilo de código
- Restricciones de arquitectura

---

## MÓDULO 40: Testing y Calidad de Código

### 40.1 Testing Automatizado
- Generación de tests con OpenCode
- Cobertura y análisis estático

### 40.2 Calidad de Código
- Formateadores automáticos (Prettier, rustfmt)
- LSP para diagnósticos en tiempo real
- Integración con linters

### 40.3 CI/CD Quality Gates
- Tests en GitHub Actions
- Validación de cambios antes de merge
- Reportes automáticos

---

## MÓDULO 41: Migración desde Otros Agentes

### 41.1 Migración desde Cursor
- Importar reglas y configuraciones
- Adaptar `.cursor/rules/` a OpenCode

### 41.2 Migración desde Claude Code
- Reutilizar skills de Claude
- Configurar proveedores equivalentes

### 41.3 Migración desde GitHub Copilot
- Aprovechar suscripción existente
- Configurar OAuth en OpenCode

---

## PROYECTOS PRÁCTICOS

### Proyecto 1: Configuración Inicial
- Instalar OpenCode
- Configurar Zen o proveedor propio
- Ejecutar `/init` en un proyecto existente
- Explorar codebase con preguntas

### Proyecto 2: Feature Completa
- Planear nueva feature con Plan mode
- Iterar sobre el plan
- Implementar con Build mode
- Deshacer y rehacer cambios

### Proyecto 3: Code Review con MCP
- Configurar MCP server (Sentry o Context7)
- Crear agente custom de review
- Revisar código existente
- Generar reporte

### Proyecto 4: Integración CI/CD
- Configurar GitHub Action
- Automatizar review de PRs
- Triage automático de issues
- Tareas programadas

### Proyecto 5: Multi-Provider Setup
- Configurar múltiples proveedores
- Comparar modelos para diferentes tareas
- Usar small_model para tareas ligeras
- Gestionar costos

### Proyecto 6: Team Setup
- Configurar managed settings
- Crear agents y skills compartidos
- Establecer permisos granulares
- Documentar flujos de trabajo

---

## EVALUACIÓN FINAL

### Examen Teórico
- Preguntas sobre configuración
- Identificación de comandos slash
- Flujo de trabajo Plan vs Build
- Permisos y políticas

### Examen Práctico
- Configurar proveedor desde cero
- Crear agente custom
- Implementar feature completa
- Configurar GitHub Action
- Debug de problemas comunes

---

## RECURSOS ADICIONALES

### Documentación
- https://opencode.ai/docs
- https://opencode.ai/docs/config
- https://opencode.ai/docs/providers
- https://opencode.ai/docs/tools
- https://opencode.ai/docs/agents
- https://opencode.ai/docs/skills
- https://opencode.ai/docs/mcp-servers
- https://opencode.ai/docs/github

### Comunidad
- Discord: opencode.ai/discord
- GitHub Issues: github.com/anomalyco/opencode/issues
- X (Twitter): @opencode

### Actualizaciones
- Changelog: opencode.ai/changelog
- Releases: github.com/anomalyco/opencode/releases

---

*Última actualización: Agosto 2026*
*Total de módulos: 31 + Proyectos Prácticos + Evaluación*
*Duración estimada: 40-60 horas*
