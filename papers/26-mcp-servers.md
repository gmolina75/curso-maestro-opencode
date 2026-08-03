---
title: "MCP Servers"
module: 26
duration: "55 min"
prerequisites: "Módulo 25 - AGENTS.md y Contexto"
---

# Clase 26: MCP Servers

## Resumen Ejecutivo

El Model Context Protocol (MCP) es un estándar que permite a los agentes de OpenCode conectar con herramientas y servicios externos. Los MCP servers proporcionan una interfaz unificada para integrar servicios como Sentry para monitoreo de errores, Context7 para documentación, o Grep de Vercel para búsqueda avanzada. OpenCode soporta tanto MCP servers locales (ejecutados en la máquina local) como remotos (accesibles vía URL), con autenticación OAuth para servidores remotos.

Los MCP servers amplían significativamente las capacidades de los agentes, permitiéndoles acceder a información y herramientas que van más allá del código fuente local. La integración de MCP servers se configura en `opencode.json` y se gestiona mediante comandos específicos de OpenCode.

## Objetivos de Aprendizaje
- Comprender qué es el Model Context Protocol (MCP)
- Configurar MCP servers locales y remotos
- Gestionar autenticación OAuth para servidores remotos
- Usar comandos de MCP para diagnóstico y gestión
- Integrar MCP servers populares en el flujo de trabajo

## Conceptos Clave

### ¿Qué es MCP?

El Model Context Protocol (MCP) es un protocolo que estandariza la comunicación entre agentes de IA y herramientas externas. Proporciona:

- **Interfaz unificada:** Misma API para diferentes servicios
- **Descubrimiento automático:** Los agentes pueden encontrar herramientas disponibles
- **Seguridad:** Autenticación y autorización integradas
- **Flexibilidad:** Soporte para servidores locales y remotos

### MCP Servers Locales

Los MCP servers locales se ejecutan en la máquina del usuario y se comunican con OpenCode a través de stdio (standard input/output).

```json
// opencode.json
{
  "mcp": {
    "servers": {
      "sentry": {
        "command": "npx",
        "args": ["-y", "@sentry/mcp-server"],
        "env": {
          "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
          "SENTRY_ORG": "mi-organizacion"
        }
      }
    }
  }
}
```

**Características de servidores locales:**
- Se ejecutan en la máquina local
- Comunicación vía stdio
- No requieren red
- Mayor seguridad (datos no salen de la máquina)

### MCP Servers Remotos

Los MCP servers remotos se acceden a través de una URL y pueden requerir autenticación OAuth.

```json
// opencode.json
{
  "mcp": {
    "servers": {
      "context7": {
        "url": "https://mcp.context7.com/mcp",
        "headers": {
          "Authorization": "Bearer ${CONTEXT7_TOKEN}"
        }
      }
    }
  }
}
```

**Características de servidores remotos:**
- Acceso vía HTTP/HTTPS
- Requieren autenticación
- Datos procesados en servidor remoto
- Ideal para servicios en la nube

### Autenticación OAuth

Para servidores remotos que requieren OAuth, OpenCode gestiona el flujo de autenticación:

```bash
# Iniciar proceso de autenticación
opencode mcp auth context7

# El comando:
# 1. Abre el navegador para autenticación
# 2. Recibe el token de retorno
# 3. Almacena el token de forma segura
# 4. Configura el servidor con el token
```

### Almacenamiento de Tokens

Los tokens de autenticación se almacenan de forma segura en el sistema:

- **macOS:** Keychain
- **Linux:** Secret Service o archivo cifrado
- **Windows:** Credential Manager

```bash
# Ver tokens almacenados
opencode mcp auth list

# Output:
# Sentry: ✓ Authenticated
# Context7: ✓ Authenticated
# GitHub: ✗ Not authenticated
```

### Comandos de MCP

OpenCode proporciona comandos específicos para gestionar MCP servers:

| Comando | Descripción |
|---------|-------------|
| `opencode mcp auth <server>` | Autenticar con un servidor MCP |
| `opencode mcp auth list` | Listar autenticaciones |
| `opencode mcp logout <server>` | Cerrar sesión en un servidor |
| `opencode mcp debug` | Depurar problemas de conexión |

### Gestión de MCP por Agente

Los MCP servers se pueden configurar por agente, permitiendo que diferentes agentes tengan acceso a diferentes herramientas:

```json
// opencode.json
{
  "agent": {
    "build": {
      "mcp": ["sentry", "context7"]
    },
    "plan": {
      "mcp": ["context7"]
    }
  }
}
```

### Ejemplos de MCP Servers Populares

#### Sentry
Monitoreo de errores y rendimiento:

```json
{
  "sentry": {
    "command": "npx",
    "args": ["-y", "@sentry/mcp-server"],
    "env": {
      "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
      "SENTRY_ORG": "mi-org"
    }
  }
}
```

**Herramientas disponibles:**
- `list_issues`: Listar errores recientes
- `get_issue`: Obtener detalles de un error
- `resolve_issue`: Marcar error como resuelto

#### Context7
Documentación de librerías y frameworks:

```json
{
  "context7": {
    "url": "https://mcp.context7.com/mcp"
  }
}
```

**Herramientas disponibles:**
- `search_docs`: Buscar documentación
- `get_page`: Obtener página específica
- `list_libraries`: Listar librerías disponibles

#### Grep by Vercel
Búsqueda avanzada en código:

```json
{
  "grep": {
    "command": "npx",
    "args": ["-y", "@vercel/mcp-grep"]
  }
}
```

**Herramientas disponibles:**
- `grep`: Buscar patrones en código
- `glob`: Buscar archivos por patrón
- `read_file`: Leer archivos

## Guía Paso a Paso

### Paso 1: Configurar un MCP Server Local

```json
// opencode.json
{
  "mcp": {
    "servers": {
      "sentry": {
        "command": "npx",
        "args": ["-y", "@sentry/mcp-server"],
        "env": {
          "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
          "SENTRY_ORG": "mi-organizacion"
        }
      }
    }
  }
}
```

### Paso 2: Autenticar con Sentry

```bash
# Configurar variable de entorno
export SENTRY_AUTH_TOKEN="tu-token-aqui"

# Autenticar con Sentry
opencode mcp auth sentry
```

### Paso 3: Verificar la Conexión

```bash
# Listar servidores autenticados
opencode mcp auth list

# Output:
# sentry: ✓ Authenticated
```

### Paso 4: Usar las Herramientas de Sentry

```
# En el chat de OpenCode:
¿Cuáles son los errores más recientes en Sentry?
```

El agente utilizará la herramienta `list_issues` del MCP server de Sentry para obtener la información.

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `mcp.servers` | Configurar servidores MCP | En opencode.json |
| `command` | Comando para servidor local | `"npx"` |
| `args` | Argumentos del comando | `["-y", "@sentry/mcp-server"]` |
| `env` | Variables de entorno | `{"SENTRY_AUTH_TOKEN": "..."}` |
| `url` | URL para servidor remoto | `"https://mcp.context7.com/mcp"` |
| `headers` | Headers HTTP | `{"Authorization": "Bearer ..."}` |
| `opencode mcp auth <server>` | Autenticar servidor | Terminal |
| `opencode mcp auth list` | Listar autenticaciones | Terminal |
| `opencode mcp logout <server>` | Cerrar sesión | Terminal |
| `opencode mcp debug` | Depurar conexión | Terminal |

## Ejercicios Guiados

### Ejercicio 1: Configurar un MCP Server Local con Sentry
**Objetivo:** Configurar y autenticar un servidor MCP local para Sentry.

**Instrucciones:**
1. Obtén un token de autenticación de Sentry
2. Configura el servidor MCP en `opencode.json`
3. Ejecuta `opencode mcp auth sentry`
4. Verifica la autenticación con `opencode mcp auth list`
5. Prueba las herramientas de Sentry en el chat

**Solución Esperada:**
```json
{
  "mcp": {
    "servers": {
      "sentry": {
        "command": "npx",
        "args": ["-y", "@sentry/mcp-server"],
        "env": {
          "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
          "SENTRY_ORG": "mi-organizacion"
        }
      }
    }
  }
}
```

```bash
# Autenticar
export SENTRY_AUTH_TOKEN="sntrys_..."
opencode mcp auth sentry

# Verificar
opencode mcp auth list
# Output: sentry: ✓ Authenticated
```

### Ejercicio 2: Configurar un MCP Server Remoto con Context7
**Objetivo:** Configurar un servidor MCP remoto con autenticación.

**Instrucciones:**
1. Configura el servidor Context7 en `opencode.json`
2. Ejecuta `opencode mcp auth context7`
3. Completa el flujo de autenticación en el navegador
4. Verifica que el servidor está conectado
5. Prueba buscar documentación de una librería

**Solución Esperada:**
```json
{
  "mcp": {
    "servers": {
      "context7": {
        "url": "https://mcp.context7.com/mcp"
      }
    }
  }
}
```

```bash
# Autenticar (abrirá navegador)
opencode mcp auth context7

# Verificar
opencode mcp auth list
# Output: context7: ✓ Authenticated
```

### Ejercicio 3: Diagnosticar Problemas de Conexión MCP
**Objetivo:** Usar herramientas de diagnóstico para resolver problemas de MCP.

**Instrucciones:**
1. Intencionalmente configura un servidor MCP con errores
2. Ejecuta `opencode mcp debug` para diagnosticar
3. Identifica el problema en la salida de debug
4. Corrige la configuración
5. Verifica que el servidor funciona correctamente

**Solución Esperada:**
```json
// Configuración con error intencional
{
  "mcp": {
    "servers": {
      "sentry": {
        "command": "npx",
        "args": ["-y", "@sentry/mcp-server-invalido"]
      }
    }
  }
}
```

```bash
# Diagnosticar
opencode mcp debug

# Output esperado:
# Error: Package not found @sentry/mcp-server-invalido
# Suggestion: Check package name and try again

# Corregir configuración y reintentar
```

## Ejercicio Desafío

**Reto:** Configura un ecosistema completo de MCP servers para un proyecto de desarrollo:
1. Sentry para monitoreo de errores
2. Context7 para documentación
3. Un servidor MCP personalizado para las APIs internas del proyecto
4. Configura cada servidor para un agente específico
5. Implementa un flujo de trabajo que utilize múltiples MCP servers

**Pistas:**
- Usa variables de entorno para tokens sensibles
- Configura permisos por agente para seguridad
- Implementa manejo de errores para conexiones fallidas
- Documenta la configuración para el equipo

## Recursos Adicionales
- [Documentación oficial de OpenCode - MCP](https://opencode.ai/docs/mcp)
- [Guía de configuración MCP](https://opencode.ai/docs/mcp/configuration)
- [Lista de MCP servers populares](https://opencode.ai/docs/mcp/servers)

## Autoevaluación
- [ ] Comprendo qué es el Model Context Protocol (MCP)
- [ ] Puedo configurar MCP servers locales y remotos
- [ ] Sé gestionar autenticación OAuth
- [ ] Uso comandos de MCP para diagnóstico
- [ ] Integro MCP servers populares en mi flujo de trabajo
- [ ] Configuro MCP servers por agente
