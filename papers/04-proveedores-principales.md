---
title: "Proveedores Principales"
module: 4
duration: "55 minutos"
prerequisites: "Módulo 3: OpenCode Zen y OpenCode Go"
---

# Clase 4: Proveedores Principales

## Resumen Ejecutivo

Los proveedores principales de OpenCode son los servicios de IA más populares y ampliamente utilizados que se integran directamente con la plataforma. Estos incluyen Anthropic (Claude), OpenAI (GPT), GitHub Copilot, GitLab Duo y Google Vertex AI. Cada proveedor ofrece diferentes modelos con fortalezas específicas, desde la razonamiento profundo de Claude hasta la versatilidad multimodal de GPT-4o.

La integración con estos proveedores se realiza principalmente a través de OAuth, lo que significa que no necesitas gestionar API keys manualmente - solo autorizas la conexión a través de tu navegador. Esto simplifica enormemente la configuración y mejora la seguridad, ya que no almacenas credenciales sensibles en tu máquina. Para algunos proveedores como Google Vertex AI, se requiere configuración adicional de Google Cloud, pero una vez configurado, la experiencia es igual de fluida.

## Objetivos de Aprendizaje

- Configurar y autenticar los proveedores principales de OpenCode
- Comprender las diferencias entre los modelos de cada proveedor
- Seleccionar el modelo adecuado para diferentes tareas
- Gestionar múltiples proveedores simultáneamente
- Optimizar costos eligiendo el modelo correcto

## Conceptos Clave

### Anthropic (Claude)

Anthropic ofrece la familia de modelos Claude, conocida por su razonamiento profundo y capacidad de análisis.

| Modelo | Descripción | Mejor Para | Velocidad |
|--------|-------------|------------|-----------|
| **Claude Opus** | El más capaz y profundo | Tareas complejas, análisis | Lento |
| **Claude Sonnet** | Balance entre capacidad y velocidad | Uso general, código | Medio |
| **Claude Haiku** | Rápido y eficiente | Tareas simples, chat | Rápido |

**Autenticación OAuth:**
```bash
# En OpenCode, selecciona Anthropic como proveedor
# Se abrirá tu navegador para autorizar
# Completa el flujo de OAuth
# ¡Listo! No necesitas API keys
```

**Modelos Disponibles:**
```yaml
anthropic_models:
  - claude-opus-4-20250514      # Último y más capaz
  - claude-sonnet-4-20250514    # Recomendado para uso general
  - claude-3-5-haiku-20241022   # Rápido, costo-efectivo
  - claude-3-5-sonnet-20241022  # Generación anterior, aún excelente
```

**Casos de Uso Ideales:**
- Análisis de código complejo
- Refactorización de grandes bases de código
- Documentación técnica detallada
- Debugging de problemas difíciles
- Arquitectura de software

### OpenAI (GPT)

OpenAI ofrece los modelos GPT, conocidos por su versatilidad y capacidades multimodales.

| Modelo | Descripción | Mejor Para | Velocidad |
|--------|-------------|------------|-----------|
| **GPT-4o** | Multimodal, razonamiento | Uso general, multimodal | Medio |
| **GPT-4o-mini** | Rápido, costo-efectivo | Tareas simples, chat | Rápido |
| **o1** | Razonamiento profundo | Matemáticas, lógica | Lento |
| **o3** | Último razonamiento | Tareas más complejas | Lento |

**Autenticación OAuth:**
```bash
# En OpenCode, selecciona OpenAI como proveedor
# Se abrirá tu navegador para autorizar con tu cuenta de ChatGPT
# Completa el flujo de OAuth
# ¡Listo! Puedes usar los modelos de OpenAI
```

**Modelos Disponibles:**
```yaml
openai_models:
  - gpt-4o                    # Multimodal, uso general
  - gpt-4o-mini               # Rápido, costo-efectivo
  - o1-preview                # Razonamiento profundo
  - o1-mini                   # Razonamiento rápido
  - o3                        # Último modelo de razonamiento
  - o3-mini                   # Razonamiento eficiente
  - o4-mini                   # Más reciente
```

**Casos de Uso Ideales:**
- Generación de código variado
- Tareas que requieren contexto multimodal (imágenes)
- Prototipado rápido
- Integración con herramientas de OpenAI
- Tareas de razonamiento lógico (modelos o1/o3)

### GitHub Copilot

GitHub Copilot se integra directamente con OpenCode para ofrecer asistencia de codificación potenciada por IA.

**Características:**
- Integración nativa con el ecosistema de GitHub
- Acceso a modelos de múltiples proveedores
- Optimizado para flujos de trabajo de desarrollo
- Soporte para lenguajes populares

**Autenticación OAuth:**
```bash
# En OpenCode, selecciona GitHub Copilot como proveedor
# Se abrirá tu navegador para autorizar con tu cuenta de GitHub
# Completa el flujo de OAuth
# ¡Listo! Copilot está disponible
```

**Modelos Disponibles:**
```yaml
copilot_models:
  - copilot-chat              # Modelo principal de chat
  - copilot-code              # Optimizado para código
  - claude-sonnet-4-20250514  # A través de Copilot
  - gpt-4o                    # A través de Copilot
```

**Casos de Uso Ideales:**
- Desarrolladores que ya usan GitHub extensivamente
- Equipos con suscripciones existentes de Copilot
- Integración con flujos de trabajo de GitHub Actions
- Code review asistido

### GitLab Duo

GitLab Duo ofrece asistencia de IA integrada en la plataforma de GitLab.

**Características:**
- Integración con el ecosistema de GitLab
- Soporte para autenticación OAuth o Personal Access Token (PAT)
- Modelos basados en Claude para mejor rendimiento
- Optimizado para DevSecOps

**Autenticación:**
```bash
# Opción 1: OAuth (recomendada)
# En OpenCode, selecciona GitLab Duo
# Se abrirá tu navegador para autorizar

# Opción 2: Personal Access Token (PAT)
# Genera un PAT en GitLab
# Configúralo en OpenCode
opencode config set provider.gitlab.token "glpat-xxx"
```

**Modelos Disponibles:**
```yaml
gitlab_duo_models:
  - claude-sonnet-4-20250514  # Modelo principal
  - claude-3-5-haiku-20241022 # Rápido
```

**Casos de Uso Ideales:**
- Equipos que usan GitLab para DevSecOps
- Organizaciones con requisitos de compliance
- Flujos de trabajo integrados de CI/CD
- Seguridad y SAST/SCA

### Google Vertex AI

Google Vertex AI ofrece acceso a los modelos Gemini a través de Google Cloud Platform.

**Requisitos Adicionales:**
- Cuenta de Google Cloud Platform habilitada
- Vertex AI habilitado en el proyecto
- Autenticación con gcloud CLI

**Configuración:**
```bash
# 1. Instalar gcloud CLI
# macOS
brew install google-cloud-sdk

# Linux
curl https://sdk.cloud.google.com | bash

# 2. Autenticarse
gcloud auth login
gcloud auth application-default login

# 3. Configurar el proyecto
gcloud config set project TU_PROJECT_ID

# 4. Habilitar Vertex AI API
gcloud services enable aiplatform.googleapis.com

# 5. En OpenCode, selecciona Google Vertex AI
opencode
# /connect → Google Vertex AI
```

**Modelos Disponibles:**
```yaml
vertex_ai_models:
  - gemini-2.5-pro            # Más capaz
  - gemini-2.5-flash          # Rápido y eficiente
  - gemini-2.0-flash          # Generación anterior
  - gemini-1.5-pro            # Largo contexto
```

**Casos de Uso Ideales:**
- Organizaciones que ya usan Google Cloud
- Modelos de largo contexto (hasta 1M tokens)
- Tareas multimodales (imágenes, video, audio)
- Integración con servicios de Google Cloud

## Guía Paso a Paso

### Paso 1: Configurar Anthropic (Claude)

```bash
# 1. Inicia OpenCode
opencode

# 2. Abre el panel de conectividad
#    Presiona / o escribe: /connect

# 3. Selecciona "Anthropic"
#    Navega con flechas y presiona Enter

# 4. Se abrirá tu navegador
#    - Inicia sesión en tu cuenta de Anthropic
#    - Autoriza la conexión a OpenCode
#    - Copia el código de autorización

# 5. Vuelve a OpenCode y pega el código
#    Claude está configurado

# 6. Verifica seleccionando un modelo Claude
#    /model → claude-sonnet-4-20250514
```

### Paso 2: Configurar OpenAI (GPT)

```bash
# 1. En OpenCode, abre /connect
# 2. Selecciona "OpenAI"
# 3. Se abrirá tu navegador
#    - Inicia sesión con tu cuenta de OpenAI
#    - Autoriza la conexión
# 4. Vuelve a OpenCode
# 5. Selecciona un modelo GPT
#    /model → gpt-4o
```

### Paso 3: Configurar GitHub Copilot

```bash
# 1. En OpenCode, abre /connect
# 2. Selecciona "GitHub Copilot"
# 3. Se abrirá tu navegador
#    - Inicia sesión con tu cuenta de GitHub
#    - Autoriza la aplicación de OpenCode
# 4. Vuelve a OpenCode
# 5. Copilot está listo para usar
```

### Paso 4: Cambiar entre Proveedores

```bash
# Dentro de la TUI:

# Cambiar modelo con el comando
/model

# O usar el atajo de teclado
# (generalmente Ctrl+M o Cmd+M en Mac)

# La lista mostrará modelos de TODOS los proveedores configurados
# Selecciona el que prefieras

# También puedes cambiar el proveedor predeterminado
opencode config set defaultProvider anthropic
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `/connect` | Abrir panel de conectividad | `/connect` |
| `/model` | Cambiar modelo activo | `/model gpt-4o` |
| `defaultProvider` | Proveedor predeterminado | `defaultProvider anthropic` |
| `provider.anthropic.apiKey` | API key de Anthropic (si usas BYOK) | `provider.anthropic.apiKey "sk-ant-xxx"` |
| `provider.openai.apiKey` | API key de OpenAI (si usas BYOK) | `provider.openai.apiKey "sk-xxx"` |
| `provider.gitlab.token` | PAT de GitLab | `provider.gitlab.token "glpat-xxx"` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Anthropic y Probar Claude

**Objetivo:** Configurar Anthropic como proveedor y evaluar los modelos de Claude.

**Instrucciones:**
1. Inicia OpenCode y abre `/connect`
2. Selecciona Anthropic y completa la autenticación OAuth
3. Prueba al menos 3 modelos de Claude diferentes
4. Usa el mismo prompt para cada modelo
5. Documenta las diferencias en calidad y velocidad

**Solución Esperada:**
```bash
# Configuración
opencode
# /connect → Anthropic → Completar OAuth

# Prueba de modelos
# Prompt: "Explica la diferencia entre programación funcional y orientada a objetos"

# Modelo 1: /model claude-sonnet-4-20250514
# Respuesta: [Documentar calidad y tiempo]

# Modelo 2: /model claude-3-5-haiku-20241022
# Respuesta: [Documentar calidad y tiempo]

# Modelo 3: /model claude-opus-4-20250514
# Respuesta: [Documentar calidad y tiempo]
```

### Ejercicio 2: Comparar Anthropic vs OpenAI

**Objetivo:** Evaluar las diferencias entre los modelos de Anthropic y OpenAI para tareas de desarrollo.

**Instrucciones:**
1. Configura ambos proveedores (Anthropic y OpenAI)
2. Prepara 5 prompts de desarrollo diferentes
3. Prueba cada prompt con al menos un modelo de cada proveedor
4. Crea una tabla comparativa
5. Identifica qué proveedor es mejor para cada tipo de tarea

**Solución Esperada:**
```markdown
## Comparativa: Anthropic vs OpenAI

| Tarea | Mejor Proveedor | Modelo Recomendado | Razón |
|-------|-----------------|-------------------|-------|
| Refactorización | Anthropic | claude-sonnet-4-20250514 | Mejor análisis de código existente |
| Generación rápida | OpenAI | gpt-4o-mini | Más rápido para tareas simples |
| Análisis complejo | Anthropic | claude-opus-4-20250514 | Razonamiento más profundo |
| Multimodal | OpenAI | gpt-4o | Mejor soporte para imágenes |
| Documentación | Anthropic | claude-sonnet-4-20250514 | Mejor escritura técnica |
```

### Ejercicio 3: Configurar y Usar GitHub Copilot

**Objetivo:** Integrar GitHub Copilot con OpenCode y evaluar su utilidad.

**Instrucciones:**
1. Verifica que tienes una suscripción activa de GitHub Copilot
2. Configura Copilot en OpenCode mediante OAuth
3. Prueba Copilot con 3 prompts diferentes
4. Compara los resultados con al menos un modelo de otro proveedor
5. Documenta las ventajas y limitaciones

**Solución Esperada:**
```bash
# Configuración
opencode
# /connect → GitHub Copilot → Completar OAuth

# Pruebas
# Prompt 1: "Crea una función para validar emails"
# Prompt 2: "Refactoriza este código para usar async/await"
# Prompt 3: "Escribe tests unitarios para esta función"

# Comparar con:
# /model claude-sonnet-4-20250514
# /model gpt-4o
```

## Ejercicio Desafío

**Reto:** Configura 3 proveedores diferentes y crea un sistema de "failover" manual donde uses el mejor modelo para cada tipo de tarea.

**Pistas:**
- Documenta qué modelo usas para cada tipo de tarea
- Crea un "playbook" de selección de modelos
- Considera factores como costo, velocidad y calidad
- Prueba con proyectos reales de tu trabajo diario
- Crea scripts o atajos para cambiar rápidamente entre modelos

## Recursos Adicionales

- [Documentación de Anthropic Claude](https://docs.anthropic.com/)
- [Documentación de OpenAI API](https://platform.openai.com/docs/)
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [GitLab Duo Documentation](https://docs.gitlab.com/ee/user/duo/)
- [Google Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Comparativa de Modelos](https://opencode.ai/docs/models/compare)

## Autoevaluación

- [ ] He configurado al menos 2 proveedores principales
- [ ] Entiendo las diferencias entre los modelos de cada proveedor
- [ ] Puedo cambiar entre proveedores y modelos en la TUI
- [ ] He identificado qué proveedor es mejor para cada tipo de tarea
- [ ] Comprendo las diferencias entre OAuth y API keys
- [ ] Puedo evaluar costos y rendimiento de cada proveedor
- [ ] Documenté mis hallazgos para referencia futura
