---
title: "Gestión Remota y Enterprise"
module: 11
duration: "60 minutos"
prerequisites: "Módulo 10: Variables de Entorno"
---

# Clase 11: Gestión Remota y Enterprise

## Resumen Ejecutivo

La gestión remota y enterprise de OpenCode permite a las organizaciones implementar, configurar y administrar OpenCode de forma centralizada en grandes despliegues. Esto incluye el endpoint `.well-known/opencode` para configuración remota, managed settings con sistemas MDM (Mobile Device Management) como Jamf, Kandji y FleetDM, y la creación de mobileconfig para macOS. Estas herramientas son esenciales para organizaciones que necesitan mantener control sobre la configuración de IA mientras permiten a los desarrolladores productividad.

El sistema de gestión enterprise de OpenCode está diseñado para equilibrar control organizacional con flexibilidad de usuario. Las organizaciones pueden establecer proveedores aprobados, modelos permitidos e instrucciones estándar, mientras que los usuarios pueden personalizar aspectos no críticos como el tema, el idioma y las instrucciones específicas del proyecto. Este enfoque garantiza cumplimiento normativo y seguridad sin sacrificar la productividad del desarrollador.

## Objetivos de Aprendizaje

- Implementar configuración remota con `.well-known/opencode`
- Configurar managed settings con sistemas MDM
- Crear mobileconfig para macOS
- Comprender las reglas de prioridad y sobreescritura
- Implementar configuración enterprise completa
- Gestionar dispositivos a gran escala
- Resolver problemas de configuración enterprise

## Conceptos Clave

### .well-known/opencode Endpoint

El endpoint `.well-known/opencode` permite a las organizaciones servir configuración desde su dominio:

```
https://tu-empresa.com/.well-known/opencode
```

**Características:**
- Accedida automáticamente por OpenCode
- No requiere configuración local en clientes
- Se verifica periódicamente para actualizaciones
- Prioridad más alta en la jerarquía de configuración

**Implementación en servidor web:**
```nginx
# Configuración Nginx
server {
    listen 443 ssl;
    server_name tu-empresa.com;
    
    location /.well-known/opencode {
        alias /var/www/opencode-config/opencode.json;
        add_header Content-Type application/json;
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        
        # CORS para acceso desde clientes
        add_header Access-Control-Allow-Origin "*";
        add_header Access-Control-Allow-Methods "GET, OPTIONS";
        add_header Access-Control-Allow-Headers "Content-Type";
    }
}
```

**Ejemplo de configuración remota:**
```json
{
  "provider": {
    "enterprise-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "models": {
        "whitelist": [
          "llama-3.1-70b",
          "llama-3.1-8b",
          "mistral-large"
        ],
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b"
      },
      "timeout": 90000
    }
  },
  
  "model": "llama-3.1-70b",
  
  "instructions": "Instrucciones estándar de la empresa para asistentes de IA...",
  
  "permissions": {
    "bash": "ask",
    "write": "approve",
    "edit": "approve"
  }
}
```

### Managed Settings con MDM

Los sistemas MDM permiten gestionar configuración de OpenCode en dispositivos gestionados:

| MDM | Plataforma | Método de Distribución |
|-----|------------|------------------------|
| **Jamf Pro** | macOS, iOS | Configuration Profiles |
| **Kandji** | macOS | Blueprints |
| **FleetDM** | macOS, Linux, Windows | Fleet Queries |
| **Microsoft Intune** | Windows, macOS | Device Configuration |
| **VMware Workspace ONE** | Multiplataforma | Profiles |

**Implementación con Jamf Pro:**
```bash
# 1. Crear Configuration Profile
# En Jamf Pro, crear un nuevo Configuration Profile

# 2. Definir el dominio de preferencias
# Domain: com.opencode.cli

# 3. Agregar configuración
<dict>
    <key>provider</key>
    <dict>
        <key>enterprise-ai</key>
        <dict>
            <key>type</key>
            <string>openai-compatible</string>
            <key>baseURL</key>
            <string>https://ai.empresa.com/v1</string>
        </dict>
    </dict>
    <key>model</key>
    <string>llama-3.1-70b</string>
</dict>
```

### Mobileconfig para macOS

Los archivos mobileconfig son la forma estándar de distribuir configuración en macOS:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- Identificador único del perfil -->
    <key>PayloadIdentifier</key>
    <string>com.empresa.opencode.config</string>
    
    <!-- Tipo de payload -->
    <key>PayloadType</key>
    <string>com.opencode.cli</string>
    
    <!-- Versión del payload -->
    <key>PayloadVersion</key>
    <integer>1</integer>
    
    <!-- Nombre del perfil para mostrar al usuario -->
    <key>PayloadDisplayName</key>
    <string>OpenCode Enterprise Configuration</string>
    
    <!-- Descripción -->
    <key>PayloadDescription</key>
    <string>Configuración empresarial de OpenCode</string>
    
    <!-- Configuración de OpenCode -->
    <key>provider</key>
    <dict>
        <key>enterprise-ai</key>
        <dict>
            <key>type</key>
            <string>openai-compatible</string>
            <key>baseURL</key>
            <string>https://ai.empresa.com/v1</string>
            <key>models</key>
            <dict>
                <key>whitelist</key>
                <array>
                    <string>llama-3.1-70b</string>
                    <string>llama-3.1-8b</string>
                </array>
            </dict>
        </dict>
    </dict>
    
    <key>model</key>
    <string>llama-3.1-70b</string>
    
    <key>instructions</key>
    <string>Instrucciones estándar de la empresa...</string>
</dict>
</plist>
```

### Reglas de Prioridad y Sobreescritura

```yaml
# Jerarquía de prioridad (de mayor a menor)
prioridad:
  1_remote: ".well-known/opencode"      # Máxima prioridad
  2_global: "~/.config/opencode/"       # Configuración de usuario
  3_custom: "OPENCODE_CONFIG_DIR"       # Directorio personalizado
  4_project: "opencode.json"            # Configuración de proyecto
  5_opencode: ".opencode/opencode.json" # Directorio .opencode
  6_inline: "--config flag"             # Configuración inline
  7_managed: "Platform settings"        # Config gestionada
  8_mdm: "MDM (Jamf, Kandji)"          # Mínima prioridad

# Reglas de sobreescritura
reglas:
  # Cada nivel sobreescribe el nivel inferior
  sobreescrita: "Nivel más alto gana"
  
  # Excepción: arrays se fusionan
  arrays: "Se fusionan, no se sobreescriben"
  
  # Excepción: objetos se fusionan recursivamente
  objetos: "Se fusionan recursivamente"
  
  # Ejemplo
  ejemplo:
    global: '{"theme": "dark", "provider": {"a": {}}}'
    proyecto: '{"theme": "light", "provider": {"b": {}}}'
    resultado: '{"theme": "light", "provider": {"a": {}, "b": {}}}'
```

### Configuración Enterprise Completa

```jsonc
{
  // Configuración remota desde el dominio de la empresa
  "$schema": "https://opencode.ai/config.json",
  
  // Proveedores aprobados por la empresa
  "provider": {
    "enterprise-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "models": {
        "whitelist": [
          "llama-3.1-70b",
          "llama-3.1-8b",
          "mistral-large"
        ],
        "blacklist": [
          "modelo-no-aprobado"
        ],
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b"
      },
      "timeout": 90000,
      "chunkTimeout": 45000
    }
  },
  
  // Modelo predeterminado de la empresa
  "model": "llama-3.1-70b",
  
  // Instrucciones estándar
  "instructions": "Eres un asistente de programación de la empresa. Sigue las guías de código...",
  
  // Permisos por defecto
  "permissions": {
    "bash": "ask",
    "write": "approve",
    "edit": "approve"
  }
}
```

### Flujo de Trabajo Enterprise

```
┌─────────────────────────────────────────────────────────────┐
│                FLUJO DE TRABAJO ENTERPRISE                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Administrador configura .well-known/opencode            │
│     └── Servidor web sirve configuración                    │
│                                                             │
│  2. OpenCode detecta configuración remota                   │
│     └── Descarga y aplica configuración                     │
│                                                             │
│  3. Usuarios instalan OpenCode normalmente                  │
│     └── Sin configuración local necesaria                   │
│                                                             │
│  4. MDM distribuye managed settings (opcional)              │
│     └── Para dispositivos gestionados                       │
│                                                             │
│  5. Usuarios personalizan configuración local               │
│     └── Solo aspectos no críticos (tema, idioma)            │
│                                                             │
│  6. OpenCode fusiona configuración de todos los niveles     │
│     └── Prioridad: remote > global > project > ...          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Gestión de Dispositivos a Gran Escala

```bash
# Script de distribución para múltiples dispositivos
#!/bin/bash

# Variables
ENTERPRISE_URL="https://tu-empresa.com/.well-known/opencode"
MDM_PROFILE="/Library/Managed Preferences/com.opencode.cli.json"

# Verificar configuración remota
echo "Verificando configuración remota..."
curl -s "$ENTERPRISE_URL" | python3 -m json.tool

# Verificar configuración MDM
if [ -f "$MDM_PROFILE" ]; then
    echo "Configuración MDM encontrada:"
    cat "$MDM_PROFILE" | python3 -m json.tool
else
    echo "No se encontró configuración MDM"
fi

# Verificar configuración actual de OpenCode
echo "Configuración actual de OpenCode:"
opencode config list
```

### Troubleshooting Enterprise

```bash
# Problema 1: Configuración remota no se carga
# Verificar acceso al endpoint
curl -I https://tu-empresa.com/.well-known/opencode
# Debería retornar 200 OK

# Verificar DNS
nslookup tu-empresa.com

# Problema 2: MDM no distribuye configuración
# Verificar perfil instalado
sudo profiles list | grep opencode

# Reinstalar perfil
sudo profiles install -path /ruta/al/perfil.mobileconfig

# Problema 3: Configuración no se fusiona correctamente
# Verificar precedencia
opencode config list --verbose

# Limpiar caché de configuración
opencode config clear-cache

# Problema 4: Permisos insuficientes
# Verificar permisos del archivo de configuración
ls -la ~/.config/opencode/opencode.json
# Debería ser legible por el usuario
```

## Guía Paso a Paso

### Paso 1: Configurar Endpoint .well-known/opencode

```bash
# 1. Crear directorio en tu servidor web
sudo mkdir -p /var/www/.well-known
sudo chown www-data:www-data /var/www/.well-known

# 2. Crear archivo de configuración
sudo cat > /var/www/.well-known/opencode << 'EOF'
{
  "provider": {
    "enterprise-ai": {
      "type": "openai-compatible",
      "baseURL": "https://ai.empresa.com/v1",
      "models": {
        "whitelist": ["llama-3.1-70b", "llama-3.1-8b"],
        "model": "llama-3.1-70b",
        "small_model": "llama-3.1-8b"
      }
    }
  },
  "model": "llama-3.1-70b",
  "instructions": "Instrucciones estándar de la empresa..."
}
EOF

# 3. Configurar permisos
sudo chmod 644 /var/www/.well-known/opencode
sudo chown www-data:www-data /var/www/.well-known/opencode

# 4. Configurar Nginx
sudo cat > /etc/nginx/sites-available/opencode << 'EOF'
server {
    listen 443 ssl;
    server_name tu-empresa.com;
    
    location /.well-known/opencode {
        alias /var/www/.well-known/opencode;
        add_header Content-Type application/json;
    }
}
EOF

# 5. Reiniciar Nginx
sudo systemctl restart nginx

# 6. Verificar
curl -I https://tu-empresa.com/.well-known/opencode
```

### Paso 2: Crear Mobileconfig para macOS

```bash
# 1. Crear archivo mobileconfig
cat > opencode-enterprise.mobileconfig << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadIdentifier</key>
    <string>com.empresa.opencode.config</string>
    <key>PayloadType</key>
    <string>com.opencode.cli</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>PayloadDisplayName</key>
    <string>OpenCode Enterprise</string>
    <key>provider</key>
    <dict>
        <key>enterprise-ai</key>
        <dict>
            <key>type</key>
            <string>openai-compatible</string>
            <key>baseURL</key>
            <string>https://ai.empresa.com/v1</string>
        </dict>
    </dict>
    <key>model</key>
    <string>llama-3.1-70b</string>
</dict>
</plist>
EOF

# 2. Firmar el perfil (opcional pero recomendado)
openssl smime -sign -in opencode-enterprise.mobileconfig \
  -out opencode-enterprise-signed.mobileconfig \
  -signer cert.pem \
  -inkey key.pem \
  -certfile ca.pem

# 3. Distribuir a través de MDM o enviar por email
```

### Paso 3: Configurar con Jamf Pro

```bash
# 1. Iniciar sesión en Jamf Pro
# Ir a https://tu-empresa.jamfcloud.com

# 2. Crear Configuration Profile
# Computers > Configuration Profiles > New

# 3. Configurar el perfil
# - Name: OpenCode Enterprise Configuration
# - Description: Configuración empresarial de OpenCode
# - Distribution Method: Install automatically

# 4. Agregar payload
# - Select a payload: Custom
# - Enter the plist domain: com.opencode.cli

# 5. Agregar configuración XML
# Pegar el contenido del mobileconfig

# 6. Asignar a scope
# - Seleccionar departamentos o dispositivos
# - Guardar y distribuir
```

### Paso 4: Configurar con FleetDM

```bash
# 1. Crear query para verificar instalación
cat > fleet-query-opencode.sql << 'EOF'
SELECT 
    path,
    data
FROM plist
WHERE path = '/Library/Managed Preferences/com.opencode.cli.json';
EOF

# 2. Ejecutar query en Fleet
fleetctl query --query "SELECT * FROM plist WHERE path LIKE '%opencode%'"

# 3. Crear archivo de configuración
cat > fleet-opencode.yml << 'EOF'
apiVersion: v1
kind: config
spec:
  config:
    provider:
      enterprise-ai:
        type: openai-compatible
        baseURL: https://ai.empresa.com/v1
    model: llama-3.1-70b
EOF

# 4. Aplicar configuración
fleetctl apply -f fleet-opencode.yml
```

### Paso 5: Verificar Configuración Enterprise

```bash
# 1. En el dispositivo cliente, verificar configuración remota
curl -s https://tu-empresa.com/.well-known/opencode | python3 -m json.tool

# 2. Verificar configuración MDM (macOS)
sudo profiles list | grep opencode
sudo profiles show -verbose

# 3. Verificar configuración cargada por OpenCode
opencode config list --verbose

# 4. Verificar precedencia
opencode config list | grep -E "(theme|model|provider)"

# 5. Probar funcionamiento
opencode
# Debería usar la configuración enterprise
```

### Paso 6: Documentar Proceso Enterprise

```bash
# Crear documentación para el equipo de IT
cat > docs/opencode-enterprise.md << 'EOF'
# Guía de Configuración Enterprise de OpenCode

## Requisitos Previos
- Servidor web con HTTPS
- Acceso a DNS para configurar .well-known
- Sistema MDM (opcional): Jamf, Kandji, FleetDM

## Pasos de Implementación

### 1. Configurar Endpoint Remoto
1. Crear archivo de configuración
2. Servir desde .well-known/opencode
3. Verificar acceso

### 2. Distribuir Managed Settings (opcional)
1. Crear mobileconfig
2. Distribuir a través de MDM
3. Verificar instalación

### 3. Verificar en Clientes
1. Instalar OpenCode
2. Verificar configuración remota
3. Probar funcionamiento

## Solución de Problemas
- Verificar DNS y HTTPS
- Revisar logs de MDM
- Verificar precedencia de configuración
EOF
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `.well-known/opencode` | Endpoint de configuración remota | `https://empresa.com/.well-known/opencode` |
| `com.opencode.cli` | Dominio MDM para macOS | Configuration Profile |
| `opencode config list --verbose` | Ver configuración con origen | `opencode config list --verbose` |
| `opencode config clear-cache` | Limpiar caché de configuración | `opencode config clear-cache` |
| `mobileconfig` | Formato de perfil macOS | `opencode-enterprise.mobileconfig` |
| `PayloadIdentifier` | ID del perfil MDM | `com.empresa.opencode.config` |

## Ejercicios Guiados

### Ejercicio 1: Implementar Endpoint Remoto

**Objetivo:** Configurar un servidor para servir configuración remota de OpenCode.

**Instrucciones:**
1. Configura un servidor web básico (puede ser local)
2. Crea el endpoint `.well-known/opencode`
3. Agrega configuración enterprise completa
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
  },
  "model": "llama-3.1-70b"
}
EOF

# 2. Iniciar servidor
cd /var/www && python3 -m http.server 8080

# 3. Verificar
curl http://localhost:8080/.well-known/opencode
```

### Ejercicio 2: Crear Mobileconfig

**Objetivo:** Crear un archivo mobileconfig para distribuir configuración en macOS.

**Instrucciones:**
1. Crea un archivo mobileconfig con configuración completa
2. Incluye proveedor, modelo e instrucciones
3. Valida que el XML es correcto
4. Simula la instalación en un dispositivo
5. Documenta el proceso de distribución

**Solución Esperada:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadIdentifier</key>
    <string>com.empresa.opencode.config</string>
    <key>PayloadType</key>
    <string>com.opencode.cli</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>provider</key>
    <dict>
        <key>enterprise</key>
        <dict>
            <key>type</key>
            <string>openai-compatible</string>
            <key>baseURL</key>
            <string>https://ai.empresa.com/v1</string>
        </dict>
    </dict>
    <key>model</key>
    <string>llama-3.1-70b</string>
</dict>
</plist>
```

### Ejercicio 3: Configurar con MDM

**Objetivo:** Distribuir configuración de OpenCode a través de un sistema MDM.

**Instrucciones:**
1. Elige un sistema MDM (Jamf, Kandji, o simulación)
2. Crea un Configuration Profile con configuración de OpenCode
3. Asigna el perfil a un grupo de dispositivos
4. Verifica la distribución
5. Documenta el proceso completo

**Solución Esperada:**
```bash
# Para Jamf Pro
# 1. Computers > Configuration Profiles > New
# 2. Name: "OpenCode Enterprise"
# 3. Custom payload > com.opencode.cli
# 4. Pegar configuración XML
# 5. Asignar a scope
# 6. Save and distribute

# Verificar en cliente
sudo profiles list | grep opencode
opencode config list --verbose
```

## Ejercicio Desafío

**Reto:** Implementa un sistema enterprise completo para 100 desarrolladores que incluya:
1. Configuración remota en `.well-known/opencode`
2. Mobileconfig para macOS
3. Script de verificación para Linux
4. Documentación completa
5. Proceso de troubleshooting

**Pistas:**
- Usa Nginx o Apache para servir la configuración
- Implementa monitoreo de la configuración remota
- Crea scripts de automatización para distribución
- Documenta el proceso de actualización de configuración
- Incluye verificaciones de salud del sistema

## Recursos Adicionales

- [Documentación Enterprise](https://opencode.ai/docs/enterprise)
- [.well-known/opencode](https://opencode.ai/docs/config/remote)
- [MDM Configuration](https://opencode.ai/docs/enterprise/mdm)
- [Mobileconfig Creation](https://opencode.ai/docs/enterprise/mobileconfig)
- [FleetDM Integration](https://opencode.ai/docs/enterprise/fleet)
- [Jamf Pro Configuration](https://opencode.ai/docs/enterprise/jamf)
- [Troubleshooting Enterprise](https://opencode.ai/docs/enterprise/troubleshooting)

## Autoevaluación

- [ ] Implementé configuración remota con .well-known/opencode
- [ ] Creé mobileconfig para distribución en macOS
- [ ] Configuré managed settings con un sistema MDM
- [ ] Comprendo las reglas de prioridad y sobreescritura
- [ ] Implementé configuración enterprise completa
- [ ] Gestioné dispositivos a gran escala
- [ ] Resolví problemas de configuración enterprise
- [ ] Documenté el proceso para el equipo de IT
