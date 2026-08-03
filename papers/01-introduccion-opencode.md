---
title: "Introducción a OpenCode"
module: 1
duration: "45 minutos"
prerequisites: "Ninguno"
---

# Clase 1: Introducción a OpenCode

## Resumen Ejecutivo

OpenCode es un agente de codificación con inteligencia artificial de código abierto que se ejecuta directamente en tu terminal. A diferencia de otras herramientas de IA para programación, OpenCode fue diseñado desde cero para ser extensible, multi-proveedor y respetar la privacidad del usuario. Con más de 160,000 estrellas en GitHub, 900+ contribuidores y 7.5 millones de desarrolladores mensuales, se ha convertido en una de las herramientas de IA para desarrollo más populares del mundo.

OpenCode no es solo una CLI: es un ecosistema completo que incluye una interfaz de terminal (TUI), una aplicación de escritorio y extensiones para IDEs populares. Su arquitectura modular permite conectar con más de 75 proveedores de modelos de IA, incluyendo opciones locales para quienes prefieren no depender de servicios en la nube. Esto lo convierte en una solución versátil para equipos de todos los tamaños, desde desarrolladores individuales hasta grandes organizaciones con requisitos de cumplimiento normativo.

## Objetivos de Aprendizaje

- Comprender qué es OpenCode y su positionamiento en el mercado de herramientas de IA para desarrollo
- Identificar las diferencias clave entre OpenCode y sus competidores principales
- Reconocer las ventajas del modelo open source y multi-proveedor
- Explorar las capacidades y casos de uso principales de la plataforma

## Conceptos Clave

### ¿Qué es OpenCode?

OpenCode es un agente de codificación con IA de código abierto. Sus características fundamentales incluyen:

- **Terminal First**: Ejecuta comandos directamente en tu terminal, integrándose con tu flujo de trabajo existente
- **Multi-Proveedor**: Soporta más de 75 proveedores de modelos de IA, desde Anthropic y OpenAI hasta opciones locales como Ollama
- **Código Abierto**: Licenciado bajo MIT, permitiendo personalización completa y auditoría del código
- **Privacidad First**: Tus datos se procesan directamente con el proveedor que tú eliges, sin intermediarios

```bash
# La experiencia básica de OpenCode
opencode

# Esto abre la interfaz TUI donde puedes:
# - Escribir prompts en lenguaje natural
# - Ver el código que la IA genera en tiempo real
# - Aprobar o rechazar cambios
# - Ejecutar comandos de terminal
```

### Arquitectura de OpenCode

OpenCode tiene una arquitectura en capas que lo hace flexible y extensible:

| Componente | Descripción | Uso Principal |
|------------|-------------|---------------|
| **TUI (Terminal UI)** | Interfaz interactiva en terminal | Desarrollo diario, scripting |
| **Desktop App** | Aplicación de escritorio nativa | Usuarios que prefieren GUI |
| **IDE Extension** | Extensiones para VS Code, JetBrains | Integración en entorno existente |
| **CLI Mode** | Modo de línea de comandos | Automatización, CI/CD |

### Comparativa con Competidores

| Característica | OpenCode | Claude Code | Cursor | Codex | Gemini CLI |
|----------------|----------|-------------|--------|-------|------------|
| **Código Abierto** | ✅ MIT | ❌ | ❌ | ❌ | ❌ |
| **Multi-Proveedor** | ✅ 75+ | ❌ Solo Anthropic | ❌ | ❌ | ❌ Solo Google |
| **Terminal First** | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Opciones Locales** | ✅ Ollama, LM Studio | ❌ | ❌ | ❌ | ❌ |
| **Gratuito** | ✅ Pago por uso | ❌ | ❌ | ❌ | ❌ |
| **Extensible** | ✅ Plugins, MCP | ❌ | ❌ | ❌ | ❌ |

### Ventajas Clave de OpenCode

**1. Modelo Open Source**
- Código auditable y modificable
- Comunidad activa de 900+ contribuidores
- Sin vendor lock-in
- Posibilidad de auto-hospedaje para cumplimiento normativo

**2. Multi-Proveedor**
- No dependes de un solo proveedor
- Puedes cambiar de modelo sin cambiar de herramienta
- Compatibilidad con modelos locales para máxima privacidad
- Failover automático entre proveedores

**3. Privacidad y Cumplimiento**
- Tus datos van directamente al proveedor que tú configuras
- Opciones locales (Ollama, LM Studio) para datos sensibles
- Cumplimiento con SOC2, HIPAA (cuando se usa con proveedores adecuados)
- Sin telemetría obligatoria

**4. Rendimiento y Eficiencia**
- TUI optimizada para baja latencia
- Streaming de respuestas en tiempo real
- Gestión eficiente de contexto y ventanas de conversación
- Soporte para tokens extendidos

### Estadísticas de la Comunidad

| Métrica | Valor |
|---------|-------|
| GitHub Stars | 160,000+ |
| Contribuidores | 900+ |
| Desarrolladores Mensuales | 7.5M |
| Proveedores Soportados | 75+ |
| Lenguajes Soportados | Todos los populares |

### Casos de Uso Principales

**Desarrollo de Software**
- Generación de código desde especificaciones
- Refactorización y optimización
- Debugging y resolución de problemas
- Writing de tests automatizados

**DevOps y SRE**
- Configuración de infraestructura como código
- Automatización de pipelines CI/CD
- Análisis y resolución de incidentes
- Documentación de sistemas

**Data Science y ML**
- Análisis exploratorio de datos
- Generación de scripts de procesamiento
- Modelado y experimentación
- Documentación de modelos

**Aprendizaje y Enseñanza**
- Tutoría interactiva de programación
- Explicación de conceptos complejos
- Generación de ejemplos educativos
- Code review formativo

## Guía Paso a Paso

### Paso 1: Explorar el Sitio Web de OpenCode

Primero, visita el sitio oficial para familiarizarte con la documentación:

```bash
# Abre tu navegador y ve a:
# https://opencode.ai

# Explora estas secciones:
# - Documentación principal
# - Guía de inicio rápido
# - Lista de proveedores soportados
# - Ejemplos de uso
```

### Paso 2: Requisitos del Sistema

Antes de instalar, verifica que tu sistema cumpla los requisitos mínimos:

```bash
# Verificar versión de Node.js (requerido: 18+)
node --version

# Verificar npm
npm --version

# Verificar Git
git --version

# Verificar sistema operativo compatible
# macOS, Linux, Windows (via WSL o native)
```

### Paso 3: Instalación Rápida

La forma más rápida de empezar:

```bash
# Opción 1: Curl (recomendada para Linux/macOS)
curl -fsSL https://opencode.ai/install | bash

# Opción 2: npm (funciona en todas las plataformas)
npm install -g opencode

# Opción 3: Para usuarios de macOS con Homebrew
brew install opencode
```

### Paso 4: Verificar la Instalación

```bash
# Verificar que OpenCode está instalado correctamente
opencode --version

# Ver ayuda disponible
opencode --help

# Iniciar OpenCode por primera vez
opencode
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode` | Iniciar la TUI | `opencode` |
| `opencode --version` | Mostrar versión actual | `opencode --version` |
| `opencode --help` | Mostrar ayuda | `opencode --help` |
| `opencode config` | Gestionar configuración | `opencode config list` |
| `opencode provider` | Gestionar proveedores | `opencode provider add` |

## Ejercicios Guiados

### Ejercicio 1: Explorar el Sitio Web de OpenCode

**Objetivo:** Familiarizarte con la documentación y recursos oficiales de OpenCode.

**Instrucciones:**
1. Abre tu navegador y navega a `https://opencode.ai`
2. Localiza y abre la sección de documentación
3. Encuentra la lista completa de proveedores soportados
4. Busca la guía de inicio rápido para tu sistema operativo
5. Identifica al menos 3 casos de uso documentados

**Solución Esperada:**
```bash
# Deberías haber encontrado:
# 1. Documentación en https://opencode.ai/docs
# 2. Proveedores en https://opencode.ai/docs/providers
# 3. Guía de instalación específica para tu SO
# 4. Ejemplos de configuración en GitHub
```

### Ejercicio 2: Comparar Funcionalidades

**Objetivo:** Evaluar las diferencias entre OpenCode y otras herramientas de IA para desarrollo.

**Instrucciones:**
1. Investigar al menos 2 competidores de OpenCode (Claude Code, Cursor, etc.)
2. Crear una tabla comparativa con 5 características clave
3. Identificar 3 ventajas únicas de OpenCode
4. Documentar 2 posibles limitaciones de OpenCode

**Solución Esperada:**
```markdown
| Característica | OpenCode | Competidor 1 | Competidor 2 |
|----------------|----------|--------------|--------------|
| Código Abierto | Sí | No | No |
| Multi-Proveedor | 75+ | Solo 1 | Solo 1 |
| Terminal First | Sí | Sí | No |
| Precio | Pago por uso | Suscripción | Suscripción |
| Opciones Locales | Sí | No | No |
```

### Ejercicio 3: Identificar Casos de Uso

**Objetivo:** Determinar cómo OpenCode puede aplicarse a tus proyectos específicos.

**Instrucciones:**
1. Listar tus proyectos actuales o tipos de desarrollo que realizas
2. Para cada proyecto, identificar 2 formas en que OpenCode podría ayudar
3. Clasificar cada caso de uso por prioridad (Alta, Media, Baja)
4. Crear un plan de implementación básico para el caso de mayor prioridad

**Solución Esperada:**
```markdown
## Mis Casos de Uso

### Proyecto 1: [Nombre]
- **Uso 1:** Generar tests automatizados - Prioridad: Alta
- **Uso 2:** Refactorizar código legacy - Prioridad: Media

### Proyecto 2: [Nombre]
- **Uso 1:** Configurar pipeline CI/CD - Prioridad: Alta
- **Uso 2:** Documentar API endpoints - Prioridad: Baja
```

## Ejercicio Desafío

**Reto:** Configura un entorno de desarrollo completo con OpenCode, incluyendo al menos 2 proveedores diferentes (uno local y uno en la nube).

**Pistas:**
- Usa Ollama para el proveedor local con un modelo pequeño como `qwen2.5-coder`
- Configura un proveedor en la nube como Anthropic o OpenAI
- Prueba cambiar entre proveedores durante una misma sesión
- Documenta las diferencias de rendimiento que observes

## Recursos Adicionales

- [Documentación Oficial de OpenCode](https://opencode.ai/docs)
- [Repositorio de GitHub](https://github.com/anomalyco/opencode)
- [Lista de Proveedores Soportados](https://opencode.ai/docs/providers)
- [Guías de Ejemplos](https://opencode.ai/docs/examples)
- [Comunidad en Discord](https://discord.gg/opencode)

## Autoevaluación

- [ ] Puedo explicar qué es OpenCode y sus ventajas principales
- [ ] Conozco las diferencias entre OpenCode y sus competidores
- [ ] Entiendo la arquitectura multi-proveedor de OpenCode
- [ ] Puedo identificar al menos 3 casos de uso para mis proyectos
- [ ] He explorado la documentación oficial y encontré recursos relevantes
- [ ] Comprendo el modelo de licenciamiento open source de OpenCode
