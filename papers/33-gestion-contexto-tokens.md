---
title: "Clase 33: Gestión de Contexto y Tokens"
module: 33
duration: "1 hora"
prerequisites: "Módulo 32 - Clase 32: Modo Servidor y API"
---

# Clase 33: Gestión de Contexto y Tokens

> **Actualizado a OpenCode v2.** En v2 la compactación se configura en `opencode.jsonc` bajo la clave `compaction` (`auto`, `keep.tokens`, `buffer`) y existe la opción de compactación nativa del proveedor. Además, la API expone `POST /api/session/{id}/compact` y `GET /api/session/{id}/context`.

## Resumen Ejecutivo

Esta clase cubre cómo administrar la ventana de contexto de los modelos en sesiones largas: qué son los tokens, cuándo el historial de una conversación se vuelve un problema de costo y calidad, y qué herramientas ofrece OpenCode v2 para mantener el contexto saludable — compactación automática, compactación manual, límites de salida de herramientas y presupuestos de tokens retenidos.

A lo largo de la sesión se exploran los siguientes temas: los límites de contexto por modelo, la compactación automática y su configuración fina, la compactación manual con el comando `/compact` y la API, la selección de contenido relevante para el contexto, y estrategias de prevención para sesiones largas. Al finalizar, el estudiante podrá diseñar configuraciones que eviten la degradación de las respuestas sin desperdiciar presupuesto de tokens.

## Objetivos de Aprendizaje

- Entender qué es la ventana de contexto y por qué importa su gestión en sesiones largas.
- Configurar la compactación automática (`compaction.auto`, `keep`, `buffer`) en `opencode.jsonc`.
- Ejecutar compactación manual desde la TUI (`/compact`) y desde la API REST.
- Distinguir entre compactación local (resumen) y compactación nativa del proveedor.
- Aplicar límites de salida de herramientas y otras palancas para controlar el consumo de tokens.

## Conceptos Clave

### La ventana de contexto y sus límites

Cada modelo tiene un presupuesto fijo de tokens de entrada (contexto) y de salida. OpenCode conoce estos límites por modelo (`limit.context`, `limit.output` en la configuración de proveedores/modelos). Cuando una sesión crece —archivos leídos, salidas de comandos, historial de mensajes— el riesgo aumenta:

- **Costos crecientes**: se paga por todo el historial en cada llamada.
- **Degradación de calidad**: el modelo "pierde de vista" instrucciones tempranas.
- **Errores por truncamiento**: si el contexto excede el límite, la llamada falla.

```jsonc
// Ver/ajustar límites conocidos de un modelo en opencode.jsonc
{
  "providers": {
    "openai": {
      "models": {
        "gpt-6.1-sol-custom": {
          "modelID": "gpt-6.1-sol",
          "limit": { "context": 200000, "output": 32000 }
        }
      }
    }
  }
}
```

### Compactación automática

OpenCode v2 puede resumir el historial automáticamente antes de que el contexto se llene:

```jsonc
{
  "compaction": {
    "auto": true,               // compacta automáticamente
    "keep": {
      "tokens": 15000           // tokens recientes que siempre se conservan
    },
    "buffer": "15%"             // porcentaje de la ventana que se mantiene libre
  }
}
```

- `buffer` es la fracción de la ventana de contexto que se mantiene libre **antes** de que arranque la compactación automática.
- La compactación automática usa el presupuesto de entrada usable del modelo seleccionado.
- `compaction.auto: false` desactiva la compactación nueva sin descartar checkpoints ya instalados.
- La respuesta compactada aparece en el historial como un mensaje de tipo `compaction`.

### Compactación manual

```bash
# Desde la TUI
/compact

# Desde la API (útil en pipelines largos)
curl -X POST http://localhost:4096/api/session/<ID>/compact
```

La compactación vía API puede indicarse con *steering*: se programa justo antes de la siguiente llamada al modelo, adelantándose a mensajes encolados.

### Compactación local vs. nativa del proveedor

Por defecto OpenCode genera **resúmenes locales** del historial. Se puede optar por la **compactación nativa** del proveedor (cuando el modelo la soporta), tanto para compactación automática como manual:

```jsonc
{
  "providers": {
    "openai": {
      "settings": { "compaction": { "type": "native" } },
      "models": {
        "mi-modelo": { "settings": { "compaction": { "type": "summary" } } }
      }
    }
  }
}
```

La configuración a nivel modelo pisa la del proveedor. Los checkpoints del proveedor conservan los mensajes recientes del usuario dentro del mismo presupuesto `compaction.keep.tokens`.

### Selección de contexto: meter solo lo relevante

El contexto se gestiona también decidiendo qué entra:

- **Referencias con descripción** (`references` en config) para contexto de apoyo nombrado sin inflar el system prompt.
- **Límites de salida de herramientas**:

```jsonc
{
  "tool_output": {
    "max_lines": 2000,     // máximo de líneas retenidas por resultado de herramienta
    "max_bytes": 51200     // máximo de bytes retenidos
  }
}
```

- **Redimensionado de imágenes** antes de enviarlas al modelo (`media.image.auto_resize`, `max_width`, `max_height`, `max_base64_bytes`).

### Prevención: diseñar sesiones que no dependan del historial

- Divide el trabajo en sesiones por objetivo; usa `fork` para ramificar sin acumular.
- Mantén las instrucciones duraderas en `AGENTS.md` o en `instructions`, no en el chat.
- Cierra sesiones largas de exploración y abre una nueva con el resumen como punto de partida.

## Guía Paso a Paso

### Paso 1: Medir el problema

Crea una sesión y trabaja un rato; luego consulta el contexto activo:

```bash
curl -s http://localhost:4096/api/session/<ID>/context
```

Este endpoint devuelve los mensajes activos de la sesión (todo lo posterior a la última compactación). Observa cómo crece tras leer archivos grandes o salidas de comandos largos.

### Paso 2: Configurar la compactación automática

Añade a `opencode.jsonc` del proyecto:

```jsonc
{
  "compaction": {
    "auto": true,
    "keep": { "tokens": 15000 },
    "buffer": "15%"
  }
}
```

Reinicia el servidor (`opencode service start` no reinicia automáticamente tras actualizaciones) y repite el escenario del Paso 1.

### Paso 3: Compactación manual en acción

Trabaja hasta acumular historial considerable y ejecuta `/compact` en la TUI. Verifica en la API que aparece un mensaje de tipo `compaction` y que `/context` ahora devuelve menos mensajes.

### Paso 4: Afinar el consumo de herramientas

Configura `tool_output` y `media.image` según el tipo de proyecto (un proyecto con muchos logs necesita `max_lines` bajo; uno con diagramas necesita límites de imagen). Repite tareas pesadas (tests, builds) y compara el tamaño del contexto.

### Paso 5: Evaluar compactación nativa

Si tu proveedor la soporta, activa `compaction.type: "native"` para ese proveedor y compara: calidad del resumen, tokens consumidos y comportamiento de los checkpoints del proveedor. Documenta cuándo prefieres local vs. nativa.

## Referencia Rápida

| Comando / Config | Descripción | Ejemplo |
|------------------|-------------|---------|
| `/compact` | Compacta el historial de la sesión actual | `/compact` en la TUI |
| `compaction.auto` | Activa compactación automática | `"auto": true` |
| `compaction.keep.tokens` | Tokens recientes siempre conservados | `{ "tokens": 15000 }` |
| `compaction.buffer` | Fracción de ventana a mantener libre | `"15%"` |
| `POST /api/session/{id}/compact` | Compacta vía API | ver Paso 3 |
| `GET /api/session/{id}/context` | Mensajes activos tras la última compactación | — |
| `tool_output.max_lines` | Líneas máx. por salida de herramienta | `2000` |
| `tool_output.max_bytes` | Bytes máx. por salida de herramienta | `51200` |
| `media.image.max_base64_bytes` | Tope de imagen en base64 | `5242880` |

## Ejercicios Guiados

1. **Medición:** en una sesión de prueba, ejecuta varios comandos con salida larga y registra el tamaño del contexto con `/api/session/{id}/context` antes y después; calcula el crecimiento por herramienta.
2. **Configuración:** define una política de compactación para un proyecto real: elige `keep.tokens` y `buffer` justificando los números según el modelo y el tipo de tarea.
3. **Comparativa:** reproduce la misma tarea larga con compactación local y nativa (si está disponible) y compara resumen, costo y tiempo de respuesta.

## Ejercicio Desafío

Diseña un "protocolo de sesiones largas" para tu equipo: reglas de cuándo dividir sesiones, política de `compaction` por tipo de tarea (exploración vs. implementación vs. revisión), límites de `tool_output` recomendados y un script que, vía API, alerte cuando una sesión supere un umbral de tokens activos. Incluye evidencia de pruebas en 3 sesiones reales.

## Recursos Adicionales

- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (sección `compaction`, `tool_output`, `media`)
- [Referencia de la API del servidor](https://opencode.ai/docs/server) (endpoints `compact` y `context`)
- Presentación de la clase: `presentaciones/nuevas-clases/33-gestion-contexto-tokens.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/33-gestion-contexto-tokens.pptx`

## Autoevaluación

- [ ] Puedo explicar qué es la ventana de contexto y sus dos límites (entrada/salida).
- [ ] Sé configurar `compaction.auto`, `keep` y `buffer` en `opencode.jsonc`.
- [ ] Puedo compactar una sesión manualmente desde TUI y desde la API.
- [ ] Entiendo la diferencia entre compactación local y nativa del proveedor.
- [ ] Sé limitar la salida de herramientas para controlar tokens.
- [ ] Puedo diseñar una estrategia de prevención para sesiones largas.
