---
title: "Ubicaciones de Configuración"
module: 9
duration: "55 minutos"
prerequisites: "Módulo 8: Formato de Configuración"
---

# Clase 9: Ubicaciones de Configuración

## Resumen Ejecutivo

OpenCode implementa un sistema de configuración jerárquico con 8 niveles de precedencia, lo que permite configuración flexibles y escalables para desde usuarios individuales hasta grandes organizaciones. Este sistema incluye configuración remota (.well-known/opencode), global (~/.config/opencode), de proyecto (opencode.json en la raíz), directorio .opencode, configuración inline, configuración gestionada por plataforma (MDM) y más. Comprender esta jerarquía es crucial para implementar OpenCode correctamente en diferentes entornos.

La jerarquía de configuración está diseñada para permitir que las organizaciones establezcan configuración base que los usuarios pueden personalizar, mientras que mantienen control sobre configuraciones críticas. Por ejemplo, una organización puede usar MDM para establecer proveedores y modelos permitidos, mientras que los usuarios pueden personalizar su tema, instrucciones y configuración de su servidor local. Este sistema equilibra flexibilidad de usuario con control organizacional.

## Objetivos de Aprendizaje

- Comprender los 8 niveles de precedencia de configuración
- Configurar OpenCode en cada nivel de la jerarquía
- Implementar configuración remota para organizaciones
- Usar configuración gestionada por MDM
- Gestionar configuración de proyecto para equipos
- Resolver conflictos de configuración entre niveles
- Implementar mejores prácticas de configuración

## Conceptos Clave

### Precedencia de Configuración (8 Niveles)

OpenCode procesa la configuración en orden de precedencia (de mayor a menor):

```
┌─────────────────────────────────────────────────────────────┐
│                  JERARQUÍA DE PRECEDENCIA                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. REMOTE (.well-known/opencode)     ← Máxima precedencia │
│     └── Configuración servida desde tu dominio              │
│                                                             │
│  2. GLOBAL (~/.config/opencode/)      ← Configuración user │
│     └── Configuración personal del usuario                  │
│                                                             │
│  3. CUSTOM (OPENCODE_CONFIG_DIR)      ← Directorio custom  │
│     └── Directorio personalizado por variable de entorno    │
│                                                             │
│  4. PROJECT (opencode.json en root)   ← Config proyecto    │
│     └── Configuración específica del proyecto               │
│                                                             │
│  5. .opencode (.opencode/opencode.json) ← Config .opencode │
│     └── Configuración oculta en directorio .opencode        │
│                                                             │
│  6. INLINE (--config flag)            ← Config inline      │
│     └── Configuración pasada por línea de comandos          │
│                                                             │
│  7. MANAGED (MDM/platform)            ← Config gestionada  │
│     └── Configuración gestionada por administrador          │
│                                                             │
│  8. MDM (Mobile Device Management)    ← Mínima precedencia │
│     └── Configuración MDM para dispositivos gestionados    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1. Remote Configuration (.well-known/opencode)

La configuración remota permite a las organizaciones servir configuración desde su dominio:

```
https://tu-empresa.com/.well-known/opencode
```

**Características:**
- Accedida automáticamente por OpenCode
- No requiere configuración local
- Ideal para configuración de organización
- Se verifica periódicamente

**Implementación:**
```bash
# En tu servidor web, crear el archivo:
# https://tu-empresa.com/.well-known/opencode

# Ejemplo de contenido:
{
  "provider": {
    "enterprise-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "models": {
        "whitelist": ["llama-3.1-70b", "llama-3.1-8b"]
      }
    }
  },
  "model": "llama-3.1-70b",
  "instructions": "Instrucciones de la empresa..."
}
```

### 2. Global Configuration

Ubicación: `~/.config/opencode/opencode.json`

```bash
# Crear configuración global
mkdir -p ~/.config/opencode

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
  "locale": "es",
  
  "instructions": "Instrucciones personales del usuario..."
}
EOF
```

### 3. Custom Configuration Directory

Controlado por la variable de entorno `OPENCODE_CONFIG_DIR`:

```bash
# Definir directorio personalizado
export OPENCODE_CONFIG_DIR="/mi/config/personalizado"

# Crear configuración en ese directorio
mkdir -p "$OPENCODE_CONFIG_DIR"

cat > "$OPENCODE_CONFIG_DIR/opencode.json" << 'EOF'
{
  "provider": {
    "mi-proveedor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  }
}
EOF
```

### 4. Project Configuration

Ubicación: `opencode.json` en la raíz del proyecto:

```bash
# En la raíz de tu proyecto
cat > opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "proyecto-provider": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "models": {
        "model": "modelo-para-este-proyecto"
      }
    }
  },
  
  "model": "modelo-para-este-proyecto",
  
  "instructions": "Instrucciones específicas para este proyecto..."
}
EOF
```

### 5. .opencode Directory Configuration

Ubicación: `.opencode/opencode.json` en la raíz del proyecto:

```bash
# Crear directorio .opencode
mkdir -p .opencode

cat > .opencode/opencode.json << 'EOF'
{
  "provider": {
    "proyecto-provider": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  },
  
  "model": "modelo-para-este-proyecto"
}
EOF
```

### 6. Inline Configuration

Pasada por línea de comandos al iniciar OpenCode:

```bash
# Especificar archivo de configuración
opencode --config /ruta/a/mi-config.json

# O usar variable de entorno
export OPENCODE_CONFIG="/ruta/a/mi-config.json"
opencode
```

### 7. Managed Settings (Platform)

Configuración gestionada por la plataforma:

```bash
# macOS - Managed Preferences
# /Library/Managed Preferences/com.opencode.cli.json

# Linux - System Configuration
# /etc/opencode/config.json

# Windows - Registry o Group Policy
# HKLM\SOFTWARE\OpenCode\config.json
```

### 8. MDM (Mobile Device Management)

Para dispositivos gestionados por MDM (Jamf, Kandji, FleetDM):

```bash
# macOS - Mobile Config
# Instalado a través de MDM
# Prioridad: más baja (se sobreescribe por otros niveles)

# Ejemplo de mobileconfig para macOS:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadIdentifier</key>
    <string>com.opencode.config</string>
    <key>PayloadType</key>
    <string>com.opencode.cli</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>provider</key>
    <dict>
        <key>enterprise</key>
        <dict>
            <key>type</key>
            <string>oauth</string>
        </dict>
    </dict>
</dict>
</plist>
```

### Reglas de Sobreescritura

```yaml
# Cada nivel más alto sobreescribe el nivel más bajo
reglas:
  remote_vs_global: "Remote sobreescribe Global"
  global_vs_project: "Global sobreescribe Project"
  project_vs_inline: "Project sobreescribe Inline"
  
  # Excepción: arrays se fusionan, no se sobreescriben
  fusion_arrays: "Los arrays de whitelist/blacklist se fusionan"
  
  # Excepción: objetos se fusionan recursivamente
  fusion_objetos: "Los objetos de provider se fusionan"
```

### Ejemplo de Sobreescritura

```jsonc
// Configuración Global (~/.config/opencode/opencode.json)
{
  "provider": {
    "anthropic": {
      "type": "oauth"
    }
  },
  "model": "claude-sonnet-4-20250514",
  "theme": "dark"
}

// Configuración de Proyecto (opencode.json)
{
  "provider": {
    "proyecto-local": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  },
  "model": "llama-3.1-70b"
}

// Resultado Fusionado
{
  "provider": {
    "anthropic": {
      "type": "oauth"
    },
    "proyecto-local": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  },
  "model": "llama-3.1-70b",  // Sobreescribe el global
  "theme": "dark"            // Se mantiene del global
}
```

## Guía Paso a Paso

### Paso 1: Configurar Configuración Global

```bash
# 1. Crear directorio de configuración global
mkdir -p ~/.config/opencode

# 2. Crear archivo de configuración global
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
  "locale": "es",
  
  "instructions": "Instrucciones personales del usuario..."
}
EOF

# 3. Verificar que se carga correctamente
opencode config list
# Debería mostrar la configuración global
```

### Paso 2: Configurar Configuración de Proyecto

```bash
# 1. Navega a la raíz de tu proyecto
cd /ruta/a/tu/proyecto

# 2. Crea archivo de configuración de proyecto
cat > opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "proyecto-provider": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1",
      "models": {
        "model": "modelo-para-este-proyecto",
        "whitelist": ["modelo-a", "modelo-b"]
      }
    }
  },
  
  "model": "modelo-para-este-proyecto",
  
  "instructions": "Instrucciones específicas para este proyecto de Python..."
}
EOF

# 3. Verificar que la configuración de proyecto se carga
opencode config list
# Debería mostrar configuración fusionada (global + proyecto)
```

### Paso 3: Configurar Configuración Remota (Para Organizaciones)

```bash
# 1. En tu servidor web, crear el endpoint:
# https://tu-empresa.com/.well-known/opencode

# Ejemplo con Nginx:
# location /.well-known/opencode {
#     alias /var/www/opencode-config/opencode.json;
#     add_header Content-Type application/json;
# }

# 2. Crear el archivo de configuración remota
cat > /var/www/opencode-config/opencode.json << 'EOF'
{
  "provider": {
    "enterprise-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "models": {
        "whitelist": ["llama-3.1-70b", "llama-3.1-8b", "mistral-large"]
      }
    }
  },
  "model": "llama-3.1-70b",
  "instructions": "Instrucciones estándar de la empresa para IA..."
}
EOF

# 3. Verificar que OpenCode puede acceder
curl -I https://tu-empresa.com/.well-known/opencode
# Debería retornar 200 OK con Content-Type: application/json
```

### Paso 4: Configurar Variables de Entorno para Custom Config

```bash
# 1. Definir OPENCODE_CONFIG_DIR
export OPENCODE_CONFIG_DIR="/mi/config/personalizado"

# 2. Crear directorio y configuración
mkdir -p "$OPENCODE_CONFIG_DIR"

cat > "$OPENCODE_CONFIG_DIR/opencode.json" << 'EOF'
{
  "provider": {
    "mi-config-personal": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  }
}
EOF

# 3. Hacer permanente
echo 'export OPENCODE_CONFIG_DIR="/mi/config/personalizado"' >> ~/.bashrc
# O para zsh
echo 'export OPENCODE_CONFIG_DIR="/mi/config/personalizado"' >> ~/.zshrc
```

### Paso 5: Usar Configuración Inline

```bash
# 1. Crear archivo de configuración temporal
cat > /tmp/opencode-temp.json << 'EOF'
{
  "provider": {
    "temp-provider": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  },
  "model": "modelo-temporal"
}
EOF

# 2. Iniciar OpenCode con configuración inline
opencode --config /tmp/opencode-temp.json

# 3. Usar variable de entorno
export OPENCODE_CONFIG="/tmp/opencode-temp.json"
opencode
```

### Paso 6: Verificar Precedencia

```bash
# 1. Crear configuración en múltiples niveles
# Global
echo '{"theme": "dark"}' > ~/.config/opencode/opencode.json

# Proyecto
echo '{"theme": "light"}' > opencode.json

# 2. Verificar qué configuración se carga
opencode config list | grep theme
# Debería mostrar "light" (la de proyecto sobreescribe la global)

# 3. Verificar el origen de cada configuración
opencode config list --verbose
# Muestra de dónde viene cada configuración
```

## Referencia Rápida

| Nivel | Ubicación | Prioridad | Uso Principal |
|-------|-----------|-----------|---------------|
| **Remote** | `.well-known/opencode` | 8 (Mayor) | Configuración de organización |
| **Global** | `~/.config/opencode/opencode.json` | 7 | Configuración personal del usuario |
| **Custom** | Directorio definido por `OPENCODE_CONFIG_DIR` | 6 | Configuración personalizada |
| **Project** | `opencode.json` en raíz del proyecto | 5 | Configuración específica del proyecto |
| **.opencode** | `.opencode/opencode.json` | 4 | Configuración oculta del proyecto |
| **Inline** | Flag `--config` o `OPENCODE_CONFIG` | 3 | Configuración temporal/especial |
| **Managed** | Configuración de plataforma | 2 | Config gestionada por administrador |
| **MDM** | MDM (Jamf, Kandji, FleetDM) | 1 (Menor) | Config de dispositivos gestionados |

| Variable de Entorno | Descripción | Ejemplo |
|---------------------|-------------|---------|
| `OPENCODE_CONFIG_DIR` | Directorio de configuración custom | `export OPENCODE_CONFIG_DIR="/mi/config"` |
| `OPENCODE_CONFIG` | Archivo de configuración inline | `export OPENCODE_CONFIG="/tmp/config.json"` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Múltiples Niveles

**Objetivo:** Implementar configuración en 3 niveles diferentes y verificar la precedencia.

**Instrucciones:**
1. Crea configuración global en `~/.config/opencode/`
2. Crea configuración de proyecto en la raíz de un proyecto
3. Crea una configuración inline en un archivo temporal
4. Verifica la precedencia ejecutando OpenCode en diferentes contextos
5. Documenta qué configuración se carga en cada caso

**Solución Esperada:**
```bash
# 1. Configuración Global
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "theme": "dark",
  "locale": "es",
  "provider": {
    "anthropic": {"type": "oauth"}
  }
}
EOF

# 2. Configuración de Proyecto
mkdir -p /tmp/test-project
cd /tmp/test-project
cat > opencode.json << 'EOF'
{
  "theme": "light",
  "provider": {
    "local": {"type": "openai-compatible", "baseURL": "http://localhost:8000/v1"}
  }
}
EOF

# 3. Verificar
opencode config list | grep theme
# Resultado: "light" (proyecto sobreescribe global)
```

### Ejercicio 2: Implementar Configuración Remota

**Objetivo:** Configurar un servidor para servir configuración remota de OpenCode.

**Instrucciones:**
1. Configura un servidor web básico (puede ser local)
2. Crea el endpoint `.well-known/opencode`
3. Agrega configuración de organización
4. Verifica que OpenCode puede acceder a la configuración
5. Documenta el proceso de implementación

**Solución Esperada:**
```bash
# 1. Usar Python http.server para pruebas
mkdir -p /var/www/.well-known
cat > /var/www/.well-known/opencode << 'EOF'
{
  "provider": {
    "enterprise": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1"
    }
  }
}
EOF

# 2. Iniciar servidor
cd /var/www && python3 -m http.server 8080

# 3. Verificar acceso
curl http://localhost:8080/.well-known/opencode
```

### Ejercicio 3: Configurar con Variables de Entorno

**Objetivo:** Usar variables de entorno para gestionar configuración personalizada.

**Instrucciones:**
1. Define `OPENCODE_CONFIG_DIR` apuntando a un directorio personalizado
2. Crea configuración en ese directorio
3. Verifica que OpenCode usa esa configuración
4. Configura `OPENCODE_CONFIG` para configuración inline
5. Documenta los diferentes escenarios de uso

**Solución Esperada:**
```bash
# 1. Configurar OPENCODE_CONFIG_DIR
export OPENCODE_CONFIG_DIR="/tmp/mi-config"
mkdir -p "$OPENCODE_CONFIG_DIR"

cat > "$OPENCODE_CONFIG_DIR/opencode.json" << 'EOF'
{
  "theme": "solarized-dark",
  "provider": {
    "mi-servidor": {
      "type": "openai-compatible",
      "baseURL": "http://localhost:8000/v1"
    }
  }
}
EOF

# 2. Verificar
opencode config list
# Debería mostrar la configuración del directorio personalizado

# 3. Para configuración inline
export OPENCODE_CONFIG="/tmp/config-temporal.json"
opencode
```

## Ejercicio Desafío

**Reto:** Implementa un sistema de configuración completo para una organización ficticia con:
1. Configuración remota en `.well-known/opencode`
2. Configuración global para usuarios
3. Configuración de proyecto para diferentes equipos
4. Variables de entorno para secrets
5. Documentación completa de la jerarquía

**Pistas:**
- Crea un diagrama de la jerarquía de configuración
- Implementa cada nivel con ejemplos reales
- Documenta cómo se resuelven los conflictos
- Crea scripts para automatizar la configuración
- Incluye ejemplos de troubleshooting

## Recursos Adicionales

- [Jerarquía de Configuración](https://opencode.ai/docs/config/hierarchy)
- [Configuración Remota](https://opencode.ai/docs/config/remote)
- [Configuración de Proyecto](https://opencode.ai/docs/config/project)
- [Variables de Entorno](https://opencode.ai/docs/config/env)
- [MDM Configuration](https://opencode.ai/docs/config/mdm)
- [Resolución de Conflictos](https://opencode.ai/docs/config/conflicts)

## Autoevaluación

- [ ] Comprendo los 8 niveles de precedencia de configuración
- [ ] Puedo configurar OpenCode en cada nivel de la jerarquía
- [ ] Implementé configuración remota para mi organización
- [ ] Gestioné configuración de proyecto para diferentes equipos
- [ ] Usé variables de entorno para secrets y configuración personalizada
- [ ] Resolví conflictos de configuración entre niveles
- [ ] Documenté la configuración para referencia futura
