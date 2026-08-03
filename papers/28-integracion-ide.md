---
title: "Integración con IDE"
module: 28
duration: "30 min"
prerequisites: "Módulo 27 - Custom Tools y Plugins"
---

# Clase 28: Integración con IDE

## Resumen Ejecutivo

OpenCode se integra de forma fluida con los principales editores de código del mercado, incluyendo VS Code, Cursor, Windsurf y VSCodium. La integración se logra mediante extensiones oficiales que permiten ejecutar OpenCode directamente desde el editor, compartir contexto como selecciones de texto y pestañas abiertas, y utilizar atajos de teclado personalizados para acceder rápidamente a las funcionalidades de OpenCode. Esta integración elimina la necesidad de cambiar entre la terminal y el editor, mejorando significativamente la productividad.

Las extensiones de OpenCode para editores están disponibles en los marketplaces oficiales de cada editor y se pueden instalar de forma automática o manual. Una vez instaladas, proporcionan acceso inmediato a todas las capacidades de OpenCode sin salir del entorno de desarrollo.

## Objetivos de Aprendizaje
- Instalar la extensión de OpenCode en VS Code, Cursor o Windsurf
- Configurar atajos de teclado para acceso rápido
- Compartir contexto entre el editor y OpenCode
- Configurar el editor por defecto para OpenCode
- Dominar los atajos de teclado de la extensión

## Conceptos Clave

### Editores Soportados

OpenCode soporta integración con los siguientes editores:

| Editor | Soporte | Marketplace |
|--------|---------|-------------|
| VS Code | Completo | Visual Studio Marketplace |
| Cursor | Completo | Cursor Marketplace |
| Windsurf | Completo | Windsurf Marketplace |
| VSCodium | Completo | Open VSX Registry |

### Instalación Automática

La forma más fácil de instalar la extensión es usar el comando de OpenCode:

```bash
# Instalar extensión para VS Code
opencode install vscode

# Instalar extensión para Cursor
opencode install cursor

# Instalar extensión para Windsurf
opencode install windsurf
```

Estos comandos:
1. Detectan si el editor está instalado
2. Instalan la extensión desde el marketplace
3. Configuran los atajos de teclado automáticamente
4. Vinculan OpenCode con el editor

### Instalación Manual

Si la instalación automática no está disponible, se puede instalar manualmente:

**VS Code:**
1. Abre VS Code
2. Ve a Extensions (Ctrl+Shift+X)
3. Busca "OpenCode"
4. Haz clic en Install

**Cursor:**
1. Abre Cursor
2. Ve a Extensions
3. Busca "OpenCode"
4. Haz clic en Install

**VSCodium:**
1. Abre VSCodium
2. Ve a Extensions
3. Busca "OpenCode" en Open VSX
4. Haz clic en Install

### Atajos de Teclado

La extensión de OpenCode proporciona atajos de teclado para acceso rápido:

| Atajo | Acción |
|-------|--------|
| `Cmd/Ctrl+Esc` | Abrir/cerrar panel de OpenCode |
| `Cmd/Ctrl+Shift+Esc` | Ejecutar comando de OpenCode |
| `Cmd/Ctrl+Option+K` | Enviar selección actual a OpenCode |

**En macOS:**
- `Cmd+Esc` → Abrir/cerrar panel
- `Cmd+Shift+Esc` → Ejecutar comando
- `Cmd+Option+K` → Enviar selección

**En Windows/Linux:**
- `Ctrl+Esc` → Abrir/cerrar panel
- `Ctrl+Shift+Esc` → Ejecutar comando
- `Ctrl+Alt+K` → Enviar selección

### Conciencia de Contexto

La extensión comparte contexto entre el editor y OpenCode:

#### Selección de Texto
Cuando seleccionas texto en el editor y usas `Cmd/Ctrl+Option+K`, OpenCode recibe:
- El contenido seleccionado
- El nombre del archivo
- La posición del cursor
- El lenguaje del archivo

#### Pestañas Abiertas
OpenCode puede acceder a las pestañas abiertas en el editor:
- Archivos abiertos actualmente
- Contenido de los archivos
- Estructura del proyecto

### Configuración del Editor por Defecto

Para usar un editor específico como predeterminado en OpenCode:

```bash
# VS Code
export EDITOR="code --wait"

# Cursor
export EDITOR="cursor --wait"

# VSCodium
export EDITOR="codium --wait"

# Windsurf
export EDITOR="windsurf --wait"
```

En Windows (PowerShell):
```powershell
$env:EDITOR="code --wait"
```

### Configuración de la Extensión

La extensión se puede configurar desde el editor:

**VS Code settings.json:**
```json
{
  "opencode.autostart": true,
  "opencode.theme": "dark",
  "opencode.shortcuts": {
    "togglePanel": "cmd+esc",
    "runCommand": "cmd+shift+esc",
    "sendSelection": "cmd+option+k"
  }
}
```

## Guía Paso a Paso

### Paso 1: Instalar la Extensión

```bash
# Instalar para VS Code
opencode install vscode

# Verificar instalación
code --list-extensions | grep opencode
```

### Paso 2: Configurar Atajos de Teclado

En VS Code, abre el archivo de configuración de atajos:
- macOS: `Cmd+Shift+P` → "Open Keyboard Shortcuts"
- Windows: `Ctrl+Shift+P` → "Open Keyboard Shortcuts"

Busca "OpenCode" y personaliza los atajos según tus preferencias.

### Paso 3: Compartir Contexto

1. Abre un archivo en VS Code
2. Selecciona una porción de código
3. Presiona `Cmd/Ctrl+Option+K`
4. OpenCode recibirá el código seleccionado

### Paso 4: Configurar Editor por Defecto

```bash
# Agregar a tu archivo de shell profile
echo 'export EDITOR="code --wait"' >> ~/.bashrc
source ~/.bashrc
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode install vscode` | Instalar extensión VS Code | Terminal |
| `Cmd/Ctrl+Esc` | Abrir/cerrar panel | Atajo de teclado |
| `Cmd/Ctrl+Shift+Esc` | Ejecutar comando | Atajo de teclado |
| `Cmd/Ctrl+Option+K` | Enviar selección | Atajo de teclado |
| `EDITOR` | Editor por defecto | `"code --wait"` |

## Ejercicios Guiados

### Ejercicio 1: Instalar la Extensión de OpenCode
**Objetivo:** Instalar y verificar la extensión de OpenCode en tu editor.

**Instrucciones:**
1. Verifica que tu editor esté instalado
2. Ejecuta el comando de instalación de OpenCode
3. Abre tu editor y verifica que la extensión aparece
4. Configura los atajos de teclado

**Solución Esperada:**
```bash
# Instalar extensión
opencode install vscode

# Verificar
code --list-extensions | grep opencode
# Output: opencode.opencode
```

### Ejercicio 2: Probar Atajos de Teclado
**Objetivo:** Familiarizarse con los atajos de teclado de la extensión.

**Instrucciones:**
1. Abre un archivo de código en tu editor
2. Presiona `Cmd/Ctrl+Esc` para abrir el panel de OpenCode
3. Escribe un mensaje y verifica que funciona
4. Presiona `Cmd/Ctrl+Esc` nuevamente para cerrar
5. Selecciona código y presiona `Cmd/Ctrl+Option+K`

**Solución Esperada:**
```
# 1. Cmd/Ctrl+Esc → Abre el panel de OpenCode
# 2. Escribe: "¿Qué hace este código?"
# 3. Cmd/Ctrl+Esc → Cierra el panel
# 4. Selecciona código → Cmd/Ctrl+Option+K → Envía selección
```

### Ejercicio 3: Compartir Contexto entre Editor y OpenCode
**Objetivo:** Verificar que OpenCode recibe correctamente el contexto del editor.

**Instrucciones:**
1. Abre un archivo complejo en tu editor
2. Selecciona una función específica
3. Usa `Cmd/Ctrl+Option+K` para enviar la selección
4. En OpenCode, pregunta sobre la función seleccionada
5. Verifica que la respuesta es precisa

**Solución Esperada:**
```
# En el editor:
# Selecciona la función calculateTotal()

# Cmd/Ctrl+Option+K → Envía la función a OpenCode

# En OpenCode:
# Pregunta: "¿Qué hace esta función y cuáles son sus posibles mejoras?"
# Respuesta: "La función calculateTotal() suma los precios de los items...
#             Sugiero manejar el caso de items vacíos y agregar
#             soporte para descuentos..."
```

## Ejercicio Desafío

**Reto:** Configura un flujo de trabajo completo de integración IDE:
1. Instala la extensión en tu editor preferido
2. Personaliza los atajos de teclado para tu estilo de trabajo
3. Configura el editor por defecto en OpenCode
4. Crea un flujo de trabajo que combine edición y asistencia de OpenCode
5. Documenta los atajos más útiles para tu equipo

**Pistas:**
- Considera atajos que no colisionen con los del editor
- Usa la conciencia de contexto para preguntas específicas
- Experimenta con diferentes flujos de trabajo
- Comparte la configuración con tu equipo

## Recursos Adicionales
- [Documentación oficial de OpenCode - IDE Integration](https://opencode.ai/docs/ide)
- [Guía de instalación de extensiones](https://opencode.ai/docs/ide/installation)
- [Personalización de atajos](https://opencode.ai/docs/ide/shortcuts)

## Autoevaluación
- [ ] Puedo instalar la extensión de OpenCode en mi editor
- [ ] Conozco y uso los atajos de teclado principales
- [ ] Puedo compartir contexto entre el editor y OpenCode
- [ ] Configuré el editor por defecto correctamente
- [ ] Entiendo cómo funciona la conciencia de contexto
- [ ] Puedo personalizar los atajos según mis necesidades
