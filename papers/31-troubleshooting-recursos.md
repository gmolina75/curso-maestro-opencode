---
title: "Troubleshooting y Recursos"
module: 31
duration: "40 min"
prerequisites: "Módulo 30 - Integración con GitLab"
---

# Clase 31: Troubleshooting y Recursos

## Resumen Ejecutivo

Este módulo cubre los problemas más comunes que los usuarios encuentran al usar OpenCode y sus soluciones. Desde problemas de instalación en Windows/WSL hasta fallos en la carga de MCP servers y skills, este capítulo proporciona guías de diagnóstico y solución para cada situación. También incluye una compilación de recursos oficiales y de la comunidad para obtener ayuda adicional.

El troubleshooting efectivo es esencial para mantener un flujo de trabajo productivo. Conocer los comandos de diagnóstico y las soluciones a problemas comunes permite resolver la mayoría de situaciones sin necesidad de buscar ayuda externa.

## Objetivos de Aprendizaje
- Diagnosticar y resolver problemas comunes de OpenCode
- Solucionar problemas específicos de Windows y WSL
- Usar comandos de debug para identificar problemas
- Encontrar recursos oficiales y comunitarios para ayuda
- Aplicar mejores prácticas de mantenimiento

## Conceptos Clave

### Problemas Comunes y Soluciones

#### Problema: OpenCode no inicia

**Síntomas:**
- El comando `opencode` no se reconoce
- Error de permisos al ejecutar
- OpenCode se cierra inmediatamente

**Soluciones:**
```bash
# Verificar instalación
which opencode

# Reinstalar OpenCode
npm install -g opencode

# Verificar permisos (Linux/Mac)
chmod +x $(which opencode)

# Verificar Node.js
node --version  # Debe ser >= 18.0.0
```

#### Problema: Errores de Conexión con LLM

**Síntomas:**
- Timeout al conectar con el modelo
- Error de autenticación
- Respuestas incompletas

**Soluciones:**
```bash
# Verificar API key
echo $ANTHROPIC_API_KEY

# Probar conexión directa
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/models

# Verificar configuración
opencode debug config
```

#### Problema: MCP Server no carga

**Síntomas:**
- Herramientas MCP no disponibles
- Error al cargar servidor
- Timeout de conexión

**Soluciones:**
```bash
# Verificar configuración MCP
opencode mcp debug

# Listar servidores configurados
cat opencode.json | grep mcp

# Verificar dependencias
npm list -g | grep mcp
```

### Problemas Específicos de Windows

#### Problema: Rutas de Archivo

**Síntomas:**
- Error al acceder a archivos
- Rutas con espacios no funcionan
- Problemas con letras de unidad

**Soluciones:**
```powershell
# Usar rutas cortas
Get-ChildItem -Path "G:\My Drive\..." | Select-Object -First 1

# Usar comillas en rutas con espacios
Set-Content -LiteralPath "ruta con espaces\archivo.txt"

# Verificar que la ruta existe
Test-Path -LiteralPath "G:\My Drive\estudios\cursos\OpenCode"
```

#### Problema: Permisos en Windows

**Síntomas:**
- Error de acceso denegado
- No puede escribir archivos
- Problemas con Git

**Soluciones:**
```powershell
# Ejecutar como administrador
Start-Process powershell -Verb RunAs

# Verificar permisos de archivo
Get-Acl "archivo.txt" | Format-List

# Conceder permisos
icacls "archivo.txt" /grant Todos:F
```

### Problemas con WSL

#### Problema: Acceso a Archivos de Windows

**Síntomas:**
- No puede acceder a archivos en `/mnt/c/`
- Errores de permisos
- Rutas incorrectas

**Soluciones:**
```bash
# Verificar montaje
ls /mnt/c/

# Usar rutas WSL correctas
cd /mnt/g/My\ Drive/estudios/cursos/OpenCode

# Configurar permisos en wsl.conf
echo -e "[automount]\nenabled = true\noptions = \"metadata\"" | sudo tee /etc/wsl.conf
```

#### Problema: Red en WSL

**Síntomas:**
- No puede conectar a servicios externos
- DNS no resuelve
- Firewalls bloquean

**Soluciones:**
```bash
# Verificar DNS
nslookup api.anthropic.com

# Verificar conectividad
curl -I https://api.anthropic.com

# Configurar DNS alternativo
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

### Problemas de Skill Discovery

**Síntomas:**
- Skills no se cargan automáticamente
- Error al cargar skill específico
- Skills duplicados

**Soluciones:**
```bash
# Verificar estructura de directorios
ls -la .opencode/skills/

# Verificar frontmatter YAML
cat .opencode/skills/mi-skill.md | head -20

# Depurar descubrimiento
opencode debug skills
```

### Problemas de LSP Experimental

**Síntomas:**
- Autocompletado no funciona
- Errores de análisis de código
- Lento rendimiento

**Soluciones:**
```bash
# Deshabilitar LSP experimental
# En opencode.json:
{
  "experimental": {
    "lsp": false
  }
}

# Verificar estado LSP
opencode debug lsp
```

### Límites de Tamaño de Imágenes

**Síntomas:**
- Error al enviar imágenes grandes
- Timeout al procesar imágenes
- Memoria insuficiente

**Soluciones:**
```bash
# Comprimir imágenes antes de enviar
convert imagen-original.png -resize 50% imagen-comprimida.png

# Verificar límites de tamaño
# Máximo recomendado: 1024x1024 píxeles
```

### Comandos de Debug

#### opencode debug config
Muestra la configuración actual de OpenCode:

```bash
opencode debug config

# Output:
# Configuration file: /path/to/opencode.json
# Model: anthropic/claude-sonnet-4-20250514
# Agent: build
# MCP Servers: 3 configured
# Skills: 5 discovered
```

#### opencode mcp auth list
Lista las autenticaciones de MCP:

```bash
opencode mcp auth list

# Output:
# Sentry: ✓ Authenticated
# Context7: ✓ Authenticated
# GitHub: ✗ Not authenticated
```

#### opencode mcp debug
Depura problemas de MCP:

```bash
opencode mcp debug

# Output:
# Checking MCP servers...
# sentry: ✓ Connection OK
# context7: ✓ Connection OK
# gitlab: ✗ Connection failed - Timeout
```

### Recursos Oficiales

#### Documentación
- **Sitio oficial:** https://opencode.ai/docs
- **Guía de inicio:** https://opencode.ai/docs/getting-started
- **Referencia de configuración:** https://opencode.ai/docs/configuration
- **API Reference:** https://opencode.ai/docs/api

#### GitHub
- **Repositorio principal:** https://github.com/opencode-ai/opencode
- **Issues:** https://github.com/opencode-ai/opencode/issues
- **Discussions:** https://github.com/opencode-ai/opencode/discussions
- **Releases:** https://github.com/opencode-ai/opencode/releases

#### Comunidad
- **Discord:** https://discord.gg/opencode
- **Twitter:** https://twitter.com/opencode_ai
- **Blog:** https://opencode.ai/blog

#### Changelog
- **Cambios recientes:** https://opencode.ai/changelog
- **Notas de versión:** https://github.com/opencode-ai/opencode/releases

### Recursos de la Comunidad

#### Plugins Populares
- `opencode-helicone-session`: Sesiones de Helicone
- `opencode-gitlab-plugin`: Integración con GitLab
- `opencode-sentry`: Monitoreo de errores

#### Templates
- `opencode-starter`: Template para proyectos nuevos
- `opencode-api`: Template para APIs
- `opencode-fullstack`: Template fullstack

#### Tutoriales
- Video tutorials en YouTube
- Artículos en Medium
- Cursos en plataformas de educación

### Mejores Prácticas de Mantenimiento

#### Actualización Regular
```bash
# Verificar versión actual
opencode --version

# Actualizar OpenCode
npm update -g opencode

# Actualizar plugins
npm update
```

#### Limpieza de Cache
```bash
# Limpiar cache de OpenCode
rm -rf ~/.opencode/cache

# Limpiar cache npm
npm cache clean --force
```

#### Monitoreo de Logs
```bash
# Ver logs de OpenCode
tail -f ~/.opencode/logs/opencode.log

# Buscar errores en logs
grep -i error ~/.opencode/logs/opencode.log
```

## Guía Paso a Paso

### Paso 1: Diagnosticar el Problema

```bash
# Verificar que OpenCode está instalado
opencode --version

# Verificar configuración
opencode debug config

# Verificar MCP servers
opencode mcp auth list
```

### Paso 2: Revisar Logs

```bash
# Ubicación de logs según OS
# macOS: ~/Library/Logs/opencode/
# Linux: ~/.local/share/opencode/logs/
# Windows: %APPDATA%\opencode\logs\

# Ver logs recientes
tail -100 ~/.opencode/logs/opencode.log
```

### Paso 3: Buscar Soluciones

1. Revisa la documentación oficial
2. Busca en GitHub Issues
3. Pregunta en Discord
4. Busca en Stack Overflow con tag `opencode`

### Paso 4: Reportar el Problema

Si no encuentras solución:
1. Crea un issue en GitHub
2. Incluye logs de error
3. Describe los pasos para reproducir
4. Incluye versión de OpenCode y SO

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode --version` | Ver versión | Terminal |
| `opencode debug config` | Ver configuración | Terminal |
| `opencode mcp auth list` | Listar autenticaciones MCP | Terminal |
| `opencode mcp debug` | Depurar MCP | Terminal |
| `opencode debug skills` | Depurar skills | Terminal |

## Ejercicios Guiados

### Ejercicio 1: Diagnosticar un Problema de Conexión
**Objetivo:** Usar comandos de debug para identificar problemas de conexión.

**Instrucciones:**
1. Simula un problema de conexión (desconecta internet)
2. Ejecuta `opencode debug config` para verificar configuración
3. Ejecuta `opencode mcp debug` para verificar MCP
4. Revisa los logs para errores
5. Reconecta y verifica que funciona

**Solución Esperada:**
```bash
# 1. Desconectar internet (simular)

# 2. Verificar configuración
opencode debug config
# Output: Configuration OK, but connection failed

# 3. Verificar MCP
opencode mcp debug
# Output: sentry: ✗ Connection timeout

# 4. Revisar logs
tail -f ~/.opencode/logs/opencode.log
# Output: Error: ECONNREFUSED

# 5. Reconectar y reintentar
opencode
# Output: Connection restored
```

### Ejercicio 2: Resolver Problema de Skill Discovery
**Objetivo:** Diagnosticar y resolver problemas de descubrimiento de skills.

**Instrucciones:**
1. Crea un skill con frontmatter YAML inválido
2. Intenta cargar el skill
3. Observa el error
4. Corrige el frontmatter
5. Verifica que el skill se carga correctamente

**Solución Esperada:**
```markdown
# Skill con error intencional
---
name: "mi-skill"
description: "Skill de prueba"
# Falta cierre de frontmatter
---

# Contenido del skill
```

```bash
# Intentar cargar skill
opencode debug skills
# Output: Error parsing frontmatter in mi-skill.md

# Corregir frontmatter
# Agregar -- al final del frontmatter

# Verificar corrección
opencode debug skills
# Output: mi-skill: ✓ Valid
```

### Ejercicio 3: Compilar Información de Debug
**Objetivo:** Recopilar toda la información necesaria para reportar un problema.

**Instrucciones:**
1. Ejecuta todos los comandos de debug
2. Recopila la salida de cada comando
3. Identifica el problema específico
4. Crea un reporte completo
5. Incluye logs relevantes

**Solución Esperada:**
```bash
# Recopilar información
opencode --version > debug-info.txt
opencode debug config >> debug-info.txt
opencode mcp auth list >> debug-info.txt
tail -50 ~/.opencode/logs/opencode.log >> debug-info.txt

# El archivo debug-info.txt contiene:
# - Versión de OpenCode
# - Configuración actual
# - Estado de MCP servers
# - Logs recientes con errores
```

## Ejercicio Desafío

**Reto:** Crea una guía de troubleshooting personalizada para tu equipo:
1. Documenta los problemas más comunes que has encontrado
2. Incluye soluciones paso a paso
3. Crea scripts de diagnóstico automatizados
4. Configura monitoreo proactivo
5. Establece un proceso de reporte de problemas

**Pistas:**
- Incluye capturas de pantalla cuando sea posible
- Documenta versiones específicas de software
- Crea plantillas de reporte de problemas
- Mantén la guía actualizada con nuevos problemas

## Recursos Adicionales
- [Documentación oficial de OpenCode - Troubleshooting](https://opencode.ai/docs/troubleshooting)
- [Guía de instalación](https://opencode.ai/docs/installation)
- [Configuración avanzada](https://opencode.ai/docs/configuration/advanced)
- [GitHub Issues](https://github.com/opencode-ai/opencode/issues)
- [Discord de la comunidad](https://discord.gg/opencode)

## Autoevaluación
- [ ] Puedo diagnosticar problemas comunes de OpenCode
- [ ] Uso comandos de debug para identificar problemas
- [ ] Resuelvo problemas específicos de Windows/WSL
- [ ] Encuentro recursos oficiales y comunitarios para ayuda
- [ ] Creo reportes de problemas completos y útiles
- [ ] Mantengo OpenCode actualizado y funcionando correctamente
