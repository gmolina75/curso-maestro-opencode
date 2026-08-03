# Curso Maestro de OpenCode

> Sistema de generación de presentaciones (PPTX) para el **Curso Maestro de OpenCode**: el agente de IA de código abierto para terminal, escritorio e IDE.

---

## 🎯 ¿Qué es este Curso?

Este curso cubre **OpenCode**, el agente de IA de código abierto más avanzado del mercado, utilizado por **7.5 millones de desarrolladores mensuales** y con **160K+ estrellas en GitHub**. Aprenderás a dominarlo desde la instalación básica hasta integraciones enterprise, pasando por configuración avanzada, agentes personalizados, MCP servers y flujos de trabajo profesionales.

### Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| GitHub Stars | 160K+ |
| Contribuidores | 900+ |
| Desarrolladores mensuales | 7.5M |
| Proveedores soportados | 75+ |
| Módulos del curso | 41 |
| Duración estimada | ~40 horas |

---

## 📦 Instalación del Sistema de Presentaciones

```bash
# Clonar o navegar al directorio
cd OpenCode

# Crear entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

---

## 📁 Estructura del Proyecto

```
OpenCode/
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── .gitignore                         # Exclusiones de Git
│
├── syllabus-opencode-completo.md      # Sílabo del curso (41 clases)
├── glosario-completo.md               # Glosario de términos
│
├── src/                               # Scripts de generación
│   ├── generar_presentaciones.py      # Generador batch desde papers/
│   ├── mejorar_presentaciones.py      # Aplica tema visual mejorado
│   └── utils.py                       # Funciones compartidas
│
├── contenido/                         # Fuente del curso
│   ├── modulos/                       # 41 lecciones en markdown
│   │   ├── 01-introduccion-opencode.md
│   │   ├── ...
│   │   └── 41-migracion-agentes.md
│   └──
│       casos-de-uso/                  # 10 escenarios prácticos
│       ├── 01-powerbi.md
│       └── ...
│
├── plantillas/
│   └── plantilla.pptx                 # Plantilla base de diseño
│
└── presentaciones/                    # PPTX generados (no commitear)
    ├── 00-silabo-completo-opencode.pptx
    ├── 01-introduccion-opencode.pptx
    ├── ...
    └── casos-de-uso/
```

---

## 🚀 Uso del Sistema de Presentaciones

### Generar todas las presentaciones desde markdown

```bash
python src/generar_presentaciones.py
```

Lee los archivos de `contenido/modulos/` y genera los PPTX en `presentaciones/`.

### Generar sílabo resumido

```bash
python src/generar_silabo.py
```

Crea `presentaciones/00-silabo-completo-opencode.pptx` con la vista general del curso.

### Generar casos de uso

```bash
python src/generar_casos_de_uso.py
```

Crea las 10 presentaciones prácticas en `presentaciones/casos-de-uso/`.

### Aplicar tema visual mejorado

```bash
python src/mejorar_presentaciones.py
```

Toma los PPTX existentes y les aplica el tema azul pastel con elementos decorativos.

---

## 📚 Sílabo Completo del Curso (41 Módulos)

### MÓDULO 1: Introducción y Fundamentos

| # | Tema | Descripción |
|---|------|-------------|
| 1 | ¿Qué es OpenCode? | Definición, arquitectura (TUI, Desktop, IDE), comparativa con Claude Code/Cursor/Codex/Gemini CLI, ventajas open source, estadísticas del proyecto |
| 2 | Requisitos Previos | Terminal moderno (WezTerm, Alacritty, Ghostty, Kitty), API keys de LLM, conocimientos de CLI, Git |
| 3 | Instalación | Métodos: curl, npm, Homebrew, Arch, Chocolatey, Scoop, Docker, WSL. Verificación y primeros pasos |

### MÓDULO 2: Configuración de Proveedores y Modelos

| # | Tema | Descripción |
|---|------|-------------|
| 4 | OpenCode Zen | Lista curada de modelos verificados, modelo pay-as-you-go, configuración paso a paso, límites de gasto |
| 5 | OpenCode Go | Plan de suscripción de bajo costo, modelos open source, comparativa con Zen |
| 6 | Proveedores Principales | Anthropic Claude, OpenAI GPT, GitHub Copilot OAuth, GitLab Duo, Google Vertex AI |
| 7 | Proveedores Cloud | AWS Bedrock, Azure OpenAI, Cloudflare, DigitalOcean, Fireworks, Groq, Hugging Face, NVIDIA, OpenRouter, Together, xAI, Z.AI |
| 8 | Modelos Locales | Ollama, LM Studio, llama.cpp, Atomic Chat. Configuración de endpoints locales |
| 9 | Proveedor Custom | Configuración de baseURL personalizado, proxies, endpoints custom, paquetes npm compatibles |
| 10 | Gestión de Modelos | Selector /models, modelo principal, small_model, blacklist/whitelist, timeout |

### MÓDULO 3: Configuración Avanzada

| # | Tema | Descripción |
|---|------|-------------|
| 11 | Formato de Configuración | Soporte JSON y JSONC, schema oficial, autocompletado y validación en editores |
| 12 | Ubicaciones de Config | Precedencia: remote, global, custom, project, .opencode, inline, managed settings, macOS mobileconfig |
| 13 | Variables de Entorno | OPENCODE_CONFIG, CONFIG_DIR, TUI_CONFIG, DISABLE_AUTOUPDATE, EXPERIMENTAL, ENABLE_EXA |
| 14 | Sustitución de Variables | Variables de entorno {env:VAR}, contenido de archivos {file:path}, uso para API keys |
| 15 | Gestión Remota | Endpoint .well-known/opencode, managed settings con MDM (Jamf, Kandji, FleetDM), mobileconfig macOS |

### MÓDULO 4: Interfaz de Usuario TUI

| # | Tema | Descripción |
|---|------|-------------|
| 16 | Navegación Básica | Lanzamiento, leader key Ctrl+X, modos Build/Plan, cambio con Tab |
| 17 | Slash Commands | /new, /connect, /init, /help, /share, /undo, /exit y todos los comandos disponibles |
| 18 | Atajos de Teclado | Ctrl+X combinaciones, Ctrl+P paleta, Tab modos, atajos de archivo con @ |

### MÓDULO 5: Herramientas Integradas (Tools)

| # | Tema | Descripción |
|---|------|-------------|
| 19 | Tools Principales | bash, edit, write, read, grep, glob, apply_patch, skill, todowrite, webfetch, websearch, question, lsp |
| 20 | Configuración de Permisos | allow/ask/deny por tool, patrones glob para MCP, seguridad granular |
| 21 | Internals | Uso de ripgrep, respeto de .gitignore, archivo .ignore para inclusiones |

### MÓDULO 6: Modos de Trabajo

| # | Tema | Descripción |
|---|------|-------------|
| 22 | Build Mode | Acceso completo a tools, lectura/escritura, ejecución shell, desarrollo de features |
| 23 | Plan Mode | Solo lectura, análisis de código, propuesta de cambios, exploración segura |
| 24 | Flujo Plan → Build | Activar Plan, describir feature, iterar, cambiar a Build, ejecutar cambios |

### MÓDULO 7: Agentes

| # | Tema | Descripción |
|---|------|-------------|
| 25 | Agentes Primarios | build (default) y plan, cambio con Tab o keybind, configuración en opencode.json |
| 26 | Subagentes | Ejecución en sesiones child, invocación @mention, profundidad configurable, navegación jerárquica |
| 27 | Agentes Custom | Definición en .opencode/agents/*.md con YAML frontmatter, modelos, prompts, tools, permisos |

### MÓDULO 8: Agent Skills y Contexto

| # | Tema | Descripción |
|---|------|-------------|
| 28 | SKILL.md | Instrucciones reutilizables, carga on-demand, estructura con frontmatter, ubicaciones, permisos |
| 29 | AGENTS.md | Contexto del proyecto, creación con /init, estructura, convenciones, guías de coding |

### MÓDULO 9: Extensibilidad

| # | Tema | Descripción |
|---|------|-------------|
| 30 | MCP Servers | Model Context Protocol, servidores locales y remotos, OAuth, ejemplos Sentry/Context7 |
| 31 | Custom Tools | Funciones definidas por usuario, ejecución de código arbitrario, definición en config |
| 32 | Plugins | Extensión con tools/hooks, carga desde npm, ejemplos Helicone y GitLab |

### MÓDULO 10: Seguridad y DevTools

| # | Tema | Descripción |
|---|------|-------------|
| 33 | Permisos y Policies | Permisos granulares, skills, policies experimentales, control de providers |
| 34 | LSP Servers | Language Server Protocol, inteligencia de código, lenguajes soportados, tool experimental |
| 35 | Formatters | Prettier, rustfmt, configuración detallada, formateadores custom |

### MÓDULO 11: Personalización TUI

| # | Tema | Descripción |
|---|------|-------------|
| 36 | Temas y Personalización | /themes, tui.json, scroll, diff_style, mouse, attention, keybinds |
| 37 | Comandos Custom | Definición en config y markdown, variables $ARGUMENTS, templates, agentes específicos |

### MÓDULO 12: Integraciones

| # | Tema | Descripción |
|---|------|-------------|
| 38 | Integración IDE | VS Code, Cursor, Windsurf, VSCodium. Instalación, atajos, context awareness |
| 39 | Integración GitHub | GitHub Actions, app oficial, eventos, /opencode, review de PRs, fixes automáticos |
| 40 | Integración GitLab | GitLab Duo Agent Platform, self-hosted, plugin oficial, MR reviews, pipelines |

### MÓDULO 13: Cierre y Mejores Prácticas

| # | Tema | Descripción |
|---|------|-------------|
| 41 | Mejores Prácticas | Flujo de trabajo recomendado, consejos de prompting, casos de uso, seguridad, troubleshooting |

---

## 📊 Resumen por Categorías

| Categoría | Módulos | Temas |
|-----------|---------|-------|
| Introducción y Fundamentos | 1–3 | Arquitectura, instalación, requisitos |
| Proveedores y Modelos | 4–10 | Zen, Go, Cloud, Locales, Custom, Gestión |
| Configuración Avanzada | 11–15 | JSON/JSONC, Precedencia, Env Vars, Remote |
| Interfaz TUI | 16–18, 36–37 | Navegación, Commands, Keybinds, Temas |
| Tools y Permisos | 19–21 | Tools integradas, Permisos, Internals |
| Modos de Trabajo | 22–24 | Build, Plan, Workflow Plan→Build |
| Agentes y Contexto | 25–29 | Primarios, Subagentes, Custom, Skills, AGENTS.md |
| Extensibilidad | 30–32 | MCP, Custom Tools, Plugins |
| Seguridad y DevTools | 33–35 | Permisos, LSP, Formatters |
| Integraciones | 38–40 | IDE, GitHub, GitLab |
| Cierre | 41 | Mejores prácticas y troubleshooting |

---

## 🛠️ Dependencias

- [python-pptx](https://python-pptx.readthedocs.io/) – Generación de archivos PowerPoint
- Python 3.8+

---

## 📄 Licencia

Contenido educativo para uso interno.
