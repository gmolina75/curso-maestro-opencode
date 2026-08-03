---
title: "Atajos de Teclado"
module: 14
duration: "40 minutos"
prerequisites: "Módulo 12: Navegación en la Interfaz TUI"
---

# Clase 14: Atajos de Teclado

## Resumen Ejecutivo

Los atajos de teclado son esenciales para trabajar eficientemente en OpenCode. La tecla líder **Ctrl+X** combina con otras teclas para ejecutar comandos rápidamente sin usar la línea de comandos. Este módulo cubre todos los atajos disponibles, cómo personalizarlos, y estrategias para maximizar tu productividad.

OpenCode utiliza un sistema de atajos inspirado en editores como Vim y Emacs. La tecla líder actúa como prefijo, permitiendo combinaciones de dos teclas para acciones complejas. Este diseño mantiene las teclas individuales libres para operaciones comunes mientras permite acceso rápido a funcionalidades avanzadas.

## Objetivos de Aprendizaje

- Dominar todas las combinaciones de tecla líder (Ctrl+X)
- Conocer los atajos de navegación y edición
- Personalizar atajos en la configuración tui.json
- Crear flujos de trabajo rápidos usando atajos
- Evitar conflictos entre atajos

## Conceptos Clave

### Sistema de Tecla Líder

La tecla líder **Ctrl+X** es el prefijo para todas las combinaciones. El flujo es:

1. Presiona `Ctrl+X` (suelta ambas teclas)
2. Presiona la tecla de combinación
3. La acción se ejecuta inmediatamente

```
Secuencia: Ctrl+X → h = Ayuda
           Ctrl+X → b = Modo Build
           Ctrl+X → p = Modo Plan
```

### Atajos Principales

| Combinación | Acción | Descripción |
|-------------|--------|-------------|
| `Ctrl+X, h` | Ayuda | Muestra panel de ayuda |
| `Ctrl+X, b` | Modo Build | Cambia a modo implementación |
| `Ctrl+X, p` | Modo Plan | Cambia a modo análisis |
| `Ctrl+X, /` | Comandos | Abre selector de comandos |
| `Ctrl+X, s` | Sesiones | Lista sesiones guardadas |
| `Ctrl+X, n` | Nueva sesión | Crea sesión limpia |
| `Ctrl+X, m` | Modelos | Cambia modelo activo |
| `Ctrl+X, t` | Temas | Cambia tema visual |
| `Ctrl+X, e` | Editor | Abre editor externo |
| `Ctrl+X, d` | Detalles | Info de sesión actual |

### Atajos de Navegación

| Tecla | Acción |
|-------|--------|
| `Tab` | Cambiar modo Build/Plan |
| `Shift+Tab` | Modo anterior |
| `Ctrl+C` | Cancelar operación |
| `Ctrl+L` | Limpiar pantalla |
| `Esc` | Salir de menús/modos |
| `Enter` | Enviar mensaje |
| `Ctrl+A` | Inicio de línea |
| `Ctrl+E` | Fin de línea |
| `Ctrl+K` | Borrar hasta fin |
| `Ctrl+U` | Borrar hasta inicio |

### Atajos de Edición

| Tecla | Acción |
|-------|--------|
| `Ctrl+W` | Borrar palabra |
| `Ctrl+R` | Buscar en historial |
| `Ctrl+S` | Buscar en sesiones |
| `Ctrl+N` | Siguiente sugerencia |
| `Ctrl+P` | Sugerencia anterior |

### Personalización de Atajos

Los atajos se personalizan en el archivo `tui.json`:

```json
{
  "keybindings": {
    "leader.h": "help",
    "leader.b": "mode.build",
    "leader.p": "mode.plan",
    "leader.s": "sessions.list",
    "ctrl+u": "input.clear_line",
    "ctrl+k": "input.delete_to_end"
  }
}
```

### Estructura del Archivo tui.json

```json
{
  "keybindings": {
    // Combinaciones con tecla líder
    "leader.{tecla}": "acción",
    
    // Atajos directos
    "ctrl+{letra}": "acción",
    
    // Atajos con Shift
    "shift+{tecla}": "acción",
    
    // Atajos con Alt
    "alt+{tecla}": "acción"
  },
  
  "leader_key": "ctrl+x",
  
  "options": {
    "timeout": 500,
    "show_leader_indicator": true
  }
}
```

## Guía Paso a Paso

### Paso 1: Dominar los Atajos Básicos

```bash
# 1. Cambiar modos rápidamente
Tab          # Build → Plan
Tab          # Plan → Build

# 2. Usar tecla líder para ayuda
Ctrl+X       # Activar líder
h            # Mostrar ayuda

# 3. Crear nueva sesión
Ctrl+X       # Activar líder
n            # Nueva sesión

# 4. Ver detalles de sesión
Ctrl+X       # Activar líder
d            # Detalles
```

### Paso 2: Navegar el Historial

```bash
# Buscar en comandos anteriores
Ctrl+R       # Modo búsqueda
_type_       # Escribe para filtrar
Enter        # Seleccionar resultado

# Navegar sugerencias
Ctrl+N       # Siguiente
Ctrl+P       # Anterior
```

### Paso 3: Editar Mensajes Eficientemente

```bash
# Escribiendo un mensaje largo...

# Ir al inicio de la línea
Ctrl+A

# Ir al final
Ctrl+E

# Borrar palabra anterior
Ctrl+W

# Borrar hasta final de línea
Ctrl+K

# Borrar toda la línea
Ctrl+U
```

### Paso 4: Configurar Atajos Personalizados

```bash
# Crea o edita tui.json
opencode
Ctrl+X       # Líder
/            # Comandos
edit-config  # Editar configuración

# O manualmente en .opencode/tui.json
```

```json
{
  "keybindings": {
    "leader.f": "files.recent",
    "leader.g": "git.status",
    "leader.r": "git.review",
    "ctrl+shift+f": "search.find",
    "ctrl+shift+g": "search.global"
  }
}
```

### Paso 5: Flujo de Trabajo con Atajos

```bash
# Ejemplo de flujo completo usando atajos:

# 1. Nueva sesión
Ctrl+X → n

# 2. Conectar proveedor
Ctrl+X → /
_type_: connect
Enter

# 3. Cambiar a modo Plan
Tab

# 4. Analizar archivo
_type_: @src/main.ts analiza esto
Enter

# 5. Cambiar a modo Build
Tab

# 6. Implementar cambios
_type_: implementa las mejoras sugeridas
Enter

# 7. Guardar y salir
Ctrl+X → s    # Ver sesiones
Ctrl+X → /    # Comando
_type_: exit
Enter
```

## Referencia Rápida

| Categoría | Atajo | Acción |
|-----------|-------|--------|
| **Modo** | `Tab` | Cambiar Build/Plan |
| **Líder** | `Ctrl+X → h` | Ayuda |
| **Líder** | `Ctrl+X → b` | Modo Build |
| **Líder** | `Ctrl+X → p` | Modo Plan |
| **Líder** | `Ctrl+X → n` | Nueva sesión |
| **Líder** | `Ctrl+X → s` | Lista sesiones |
| **Líder** | `Ctrl+X → m` | Cambiar modelo |
| **Líder** | `Ctrl+X → t` | Cambiar tema |
| **Líder** | `Ctrl+X → e` | Abrir editor |
| **Líder** | `Ctrl+X → d` | Detalles sesión |
| **Navegación** | `Ctrl+A` | Inicio línea |
| **Navegación** | `Ctrl+E` | Fin línea |
| **Navegación** | `Ctrl+R` | Buscar historial |
| **Edición** | `Ctrl+W` | Borrar palabra |
| **Edición** | `Ctrl+K` | Borrar hasta fin |
| **Edición** | `Ctrl+U` | Borrar línea |
| **Control** | `Ctrl+C` | Cancelar |
| **Control** | `Ctrl+L` | Limpiar pantalla |
| **Control** | `Esc` | Salir |

## Ejercicios Guiados

### Ejercicio 1: Práctica de Atajos Básicos

**Objetivo:** Internalizar los atajos más usados hasta que sean automáticos.

**Instrucciones:**
1. Inicia OpenCode
2. Practica cambiar de modo 10 veces con Tab
3. Usa Ctrl+X → h para ver la ayuda 5 veces
4. Crea 3 sesiones nuevas con Ctrl+X → n
5. Lista sesiones con Ctrl+X → s
6. Mide cuánto tiempo toma cada operación

**Solución Esperada:**
```bash
# Ejercicio: Cambio de modo (debería tomar <1 segundo)
Tab → Tab → Tab → Tab → Tab → Tab → Tab → Tab → Tab → Tab

# Ver ayuda
Ctrl+X → h
# (repite 5 veces)

# Crear sesiones
Ctrl+X → n
Ctrl+X → n
Ctrl+X → n

# Listar
Ctrl+X → s
```

### Ejercicio 2: Edición Eficiente de Mensajes

**Objetivo:** Dominar la edición de texto en la barra de entrada.

**Instrucciones:**
1. Escribe un mensaje largo (más de 100 caracteres)
2. Usa Ctrl+A para ir al inicio
3. Usa Ctrl+E para ir al final
4. Usa Ctrl+W para borrar las últimas 3 palabras
5. Usa Ctrl+K para borrar hasta el medio
6. Restaura el texto y envía el mensaje

**Solución Esperada:**
```bash
# Escribe tu mensaje largo
_type_: Este es un mensaje de prueba muy largo que usaremos para practicar los atajos de teclado en OpenCode de manera efectiva

# Navega
Ctrl+A    # Ve al inicio
Ctrl+E    # Ve al final

# Edita
Ctrl+W    # Borrar "efectiva"
Ctrl+W    # Borrar "de"
Ctrl+W    # Borrar "manera"

Ctrl+K    # Borrar hasta "prueba"

# Restaura y envía
Ctrl+U    # Borrar todo
_type_: Mensaje final corregido
Enter
```

### Ejercicio 3: Crear Atajos Personalizados

**Objetivo:** Configurar atajos personalizados en tui.json para tu flujo de trabajo.

**Instrucciones:**
1. Abre la configuración con Ctrl+X → / → edit-config
2. Agrega un atajo para archivos recientes
3. Agrega un atajo para estado de git
4. Agrega un atajo para buscar en el proyecto
5. Guarda y reinicia OpenCode
6. Prueba los nuevos atajos

**Solución Esperada:**
```json
{
  "keybindings": {
    "leader.f": "files.recent",
    "leader.g": "git.status",
    "ctrl+shift+f": "search.project",
    "leader.w": "workspace.save",
    "leader.q": "session.quit"
  }
}
```

```bash
# Prueba los nuevos atajos
Ctrl+X → f    # Archivos recientes
Ctrl+X → g    # Estado de git
Ctrl+Shift+F  # Buscar en proyecto
```

## Ejercicio Desafío

**Reto:** Crea un "maratón de atajos" donde:
1. Realiza una tarea completa usando SOLO atajos de teclado
2. La tarea: Analizar un archivo, sugerir mejoras, implementar una, y verificar
3. No puedes usar la barra de comandos `/`
4. Documenta cada paso con el atajo utilizado
5. Mide el tiempo total y compara con hacerlo sin atajos

**Pistas:**
- Usa Tab para cambiar modos
- Ctrl+X para acceso rápido
- Ctrl+R para buscar comandos anteriores
- Practica hasta que los atajos sean automáticos

## Recursos Adicionales

- [Tabla completa de atajos](https://opencode.ai/docs/keyboard-shortcuts)
- [Personalización de keybindings](https://opencode.ai/docs/tui#keybindings)
- [Guía de productividad](https://opencode.ai/docs/productivity)

## Autoevaluación

- [ ] Conozco las combinaciones principales de Ctrl+X
- [ ] Puedo cambiar entre modos sin usar la barra de comandos
- [ ] Edito mensajes eficientemente con Ctrl+A, Ctrl+E, Ctrl+W
- [ ] Sé buscar en el historial con Ctrl+R
- [ ] He personalizado al menos 3 atajos en tui.json
- [ ] Uso atajos de forma automática sin pensar
