---
title: "Clase 39: Personalización de System Prompts"
module: 39
duration: "1 hora"
prerequisites: "Módulo 38 - Clase 38: Seguridad Avanzada"
---

# Clase 39: Personalización de System Prompts

## Resumen Ejecutivo

Esta clase cubre personalización de system prompts. Instrucciones de alto nivel que definen el comportamiento del agente Se envían en cada interacción con el modelo Determinan tono, estilo, restricciones y capacidades.

A lo largo de la sesión se exploran los siguientes temas: ¿qué son system prompts?, personalización en config, técnicas de prompt engineering, ejemplos prácticos. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Instrucciones de alto nivel que definen el comportamiento del agente
- Se envían en cada interacción con el modelo
- Determinan tono, estilo, restricciones y capacidades
- Diferentes de los user prompts (lo que escribes tú)
- Personalizarlos = mejores resultados específicos

## Conceptos Clave

### ¿Qué son System Prompts?

- Instrucciones de alto nivel que definen el comportamiento del agente
- Se envían en cada interacción con el modelo
- Determinan tono, estilo, restricciones y capacidades
- Diferentes de los user prompts (lo que escribes tú)
- Personalizarlos = mejores resultados específicos

### Personalización en Config

```bash
{
"agent": {
"default": {
"prompt": "You are an expert Go developer.
Always add tests for new code.
Prefer composition over inheritance."
}
}
}
```

- Campo prompt en definición de agente
- También en AGENTS.md para contexto de proyecto
- Array instructions para múltiples archivos

### Técnicas de Prompt Engineering

- **Role prompting:** "You are a senior React architect..."
- **Few-shot:** Incluir ejemplos de código deseado
- **Chain-of-thought:** Pedir razonamiento paso a paso
- **Constraints:** Limitar longitud, estilo, librerías
- **Output format:** Especificar formato de respuesta

### Ejemplos Prácticos

```bash
# Code reviewer
"You are a strict code reviewer. Flag any
security issues, performance bottlenecks,
and missing error handling."

# API designer
"Design RESTful APIs following OpenAPI 3.0.
Always include pagination and rate limits."
```

- Guardar prompts reutilizables como skills
- Iterar y refinar según resultados

## Guía Paso a Paso

### Paso 1: ¿Qué son System Prompts?

- Instrucciones de alto nivel que definen el comportamiento del agente
- Se envían en cada interacción con el modelo
- Determinan tono, estilo, restricciones y capacidades
- Diferentes de los user prompts (lo que escribes tú)
- Personalizarlos = mejores resultados específicos

### Paso 2: Personalización en Config

```bash
{
"agent": {
"default": {
"prompt": "You are an expert Go developer.
Always add tests for new code.
Prefer composition over inheritance."
}
}
}
```

- Campo prompt en definición de agente
- También en AGENTS.md para contexto de proyecto
- Array instructions para múltiples archivos

### Paso 3: Técnicas de Prompt Engineering

- **Role prompting:** "You are a senior React architect..."
- **Few-shot:** Incluir ejemplos de código deseado
- **Chain-of-thought:** Pedir razonamiento paso a paso
- **Constraints:** Limitar longitud, estilo, librerías
- **Output format:** Especificar formato de respuesta

### Paso 4: Ejemplos Prácticos

```bash
# Code reviewer
"You are a strict code reviewer. Flag any
security issues, performance bottlenecks,
and missing error handling."

# API designer
"Design RESTful APIs following OpenAPI 3.0.
Always include pagination and rate limits."
```

- Guardar prompts reutilizables como skills
- Iterar y refinar según resultados

## Referencia Rápida

| Comando | Descripción |
|---------|-------------|
| `security issues, performance bottlenecks,` | Ejemplo de ejemplos prácticos |
| `and missing error handling."` | Ejemplo de ejemplos prácticos |

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de ¿qué son system prompts? paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica personalización en config en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina técnicas de prompt engineering con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (¿qué son system prompts?, personalización en config, técnicas de prompt engineering). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/39-system-prompts.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/39-system-prompts.pptx`

## Autoevaluación

- [ ] Puedo explicar ¿qué son system prompts? sin consultar apuntes
- [ ] Puedo explicar personalización en config sin consultar apuntes
- [ ] Puedo explicar técnicas de prompt engineering sin consultar apuntes
- [ ] Puedo explicar ejemplos prácticos sin consultar apuntes
