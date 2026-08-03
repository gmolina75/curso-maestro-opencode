---
title: "Custom Tools y Plugins"
module: 27
duration: "45 min"
prerequisites: "Módulo 26 - MCP Servers"
---

# Clase 27: Custom Tools y Plugins

## Resumen Ejecutivo

OpenCode permite extender sus capacidades mediante herramientas personalizadas (custom tools) y un sistema de plugins. Los custom tools son funciones definidas por el usuario en la configuración que los agentes pueden invocar para realizar tareas específicas. El sistema de plugins permite modular funcionalidad reutilizable que se puede compartir entre proyectos y equipos. Los plugins se cargan desde directorios locales o desde paquetes npm, proporcionando una arquitectura extensible y mantenible.

Los custom tools y plugins son fundamentales para adaptar OpenCode a flujos de trabajo específicos, permitiendo integrar servicios internos, automatizar procesos repetitivos, y crear abstracciones de alto nivel para tareas complejas.

## Objetivos de Aprendizaje
- Crear custom tools definidas en la configuración
- Entender el sistema de plugins de OpenCode
- Cargar plugins desde directorios locales y npm
- Configurar plugins en opencode.json
- Integrar plugins populares en el flujo de trabajo

## Conceptos Clave

### Custom Tools: Herramientas Definidas por el Usuario

Los custom tools son funciones que se definen en `opencode.json` y que los agentes pueden invocar como cualquier otra herramienta.

```json
// opencode.json
{
  "tools": {
    "deploy_preview": {
      "description": "Desplegar una vista previa del proyecto",
      "parameters": {
        "branch": {
          "type": "string",
          "description": "Nombre de la rama a desplegar"
        }
      },
      "command": "npm run deploy:preview --branch={{branch}}"
    },
    "create_ticket": {
      "description": "Crear un ticket en el sistema de seguimiento",
      "parameters": {
        "title": {
          "type": "string",
          "description": "Título del ticket"
        },
        "description": {
          "type": "string",
          "description": "Descripción del ticket"
        },
        "priority": {
          "type": "string",
          "enum": ["low", "medium", "high"],
          "description": "Prioridad del ticket"
        }
      },
      "command": "node scripts/create-ticket.js --title='{{title}}' --desc='{{description}}' --priority={{priority}}"
    }
  }
}
```

**Características de custom tools:**
- Se definen en la configuración
- Aceptan parámetros con tipos
- Ejecutan comandos del sistema
- Retornan resultados al agente

### Sistema de Plugins

Los plugins de OpenCode son módulos reutilizables que extienden la funcionalidad del sistema. Se cargan desde:

1. **Directorios locales:** `.opencode/plugins/` o `~/.config/opencode/plugins/`
2. **Paquetes npm:** Instalados desde el registro npm

### Estructura de un Plugin

Un plugin de OpenCode sigue una estructura estándar:

```
mi-plugin/
├── index.js          # Punto de entrada del plugin
├── package.json      # Metadatos del plugin
└── README.md         # Documentación
```

**package.json mínimo:**
```json
{
  "name": "opencode-mi-plugin",
  "version": "1.0.0",
  "description": "Plugin personalizado para OpenCode",
  "main": "index.js",
  "keywords": ["opencode", "plugin"],
  "opencode": {
    "version": ">=1.0.0"
  }
}
```

**index.js del plugin:**
```javascript
module.exports = {
  name: "mi-plugin",
  version: "1.0.0",
  
  // Configuración del plugin
  config: {
    apiKey: {
      type: "string",
      required: true,
      description: "API key for external service"
    }
  },
  
  // Herramientas que provee el plugin
  tools: {
    "my_tool": {
      description: "Herramienta personalizada del plugin",
      parameters: {
        input: {
          type: "string",
          description: "Input para la herramienta"
        }
      },
      execute: async (params, context) => {
        // Lógica de la herramienta
        return { result: "..." };
      }
    }
  },
  
  // Hook de inicialización
  init: async (config) => {
    console.log("Plugin initialized with config:", config);
  }
};
```

### Carga de Plugins desde npm

Los plugins se pueden instalar desde npm y cargar automáticamente:

```bash
# Instalar plugin desde npm
npm install -g opencode-helicone-session

# O localmente en el proyecto
npm install opencode-helicone-session
```

```json
// opencode.json
{
  "plugins": {
    "helicone": {
      "package": "opencode-helicone-session",
      "config": {
        "apiKey": "${HELICONE_API_KEY}"
      }
    }
  }
}
```

### Ejemplos de Plugins Populares

#### opencode-helicone-session
Plugin para sesiones de Helicone:

```json
{
  "plugins": {
    "helicone": {
      "package": "opencode-helicone-session",
      "config": {
        "apiKey": "${HELICONE_API_KEY}",
        "project": "mi-proyecto"
      }
    }
  }
}
```

**Herramientas proporcionadas:**
- `helicone_log`: Registrar interacciones
- `helicone_analytics`: Obtener análisis de uso

#### opencode-gitlab-plugin
Plugin para integración con GitLab:

```json
{
  "plugins": {
    "gitlab": {
      "package": "opencode-gitlab-plugin",
      "config": {
        "token": "${GITLAB_TOKEN}",
        "url": "https://gitlab.com"
      }
    }
  }
}
```

**Herramientas proporcionadas:**
- `gitlab_create_mr`: Crear merge request
- `gitlab_list_projects`: Listar proyectos
- `gitlab_get_file`: Obtener archivo de GitLab

### Configuración de Plugins en opencode.json

```json
{
  "plugins": {
    "plugin-name": {
      "package": "opencode-plugin-name",
      "enabled": true,
      "config": {
        "key1": "value1",
        "key2": "${ENV_VARIABLE}"
      }
    }
  }
}
```

**Campos de configuración:**
- `package`: Nombre del paquete npm
- `enabled`: Habilitar/deshabilitar plugin
- `config`: Configuración específica del plugin

### Integración en el Flujo de Trabajo

Los plugins se integran en el flujo de trabajo de los agentes:

1. **Descubrimiento:** OpenCode carga los plugins al iniciar
2. **Inicialización:** Los plugins se inicializan con su configuración
3. **Registro:** Las herramientas se registran en el sistema
4. **Uso:** Los agentes pueden invocar las herramientas
5. **Limpieza:** Los plugins se descargan al cerrar OpenCode

## Guía Paso a Paso

### Paso 1: Crear un Custom Tool

```json
// opencode.json
{
  "tools": {
    "run_tests": {
      "description": "Ejecutar suite de pruebas",
      "parameters": {
        "pattern": {
          "type": "string",
          "description": "Patrón de archivos de prueba",
          "default": "**/*.test.js"
        }
      },
      "command": "npm test -- --testPathPattern={{pattern}}"
    }
  }
}
```

### Paso 2: Crear un Plugin Local

```bash
# Crear directorio de plugins
mkdir -p .opencode/plugins

# Crear estructura del plugin
mkdir -p .opencode/plugins/my-plugin
cd .opencode/plugins/my-plugin
```

```javascript
// .opencode/plugins/my-plugin/index.js
module.exports = {
  name: "my-plugin",
  version: "1.0.0",
  
  tools: {
    "greet": {
      description: "Saluda al usuario",
      parameters: {
        name: {
          type: "string",
          description: "Nombre del usuario"
        }
      },
      execute: async (params) => {
        return { 
          message: `¡Hola, ${params.name}! Bienvenido a OpenCode.` 
        };
      }
    }
  }
};
```

```json
// .opencode/plugins/my-plugin/package.json
{
  "name": "opencode-my-plugin",
  "version": "1.0.0",
  "main": "index.js",
  "keywords": ["opencode", "plugin"]
}
```

### Paso 3: Configurar el Plugin

```json
// opencode.json
{
  "plugins": {
    "my-plugin": {
      "package": "./.opencode/plugins/my-plugin",
      "enabled": true
    }
  }
}
```

### Paso 4: Usar el Plugin

```bash
# Reiniciar OpenCode para cargar el plugin
opencode

# En el chat:
Saluda a Juan usando la herramienta greet
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `tools` | Definir custom tools | En opencode.json |
| `plugins` | Configurar plugins | En opencode.json |
| `package` | Paquete npm del plugin | `"opencode-plugin-name"` |
| `enabled` | Habilitar/deshabilitar | `true` / `false` |
| `config` | Configuración del plugin | `{"key": "value"}` |
| `.opencode/plugins/` | Directorio local de plugins | - |

## Ejercicios Guiados

### Ejercicio 1: Crear un Custom Tool para Deployment
**Objetivo:** Crear una herramienta personalizada que automatice el proceso de deployment.

**Instrucciones:**
1. Define un custom tool `deploy` en `opencode.json`
2. Configura parámetros para ambiente y versión
3. Incluye validación de parámetros
4. Prueba la herramienta ejecutando un deployment de prueba

**Solución Esperada:**
```json
{
  "tools": {
    "deploy": {
      "description": "Desplegar la aplicación a un ambiente",
      "parameters": {
        "environment": {
          "type": "string",
          "enum": ["staging", "production"],
          "description": "Ambiente de destino"
        },
        "version": {
          "type": "string",
          "description": "Versión a desplegar (e.g., v1.2.3)"
        }
      },
      "command": "node scripts/deploy.js --env={{environment}} --version={{version}}"
    }
  }
}
```

### Ejercicio 2: Crear un Plugin de Notificaciones
**Objetivo:** Crear un plugin que envíe notificaciones cuando se completen tareas.

**Instrucciones:**
1. Crea la estructura del plugin en `.opencode/plugins/`
2. Implementa una herramienta `notify` que envíe notificaciones
3. Configura el plugin en `opencode.json`
4. Prueba el plugin ejecutando una tarea

**Solución Esperada:**
```javascript
// .opencode/plugins/notify/index.js
module.exports = {
  name: "notify",
  version: "1.0.0",
  
  config: {
    webhookUrl: {
      type: "string",
      required: true,
      description: "Webhook URL for notifications"
    }
  },
  
  tools: {
    "send_notification": {
      description: "Enviar notificación a webhook",
      parameters: {
        message: {
          type: "string",
          "description": "Mensaje de notificación"
        },
        level: {
          type: "string",
          enum: ["info", "warning", "error"],
          description: "Nivel de la notificación"
        }
      },
      execute: async (params, context) => {
        const response = await fetch(context.config.webhookUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            text: `[${params.level.toUpperCase()}] ${params.message}`
          })
        });
        
        return { 
          success: response.ok,
          status: response.status 
        };
      }
    }
  }
};
```

```json
{
  "plugins": {
    "notify": {
      "package": "./.opencode/plugins/notify",
      "config": {
        "webhookUrl": "${NOTIFICATION_WEBHOOK_URL}"
      }
    }
  }
}
```

### Ejercicio 3: Instalar y Configurar un Plugin de npm
**Objetivo:** Instalar un plugin existente desde npm y configurarlo.

**Instrucciones:**
1. Busca un plugin de OpenCode en npm
2. Instálalo en tu proyecto
3. Configúralo en `opencode.json`
4. Verifica que las herramientas están disponibles
5. Prueba una de las herramientas del plugin

**Solución Esperada:**
```bash
# Instalar plugin
npm install opencode-helicone-session
```

```json
{
  "plugins": {
    "helicone": {
      "package": "opencode-helicone-session",
      "config": {
        "apiKey": "${HELICONE_API_KEY}"
      }
    }
  }
}
```

## Ejercicio Desafío

**Reto:** Crea un ecosistema completo de plugins para tu proyecto:
1. Un plugin de `deploy` con soporte para múltiples ambientes
2. Un plugin de `notifications` para alertas del equipo
3. Un plugin de `analytics` para métricas de uso
4. Un custom tool para gestión de migraciones de base de datos

Cada plugin debe estar documentado, tener configuración flexible, y manejar errores apropiadamente.

**Pistas:**
- Usa variables de entorno para datos sensibles
- Implementa validación de parámetros
- Incluye logging para debugging
- Documenta cada herramienta con ejemplos de uso

## Recursos Adicionales
- [Documentación oficial de OpenCode - Plugins](https://opencode.ai/docs/plugins)
- [Guía de creación de plugins](https://opencode.ai/docs/plugins/creating)
- [Plugins populares](https://opencode.ai/docs/plugins/popular)

## Autoevaluación
- [ ] Puedo crear custom tools en `opencode.json`
- [ ] Entiendo la estructura de un plugin de OpenCode
- [ ] Puedo crear plugins locales con herramientas personalizadas
- [ ] Sé instalar y configurar plugins desde npm
- [ ] Configuro plugins con datos sensibles usando variables de entorno
- [ ] Implemento manejo de errores en mis plugins
