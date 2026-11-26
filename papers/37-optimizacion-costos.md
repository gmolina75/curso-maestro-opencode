---
title: "Clase 37: Optimización de Costos"
module: 37
duration: "1 hora"
prerequisites: "Módulo 36 - Clase 36: Desktop App"
---

# Clase 37: Optimización de Costos

> **Actualizado a OpenCode v2.** En v2 las palancas de costo son: selección de modelo por agente (`model` con variantes `#high`/`#low`), configuración de límites por modelo (`limit.context/output`), caché con `warming` y `cache.ttl`, compactación (`compaction.keep.tokens`, `buffer`), límites de salida de herramientas (`tool_output`) y medición real vía `GET /api/experimental/session/stats`.

## Resumen Ejecutivo

Esta clase cubre cómo controlar el gasto en modelos sin sacrificar calidad: dónde se gastan los tokens en un flujo de trabajo con OpenCode (historial, salidas de herramientas, imágenes, subagentes), qué configuraciones permiten ajustar el consumo y cómo medir el resultado para iterar. La idea central es que el costo es un diseño, no un accidente: se decide con configuración y se verifica con datos.

A lo largo de la sesión se exploran los siguientes temas: comprensión del gasto de tokens, selección de modelos y variantes, caché y warming, optimización del contexto (compactación y salidas de herramientas), y monitoreo del consumo real. Al finalizar, el estudiante podrá construir un presupuesto de tokens concreto para su equipo y verificarlo semanalmente.

## Objetivos de Aprendizaje

- Identificar los principales focos de gasto de tokens en sesiones con OpenCode.
- Asignar modelos por agente y usar variantes (`#high`, `#low`) según la criticidad de la tarea.
- Configurar caché (`warming`, `cache.ttl`) para reducir llamadas repetidas y latencia.
- Aplicar límites de contexto (`tool_output`, `media.image`, `compaction`) para reducir tokens por llamada.
- Medir el consumo real con el endpoint de estadísticas de sesiones.

## Conceptos Clave

### Dónde se gasta el dinero

| Foco | Qué pasa | Palanca |
|------|----------|---------|
| Historial de sesión | Cada llamada reenvía todo el historial | `compaction` (ver Clase 33) |
| Salidas de herramientas | Un `cat` de log de 5k líneas entra completo al contexto | `tool_output.max_lines/max_bytes` |
| Imágenes | Screenshots grandes en base64 | `media.image.max_*` |
| Subagentes | Cada uno con contexto fresco puede duplicar trabajo | `subagent_depth`, diseño de tareas |
| Llamadas repetidas | Re-lecturas del mismo archivo en la sesión | Caché (`warming`, `cache.ttl`) |
| Modelo mal elegido | Modelo caro para tareas triviales | `model` por agente, variantes |

### Selección de modelos y variantes

Formato de referencia: `proveedor/modelo` con variante opcional `#variante`:

```jsonc
{
  "model": "anthropic/claude-sonnet-5-5",
  "agents": {
    "reviewer": {
      "description": "Reviews changes for correctness",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-5-5#high"   // variante de razonamiento alto
    },
    "explorador": {
      "description": "Searches and reads code",
      "mode": "subagent",
      "model": "openai/gpt-6.1-nano"                 // modelo barato para lectura
    }
  }
}
```

Estrategia típica: modelo principal potente para el agente `build`, modelos económicos para exploración y tareas mecánicas, y variantes altas solo donde el razonamiento profundo paga (arquitectura, debugging complejo).

### Caché y warming

Los proveedores con caché de prompts permiten pagar solo por los tokens **nuevos**. OpenCode puede mantener la caché caliente:

```jsonc
{
  "warming": {
    "prompt": "Do not perform any work. Reply with exactly: OK",
    "interval": "auto",          // justo antes de que expire la caché
    "duration": "30 minutes"     // hasta 30 min de calentamiento
  }
}
```

- El warming está **desactivado por defecto**; cada petición de calentamiento consume tokens, así que evalúa costo/beneficio.
- `providers.<id>.settings.cache.ttl` define cuánto mantiene el proveedor la caché; `settings.cache.warming` puede anular el global por proveedor/modelo.

### Optimización del contexto (recordatorio operativo)

```jsonc
{
  "tool_output": { "max_lines": 1000, "max_bytes": 25600 },
  "media": { "image": { "auto_resize": true, "max_width": 2000, "max_height": 2000, "max_base64_bytes": 5242880 } },
  "compaction": { "auto": true, "keep": { "tokens": 10000 }, "buffer": "20%" }
}
```

- Menos tokens por llamada = menos costo **y** menos riesgo de truncamiento.
- `buffer` mayor (p. ej. `"20%"`) compacta antes: cuesta una llamada de resumen pero evita llamadas infladas.

### Medición real

```bash
# Estadísticas agregadas de sesiones: actividad, uso y fiabilidad de herramientas
curl -s "http://localhost:4096/api/experimental/session/stats?from=<ms>&tools=detail" | jq .
```

El endpoint (experimental) agrupa actividad por día según zona horaria y reporta tokens y costo. Úsalo para responder: ¿qué sesiones consumen más? ¿qué herramientas devuelven más tokens? ¿en qué horario se concentra el gasto?

## Guía Paso a Paso

### Paso 1: Línea base

Antes de optimizar, mide: durante 2–3 días de trabajo normal, consulta `/api/experimental/session/stats` y anota tokens por sesión y por herramienta. Identifica los 2 mayores focos de gasto.

### Paso 2: Modelos por agente

Define una matriz de modelos: `build` (principal), `plan` (razonamiento medio), `explore` (económico), `reviewer` (medio-alto con `#high` si lo necesita). Implementa la mitad en `opencode.jsonc` y compara costo/resultado contra la línea base.

### Paso 3: Límites de contexto

Ajusta `tool_output`, `media.image` y `compaction` según el proyecto (uno con logs enormes vs. uno con capturas de UI). Mide el cambio en tokens por llamada con el diff de contexto (`GET /api/session/{id}/context` antes/después de una tarea estándar).

### Paso 4: Caché y warming

Habilita `warming` para tu sesión principal de trabajo si usas un proveedor con caché; define `cache.ttl` coherente con tu ritmo de trabajo. Mide si el ahorro en tokens nuevos supera el costo del calentamiento.

### Paso 5: Presupuesto y alertas

Establece un presupuesto semanal por proyecto. Escribe un script que consulte `/stats` y alerte al superar el 80% del presupuesto. Documenta decisiones: qué se ajustó, cuánto se ahorró y qué calidad se mantuvo.

## Referencia Rápida

| Config / Endpoint | Descripción | Ejemplo |
|-------------------|-------------|---------|
| `model` (raíz o agente) | Modelo por defecto o por agente | `"anthropic/claude-sonnet-5-5"` |
| Variante `#high` / `#low` | Nivel de razonamiento del modelo | `"...#high"` |
| `warming` | Mantiene la caché del proveedor caliente | `interval: "auto"` |
| `cache.ttl` | Vida de la caché por proveedor | `settings.cache.ttl` |
| `tool_output.max_lines` | Tope de líneas por herramienta | `1000` |
| `compaction.keep.tokens` | Tokens recientes conservados | `10000` |
| `GET /api/experimental/session/stats` | Uso y costo por rango de fechas | `?tools=detail` |
| `experimental.subagent_depth` | Límite de anidación de subagentes | `1` (default) |

## Ejercicios Guiados

1. **Auditoría:** identifica las 3 sesiones que más consumieron esta semana con `/api/experimental/session/stats` y propone una medida concreta para cada una.
2. **Modelos por tarea:** configura al menos dos agentes con modelos distintos (uno económico, uno potente) y ejecuta la misma tarea con ambos; compara costo, tiempo y calidad.
3. **Límites:** reproduce una tarea que lea archivos/logs grandes con y sin `tool_output` reducido; calcula el ahorro porcentual de tokens.

## Ejercicio Desafío

Construye el "tablero de costos" de tu equipo: presupuesto mensual por proyecto, medición semanal automática con `/stats`, alerta al 80%, y un informe que relacione gasto con entregables (features completadas, bugs resueltos). Presenta un caso de ajuste real donde bajaste el costo ≥ 30% sin perder calidad medible.

## Recursos Adicionales

- [Documentación oficial de OpenCode — Configuración](https://opencode.ai/docs/config) (`providers`, `warming`, `compaction`, `tool_output`, `media`)
- [Documentación oficial de OpenCode — Agentes](https://opencode.ai/docs/agents) (`model`, variantes, `subagent`)
- Presentación de la clase: `presentaciones/nuevas-clases/37-optimizacion-costos.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/37-optimizacion-costos.pptx`

## Autoevaluación

- [ ] Puedo enumerar los 5 focos principales de gasto de tokens.
- [ ] Sé asignar modelos y variantes por agente.
- [ ] Puedo explicar qué es el warming y cuándo conviene activarlo.
- [ ] Sé ajustar `tool_output`, `media.image` y `compaction` para reducir tokens por llamada.
- [ ] Puedo medir el consumo real con `/api/experimental/session/stats`.
- [ ] Tengo un método para verificar que la optimización no degrada la calidad.
