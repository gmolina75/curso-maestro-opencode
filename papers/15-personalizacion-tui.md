---
title: "Personalización de la TUI"
module: 15
duration: "45 minutos"
prerequisites: "Módulo 14: Atajos de Teclado"
---

# Clase 15: Personalización de la TUI

## Resumen Ejecutivo

La personalización de la interfaz de usuario de terminal (TUI) de OpenCode te permite adaptar la herramienta a tus preferencias y estilo de trabajo. El archivo `tui.json` es el centro de configuración donde puedes ajustar desde la velocidad de desplazamiento hasta los temas visuales, pasando por el soporte de ratón y las notificaciones.

Una TUI bien configurada mejora significativamente la productividad y reduce la fatiga visual durante sesiones largas de trabajo. OpenCode ofrece un equilibrio entre simplicidad y personalización, permitiendo configuraciones avanzadas sin abrumar al usuario principiante.

## Objetivos de Aprendizaje

- Localizar y editar el archivo tui.json
- Configurar parámetros de visualización (scroll, diff, temas)
- Habilitar y configurar soporte de ratón
- Personalizar notificaciones y atención
- Optimizar la TUI para diferentes flujos de trabajo

## Conceptos Clave

### Ubicación del Archivo tui.json

El archivo de configuración de la TUI se encuentra en:

```bash
# Linux/macOS
~/.config/opencode/tui.json

# Windows
%APPDATA%\opencode\tui.json

# O en el proyecto (local)
.opencode/tui.json
```

La configuración global afecta todas las sesiones. La configuración local del proyecto sobreescribe la global para ese proyecto específico.

### Estructura Completa del tui.json

```json
{
  "scroll_speed": 3,
  "scroll_acceleration": true,
  "diff_style": "unified",
  "mouse_support": true,
  "attention": {
    "notifications": true,
    "sounds": false,
    "visual_bell": true
  },
  "theme": "dark",
  "font_size": 14,
  "show_line_numbers": true,
  "word_wrap": true,
  "keybindings": {},
  "layout": {
    "sidebar_width": 30,
    "chat_height": "70%",
    "show_status_bar": true
  }
}
```

### Parámetros de Desplazamiento

```json
{
  "scroll_speed": 3,
  "scroll_acceleration": true
}
```

- **scroll_speed**: Velocidad base de desplazamiento (1-10). Valor mayor = más rápido.
- **scroll_acceleration**: Si es `true`, mantener presionado aumenta la velocidad progresivamente.

### Estilos de Diff

```json
{
  "diff_style": "unified"
}
```

Opciones disponibles:
- `"unified"`: Formato unificado (predeterminado). Muestra cambios con + y -
- `"side-by-side"`: Lado a lado. Compara original vs modificado
- `"inline"`: En línea. Muestra todo en un solo bloque

### Soporte de Ratón

```json
{
  "mouse_support": true
}
```

Cuando está habilitado:
- Click en mensajes para seleccionar
- Scroll para navegar el historial
- Click en enlaces para abrir
- Selección de texto con click y arrastrar

### Sistema de Atención (Notificaciones)

```json
{
  "attention": {
    "notifications": true,
    "sounds": false,
    "visual_bell": true
  }
}
```

- **notifications**: Notificaciones del sistema operativo
- **sounds**: Sonidos al completar tareas
- **visual_bell**: Flash visual en la terminal

### Selección de Tema

```json
{
  "theme": "dark"
}
```

Temas disponibles:
- `"dark"`: Tema oscuro (predeterminado)
- `"light"`: Tema claro
- `"high-contrast"`: Alto contraste para accesibilidad
- `"monokai"`: Estilo Monokai
- `"dracula"`: Estilo Dracula
- `"solarized-dark"`: Solarized oscuro
- `"solarized-light"`: Solarized claro

### Configuración de Fuentes

```json
{
  "font_size": 14,
  "font_family": "JetBrains Mono",
  "line_height": 1.5
}
```

### Diseño de Pantalla

```json
{
  "layout": {
    "sidebar_width": 30,
    "chat_height": "70%",
    "show_status_bar": true,
    "show_input_area": true,
    "compact_mode": false
  }
}
```

## Guía Paso a Paso

### Paso 1: Localizar y Abrir tui.json

```bash
# Verifica si existe configuración global
ls ~/.config/opencode/tui.json

# Si no existe, créalo
mkdir -p ~/.config/opencode
touch ~/.config/opencode/tui.json

# O usa el comando de OpenCode para abrirlo
opencode
Ctrl+X → /     # Selector de comandos
_type_: config
Enter
```

### Paso 2: Configurar Desplazamiento

```json
{
  "scroll_speed": 5,
  "scroll_acceleration": true
}
```

```bash
# Prueba los cambios
# Usa la rueda del ratón o flechas para desplazar
# Mantén presionado para aceleración
```

### Paso 3: Elegir Estilo de Diff

```json
{
  "diff_style": "side-by-side"
}
```

```bash
# Ahora cuando OpenCode muestre cambios:
# Los verás en formato lado a lado
# Original a la izquierda, modificaciones a la derecha
```

### Paso 4: Configurar Notificaciones

```json
{
  "attention": {
    "notifications": true,
    "sounds": true,
    "visual_bell": true
  }
}
```

```bash
# Las notificaciones aparecerán:
# - Al completar una tarea larga
# - Cuando el asistente termine de procesar
# - En errores importantes
```

### Paso 5: Seleccionar Tema

```json
{
  "theme": "solarized-dark",
  "font_size": 13
}
```

```bash
# Los cambios se aplican inmediatamente
# Puedes cambiar en tiempo real con:
Ctrl+X → t    # Selector de temas
```

### Paso 6: Configuración Completa de Ejemplo

```json
{
  "scroll_speed": 4,
  "scroll_acceleration": true,
  "diff_style": "unified",
  "mouse_support": true,
  "attention": {
    "notifications": true,
    "sounds": false,
    "visual_bell": true
  },
  "theme": "dark",
  "font_size": 14,
  "show_line_numbers": true,
  "word_wrap": true,
  "layout": {
    "sidebar_width": 35,
    "chat_height": "75%",
    "show_status_bar": true,
    "compact_mode": false
  },
  "keybindings": {
    "leader.f": "files.recent",
    "leader.g": "git.status"
  }
}
```

## Referencia Rápida

| Parámetro | Tipo | Valores | Descripción |
|-----------|------|---------|-------------|
| `scroll_speed` | number | 1-10 | Velocidad de desplazamiento |
| `scroll_acceleration` | boolean | true/false | Aceleración al mantener |
| `diff_style` | string | unified, side-by-side, inline | Formato de diferencias |
| `mouse_support` | boolean | true/false | Soporte de ratón |
| `attention.notifications` | boolean | true/false | Notificaciones sistema |
| `attention.sounds` | boolean | true/false | Sonidos |
| `attention.visual_bell` | boolean | true/false | Flash visual |
| `theme` | string | dark, light, etc. | Tema visual |
| `font_size` | number | 10-24 | Tamaño de fuente |
| `word_wrap` | boolean | true/false | Ajuste de línea |
| `layout.sidebar_width` | number | 20-50 | Ancho del sidebar |
| `layout.compact_mode` | boolean | true/false | Modo compacto |

## Ejercicios Guiados

### Ejercicio 1: Configurar TUI para Productividad

**Objetivo:** Optimizar la interfaz para sesiones largas de trabajo.

**Instrucciones:**
1. Abre tui.json
2. Configura scroll_speed a 6 para navegar rápido
3. Habilita scroll_acceleration
4. Cambia diff_style a "side-by-side" para ver cambios claros
5. Configura notificaciones para saber cuándo tareas terminan
6. Elige un tema oscuro que sea cómodo para tus ojos
7. Guarda y reinicia OpenCode

**Solución Esperada:**
```json
{
  "scroll_speed": 6,
  "scroll_acceleration": true,
  "diff_style": "side-by-side",
  "mouse_support": true,
  "attention": {
    "notifications": true,
    "sounds": false,
    "visual_bell": true
  },
  "theme": "solarized-dark"
}
```

### Ejercicio 2: Personalizar Layout y Fuentes

**Objetivo:** Adaptar la pantalla a tu monitor y preferencias visuales.

**Instrucciones:**
1. Mide el ancho de tu terminal
2. Configura sidebar_width al 25% de tu ancho
3. Ajusta font_size según tu monitor
4. Habilita line_numbers si programas frecuentemente
5. Configura word_wrap para mensajes largos
6. Prueba compact_mode para más espacio

**Solución Esperada:**
```json
{
  "font_size": 14,
  "show_line_numbers": true,
  "word_wrap": true,
  "layout": {
    "sidebar_width": 40,
    "chat_height": "80%",
    "show_status_bar": true,
    "compact_mode": true
  }
}
```

### Ejercicio 3: Crear Configuración por Proyecto

**Objetivo:** Configuraciones diferentes para diferentes tipos de proyecto.

**Instrucciones:**
1. Para un proyecto de frontend: usa tema claro, fuente grande
2. Para un proyecto de backend: usa tema oscuro, diff unificado
3. Para un proyecto de datos: usa alto contraste, scroll rápido
4. Guarda cada configuración en `.opencode/tui.json` de cada proyecto

**Solución - Proyecto Frontend:**
```json
{
  "theme": "light",
  "font_size": 16,
  "diff_style": "side-by-side"
}
```

**Solución - Proyecto Backend:**
```json
{
  "theme": "dark",
  "font_size": 13,
  "diff_style": "unified"
}
```

**Solución - Proyecto Datos:**
```json
{
  "theme": "high-contrast",
  "scroll_speed": 8,
  "diff_style": "inline"
}
```

## Ejercicio Desafío

**Reto:** Crea un "tema personalizado" completo:
1. Diseña un esquema de colores coherente
2. Configura todos los parámetros de layout
3. Crea 5+ atajos de teclado personalizados
4. Documenta cada decisión de diseño
5. Comparte tu configuración con un compañero
6. Prueba su configuración y compara experiencia

**Pistas:**
- Usa colores con buen contraste para accesibilidad
- Piensa en tu flujo de trabajo específico
- Los atajos deben ser fáciles de recordar
- Documenta TODO para mantenimiento futuro

## Recursos Adicionales

- [Referencia completa de tui.json](https://opencode.ai/docs/tui-config)
- [Galería de temas](https://opencode.ai/docs/themes)
- [Guía de accesibilidad](https://opencode.ai/docs/accessibility)

## Autoevaluación

- [ ] Puedo localizar y editar tui.json
- [ ] Entiendo la función de cada parámetro
- [ ] He configurado scroll_speed y acceleration
- [ ] He cambiado el estilo de diff
- [ ] He personalizado las notificaciones
- [ ] He seleccionado un tema adecuado
- [ ] He configurado el layout de pantalla
