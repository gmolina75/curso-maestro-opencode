---
title: "Instalación y Configuración"
module: 2
duration: "60 minutos"
prerequisites: "Módulo 1: Introducción a OpenCode"
---

# Clase 2: Instalación y Configuración

## Resumen Ejecutivo

La instalación de OpenCode es un proceso sencillo que se adapta a múltiples plataformas y gestores de paquetes. OpenCode está diseñado para funcionar en terminales modernas como WezTerm, Alacritty, Ghostty o Kitty, aprovechando capacidades avanzadas de renderizado como ligatures, true color y soporte Unicode completo. La instalación puede realizarse mediante curl, npm, gestores de paquetes del sistema, Docker o WSL para usuarios de Windows.

Es fundamental comprender que OpenCode requiere un mínimo de configuración post-instalación, principalmente relacionado con la autenticación de proveedores de IA. Sin embargo, la herramienta está diseñada para ser funcional inmediatamente después de la instalación, con opciones de configuración que se pueden ir refinando según las necesidades del usuario. Este módulo cubre todos los métodos de instalación, verificación y troubleshooting básico.

## Objetivos de Aprendizaje

- Instalar OpenCode correctamente en tu sistema operativo
- Verificar que la instalación funciona correctamente
- Configurar terminales modernas para una experiencia óptima
- Resolver problemas comunes de instalación
- Mantener OpenCode actualizado

## Conceptos Clave

### Requisitos del Sistema

OpenCode tiene requisitos mínimos pero específicos:

| Requisito | Mínimo | Recomendado |
|-----------|--------|-------------|
| **Node.js** | 18.0+ | 20 LTS o superior |
| **Terminal** | Cualquier terminal moderna | WezTerm, Alacritty, Ghostty |
| **Sistema Operativo** | macOS, Linux, Windows | macOS o Linux nativo |
| **RAM** | 512MB disponibles | 2GB+ para modelos locales |
| **Disco** | 200MB para instalación | 2GB+ con modelos locales |

### Terminales Recomendadas

OpenCode aprovecha al máximo las capacidades de terminales modernas:

```bash
# WezTerm - Recomendada por su rendimiento y personalización
# macOS/Linux:
brew install wezterm
# O descargar desde https://wezfurlong.org/wezterm/

# Alacritty - Terminal GPU-accelerada
# macOS:
brew install alacritty
# Linux (Ubuntu/Debian):
sudo apt install alacritty

# Ghostty - Terminal moderna y rápida
# macOS:
brew install ghostty

# Kitty - Terminal con soporte GPU
# macOS:
brew install kitty
# Linux:
sudo apt install kitty
```

### Métodos de Instalación

#### 1. Curl (Recomendado para Linux/macOS)

```bash
# Instalación directa con curl
curl -fsSL https://opencode.ai/install | bash

# Esto descarga e instala OpenCode en /usr/local/bin
# No requiere permisos sudo en la mayoría de configuraciones
```

#### 2. npm (Multi-plataforma)

```bash
# Instalación global con npm
npm install -g opencode

# Con permisos sudo si es necesario (Linux/macOS)
sudo npm install -g opencode

# Con yarn
yarn global add opencode

# Con pnpm
pnpm add -g opencode

# Con bun
bun add -g opencode
```

#### 3. Homebrew (macOS)

```bash
# Agregar el tap de OpenCode (si está disponible)
brew tap anomalyco/opencode

# Instalar
brew install opencode

# O instalar directamente
brew install anomalyco/opencode/opencode
```

#### 4. Gestores de Paquetes de Linux

```bash
# Arch Linux (AUR)
paru -S opencode
# O con yay
yay -S opencode

# Debian/Ubuntu (si hay repo oficial)
sudo apt update
sudo apt install opencode

# Fedora (si hay repo oficial)
sudo dnf install opencode
```

#### 5. Windows

```bash
# Chocolatey
choco install opencode

# Scoop
scoop install opencode

# Mise (gestor de versiones multi-herramienta)
mise use -g opencode@latest

# Docker (cualquier plataforma)
docker run -it anomalyco/opencode:latest
```

#### 6. Windows Subsystem for Linux (WSL)

```bash
# Dentro de WSL (Ubuntu recomendado)
# Actualizar paquetes
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y curl git build-essential

# Instalar Node.js (necesario)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Instalar OpenCode
curl -fsSL https://opencode.ai/install | bash
```

## Guía Paso a Paso

### Paso 1: Verificar Entorno Previo

Antes de instalar, asegúrate de que tu sistema está listo:

```bash
# Verificar Node.js
node --version
# Debe mostrar v18.0.0 o superior

# Verificar npm
npm --version

# Verificar Git
git --version

# Verificar sistema operativo
uname -a
# macOS: Darwin
# Linux: Linux
# Windows: MINGW/MSYS si usas Git Bash, o Microsoft Windows si usas PowerShell

# Verificar arquitectura del procesador
uname -m
# x86_64 o amd64 para 64-bit
# arm64 o aarch64 para Apple Silicon
```

### Paso 2: Instalar OpenCode

Elige el método que mejor se adapte a tu sistema:

```bash
# Opción A: Para usuarios de Linux/macOS (recomendada)
curl -fsSL https://opencode.ai/install | bash

# Opción B: Para usuarios que prefieren npm
npm install -g opencode

# Opción C: Para macOS con Homebrew
brew install opencode

# Opción D: Para Windows con Chocolatey
choco install opencode
```

### Paso 3: Configurar la Terminal

Para una experiencia óptima, configura tu terminal:

```bash
# Para WezTerm, crea o edita ~/.wezterm.lua
# Agrega estas configuraciones:

# Para Alacritty, edita ~/.config/alacritty/alacritty.toml
# Asegúrate de tener:
# - Fuente con ligatures (FiraCode, JetBrains Mono)
# - True color habilitado
# - Soporte Unicode

# Verificar que tu terminal soporta true color
echo -e "\e[38;2;255;100;0mTest\e[0m"
# Deberías ver un color naranja, no colores planos
```

### Paso 4: Verificar la Instalación

```bash
# Verificar versión instalada
opencode --version
# Debe mostrar algo como: opencode v1.x.x

# Ver ayuda completa
opencode --help

# Verificar configuración inicial
opencode config list

# Iniciar OpenCode por primera vez
opencode
# Esto abrirá la interfaz TUI
```

### Paso 5: Configuración Inicial en la TUI

Cuando inicies OpenCode por primera vez:

```bash
# 1. Selecciona tu proveedor de IA preferido
#    - Opción más rápida: OpenCode Zen (balance de $20 incluido)
#    - Opción gratuita limitada: Proveedores con tier gratuito

# 2. Autentícate según el proveedor elegido
#    - OAuth: Se abre navegador para autorizar
#    - API Key: Se solicita ingresar la clave

# 3. Verifica que todo funciona escribiendo un prompt simple
#    "Hola, ¿puedes confirmar que funcionas correctamente?"
```

### Paso 6: Mantener OpenCode Actualizado

```bash
# Si instalaste con curl
opencode update
# O vuelve a ejecutar el instalador
curl -fsSL https://opencode.ai/install | bash

# Si instalaste con npm
npm update -g opencode

# Si instalaste con Homebrew
brew upgrade opencode

# Verificar la versión después de actualizar
opencode --version
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode` | Iniciar la TUI | `opencode` |
| `opencode --version` | Mostrar versión | `opencode --version` |
| `opencode --help` | Mostrar ayuda | `opencode --help` |
| `opencode update` | Actualizar OpenCode | `opencode update` |
| `opencode config list` | Ver configuración | `opencode config list` |
| `npm list -g opencode` | Verificar instalación npm | `npm list -g opencode` |
| `which opencode` | Ubicación del binario | `which opencode` |

## Ejercicios Guiados

### Ejercicio 1: Instalación Completa

**Objetivo:** Instalar OpenCode en tu sistema y verificar que funciona correctamente.

**Instrucciones:**
1. Verifica que cumples los requisitos mínimos (Node.js 18+)
2. Elige el método de instalación apropiado para tu SO
3. Ejecuta la instalación
4. Verifica la versión instalada
5. Inicia OpenCode y completa la configuración inicial

**Solución Esperada:**
```bash
# Verificar requisitos
node --version  # v18.x.x o superior
npm --version

# Instalar (ejemplo con curl)
curl -fsSL https://opencode.ai/install | bash

# Verificar
opencode --version
# opencode v1.x.x

# Iniciar
opencode
# Debería abrir la interfaz TUI
```

### Ejercicio 2: Configuración de Terminal

**Objetivo:** Configurar tu terminal para una experiencia óptima con OpenCode.

**Instrucciones:**
1. Identifica tu terminal actual
2. Verifica si es una terminal moderna recomendada
3. Si no lo es, instala una terminal recomendada (WezTerm o Alacritty)
4. Configura la fuente con ligatures
5. Verifica soporte de true color

**Solución Esperada:**
```bash
# Verificar terminal actual
echo $TERM
# xterm-256color es bueno, xterm-256color-italic es mejor

# Para Alacritty, verificar configuración
cat ~/.config/alacritty/alacritty.toml | grep -i font
# Debe mostrar una fuente como FiraCode o JetBrains Mono

# Para WezTerm
cat ~/.wezterm.lua | grep font
```

### Ejercicio 3: Actualización y Mantenimiento

**Objetivo:** Aprender a mantener OpenCode actualizado y resolver problemas básicos.

**Instrucciones:**
1. Verifica tu versión actual de OpenCode
2. Investiga cuál es la última versión disponible
3. Si no es la última, actualiza
4. Documenta el proceso que utilizaste
5. Crea un recordatorio para actualizar periódicamente

**Solución Esperada:**
```bash
# Verificar versión actual
opencode --version
# opencode v1.x.x

# Verificar última versión (consulta GitHub releases)
# https://github.com/anomalyco/opencode/releases

# Actualizar (ejemplo con npm)
npm update -g opencode

# Verificar después de actualización
opencode --version
# Debería mostrar la versión más reciente
```

## Ejercicio Desafío

**Reto:** Configura un entorno de desarrollo multi-plataforma con OpenCode en al menos 2 sistemas operativos diferentes (por ejemplo, macOS y Linux, o Windows con WSL y Linux nativo).

**Pistas:**
- Usa Docker para probar en diferentes distribuciones de Linux
- Configura el mismo proveedor de IA en ambos entornos
- Documenta las diferencias de instalación entre plataformas
- Prueba que OpenCode funciona correctamente en ambos entornos
- Configura sincronización de configuración entre entornos

## Recursos Adicionales

- [Guía de Instalación Oficial](https://opencode.ai/docs/installation)
- [Soporte de Terminales](https://opencode.ai/docs/terminal-support)
- [Docker Hub - OpenCode](https://hub.docker.com/r/anomalyco/opencode)
- [GitHub Releases](https://github.com/anomalyco/opencode/releases)
- [Troubleshooting Común](https://opencode.ai/docs/troubleshooting)

## Autoevaluación

- [ ] He instalado OpenCode correctamente en mi sistema
- [ ] Puedo verificar la versión instalada con `opencode --version`
- [ ] Mi terminal está configurada con fuentes y colores apropiados
- [ ] He completado la configuración inicial de un proveedor de IA
- [ ] Entiendo cómo actualizar OpenCode cuando sea necesario
- [ ] Puedo resolver problemas básicos de instalación
- [ ] He documentado mi proceso de instalación para referencia futura
