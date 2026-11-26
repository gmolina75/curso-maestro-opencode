---
title: "Clase 33: Gestión de Contexto y Tokens"
module: 33
duration: "1.5 horas"
prerequisites: "Módulo 32 - Clase 32: Modo Servidor y API"
---

# Clase 33: Gestión de Contexto y Tokens

## Resumen Ejecutivo

Esta clase cubre gestión de contexto y tokens. Cantidad máxima de tokens que un modelo puede procesar Incluye: system prompt, historial de mensajes, archivos referenciados Si se excede, el modelo pierde información del inicio.

A lo largo de la sesión se exploran los siguientes temas: ¿qué es la ventana de contexto?, límites de contexto por proveedor, estrategias de compactación, selección de modelos por tarea. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Cantidad máxima de tokens que un modelo puede procesar
- Incluye: system prompt, historial de mensajes, archivos referenciados
- Si se excede, el modelo pierde información del inicio
- OpenCode muestra el conteo de tokens en la barra de estado
- Gestionar el contexto = mejores respuestas y menor costo

## Conceptos Clave

### ¿Qué es la Ventana de Contexto?

- Cantidad máxima de tokens que un modelo puede procesar
- Incluye: system prompt, historial de mensajes, archivos referenciados
- Si se excede, el modelo pierde información del inicio
- OpenCode muestra el conteo de tokens en la barra de estado
- Gestionar el contexto = mejores respuestas y menor costo

### Límites de Contexto por Proveedor

Contenido visual de la presentación (ver diapositiva `33-limites`).

### Estrategias de Compactación

- /compact o /summarize: Resume el historial manteniendo esencia
- Referenciar solo archivos necesarios con @archivo
- Dividir tareas grandes en sesiones separadas
- Usar small_model para tareas menores y ahorrar tokens
- Configurar num_ctx en modelos locales (Ollama)

### Selección de Modelos por Tarea

- **Refactoring complejo:** Claude Opus o GPT-4o
- **Bug fixes simples:** Sonnet / Haiku (más rápido, más barato)
- **Generación de tests:** Qwen-Coder, DeepSeek-Coder
- **Explicaciones / docs:** Cualquier modelo con buen contexto
- **CI/CD headless:** Modelo rápido y económico

## Guía Paso a Paso

### Paso 1: ¿Qué es la Ventana de Contexto?

- Cantidad máxima de tokens que un modelo puede procesar
- Incluye: system prompt, historial de mensajes, archivos referenciados
- Si se excede, el modelo pierde información del inicio
- OpenCode muestra el conteo de tokens en la barra de estado
- Gestionar el contexto = mejores respuestas y menor costo

### Paso 2: Límites de Contexto por Proveedor

Revisar la diapositiva `33-limites` de la presentación.

### Paso 3: Estrategias de Compactación

- /compact o /summarize: Resume el historial manteniendo esencia
- Referenciar solo archivos necesarios con @archivo
- Dividir tareas grandes en sesiones separadas
- Usar small_model para tareas menores y ahorrar tokens
- Configurar num_ctx en modelos locales (Ollama)

### Paso 4: Selección de Modelos por Tarea

- **Refactoring complejo:** Claude Opus o GPT-4o
- **Bug fixes simples:** Sonnet / Haiku (más rápido, más barato)
- **Generación de tests:** Qwen-Coder, DeepSeek-Coder
- **Explicaciones / docs:** Cualquier modelo con buen contexto
- **CI/CD headless:** Modelo rápido y económico

## Referencia Rápida

_Esta clase no introduce comandos nuevos; se trabaja sobre configuración y buenas prácticas._

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de ¿qué es la ventana de contexto? paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica límites de contexto por proveedor en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina estrategias de compactación con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (¿qué es la ventana de contexto?, límites de contexto por proveedor, estrategias de compactación). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/33-gestion-contexto-tokens.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/33-gestion-contexto-tokens.pptx`

## Autoevaluación

- [ ] Puedo explicar ¿qué es la ventana de contexto? sin consultar apuntes
- [ ] Puedo explicar límites de contexto por proveedor sin consultar apuntes
- [ ] Puedo explicar estrategias de compactación sin consultar apuntes
- [ ] Puedo explicar selección de modelos por tarea sin consultar apuntes
