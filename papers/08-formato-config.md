---
title: "Formato de Configuración"
module: 8
duration: "45 minutos"
prerequisites: "Módulo 7: Proveedor Custom"
---

# Clase 8: Formato de Configuración

## Resumen Ejecutivo

OpenCode utiliza un sistema de configuración flexible y potente que soporta múltiples formatos y ubicaciones. El archivo de configuración principal puede estar en formato JSON o JSONC (JSON con comentarios), lo que permite documentar la configuración directamente en el archivo. La configuración de OpenCode es extremadamente detallada, cubriendo desde la selección de proveedores y modelos hasta aspectos avanzados como timeouts, variables de entorno y preferencias de la interfaz de usuario.

Un aspecto crucial de la configuración de OpenCode es el esquema JSON disponible en `https://opencode.ai/config.json`, que permite la validación en tiempo real y autocompletado en editores de código. Esto es especialmente útil para evitar errores de configuración y para descubrir opciones disponibles. El sistema de configuración está diseñado para ser jerárquico, con múltiples niveles de precedencia que permiten configuración global, de proyecto y por usuario.

## Objetivos de Aprendizaje

- Comprender los formatos de configuración soportados (JSON y JSONC)
- Usar el esquema JSON para validación y autocompletado
- Crear archivos de configuración correctos y completos
- Configurar todas las secciones principales de OpenCode
- Validar la configuración existente
- Documentar la configuración con comentarios

## Conceptos Clave

### Formatos Soportados

OpenCode soporta dos formatos principales:

| Formato | Extensión | Características | Uso Recomendado |
|---------|-----------|-----------------|-----------------|
| **JSON** | `.json` | Estándar, sin comentarios | Configuración programática |
| **JSONC** | `.jsonc` | JSON con comentarios | Configuración documentada |

```jsonc
// Ejemplo de JSONC (JSON con comentarios)
{
  // Configuración del proveedor
  "provider": {
    "anthropic": {
      // OAuth - no requiere API key
      "type": "oauth"
    }
  },
  
  // Modelo predeterminado
  "model": "claude-sonnet-4-20250514",
  
  // Preferencias de la interfaz
  "theme": "dark"
}
```

### JSON Schema para Validación

OpenCode proporciona un esquema JSON oficial para validación:

```bash
# URL del esquema
# https://opencode.ai/config.json

# Para usar en tu archivo de configuración
{
  "$schema": "https://opencode.ai/config.json",
  // resto de la configuración...
}
```

**Ventajas del esquema:**
- Validación en tiempo real en editores como VS Code
- Autocompletado de opciones disponibles
- Documentación integrada de cada opción
- Detección temprana de errores

### Estructura del Archivo de Configuración

El archivo de configuración tiene una estructura jerárquica bien definida:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  
  // ============ PROVEEDORES ============
  "provider": {
    "nombre-proveedor": {
      "type": "oauth|api-key|openai-compatible",
      "baseURL": "https://...",
      "apiKey": "sk-...",
      "models": {
        "model": "modelo-principal",
        "small_model": "modelo-rapido",
        "blacklist": [],
        "whitelist": []
      },
      "timeout": 60000,
      "chunkTimeout": 30000
    }
  },
  
  // ============ MODELOS ============
  "model": "nombre-del-modelo",
  "smallModel": "nombre-modelo-rapido",
  
  // ============ INTERFAZ ============
  "theme": "dark|light|system",
  "locale": "es|en|...",
  
  // ============ VARIABLES DE ENTORNO ============
  "env": {
    "VARIABLE": "valor"
  },
  
  // ============ INSTRUCCIONES ============
  "instructions": "Instrucciones personalizadas para la IA",
  
  // ============ PERMISOS ============
  "permissions": {
    "bash": "approve|reject|ask",
    "write": "approve|reject|ask",
    "edit": "approve|reject|ask"
  }
}
```

### Secciones Principales de Configuración

#### 1. Provider Configuration

```jsonc
{
  "provider": {
    // Proveedor OAuth (sin API key)
    "anthropic": {
      "type": "oauth"
    },
    
    // Proveedor con API key
    "openai": {
      "type": "api-key",
      "apiKey": "sk-..."
    },
    
    // Proveedor compatible con OpenAI
    "mi-servidor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "apiKey": "mi-key",
      "models": {
        "model": "mi-modelo",
        "small_model": "mi-modelo-rapido",
        "whitelist": ["modelo-1", "modelo-2"]
      },
      "timeout": 90000
    }
  }
}
```

#### 2. Model Configuration

```jsonc
{
  // Modelo principal para tareas complejas
  "model": "claude-sonnet-4-20250514",
  
  // Modelo rápido para tareas simples
  "smallModel": "claude-3-5-haiku-20241022",
  
  // O configurar por proveedor
  "provider": {
    "anthropic": {
      "models": {
        "model": "claude-sonnet-4-20250514",
        "small_model": "claude-3-5-haiku-20241022"
      }
    }
  }
}
```

#### 3. Interface Configuration

```jsonc
{
  // Tema de la interfaz
  "theme": "dark",
  
  // Idioma
  "locale": "es",
  
  // Configuración de la TUI
  "tui": {
    "showLineNumbers": true,
    "wordWrap": true,
    "vimMode": false
  }
}
```

#### 4. Environment Variables

```jsonc
{
  // Variables de entorno para la configuración
  "env": {
    "ANTHROPIC_API_KEY": "{env:ANTHROPIC_API_KEY}",
    "OPENAI_API_KEY": "{env:OPENAI_API_KEY}",
    "MI_VARIABLE_CUSTOM": "valor-estatico"
  }
}
```

#### 5. Instructions

```jsonc
{
  // Instrucciones personalizadas para la IA
  "instructions": "Eres un asistente de programación especializado en Python. Siempre usa type hints y sigue PEP 8.",
  
  // O cargar desde archivo
  "instructionsFile": "~/.config/opencode/instructions.md"
}
```

#### 6. Permissions

```jsonc
{
  // Configuración de permisos para acciones
  "permissions": {
    // Ejecución de comandos bash
    "bash": "ask",
    
    // Escritura de archivos
    "write": "approve",
    
    // Edición de archivos
    "edit": "approve",
    
    // Acceso a red
    "network": "allow"
  }
}
```

### Validación de Configuración

```bash
# Validar archivo de configuración
opencode config validate

# Ver configuración actual
opencode config list

# Verificar una sección específica
opencode config list | grep provider

# Resetear configuración a valores por defecto
opencode config reset

# Exportar configuración actual
opencode config export > backup-config.json
```

## Guía Paso a Paso

### Paso 1: Crear Archivo de Configuración con JSON Schema

```bash
# 1. Crear directorio de configuración
mkdir -p ~/.config/opencode

# 2. Crear archivo de configuración básico
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "oauth"
    }
  },
  
  "model": "claude-sonnet-4-20250514",
  "theme": "dark",
  "locale": "es"
}
EOF

# 3. Verificar que el esquema está configurado correctamente
# En VS Code, el editor debería mostrar autocompletado y validación
```

### Paso 2: Configurar Proveedores

```bash
# Agregar múltiples proveedores
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "oauth"
    },
    "openai": {
      "type": "oauth"
    },
    "mi-servidor-local": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "models": {
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b",
        "whitelist": ["llama-3.1-70b", "llama-3.1-8b"]
      },
      "timeout": 90000
    }
  },
  
  "model": "claude-sonnet-4-20250514",
  "theme": "dark"
}
EOF
```

### Paso 3: Configurar Variables de Entorno

```bash
# Agregar variables de entorno
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "oauth"
    }
  },
  
  "env": {
    "ANTHROPIC_API_KEY": "{env:ANTHROPIC_API_KEY}",
    "OPENAI_API_KEY": "{env:OPENAI_API_KEY}"
  },
  
  "model": "claude-sonnet-4-20250514"
}
EOF

# Las variables de entorno del sistema se usarán automáticamente
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
```

### Paso 4: Configurar Instrucciones Personalizadas

```bash
# Crear archivo de instrucciones
cat > ~/.config/opencode/instructions.md << 'EOF'
# Instrucciones para la IA

## Estilo de Código
- Usa type hints en Python
- Sigue PEP 8
- Incluye docstrings en todas las funciones
- Usa nombres descriptivos para variables

## Respuestas
- Sé conciso pero completo
- Incluye ejemplos de uso
- Explica el porqué de las decisiones

## Seguridad
- Nunca incluyas secrets o API keys en el código
- Valida siempre las entradas de usuario
- Usa parámetros seguros por defecto
EOF

# Referenciar en la configuración
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "oauth"
    }
  },
  
  "instructionsFile": "~/.config/opencode/instructions.md",
  "model": "claude-sonnet-4-20250514"
}
EOF
```

### Paso 5: Validar la Configuración

```bash
# Validar que el archivo JSON es válido
python3 -m json.tool ~/.config/opencode/opencode.json

# Ver la configuración cargada por OpenCode
opencode config list

# Verificar proveedores configurados
opencode config list | grep -A 10 provider

# Probar la configuración
opencode
# Debería abrir con la configuración aplicada
```

### Paso 6: Documentar con Comentarios (JSONC)

```bash
# Para documentar la configuración, usa JSONC
cat > ~/.config/opencode/opencode.jsonc << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  // ============================================
  // CONFIGURACIÓN DE PROVEEDORES
  // ============================================
  "provider": {
    // Proveedor principal - Anthropic con OAuth
    "anthropic": {
      "type": "oauth"
    },
    
    // Servidor local para uso offline
    "mi-servidor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      // Timeout aumentado para modelos grandes
      "timeout": 120000,
      "models": {
        // Solo mostrar modelos específicos
        "whitelist": ["llama-3.1-70b", "llama-3.1-8b"],
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b"
      }
    }
  },
  
  // ============================================
  // CONFIGURACIÓN DE INTERFAZ
  // ============================================
  // Tema oscuro para mejor experiencia visual
  "theme": "dark",
  
  // Idioma español
  "locale": "es",
  
  // ============================================
  // INSTRUCCIONES PERSONALIZADAS
  // ============================================
  // Instrucciones que se agregarán a cada prompt
  "instructions": "Eres un experto en desarrollo de software."
}
EOF

# Nota: OpenCode también acepta .jsonc como extensión
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `$schema` | URL del esquema JSON | `"$schema": "https://opencode.ai/config.json"` |
| `provider.*.type` | Tipo de proveedor | `"type": "oauth"` |
| `provider.*.baseURL` | URL base del endpoint | `"baseURL": "http://localhost:8000/v1"` |
| `provider.*.apiKey` | API key | `"apiKey": "sk-xxx"` |
| `model` | Modelo principal | `"model": "claude-sonnet-4-20250514"` |
| `smallModel` | Modelo rápido | `"smallModel": "claude-3-5-haiku-20241022"` |
| `theme` | Tema de la interfaz | `"theme": "dark"` |
| `locale` | Idioma | `"locale": "es"` |
| `env.*` | Variables de entorno | `"env": {"KEY": "{env:KEY}"}` |
| `instructions` | Instrucciones personalizadas | `"instructions": "..."` |
| `instructionsFile` | Archivo de instrucciones | `"instructionsFile": "~/.config/opencode/instructions.md"` |
| `permissions.*` | Permisos de acciones | `"permissions": {"bash": "ask"}` |

## Ejercicios Guiados

### Ejercicio 1: Crear Configuración Completa

**Objetivo:** Crear un archivo de configuración completo y válido para OpenCode.

**Instrucciones:**
1. Crea un archivo de configuración con el esquema JSON
2. Configura al menos 2 proveedores (1 OAuth, 1 custom)
3. Establece un modelo principal y uno rápido
4. Configura el tema y el idioma
5. Agrega instrucciones personalizadas
6. Valida que el archivo es correcto

**Solución Esperada:**
```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "oauth"
    },
    "mi-servidor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "models": {
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b"
      }
    }
  },
  
  "model": "claude-sonnet-4-20250514",
  "smallModel": "claude-3-5-haiku-20241022",
  "theme": "dark",
  "locale": "es",
  "instructions": "Eres un experto en desarrollo de software."
}
```

### Ejercicio 2: Usar JSON Schema en VS Code

**Objetivo:** Configurar VS Code para usar el esquema JSON de OpenCode.

**Instrucciones:**
1. Instala la extensión de OpenCode para VS Code (si está disponible)
2. Crea un archivo de configuración OpenCode
3. Verifica que el autocompletado funciona
4. Introduce un error a propósito
5. Verifica que el validador detecta el error
6. Corrige el error y verifica

**Solución Esperada:**
```bash
# En VS Code:
# 1. Crear archivo opencode.json en ~/.config/opencode/
# 2. VS Code debería mostrar autocompletado al escribir "pro"
# 3. Intentar agregar un campo inexistente: "invalidField": true
# 4. VS Code debería mostrar una advertencia/error
# 5. Corregir el campo
```

### Ejercicio 3: Configurar Variables de Entorno

**Objetivo:** Usar variables de entorno en la configuración de OpenCode.

**Instrucciones:**
1. Define una variable de entorno personalizada
2. Configura OpenCode para usar esa variable
3. Verifica que la variable se resuelve correctamente
4. Configura múltiples variables
5. Documenta el uso de cada variable

**Solución Esperada:**
```bash
# Definir variable de entorno
export MI_API_KEY="sk-custom-key-123"

# Configurar en OpenCode
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "env": {
    "MI_API_KEY": "{env:MI_API_KEY}"
  },
  "provider": {
    "mi-proveedor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "apiKey": "{env:MI_API_KEY}"
    }
  }
}
EOF

# Verificar
opencode config list | grep MI_API_KEY
```

## Ejercicio Desafío

**Reto:** Crea un sistema de configuración modular para OpenCode que incluya:
1. Configuración base compartida entre proyectos
2. Configuración específica por proyecto
3. Variables de entorno para secrets
4. Instrucciones personalizadas por tipo de proyecto
5. Documentación completa de cada sección

**Pistas:**
- Usa la jerarquía de configuración de OpenCode
- Crea templates de configuración reutilizables
- Implementa scripts de validación
- Documenta con comentarios en formato JSONC
- Crea un "config generator" que genere archivos de configuración

## Recursos Adicionales

- [Esquema JSON de Configuración](https://opencode.ai/config.json)
- [Documentación de Configuración](https://opencode.ai/docs/config)
- [Configuración Jerárquica](https://opencode.ai/docs/config/hierarchy)
- [Variables de Entorno](https://opencode.ai/docs/config/env)
- [Mejores Prácticas](https://opencode.ai/docs/config/best-practices)

## Autoevaluación

- [ ] Puedo crear archivos de configuración válidos en JSON y JSONC
- [ ] Uso el esquema JSON para validación y autocompletado
- [ ] Configuré múltiples proveedores correctamente
- [ ] Establecí modelos principales y rápidos
- [ ] Configuré variables de entorno para secrets
- [ ] Documenté mi configuración con comentarios
- [ ] Validé que la configuración funciona correctamente
