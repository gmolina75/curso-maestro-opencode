---
title: "Integración con GitLab"
module: 30
duration: "45 min"
prerequisites: "Módulo 29 - Integración con GitHub"
---

# Clase 30: Integración con GitLab

## Resumen Ejecutivo

OpenCode se integra con GitLab a través de GitLab Duo Agent Platform (DAP), proporcionando capacidades de IA para automatizar tareas en repositorios GitLab. La integración requiere una suscripción Premium o Ultimate de GitLab y se autentica mediante OAuth o Personal Access Token. OpenCode soporta múltiples modelos de GitLab DAP incluyendo Haiku, Sonnet y Opus, permitiendo elegir el modelo apropiado según la tarea y el presupuesto.

La integración con GitLab incluye soporte para repositorios auto-hospedados, un plugin de API Tools para interacción directa con la API de GitLab, y workflows específicos para diferentes eventos de GitLab como merge requests, issues y pipelines.

## Objetivos de Aprendizaje
- Configurar la integración de OpenCode con GitLab
- Autenticar usando OAuth o Personal Access Token
- Seleccionar el modelo apropiado de GitLab DAP
- Configurar repositorios auto-hospedados
- Usar el plugin de GitLab API Tools

## Conceptos Clave

### GitLab Duo Agent Platform (DAP)

GitLab DAP es la plataforma de IA de GitLab que permite a OpenCode conectarse y automatizar tareas. Proporciona:

- **Modelos de IA:** Múltiples opciones según necesidades
- **Integración nativa:** Funciona directamente con GitLab
- **Seguridad:** Autenticación robusta y permisos granulares
- **Escalabilidad:** Soporte para repositorios grandes

### Requisitos de Suscripción

La integración con GitLab DAP requiere:

| Suscripción | Modelos Disponibles | Límites |
|-------------|---------------------|---------|
| Premium | Haiku, Sonnet | Uso moderado |
| Ultimate | Haiku, Sonnet, Opus | Uso ilimitado |

### Modelos Disponibles

| Modelo | Velocidad | Calidad | Costo | Uso Recomendado |
|--------|-----------|---------|-------|-----------------|
| Haiku 4.5 | Rápido | Bueno | Bajo | Tareas simples |
| Sonnet 4.5 | Medio | Excelente | Medio | Tareas complejas |
| Opus 4.5 | Lento | Máximo | Alto | Tareas críticas |

### Autenticación con OAuth

La autenticación OAuth es el método recomendado:

```bash
# Iniciar flujo de autenticación OAuth
opencode gitlab auth

# El comando:
# 1. Abre el navegador para autenticación
# 2. Redirige a GitLab para autorización
# 3. Recibe el token de retorno
# 4. Almacena el token de forma segura
```

### Autenticación con Personal Access Token

Alternativamente, se puede usar un Personal Access Token:

```bash
# Configurar token manualmente
export GITLAB_TOKEN="glpat-..."

# O en opencode.json
{
  "gitlab": {
    "token": "${GITLAB_TOKEN}"
  }
}
```

**Permisos requeridos del token:**
- `api` - Acceso completo a la API
- `read_repository` - Leer repositorios
- `write_repository` - Escribir en repositorios
- `read_api` - Leer datos de la API

### Configuración de Repositorios Auto-Hospedados

Para GitLab auto-hospedado, se debe configurar la URL:

```json
{
  "gitlab": {
    "url": "https://gitlab.mi-empresa.com",
    "token": "${GITLAB_TOKEN}"
  }
}
```

```bash
# Autenticar con GitLab auto-hospedado
opencode gitlab auth --url https://gitlab.mi-empresa.com
```

### Plugin de GitLab API Tools

El plugin de GitLab API Tools proporciona herramientas para interactuar directamente con la API de GitLab:

```json
{
  "plugins": {
    "gitlab-api": {
      "package": "opencode-gitlab-plugin",
      "config": {
        "token": "${GITLAB_TOKEN}",
        "url": "https://gitlab.com"
      }
    }
  }
}
```

**Herramientas disponibles:**
- `gitlab_list_projects`: Listar proyectos
- `gitlab_get_project`: Obtener detalles de un proyecto
- `gitlab_create_merge_request`: Crear merge request
- `gitlab_list_merge_requests`: Listar merge requests
- `gitlab_get_merge_request`: Obtener detalles de MR
- `gitlab_create_issue`: Crear issue
- `gitlab_list_issues`: Listar issues
- `gitlab_get_file`: Obtener archivo del repositorio
- `gitlab_list_pipelines`: Listar pipelines

### DAP Workflow Models

Los modelos DAP se utilizan para diferentes flujos de trabajo:

#### Modelo de Análisis
```json
{
  "gitlab": {
    "workflow": {
      "model": "sonnet-4-5",
      "tasks": ["code-review", "security-analysis"]
    }
  }
}
```

#### Modelo de Generación
```json
{
  "gitlab": {
    "workflow": {
      "model": "opus-4-5",
      "tasks": ["code-generation", "documentation"]
    }
  }
}
```

### Configuración en opencode.json

```json
{
  "gitlab": {
    "url": "https://gitlab.com",
    "token": "${GITLAB_TOKEN}",
    "model": "sonnet-4-5",
    "workflow": {
      "auto_review": true,
      "auto_test": true
    }
  }
}
```

### Eventos Soportados

| Evento | Descripción | Uso Típico |
|--------|-------------|------------|
| `merge_request` | Creación/actualización de MR | Revisión automática |
| `issue` | Creación/actualización de issue | Análisis y respuesta |
| `pipeline` | Ejecución de pipeline | Monitoreo y reportes |
| `push` | Push de código | Análisis de cambios |

## Guía Paso a Paso

### Paso 1: Configurar Autenticación

```bash
# Usando OAuth (recomendado)
opencode gitlab auth

# Usando Personal Access Token
export GITLAB_TOKEN="glpat-..."
```

### Paso 2: Configurar en opencode.json

```json
{
  "gitlab": {
    "url": "https://gitlab.com",
    "token": "${GITLAB_TOKEN}",
    "model": "sonnet-4-5"
  }
}
```

### Paso 3: Instalar Plugin de API Tools

```bash
# Instalar plugin
npm install opencode-gitlab-plugin
```

```json
{
  "plugins": {
    "gitlab-api": {
      "package": "opencode-gitlab-plugin",
      "config": {
        "token": "${GITLAB_TOKEN}"
      }
    }
  }
}
```

### Paso 4: Probar la Integración

```bash
# Reiniciar OpenCode
opencode

# En el chat:
¿Cuáles son los merge requests abiertos en mi proyecto?
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode gitlab auth` | Autenticar con GitLab | Terminal |
| `gitlab.url` | URL de GitLab | `"https://gitlab.com"` |
| `gitlab.token` | Token de autenticación | `"${GITLAB_TOKEN}"` |
| `gitlab.model` | Modelo a utilizar | `"sonnet-4-5"` |
| `opencode-gitlab-plugin` | Plugin de API Tools | En npm |

## Ejercicios Guiados

### Ejercicio 1: Configurar Autenticación OAuth con GitLab
**Objetivo:** Establecer conexión segura con GitLab usando OAuth.

**Instrucciones:**
1. Verifica que tienes suscripción Premium o Ultimate
2. Ejecuta `opencode gitlab auth`
3. Completa el flujo de autenticación en el navegador
4. Verifica que el token se almacena correctamente
5. Prueba la conexión listando proyectos

**Solución Esperada:**
```bash
# Autenticar
opencode gitlab auth

# Verificar autenticación
opencode gitlab auth list
# Output: gitlab: ✓ Authenticated

# Probar conexión
opencode
# En chat: Lista mis proyectos en GitLab
```

### Ejercicio 2: Configurar GitLab Auto-Hospedado
**Objetivo:** Conectar OpenCode con una instancia de GitLab auto-hospedada.

**Instrucciones:**
1. Obtén la URL de tu instancia de GitLab
2. Genera un Personal Access Token con permisos API
3. Configura la URL y token en opencode.json
4. Prueba la conexión con tu instancia

**Solución Esperada:**
```json
{
  "gitlab": {
    "url": "https://gitlab.mi-empresa.com",
    "token": "${GITLAB_TOKEN}",
    "model": "sonnet-4-5"
  }
}
```

```bash
export GITLAB_TOKEN="glpat-..."

opencode
# En chat: ¿Qué proyectos hay en mi instancia de GitLab?
```

### Ejercicio 3: Usar el Plugin de API Tools
**Objetivo:** Interactuar con GitLab directamente a través del plugin.

**Instrucciones:**
1. Instala el plugin `opencode-gitlab-plugin`
2. Configúralo en opencode.json
3. Usa las herramientas del plugin para listar merge requests
4. Crea un issue de prueba
5. Verifica que las acciones se reflejan en GitLab

**Solución Esperada:**
```bash
npm install opencode-gitlab-plugin
```

```json
{
  "plugins": {
    "gitlab-api": {
      "package": "opencode-gitlab-plugin",
      "config": {
        "token": "${GITLAB_TOKEN}",
        "url": "https://gitlab.com"
      }
    }
  }
}
```

```
# En chat de OpenCode:
¿Cuáles son los merge requests pendientes en mi proyecto?

# Resultado:
# 1. !123 - Actualizar dependencias (opened)
# 2. !124 - Fix: Corregir error de autenticación (opened)

# Crear issue de prueba:
Crea un issue con título "Test Issue" y descripción "Este es un issue de prueba"
```

## Ejercicio Desafío

**Reto:** Configura un sistema completo de automatización GitLab con OpenCode:
1. Configura autenticación OAuth con tu instancia de GitLab
2. Instala y configura el plugin de API Tools
3. Crea un workflow que revise automáticamente los merge requests
4. Implementa análisis de código para issues nuevos
5. Configura monitoreo de pipelines con notificaciones

**Pistas:**
- Usa diferentes modelos según la tarea
- Implementa manejo de errores para operaciones de API
- Configura timeouts para operaciones largas
- Documenta la configuración para el equipo

## Recursos Adicionales
- [Documentación oficial de OpenCode - GitLab Integration](https://opencode.ai/docs/gitlab)
- [Guía de GitLab DAP](https://opencode.ai/docs/gitlab/dap)
- [Plugin de API Tools](https://opencode.ai/docs/gitlab/plugin)

## Autoevaluación
- [ ] Puedo configurar autenticación OAuth con GitLab
- [ ] Selecciono el modelo apropiado según la tarea
- [ ] Configuro repositorios auto-hospedados correctamente
- [ ] Uso el plugin de API Tools para interactuar con GitLab
- [ ] Implemento workflows automatizados para merge requests
- [ ] Manejo errores y configuro timeouts apropiados
