---
title: "Comandos Slash"
module: 13
duration: "50 minutos"
prerequisites: "Módulo 12: Navegación en la Interfaz TUI"
---

# Clase 13: Comandos Slash

## Resumen Ejecutivo

Los comandos slash son atajos de texto que se escriben directamente en la barra de entrada de OpenCode para realizar acciones especiales. Estos comandos comienzan con `/` y proporcionan acceso rápido a funciones como crear nuevas sesiones, gestionar proveedores, inicializar configuraciones y controlar el comportamiento de la herramienta.

Dominar los comandos slash es esencial para un flujo de trabajo eficiente. Te permiten ejecutar operaciones complejas con una sola línea de texto, sin necesidad de navegar por menús o usar combinaciones de teclas. Cada comando está diseñado para una tarea específica y many de ellos aceptan argumentos adicionales para personalizar su comportamiento.

## Objetivos de Aprendizaje

- Conocer y utilizar todos los comandos slash disponibles
- Gestionar sesiones de chat eficientemente
- Conectar y configurar proveedores de modelos
- Inicializar y configurar proyectos
- Personalizar la experiencia de usuario

## Conceptos Clave

### Comandos de Sesión

Los comandos de sesión controlan el ciclo de vida de las conversaciones con OpenCode.

**`/new`** - Crear una nueva sesión
```bash
# Inicia una nueva conversación limpia
/new

# También puedes especificar un tema
/new "Refactorización del módulo de autenticación"
```

**`/sessions`** - Listar sesiones existentes
```bash
# Muestra todas las sesiones guardadas
/sessions

# Filtra por nombre
/sessions "autenticación"
```

**`/compact`** - Compactar la sesión actual
```bash
# Reduce el contexto de la conversación manteniendo puntos clave
/compact

# Compacta con nivel específico
/compact aggressive
```

**`/share` y `/unshare`** - Compartir sesión
```bash
# Genera un enlace para compartir la sesión
/share

# Elimina el enlace de compartir
/unshare
```

**`/export`** - Exportar sesión
```bash
# Exporta la conversación a un archivo
/export

# Exporta en formato específico
/export markdown
/export json
```

**`/undo` y `/redo`** - Deshacer/rehacer cambios
```bash
# Deshace el último cambio de archivos
/undo

# Rehace el último cambio deshecho
/redo
```

### Comandos de Proveedor

Estos comandos gestionan la conexión con servicios de modelos de IA.

**`/connect`** - Conectar proveedor
```bash
# Conectar a OpenAI
/connect openai

# Conectar a Anthropic
/connect anthropic

# Conectar con API key específica
/connect openai sk-xxxx
```

**`/models`** - Gestionar modelos
```bash
# Listar modelos disponibles
/models

# Cambiar modelo activo
/models gpt-4

# Ver información del modelo actual
/models current
```

### Comandos de Inicialización

Ayudan a configurar OpenCode para tu proyecto.

**`/init`** - Inicialización básica
```bash
# Crea configuración inicial de OpenCode
/init

# Genera archivos de configuración en .opencode/
```

**`/init-deep`** - Inicialización profunda
```bash
# Análisis completo del proyecto
/init-deep

# Genera documentación de la estructura del código
# Identifica frameworks, dependencias y patrones
```

### Comandos de Navegación

Proporcionan acceso a información y configuraciones.

**`/help`** - Mostrar ayuda
```bash
# Lista todos los comandos disponibles
/help

# Ayuda específica de un comando
/help compact
```

**`/details`** - Detalles de la sesión
```bash
# Información detallada de la sesión actual
/details

# Incluye: modelo, tokens, duración, archivos
```

**`/thinking`** - Modo de razonamiento
```bash
# Activa/desactiva el pensamiento detallado
/thinking

# Ver estado actual
/thinking status
```

**`/themes`** - Gestión de temas
```bash
# Listar temas disponibles
/themes

# Aplicar tema
/themes dark

# Tema personalizado
/themes custom my-theme
```

**`/editor`** - Configurar editor
```bash
# Configurar editor externo
/editor vscode

# Configurar con opciones
/editor "code --new-window"
```

### Comandos de Control

Gestionan el comportamiento general de OpenCode.

**`/exit`** - Salir de OpenCode
```bash
# Cierra la aplicación
/exit

# También puedes usar Ctrl+C
```

## Guía Paso a Paso

### Paso 1: Crear y Gestionar Sesiones

```bash
# Inicia OpenCode
opencode

# Crea una nueva sesión con tema
/new "Desarrollo de API REST"

# Trabaja en la sesión...

# Guarda y crea otra
/compact
/new "Pruebas unitarias"

# Lista tus sesiones
/sessions

# Recupera una sesión anterior
/sessions "API REST"
```

### Paso 2: Conectar y Configurar Proveedores

```bash
# Verifica tu conexión actual
/models current

# Conecta a un nuevo proveedor
/connect anthropic

# Lista modelos disponibles
/models

# Cambia a un modelo específico
/models claude-3-5-sonnet

# Verifica el cambio
/models current
```

### Paso 3: Inicializar un Proyecto

```bash
# Para un proyecto nuevo
cd ~/nuevo-proyecto
opencode

# Ejecuta inicialización profunda
/init-deep

# OpenCode analizará:
# - Estructura de archivos
# - Dependencias (package.json, requirements.txt)
# - Frameworks detectados
# - Configuraciones existentes

# Esto genera archivos en .opencode/
ls .opencode/
# config.json
# project-context.md
```

### Paso 4: Exportar y Compartir Trabajo

```bash
# Trabaja en una solución...

# Exporta la conversación
/export markdown

# Crea un enlace para compartir
/share

# Copia el enlace y compártelo con tu equipo

# Cuando termines, elimina el enlace
/unshare
```

### Paso 5: Deshacer Cambios y Usar Ayuda

```bash
# Si hiciste un cambio que no querías
/undo

# Si necesitas rehacer
/redo

# ¿Olvidaste un comando?
/help

# Detalles de la sesión actual
/details
```

## Referencia Rápida

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `/new [tema]` | Nueva sesión | `/new "Auth refactor"` |
| `/sessions` | Listar sesiones | `/sessions` |
| `/compact` | Compactar contexto | `/compact aggressive` |
| `/share` | Compartir sesión | `/share` |
| `/unshare` | Dejar de compartir | `/unshare` |
| `/export [fmt]` | Exportar conversación | `/export markdown` |
| `/undo` | Deshacer cambio | `/undo` |
| `/redo` | Rehacer cambio | `/redo` |
| `/connect [prov]` | Conectar proveedor | `/connect openai` |
| `/models` | Listar/cambiar modelos | `/models gpt-4` |
| `/init` | Inicialización básica | `/init` |
| `/init-deep` | Inicialización profunda | `/init-deep` |
| `/help [cmd]` | Mostrar ayuda | `/help compact` |
| `/details` | Detalles de sesión | `/details` |
| `/thinking` | Modo razonamiento | `/thinking` |
| `/themes [tema]` | Gestionar temas | `/themes dark` |
| `/editor [editor]` | Configurar editor | `/editor vscode` |
| `/exit` | Salir | `/exit` |

## Ejercicios Guiados

### Ejercicio 1: Gestión Completa de Sesiones

**Objetivo:** Crear, gestionar y alternar entre múltiples sesiones de trabajo.

**Instrucciones:**
1. Inicia OpenCode
2. Crea una sesión para "Diseño de base de datos"
3. Escribe 3-4 mensajes sobre el diseño
4. Compacta la sesión con `/compact`
5. Crea una nueva sesión para "API endpoints"
6. Lista todas las sesiones con `/sessions`
7. Cambia a la primera sesión
8. Verifica que el contexto se mantiene

**Solución Esperada:**
```bash
# Paso 1
opencode

# Paso 2
/new "Diseño de base de datos"

# Paso 3-4
> [trabajas en diseño...]
/compact

# Paso 5
/new "API endpoints"

# Paso 6
/sessions
# Mostrará ambas sesiones listadas

# Paso 7
/sessions "base de datos"
```

### Ejercicio 2: Configurar Proveedor y Modelo

**Objetivo:** Conectar un proveedor de IA y seleccionar el modelo adecuado.

**Instrucciones:**
1. Verifica el modelo actual con `/models current`
2. Conecta a Anthropic con `/connect anthropic`
3. Lista los modelos disponibles
4. Selecciona un modelo específico
5. Confirma el cambio con `/details`

**Solución Esperada:**
```bash
# Paso 1
/models current
# Muestra el modelo activo actual

# Paso 2
/connect anthropic

# Paso 3
/models
# Lista: claude-3-5-sonnet, claude-3-opus, etc.

# Paso 4
/models claude-3-5-sonnet

# Paso 5
/details
# Muestra el nuevo modelo configurado
```

### Ejercicio 3: Inicialización Profunda y Exportación

**Objetivo:** Configurar un proyecto existente y documentar el trabajo realizado.

**Instrucciones:**
1. Navega a un proyecto existente con código
2. Inicia OpenCode
3. Ejecuta `/init-deep` para análisis completo
4. Revisa los archivos generados en `.opencode/`
5. Pregunta sobre la arquitectura del proyecto
6. Exporta la conversación completa
7. Comparte el enlace

**Solución Esperada:**
```bash
# Paso 1-2
cd ~/proyecto-existente
opencode

# Paso 3
/init-deep

# Paso 4
ls .opencode/
# project-context.md
# config.json

# Paso 5
> ¿Cuál es la arquitectura general del proyecto?

# Paso 6
/export markdown

# Paso 7
/share
```

## Ejercicio Desafío

**Reto:** Crea un flujo de trabajo completo que incluya:
1. Crear 3 sesiones para diferentes tareas (diseño, desarrollo, testing)
2. Usar `/compact` en cada una después de trabajar
3. Exportar todas las sesiones a archivos separados
4. Usar `/undo` para revertir un cambio y luego `/redo`
5. Documentar todo el proceso con `/details`

**Pistas:**
- Usa temas descriptivos para cada sesión
- El formato markdown es ideal para documentación
- `/details` te da información sobre tokens y duración

## Recursos Adicionales

- [Documentación de comandos slash](https://opencode.ai/docs/commands)
- [Guía de gestión de sesiones](https://opencode.ai/docs/sessions)
- [Configuración de proveedores](https://opencode.ai/docs/providers)

## Autoevaluación

- [ ] Puedo crear y gestionar múltiples sesiones
- [ ] Sé conectar diferentes proveedores de IA
- [ ] Entiendo cómo inicializar un proyecto con /init-deep
- [ ] Puedo exportar conversaciones en diferentes formatos
- [ ] Utilizo /undo y /redo correctamente
- [ ] Conozco la función de cada comando slash disponible
