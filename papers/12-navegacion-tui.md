---
title: "Navegación en la Interfaz TUI"
module: 12
duration: "45 minutos"
prerequisites: "Módulo 11: Instalación y Primeros Pasos"
---

# Clase 12: Navegación en la Interfaz TUI

## Resumen Ejecutivo

La interfaz de usuario de terminal (TUI) de OpenCode es el entorno principal donde interactuarás con el asistente de código. Esta lección cubre cómo iniciar la aplicación, navegar entre modos de operación, utilizar la tecla líder para acceso rápido, y manejar referencias de archivos e imágenes dentro del chat.

OpenCode opera en dos modos principales: **Build** (para implementar cambios) y **Plan** (para analizar y planificar). La navegación eficiente entre estos modos es fundamental para un flujo de trabajo productivo. Dominar la TUI te permitirá trabajar de manera más rápida y efectiva, aprovechando todas las funcionalidades disponibles.

## Objetivos de Aprendizaje

- Iniciar OpenCode correctamente desde un directorio de proyecto
- Comprender la función de la tecla líder (Ctrl+X) y sus combinaciones
- Diferenciar y cambiar entre los modos Build y Plan
- Utilizar referencias de archivos con @ y arrastrar imágenes
- Navegar la interfaz de manera eficiente

## Conceptos Clave

### Iniciando OpenCode

OpenCode se ejecuta desde la línea de comandos dentro de tu directorio de proyecto. Es importante que estés en la raíz de tu repositorio para que la herramienta pueda analizar correctamente la estructura del código.

```bash
# Navega a tu directorio de proyecto
cd /ruta/a/tu/proyecto

# Inicia OpenCode
opencode
```

Al ejecutar el comando, OpenCode analizará tu proyecto y mostrará la interfaz TUI con el chat principal.

### La Tecla Líder (Leader Key)

La tecla líder es **Ctrl+X** por defecto. Funciona como un prefijo para acceder rápidamente a comandos y atajos de teclado. Al presionar Ctrl+X, entrarás en un modo temporal donde las siguientes teclas activarán acciones específicas.

**Flujo de uso:**
1. Presiona y suelta `Ctrl+X`
2. Observa el indicador en la parte inferior de la pantalla
3. Presiona la tecla de combinación deseada
4. La acción se ejecutará inmediatamente

### Modos de Operación

OpenCode tiene dos modos principales:

| Modo | Función | Acceso |
|------|---------|--------|
| **Build** | Implementar cambios en archivos | Predeterminado |
| **Plan** | Analizar código y proponer cambios sin modificar | Tab o Ctrl+X, p |

El modo **Build** permite todas las operaciones: leer, escribir, editar archivos y ejecutar comandos. El modo **Plan** es de solo lectura, ideal para explorar código unfamiliar o planificar cambios complejos.

### Referencias de Archivos con @

Puedes referenciar archivos específicos en tus mensajes usando el símbolo `@`. Esto permite que OpenCode cargue el contenido del archivo y lo tenga en cuenta al responder.

```markdown
# Ejemplos de referencias
@src/main.ts
@package.json
@README.md
```

Simplemente escribe `@` seguido de la ruta del archivo. OpenCode mostrará autocompletado mientras escribes.

### Imágenes y Arrastre

Soporta arrastrar imágenes directamente al chat para análisis visual. Esto es útil para diagramas de arquitectura, capturas de pantalla de errores, y diseños de UI.

## Guía Paso a Paso

### Paso 1: Iniciar OpenCode en tu Proyecto

```bash
# Navega a la raíz de tu proyecto
cd ~/mi-proyecto

# Verifica que estás en el lugar correcto
ls
# Deberías ver: package.json, src/, README.md, etc.

# Inicia OpenCode
opencode
```

La interfaz mostrará el nombre del proyecto en la parte superior, el historial de mensajes, la barra de entrada en la parte inferior, e indicadores de modo (Build/Plan).

### Paso 2: Explorar la Interfaz TUI

La pantalla de OpenCode tiene varias secciones:

```
+-------------------------------------+
|  [Proyecto] OpenCode - Build Mode   |  <- Barra de estado
+-------------------------------------+
|                                     |
|  [Area de chat]                     |  <- Mensajes y respuestas
|                                     |
+-------------------------------------+
|  > Escribe tu mensaje...            |  <- Barra de entrada
|  Ctrl+X: Leader | Tab: Cambiar modo |  <- Indicadores
+-------------------------------------+
```

### Paso 3: Cambiar entre Modos con Tab

```bash
# Presiona Tab para cambiar de Build a Plan
Tab

# La barra de estado cambiará a "Plan Mode"
# Ahora el asistente solo puede leer, no modificar

# Presiona Tab de nuevo para volver a Build
Tab
```

### Paso 4: Usar la Tecla Líder

```bash
# Presiona Ctrl+X para activar el modo líder
Ctrl+X

# Ahora presiona una tecla de comando:
# h = Ayuda
# p = Modo Plan
# b = Modo Build
# / = Comandos slash
```

### Paso 5: Referenciar un Archivo

```markdown
# En la barra de entrada, escribe:
Analiza el archivo @src/utils.ts y sugiere mejoras

# OpenCode cargará el contenido automáticamente
# y lo usará como contexto para su respuesta
```

## Referencia Rápida

| Comando/Acción | Descripción | Ejemplo |
|----------------|-------------|---------|
| `opencode` | Iniciar la TUI | `opencode` |
| `Ctrl+X` | Activar tecla líder | Leader mode ON |
| `Tab` | Cambiar modo Build/Plan | Build → Plan |
| `@ruta` | Referenciar archivo | `@src/main.ts` |
| `Ctrl+C` | Cancelar operación actual | Cancel generation |
| `Ctrl+L` | Limpiar pantalla | Clear terminal |
| `Esc` | Salir de menus/modos | Exit leader mode |
| `Enter` | Enviar mensaje | Submit message |

## Ejercicios Guiados

### Ejercicio 1: Lanzar y Explorar la TUI

**Objetivo:** Familiarizarse con la interfaz de OpenCode y sus componentes principales.

**Instrucciones:**
1. Abre una terminal en tu directorio de proyecto
2. Ejecuta `opencode`
3. Observa la barra de estado y nota el modo actual (Build o Plan)
4. Escribe un mensaje de prueba y envíalo
5. Observa la respuesta del asistente

**Solución Esperada:**
```bash
# Terminal 1
cd ~/mi-proyecto
opencode

# En el chat de OpenCode:
> Hola, ¿puedes mostrarme la estructura del proyecto?

# OpenCode responderá con un análisis del proyecto
```

### Ejercicio 2: Cambiar Modos y Usar la Tecla Líder

**Objetivo:** Practicar el cambio entre modos Build y Plan usando Tab y Ctrl+X.

**Instrucciones:**
1. Inicia OpenCode en modo Build (predeterminado)
2. Presiona Tab para cambiar a modo Plan
3. Observa el indicador de modo en la barra de estado
4. Presiona Ctrl+X y luego `h` para ver la ayuda
5. Presiona Ctrl+X y luego `b` para volver a Build
6. Confirma que el modo cambió correctamente

**Solución Esperada:**
```bash
# Paso 1: Modo Build activo (mostrado en barra de estado)
# Paso 2-3: Tab cambia a "Plan Mode"
# Paso 4: Ctrl+X → h muestra panel de ayuda
# Paso 5-6: Ctrl+X → b vuelve a "Build Mode"
```

### Ejercicio 3: Referenciar Archivos con @

**Objetivo:** Aprender a usar referencias de archivos para dar contexto al asistente.

**Instrucciones:**
1. Asegúrate de estar en modo Build
2. Escribe un mensaje que incluya una referencia a un archivo existente
3. Usa `@` y la ruta del archivo
4. Envía el mensaje y observa cómo OpenCode usa el contexto
5. Prueba referenciar múltiples archivos en un solo mensaje

**Solución Esperada:**
```markdown
# Ejemplo de mensaje con referencias
Revisa @src/components/Button.tsx y @src/styles/button.css
para asegurarte de que los estilos son consistentes

# OpenCode cargará ambos archivos y los analizará
```

## Ejercicio Desafío

**Reto:** Crea una secuencia de comandos que incluya:
1. Iniciar en modo Plan
2. Analizar 3 archivos específicos con @
3. Cambiar a modo Build
4. Implementar una corrección sugerida por el asistente
5. Verificar los cambios con un comando shell

**Pistas:**
- Usa Tab para cambiar entre modos
- Recuerda que en Plan no se pueden hacer modificaciones
- Usa Ctrl+X para accesos rápidos

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai)
- [Guía de configuración de la TUI](https://opencode.ai/docs/tui)
- [Lista de atajos de teclado](https://opencode.ai/docs/shortcuts)

## Autoevaluación

- [ ] Puedo iniciar OpenCode desde mi directorio de proyecto
- [ ] Entiendo la función de la tecla líder Ctrl+X
- [ ] Puedo cambiar entre modos Build y Plan con Tab
- [ ] Sé usar @ para referenciar archivos
- [ ] Conozco los atajos básicos de navegación
