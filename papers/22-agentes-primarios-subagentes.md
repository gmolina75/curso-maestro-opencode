---
title: "Agentes Primarios y Subagentes"
module: 22
duration: "45 min"
prerequisites: "Módulo 21 - Fundamentos de Agentes"
---

# Clase 22: Agentes Primarios y Subagentes

## Resumen Ejecutivo

OpenCode utiliza una arquitectura de agentes jerárquica compuesta por agentes primarios y subagentes. Los agentes primarios son las sesiones de trabajo principales que el usuario utiliza directamente, mientras que los subagentes son sesiones secundarias invocadas automáticamente o manualmente para realizar tareas específicas en paralelo. Esta arquitectura permite ejecutar múltiples operaciones simultáneamente sin bloquear la interfaz principal, mejorando significativamente la productividad y el flujo de trabajo.

El sistema está diseñado para que el agente principal (build, por defecto) pueda delegar tareas a subagentes cuando detecta que una operación compleja puede dividirse en partes manejables. Los subagentes ejecutan sus tareas de forma independiente y reportan resultados al agente padre, permitiendo navegación entre sesiones para monitorear el progreso.

## Objetivos de Aprendizaje
- Diferenciar entre agentes primarios (build, plan) y sus roles específicos
- Dominar el sistema de subagentes y su ejecución en sesiones secundarias
- Configurar y controlar la profundidad de subagentes con `subagent_depth`
- Navegar eficientemente entre sesiones padre e hijos usando atajos de teclado
- Invocar subagentes manualmente mediante @mention

## Conceptos Clave

### Agentes Primarios

Los agentes primarios son el punto de entrada principal del usuario en OpenCode. Cada agente primario tiene un propósito definido y un conjunto de herramientas disponibles.

#### Agente Build (Por Defecto)
El agente build es el agente predeterminado para tareas de desarrollo de software. Está diseñado para:
- Leer, escribir y modificar archivos de código
- Ejecutar comandos en terminal
- Realizar búsquedas en el código fuente
- Gestionar repositorios Git
- Ejecutar pruebas y herramientas de linting

#### Agente Plan
El agente plan está diseñado para tareas de planificación y análisis. Es ideal para:
- Analizar estructuras de código existentes
- Diseñar arquitecturas y flujos de trabajo
- Generar documentación técnica
- Revisar y evaluar propuestas de cambio

### Cambio de Modo con Tab

El sistema permite alternar entre agentes primarios usando la tecla Tab o el keybind configurado como `switch_agent`. Esto es útil cuando se necesita cambiar el contexto de trabajo sin perder el progreso actual.

```
Tab → Cambia al siguiente agente primario disponible
```

La configuración del keybind se realiza en `opencode.json`:

```json
{
  "keybinds": {
    "switch_agent": "tab"
  }
}
```

### Subagentes: Ejecución en Sesiones Secundarias

Los subagentes son sesiones de trabajo derivadas del agente padre. Se crean cuando el agente primario necesita realizar una tarea que puede ejecutarse de forma independiente. Cada subagente:
- Tiene su propio contexto de conversación
- Ejecuta herramientas de forma autónoma
- Reporta resultados al agente padre
- Se ejecuta en segundo plano sin bloquear la interfaz

### Invocación Automática

El agente primario invoca subagentes automáticamente cuando detecta que una tarea compleja puede dividirse en subtareas paralelas. Por ejemplo, al recibir la instrucción "revisar todo el proyecto", el agente puede crear subagentes para analizar diferentes módulos simultáneamente.

### Invocación Manual con @mention

Los usuarios pueden invocar subagentes manualmente utilizando la sintaxis `@nombre-del-agente` en el chat. Esto es útil para tareas específicas que requieren un agente particular.

```
@build Crear una función de validación de email
@plan Analizar la arquitectura del módulo de autenticación
```

### Configuración de subagent_depth

El parámetro `subagent_depth` controla cuántos niveles de subagentes pueden crearse. Por defecto, el valor es 1, lo que significa que solo se permite un nivel de subagentes (los subagentes no pueden crear sus propios subagentes).

```json
{
  "agent": {
    "subagent_depth": 1
  }
}
```

Para permitir subagentes anidados (subagentes que crean sus propios subagentes), se puede incrementar este valor:

```json
{
  "agent": {
    "subagent_depth": 2
  }
}
```

### Navegación entre Sesiones

El sistema de navegación permite moverse entre sesiones padre e hijos de forma intuitiva:

| Atajo de Teclado | Acción |
|-------------------|--------|
| Leader + Down | Navegar a un subagente hijo |
| Leader + Right | Ciclar al siguiente subagente hermano |
| Leader + Left | Ciclar al subagente hermano anterior |
| Leader + Up | Volver al agente padre |

Estos atajos permiten monitorear el progreso de subagentes y proporcionar entrada adicional si es necesario.

## Guía Paso a Paso

### Paso 1: Configurar el Agente Primario

```json
// opencode.json
{
  "agent": {
    "primary": "build",
    "subagent_depth": 1
  },
  "keybinds": {
    "switch_agent": "tab"
  }
}
```

### Paso 2: Invocar un Subagente Manualmente

En el chat de OpenCode, escribe:

```
@build Revisar el archivo src/utils.ts y sugerir mejoras
```

El subagente se creará automáticamente y comenzará a ejecutar la tarea en una sesión secundaria.

### Paso 3: Navegar entre Sesiones

Usa los atajos de teclado para moverte entre sesiones:

```
Leader + Down  → Entrar al subagente hijo
Leader + Right → Ciclar al siguiente subagente
Leader + Up    → Volver al agente principal
```

### Paso 4: Monitorear el Progreso

Mientras el subagente ejecuta su tarea, puedes observar su progreso en la interfaz. Los subagentes muestran un indicador de estado (ejecutando, completado, error).

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `agent.primary` | Agente primario por defecto | `"build"` |
| `subagent_depth` | Profundidad máxima de subagentes | `1` |
| `switch_agent` | Keybind para cambiar de agente | `"tab"` |
| `@build` | Invocar agente build como subagente | `@build revisar código` |
| `@plan` | Invocar agente plan como subagente | `@plan diseñar arquitectura` |
| `Leader+Down` | Navegar a subagente hijo | Atajo de teclado |
| `Leader+Right` | Ciclar al siguiente subagente | Atajo de teclado |
| `Leader+Up` | Volver al agente padre | Atajo de teclado |

## Ejercicios Guiados

### Ejercicio 1: Usar el Agente Build por Defecto
**Objetivo:** Familiarizarse con el agente primario build y sus capacidades básicas.

**Instrucciones:**
1. Abre OpenCode en tu terminal
2. Verifica que el agente build esté activo (debería ser el predeterminado)
3. Solicita al agente que lea un archivo de tu proyecto
4. Observa cómo el agente utiliza las herramientas disponibles

**Solución Esperada:**
```
# En el chat de OpenCode:
Lee el archivo package.json y muéstrame sus dependencias

# Resultado esperado:
# El agente utiliza la herramienta Read para cargar package.json
# y presenta el contenido formateado
```

### Ejercicio 2: Invocar un Subagente con @mention
**Objetivo:** Aprender a invocar subagentes manualmente para tareas específicas.

**Instrucciones:**
1. En el chat de OpenCode, escribe una instrucción que incluya @build
2. Pide al subagente que realice una tarea específica
3. Observa cómo se crea la sesión secundaria
4. Verifica que el subagente ejecuta la tarea de forma independiente

**Solución Esperada:**
```
# En el chat:
@build Buscar todas las funciones que manejan errores en src/

# Resultado esperado:
# Se crea una sesión secundaria del agente build
# El subagente busca patrones de manejo de errores
# Los resultados se reportan al agente principal
```

### Ejercicio 3: Navegar entre Sesiones
**Objetivo:** Dominar la navegación entre sesiones padre e hijos.

**Instrucciones:**
1. Invoca al menos dos subagentes diferentes
2. Usa Leader + Down para entrar al primer subagente
3. Usa Leader + Right para ciclar al segundo subagente
4. Usa Leader + Up para volver al agente principal
5. Verifica que puedes moverte libremente entre sesiones

**Solución Esperada:**
```
# Flujo de navegación:
# 1. Invocar: @build revisar src/utils.ts
# 2. Invocar: @plan analizar arquitectura
# 3. Leader + Down → Entrar al subagente build
# 4. Leader + Right → Ciclar al subagente plan
# 5. Leader + Up → Volver al agente principal
```

## Ejercicio Desafío

**Reto:** Configura un sistema de subagentes para revisar un proyecto completo. Crea un subagente para analizar la estructura, otro para revisar la calidad del código, y un tercero para generar documentación. Configura `subagent_depth` para permitir que los subagentes puedan crear sus propios subagentes.

**Pistas:**
- Usa `subagent_depth: 2` para permitir anidación
- Cada subagente debe tener una tarea clara y delimitada
- Monitorea el progreso de todos los subagentes usando la navegación
- Verifica que los resultados se reporten correctamente al agente principal

## Recursos Adicionales
- [Documentación oficial de OpenCode - Agentes](https://opencode.ai/docs/agents)
- [Guía de configuración de agentes](https://opencode.ai/docs/configuration)
- [Referencia de atajos de teclado](https://opencode.ai/docs/keybinds)

## Autoevaluación
- [ ] Puedo identificar la diferencia entre agentes primarios y subagentes
- [ ] Sé invocar subagentes usando @mention
- [ ] Puedo navegar entre sesiones padre e hijos usando atajos de teclado
- [ ] Entiendo cómo funciona la invocación automática de subagentes
- [ ] Puedo configurar `subagent_depth` según las necesidades del proyecto
- [ ] Sé alternar entre agentes primarios usando Tab
