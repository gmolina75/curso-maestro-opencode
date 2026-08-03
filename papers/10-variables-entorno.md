---
title: "Variables de Entorno"
module: 10
duration: "50 minutos"
prerequisites: "Módulo 9: Ubicaciones de Configuración"
---

# Clase 10: Variables de Entorno

## Resumen Ejecutivo

Las variables de entorno son una parte fundamental de la configuración de OpenCode, permitiendo separar la configuración sensible de los archivos de configuración, compartir snippets de configuración entre proyectos y adaptar el comportamiento de OpenCode a diferentes entornos. OpenCode soporta múltiples variables de entorno específicas (OPENCODE_CONFIG, OPENCODE_CONFIG_DIR, OPENCODE_TUI_CONFIG) además de un sistema de sustitución de variables que permite referenciar variables del sistema, valores de archivos y datos dinámicos dentro de la configuración.

El uso adecuado de variables de entorno es esencial para mantener la seguridad (evitando hardcodear API keys), la portabilidad (configuración que funciona en diferentes máquinas) y la mantenibilidad (actualizar valores en un solo lugar). OpenCode implementa un sistema de sustitución que soporta `{env:VARIABLE}` para variables del sistema y `{file:path}` para contenido de archivos, lo que permite configuraciones extremadamente flexibles y seguras.

## Objetivos de Aprendizaje

- Configurar variables de entorno específicas de OpenCode
- Usar el sistema de sustitución de variables en configuración
- Implementar mejores prácticas de seguridad con variables de entorno
- Gestionar API keys y secrets de forma segura
- Crear configuraciones portables entre entornos
- Debuggear problemas relacionados con variables de entorno
- Implementar configuración para diferentes entornos (dev, staging, prod)

## Conceptos Clave

### Variables de Entorno Específicas de OpenCode

```bash
# Variables principales de OpenCode

# 1. OPENCODE_CONFIG - Ruta al archivo de configuración
export OPENCODE_CONFIG="/ruta/a/config.json"

# 2. OPENCODE_CONFIG_DIR - Directorio de configuración
export OPENCODE_CONFIG_DIR="/directorio/config"

# 3. OPENCODE_TUI_CONFIG - Configuración de la TUI
export OPENCODE_TUI_CONFIG="/ruta/a/tui-config.json"

# 4. OPENCODE_LOG_LEVEL - Nivel de logging
export OPENCODE_LOG_LEVEL="debug"

# 5. OPENCODE_HOME - Directorio base de OpenCode
export OPENCODE_HOME="/ruta/a/opencode"
```

### Sistema de Sustitución de Variables

OpenCode permite usar variables dentro de los archivos de configuración:

```jsonc
{
  "provider": {
    "anthropic": {
      "type": "api-key",
      // Sustituir variable de entorno
      "apiKey": "{env:ANTHROPIC_API_KEY}"
    },
    "custom": {
      "type": "openai-compatible",
      // Sustituir desde archivo
      "apiKey": "{file:/run/secrets/api-key}",
      "baseURL": "{env:AI_BASE_URL}"
    }
  },
  
  "env": {
    // Variables que se pasarán al entorno de ejecución
    "DATABASE_URL": "{env:DATABASE_URL}",
    "API_SECRET": "{file:/run/secrets/api-secret}"
  }
}
```

### Tipos de Sustitución

```yaml
# 1. Variable de entorno del sistema
sustitucion_env: "{env:VARIABLE_NAME}"
ejemplo: "{env:ANTHROPIC_API_KEY}"

# 2. Contenido de archivo
sustitucion_file: "{file:/ruta/al/archivo}"
ejemplo: "{file:/run/secrets/api-key}"

# 3. Variable de entorno con valor por defecto
sustitucion_default: "{env:VARIABLE:-valor_default}"
ejemplo: "{env:PORT:-8080}"

# 4. Variable anidada
sustitucion_anidada: "{env:GROUP_VARIABLE}"
ejemplo: "{env:AI_ANTHROPIC_API_KEY}"
```

### Uso de Variables de Entorno en Diferentes Contextos

```bash
# Para shell scripts
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GROQ_API_KEY="gsk_..."

# Para Docker
docker run -e ANTHROPIC_API_KEY="sk-ant-..." \
           -e OPENAI_API_KEY="sk-..." \
           anomalyco/opencode:latest

# Para docker-compose
environment:
  - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
  - OPENAI_API_KEY=${OPENAI_API_KEY}

# Para Kubernetes
env:
  - name: ANTHROPIC_API_KEY
    valueFrom:
      secretKeyRef:
        name: opencode-secrets
        key: anthropic-api-key
```

### Mejores Prácticas de Seguridad

```yaml
# NUNCA hacer esto:
bad_practice:
  - "Hardcodear API keys en archivos de configuración"
  - "Subir archivos de configuración con secrets a repositorios"
  - "Usar variables de entorno en logs o mensajes de error"
  - "Compartir archivos .env entre diferentes entornos"

# SIEMPRE hacer esto:
good_practice:
  - "Usar {env:VARIABLE} en archivos de configuración"
  - "Agregar .env a .gitignore"
  - "Usar secret managers (Vault, AWS Secrets Manager)"
  - "Usar diferentes secrets para diferentes entornos"
  - "Rotar secrets periódicamente"
  - "Usar variables de entorno del sistema en producción"
```

### Configuración para Diferentes Entornos

```bash
# Estructura de directorios para múltiples entornos
.config/
├── opencode/
│   ├── opencode.json         # Config base
│   ├── .env.development      # Variables de desarrollo
│   ├── .env.staging          # Variables de staging
│   └── .env.production       # Variables de producción

# Desarrollo (.env.development)
ANTHROPIC_API_KEY=sk-ant-dev-...
AI_BASE_URL=http://localhost:8000/v1
LOG_LEVEL=debug

# Producción (.env.production)
ANTHROPIC_API_KEY=sk-ant-prod-...
AI_BASE_URL=https://ai.empresa.com/v1
LOG_LEVEL=info
```

### Uso de {file:path} para Secrets

```jsonc
{
  "provider": {
    "anthropic": {
      "type": "api-key",
      // Leer API key desde un archivo de secret
      "apiKey": "{file:/run/secrets/anthropic-api-key}"
    }
  }
}
```

```bash
# En Docker, montar secrets como archivos
docker run -v /path/to/secrets:/run/secrets:ro \
           anomalyco/opencode:latest

# En Kubernetes, usar Secrets
volumes:
  - name: opencode-secrets
    secret:
      secretName: opencode-secrets

# En systemd, usar CredentialFiles
[Service]
LoadCredential=anthropic-api-key:/etc/opencode/secrets/anthropic-api-key
EnvironmentFile=-/run/credentials/%N
```

### Debugging de Variables de Entorno

```bash
# Verificar variables de entorno actuales
env | grep OPENCODE
env | grep ANTHROPIC
env | grep AI

# Verificar que OpenCode carga las variables
opencode config list | grep env

# Logging detallado
OPENCODE_LOG_LEVEL=debug opencode

# Verificar sustitución de variables
opencode config list | grep apiKey
# Debería mostrar el valor resuelto, no {env:VARIABLE}
```

## Guía Paso a Paso

### Paso 1: Configurar Variables de Entorno Básicas

```bash
# 1. Definir variables para proveedores
export ANTHROPIC_API_KEY="sk-ant-tu-api-key"
export OPENAI_API_KEY="sk-tu-api-key"
export GROQ_API_KEY="gsk_tu-api-key"

# 2. Verificar que las variables están definidas
echo $ANTHROPIC_API_KEY
echo $OPENAI_API_KEY

# 3. Hacer permanentes en tu shell
# Para bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc

# Para zsh
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc
```

### Paso 2: Usar Variables en Configuración

```bash
# 1. Crear archivo de configuración que use variables
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  
  "provider": {
    "anthropic": {
      "type": "api-key",
      "apiKey": "{env:ANTHROPIC_API_KEY}"
    },
    "openai": {
      "type": "api-key",
      "apiKey": "{env:OPENAI_API_KEY}"
    },
    "groq": {
      "type": "api-key",
      "apiKey": "{env:GROQ_API_KEY}"
    }
  },
  
  "env": {
    "DATABASE_URL": "{env:DATABASE_URL}",
    "API_SECRET": "{env:API_SECRET}"
  }
}
EOF

# 2. Verificar que la sustitución funciona
opencode config list | grep apiKey
# Debería mostrar los valores resueltos, no {env:...}
```

### Paso 3: Usar Variables para Secrets con {file:path}

```bash
# 1. Crear directorio de secrets (no versionar en git)
mkdir -p ~/.config/opencode/secrets

# 2. Crear archivo con el secret
echo "sk-ant-tu-api-key" > ~/.config/opencode/secrets/anthropic-key

# 3. Configurar permisos restrictivos
chmod 600 ~/.config/opencode/secrets/anthropic-key

# 4. Usar en configuración
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "provider": {
    "anthropic": {
      "type": "api-key",
      "apiKey": "{file:~/.config/opencode/secrets/anthropic-key}"
    }
  }
}
EOF
```

### Paso 4: Configurar Variables para Docker

```bash
# 1. Crear archivo .env (no versionar en git)
cat > .env << 'EOF'
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
DATABASE_URL=postgres://user:pass@localhost/db
EOF

# 2. Agregar .env a .gitignore
echo ".env" >> .gitignore

# 3. Usar en docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  opencode:
    image: anomalyco/opencode:latest
    env_file:
      - .env
    volumes:
      - ~/.config/opencode:/root/.config/opencode
EOF

# 4. Ejecutar
docker-compose up -d
```

### Paso 5: Configurar Variables para Kubernetes

```bash
# 1. Crear Secret en Kubernetes
kubectl create secret generic opencode-secrets \
  --from-literal=anthropic-api-key=sk-ant-... \
  --from-literal=openai-api-key=sk-...

# 2. Referenciar en Deployment
cat > deployment.yml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opencode
spec:
  template:
    spec:
      containers:
        - name: opencode
          image: anomalyco/opencode:latest
          env:
            - name: ANTHROPIC_API_KEY
              valueFrom:
                secretKeyRef:
                  name: opencode-secrets
                  key: anthropic-api-key
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: opencode-secrets
                  key: openai-api-key
EOF
```

### Paso 6: Debugging de Variables

```bash
# 1. Ver todas las variables de entorno de OpenCode
env | grep OPENCODE

# 2. Verificar variables de proveedores
env | grep -E "(ANTHROPIC|OPENAI|GROQ|AI_)"
env | grep -i api

# 3. Verificar que OpenCode carga las variables
OPENCODE_LOG_LEVEL=debug opencode 2>&1 | grep -i "env\|variable\|key"

# 4. Verificar sustitución en configuración
opencode config list | grep -E "(apiKey|env)"
# Debería mostrar valores resueltos

# 5. Test de sustitución
cat > /tmp/test-config.json << 'EOF'
{
  "test": "{env:HOME}"
}
EOF
# Verificar que se resuelve a /home/usuario
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `OPENCODE_CONFIG` | Ruta al archivo de configuración | `export OPENCODE_CONFIG="/path/to/config.json"` |
| `OPENCODE_CONFIG_DIR` | Directorio de configuración | `export OPENCODE_CONFIG_DIR="/path/to/config/dir"` |
| `OPENCODE_TUI_CONFIG` | Configuración de la TUI | `export OPENCODE_TUI_CONFIG="/path/to/tui.json"` |
| `OPENCODE_LOG_LEVEL` | Nivel de logging | `export OPENCODE_LOG_LEVEL="debug"` |
| `OPENCODE_HOME` | Directorio base de OpenCode | `export OPENCODE_HOME="/path/to/opencode"` |
| `{env:VARIABLE}` | Sustituir variable de entorno | `"apiKey": "{env:ANTHROPIC_API_KEY}"` |
| `{file:path}` | Sustituir contenido de archivo | `"apiKey": "{file:/run/secrets/key}"` |
| `{env:VAR:-default}` | Variable con valor por defecto | `"port": "{env:PORT:-8080}"` |

## Ejercicios Guiados

### Ejercicio 1: Configurar Variables para Proveedores

**Objetivo:** Usar variables de entorno para gestionar API keys de múltiples proveedores.

**Instrucciones:**
1. Define variables de entorno para 3 proveedores diferentes
2. Crea un archivo de configuración que use esas variables
3. Verifica que la sustitución funciona correctamente
4. Asegura que los secrets no están hardcodeados
5. Documenta el proceso

**Solución Esperada:**
```bash
# 1. Definir variables
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GROQ_API_KEY="gsk_..."

# 2. Configuración
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {"type": "api-key", "apiKey": "{env:ANTHROPIC_API_KEY}"},
    "openai": {"type": "api-key", "apiKey": "{env:OPENAI_API_KEY}"},
    "groq": {"type": "api-key", "apiKey": "{env:GROQ_API_KEY}"}
  }
}
EOF

# 3. Verificar
opencode config list | grep apiKey
# Debe mostrar valores resueltos
```

### Ejercicio 2: Usar {file:path} para Secrets

**Objetivo:** Implementar secrets usando archivos en lugar de variables de entorno.

**Instrucciones:**
1. Crea un directorio de secrets con permisos restrictivos
2. Almacena una API key en un archivo
3. Configura OpenCode para leer desde el archivo
4. Verifica que funciona
5. Documenta las ventajas de este enfoque

**Solución Esperada:**
```bash
# 1. Crear directorio de secrets
mkdir -p ~/.config/opencode/secrets
chmod 700 ~/.config/opencode/secrets

# 2. Almacenar API key
echo "sk-ant-..." > ~/.config/opencode/secrets/anthropic-key
chmod 600 ~/.config/opencode/secrets/anthropic-key

# 3. Configurar
cat > ~/.config/opencode/opencode.json << 'EOF'
{
  "provider": {
    "anthropic": {
      "type": "api-key",
      "apiKey": "{file:~/.config/opencode/secrets/anthropic-key}"
    }
  }
}
EOF

# 4. Verificar
opencode config list | grep apiKey
```

### Ejercicio 3: Configurar Múltiples Entornos

**Objetivo:** Crear configuración portables para diferentes entornos (dev, prod).

**Instrucciones:**
1. Crea archivos .env para desarrollo y producción
2. Configura OpenCode para usar el entorno apropiado
3. Implementa un script para cambiar entre entornos
4. Verifica que la configuración se adapta correctamente
5. Documenta el proceso de despliegue

**Solución Esperada:**
```bash
# 1. Archivos .env
cat > .env.development << 'EOF'
ANTHROPIC_API_KEY=sk-ant-dev-...
AI_BASE_URL=http://localhost:8000/v1
LOG_LEVEL=debug
EOF

cat > .env.production << 'EOF'
ANTHROPIC_API_KEY=sk-ant-prod-...
AI_BASE_URL=https://ai.empresa.com/v1
LOG_LEVEL=info
EOF

# 2. Script de cambio de entorno
cat > switch-env.sh << 'EOF'
#!/bin/bash
ENV=${1:-development}
export $(cat .env.$ENV | xargs)
echo "Entorno cambiado a: $ENV"
opencode
EOF

# 3. Uso
chmod +x switch-env.sh
./switch-env.sh development
```

## Ejercicio Desafío

**Reto:** Implementa un sistema completo de variables de entorno para OpenCode que incluya:
1. Gestión de secrets con {file:path}
2. Configuración para 3 entornos diferentes
3. Integración con Docker y Kubernetes
4. Script de automatización para rotación de secrets
5. Documentación completa del proceso

**Pistas:**
- Usa Docker secrets o Kubernetes secrets
- Implementa un script de rotación de API keys
- Documenta el proceso de despliegue para cada entorno
- Incluye verificaciones de seguridad
- Crea un README con instrucciones de uso

## Recursos Adicionales

- [Variables de Entorno de OpenCode](https://opencode.ai/docs/config/env)
- [Sustitución de Variables](https://opencode.ai/docs/config/substitution)
- [Gestión de Secrets](https://opencode.ai/docs/security/secrets)
- [Docker Configuration](https://opencode.ai/docs/deployment/docker)
- [Kubernetes Configuration](https://opencode.ai/docs/deployment/kubernetes)
- [Mejores Prácticas de Seguridad](https://opencode.ai/docs/security/best-practices)

## Autoevaluación

- [ ] Configuré variables de entorno específicas de OpenCode
- [ ] Uso {env:VARIABLE} para API keys y secrets
- [ ] Implementé {file:path} para secrets más seguros
- [ ] Creé configuración portables entre entornos
- [ ] Integré OpenCode con Docker usando variables de entorno
- [ ] Debugué problemas relacionados con variables de entorno
- [ ] Documenté las mejores prácticas de seguridad para secrets
