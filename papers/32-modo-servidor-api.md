---
title: "Clase 32: Modo Servidor y API"
module: 32
duration: "1 hora"
prerequisites: "Módulo 31 - Clase 31: Troubleshooting y Recursos"
---

# Clase 32: Modo Servidor y API

## Resumen Ejecutivo

Esta clase cubre modo servidor y api. Modo headless para automatización y CI/CD Expone una API HTTP para integración con otros servicios Ideal para pipelines, scripts y herramientas externas.

A lo largo de la sesión se exploran los siguientes temas: ¿qué es el modo servidor?, iniciar el servidor, api endpoints principales, uso headless y ci/cd. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Modo headless para automatización y CI/CD
- Expone una API HTTP para integración con otros servicios
- Ideal para pipelines, scripts y herramientas externas
- Ejecuta tareas sin interfaz interactiva
- Compatible con todos los proveedores y modelos configurados

## Conceptos Clave

### ¿Qué es el Modo Servidor?

- Modo headless para automatización y CI/CD
- Expone una API HTTP para integración con otros servicios
- Ideal para pipelines, scripts y herramientas externas
- Ejecuta tareas sin interfaz interactiva
- Compatible con todos los proveedores y modelos configurados

### Iniciar el Servidor

```bash
# Iniciar servidor en puerto por defecto (4096)
opencode server

# Especificar puerto
opencode server --port 8080

# Modo background
opencode server --detach
```

- Configurar puerto en opencode.json bajo server.port
- El servidor usa la misma configuración que la TUI
- Soporta autenticación con API keys

### API Endpoints Principales

Contenido visual de la presentación (ver diapositiva `32-endpoints`).

### Uso Headless y CI/CD

```bash
# Ejecutar tarea desde script
opencode --headless --prompt "Refactor auth module"

# En GitHub Actions
opencode --headless --config ci-config.json
```

- Perfecto para automatización de pipelines
- Integración con cron jobs y schedulers
- Output en JSON para consumo programático
- Requiere configuración completa en archivo o variables

## Guía Paso a Paso

### Paso 1: ¿Qué es el Modo Servidor?

- Modo headless para automatización y CI/CD
- Expone una API HTTP para integración con otros servicios
- Ideal para pipelines, scripts y herramientas externas
- Ejecuta tareas sin interfaz interactiva
- Compatible con todos los proveedores y modelos configurados

### Paso 2: Iniciar el Servidor

```bash
# Iniciar servidor en puerto por defecto (4096)
opencode server

# Especificar puerto
opencode server --port 8080

# Modo background
opencode server --detach
```

- Configurar puerto en opencode.json bajo server.port
- El servidor usa la misma configuración que la TUI
- Soporta autenticación con API keys

### Paso 3: API Endpoints Principales

Revisar la diapositiva `32-endpoints` de la presentación.

### Paso 4: Uso Headless y CI/CD

```bash
# Ejecutar tarea desde script
opencode --headless --prompt "Refactor auth module"

# En GitHub Actions
opencode --headless --config ci-config.json
```

- Perfecto para automatización de pipelines
- Integración con cron jobs y schedulers
- Output en JSON para consumo programático
- Requiere configuración completa en archivo o variables

## Referencia Rápida

| Comando | Descripción |
|---------|-------------|
| `opencode server` | Ejemplo de iniciar el servidor |
| `opencode server --port 8080` | Ejemplo de iniciar el servidor |
| `opencode server --detach` | Ejemplo de iniciar el servidor |
| `opencode --headless --prompt "Refactor auth module"` | Ejemplo de uso headless y ci/cd |
| `opencode --headless --config ci-config.json` | Ejemplo de uso headless y ci/cd |

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de ¿qué es el modo servidor? paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica iniciar el servidor en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina api endpoints principales con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (¿qué es el modo servidor?, iniciar el servidor, api endpoints principales). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/32-modo-servidor-api.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/32-modo-servidor-api.pptx`

## Autoevaluación

- [ ] Puedo explicar ¿qué es el modo servidor? sin consultar apuntes
- [ ] Puedo explicar iniciar el servidor sin consultar apuntes
- [ ] Puedo explicar api endpoints principales sin consultar apuntes
- [ ] Puedo explicar uso headless y ci/cd sin consultar apuntes
