---
title: "Integración con GitHub"
module: 29
duration: "50 min"
prerequisites: "Módulo 28 - Integración con IDE"
---

# Clase 29: Integración con GitHub

## Resumen Ejecutivo

OpenCode se integra profundamente con GitHub a través de GitHub Actions, permitiendo que los agentes de IA respondan automáticamente a eventos en el repositorio como comentarios en issues, revisiones de pull requests, y más. La integración se configura mediante el comando `opencode github install`, que instala un GitHub App y configura los workflows necesarios. Esta integración permite automatizar tareas como explicar issues, revisar pull requests, y ejecutar comandos basados en eventos de GitHub.

El sistema utiliza un GitHub App llamado `opencode-agent` que actúa como intermediario entre GitHub y los agentes de OpenCode. Los workflows de GitHub Actions se encargan de desencadenar las acciones apropiadas cuando ocurren eventos configurados.

## Objetivos de Aprendizaje
- Configurar la integración de OpenCode con GitHub Actions
- Instalar y configurar el GitHub App de OpenCode
- Crear workflows personalizados para diferentes eventos
- Configurar opciones como modelo, agente y tokens
- Implementar flujos de trabajo automatizados con GitHub

## Conceptos Clave

### Configuración de GitHub Actions

La integración con GitHub Actions se configura mediante el comando:

```bash
# Instalar integración de GitHub
opencode github install
```

Este comando:
1. Instala el GitHub App `opencode-agent`
2. Crea el archivo `.github/workflows/opencode.yml`
3. Configura los permisos necesarios
4. Establece los eventos por defecto

### GitHub App: opencode-agent

El GitHub App `opencode-agent` es el intermediario entre GitHub y OpenCode:

- **Permisos:**
  - Issues: Leer y escribir
  - Pull Requests: Leer y escribir
  - Comments: Leer y escribir
  - Contents: Leer
  
- **Eventos soportados:**
  - `issue_comment`: Comentarios en issues
  - `pull_request_review_comment`: Comentarios en revisiones de PR
  - `issues`: Creación/actualización de issues
  - `pull_request`: Creación/actualización de PRs
  - `schedule`: Ejecución programada
  - `workflow_dispatch`: Ejecución manual

### Archivo de Workflow

El workflow principal se crea en `.github/workflows/opencode.yml`:

```yaml
name: OpenCode Agent

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, edited]
  pull_request:
    types: [opened, edited, synchronize]
  schedule:
    - cron: '0 0 * * *'  # Diario a medianoche
  workflow_dispatch:
    inputs:
      prompt:
        description: 'Prompt personalizado'
        required: true

jobs:
  opencode:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run OpenCode Agent
        uses: opencode-ai/opencode-action@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          model: ${{ vars.OPENCODE_MODEL || 'anthropic/claude-sonnet-4-20250514' }}
          agent: ${{ vars.OPENCODE_AGENT || 'build' }}
          prompt: ${{ github.event.inputs.prompt || '' }}
```

### Opciones de Configuración

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `OPENCODE_MODEL` | Modelo de IA a utilizar | `anthropic/claude-sonnet-4-20250514` |
| `OPENCODE_AGENT` | Agente a ejecutar | `build`, `plan` |
| `OPENCODE_SHARE` | Compartir resultados | `true`, `false` |
| `OPENCODE_PROMPT` | Prompt personalizado | `"Revisa este PR"` |
| `OPENCODE_TOKEN` | Token de autenticación | Token de GitHub |

### Eventos Soportados

#### issue_comment
Se ejecuta cuando se crea un comentario en un issue:

```yaml
on:
  issue_comment:
    types: [created]
```

**Uso típico:**
- Explicar el contenido de un issue
- Ejecutar comandos mencionados en el issue
- Responder preguntas sobre el issue

#### pull_request_review_comment
Se ejecuta cuando se comenta en una revisión de PR:

```yaml
on:
  pull_request_review_comment:
    types: [created]
```

**Uso típico:**
- Revisar cambios sugeridos
- Explicar fragmentos de código
- Sugerir mejoras específicas

#### issues
Se ejecuta en eventos de issues:

```yaml
on:
  issues:
    types: [opened, edited]
```

**Uso típico:**
- Auto-etiquetar issues
- Generar plantillas de respuesta
- Analizar complejidad del issue

#### pull_request
Se ejecuta en eventos de pull requests:

```yaml
on:
  pull_request:
    types: [opened, edited, synchronize]
```

**Uso típico:**
- Revisar código automáticamente
- Ejecutar pruebas
- Verificar estándares de código

### Prompts Personalizados

Los prompts personalizados permiten definir comportamientos específicos:

```yaml
env:
  OPENCODE_PROMPT: |
    Eres un revisor de código experto.
    Revisa este pull request y:
    1. Identifica problemas potenciales
    2. Sugiere mejoras
    3. Verifica la adherencia a estándares
    4. Reporta hallazgos de forma clara
```

### Ejemplos de Uso

#### Explicar un Issue
```yaml
# En un comentario del issue:
@opencode-agent Explica este issue y sugiere pasos para resolverlo
```

#### Revisar un PR
```yaml
# En un comentario del PR:
@opencode-agent Revisa los cambios y sugiere mejoras
```

#### Ejecutar un Comando
```yaml
# En un comentario:
@opencode-agent Ejecuta npm test y reporta resultados
```

### Autenticación y Seguridad

La integración utiliza el token de GitHub Actions para autenticación:

```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Permisos del token:**
- `contents: read` - Leer archivos del repositorio
- `issues: write` - Crear/modificar issues
- `pull_requests: write` - Crear/modificar PRs
- `checks: write` - Crear checks de status

### Configuración por Repositorio

Las variables de configuración se establecen en Settings → Secrets and variables → Actions:

```
Variables:
- OPENCODE_MODEL: anthropic/claude-sonnet-4-20250514
- OPENCODE_AGENT: build
- OPENCODE_SHARE: true

Secrets:
- OPENCODE_TOKEN: Token personalizado (opcional)
```

## Guía Paso a Paso

### Paso 1: Instalar la Integración

```bash
# Navega al directorio de tu repositorio
cd mi-repositorio

# Instala la integración de GitHub
opencode github install
```

### Paso 2: Verificar la Instalación

```bash
# Verifica que se creó el workflow
cat .github/workflows/opencode.yml

# Verifica que el GitHub App está instalado
# Ve a GitHub → Settings → Integrations
```

### Paso 3: Configurar Variables

En GitHub, ve a tu repositorio:
1. Settings → Secrets and variables → Actions
2. Pestaña Variables → New repository variable
3. Agrega `OPENCODE_MODEL` con el valor deseado
4. Agrega `OPENCODE_AGENT` con el agente preferido

### Paso 4: Probar la Integración

```bash
# Crea un issue o PR
# Agrega un comentario mencionando al bot
@opencode-agent Explica este issue
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode github install` | Instalar integración GitHub | Terminal |
| `OPENCODE_MODEL` | Modelo de IA | `"anthropic/claude-sonnet-4-20250514"` |
| `OPENCODE_AGENT` | Agente a ejecutar | `"build"` |
| `OPENCODE_SHARE` | Compartir resultados | `"true"` |
| `OPENCODE_PROMPT` | Prompt personalizado | `"Revisa este PR"` |
| `@opencode-agent` | Mencionar al bot | En comentarios |

## Ejercicios Guiados

### Ejercicio 1: Instalar GitHub Actions para OpenCode
**Objetivo:** Configurar la integración completa de OpenCode con GitHub Actions.

**Instrucciones:**
1. Navega al directorio de tu repositorio en GitHub
2. Ejecuta `opencode github install`
3. Verifica que se creó el archivo `.github/workflows/opencode.yml`
4. Confirma que el GitHub App está instalado
5. Prueba la integración creando un issue

**Solución Esperada:**
```bash
# Instalar
opencode github install

# Verificar workflow
cat .github/workflows/opencode.yml

# Crear issue de prueba
gh issue create --title "Test Issue" --body "Este es un issue de prueba"

# Comentar en el issue
gh issue comment 1 --body "@opencode-agent Explica este issue"
```

### Ejercicio 2: Crear un Workflow Personalizado
**Objetivo:** Crear un workflow personalizado para revisión automática de PRs.

**Instrucciones:**
1. Edita el archivo `.github/workflows/opencode.yml`
2. Configura el evento `pull_request`
3. Agrega un prompt personalizado para revisión de código
4. Configura las variables necesarias
5. Prueba creando un PR

**Solución Esperada:**
```yaml
name: OpenCode PR Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: OpenCode Review
        uses: opencode-ai/opencode-action@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          model: anthropic/claude-sonnet-4-20250514
          prompt: |
            Revisa este pull request:
            1. Analiza los cambios realizados
            2. Identifica problemas potenciales
            3. Sugiere mejoras específicas
            4. Verifica la adherencia a estándares
            5. Reporta hallazgos de forma clara
```

### Ejercicio 3: Configurar Ejecución Programada
**Objetivo:** Configurar un workflow que se ejecute periódicamente.

**Instrucciones:**
1. Agrega el evento `schedule` al workflow
2. Configura un cron para ejecución diaria
3. Define un prompt para análisis periódico
4. Verifica que el workflow se ejecuta según lo programado

**Solución Esperada:**
```yaml
on:
  schedule:
    - cron: '0 9 * * 1-5'  # Lunes a viernes a las 9am
  
jobs:
  daily-analysis:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Daily Code Analysis
        uses: opencode-ai/opencode-action@v1
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          prompt: |
            Análisis diario del proyecto:
            1. Revisa cambios recientes
            2. Identifica posibles mejoras
            3. Sugiere tareas pendientes
            4. Reporta métricas de calidad
```

## Ejercicio Desafío

**Reto:** Crea un sistema completo de automatización GitHub con OpenCode:
1. Workflow para revisión automática de PRs
2. Workflow para explicación de issues
3. Workflow de análisis periódico de código
4. Workflow de ejecución manual con prompts personalizados
5. Configura notificaciones por email para resultados importantes

Cada workflow debe manejar errores apropiadamente y registrar información de depuración.

**Pistas:**
- Usa `if: always()` para asegurar que los logs se capturen
- Configura timeouts apropiados para workflows largos
- Usa artifacts para preservar resultados entre ejecuciones
- Documenta los prompts personalizados para el equipo

## Recursos Adicionales
- [Documentación oficial de OpenCode - GitHub Integration](https://opencode.ai/docs/github)
- [Guía de configuración de GitHub Actions](https://opencode.ai/docs/github/actions)
- [Ejemplos de workflows](https://opencode.ai/docs/github/examples)

## Autoevaluación
- [ ] Puedo instalar la integración de OpenCode con GitHub
- [ ] Configuro variables de entorno para personalizar el comportamiento
- [ ] Creo workflows personalizados para diferentes eventos
- [ ] Uso prompts personalizados para guiar el comportamiento del agente
- [ ] Implemento ejecución programada y manual
- [ ] Manejo errores y registro información de depuración
