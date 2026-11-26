---
title: "Clase 35: Multi-sesión y Trabajo Paralelo"
module: 35
duration: "1 hora"
prerequisites: "Módulo 34 - Clase 34: Flujo de Trabajo con Git"
---

# Clase 35: Multi-sesión y Trabajo Paralelo

## Resumen Ejecutivo

Esta clase cubre multi-sesión y trabajo paralelo. Capacidad de abrir múltiples sesiones de trabajo simultáneas Cada sesión tiene su propio contexto y historial Ideal para trabajar en diferentes partes del proyecto.

A lo largo de la sesión se exploran los siguientes temas: ¿qué es multi-sesión?, crear y gestionar sesiones, trabajo en paralelo, casos de uso. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Capacidad de abrir múltiples sesiones de trabajo simultáneas
- Cada sesión tiene su propio contexto y historial
- Ideal para trabajar en diferentes partes del proyecto
- Sesiones child para tareas especializadas (subagentes)
- Disponible en TUI y Desktop App

## Conceptos Clave

### ¿Qué es Multi-sesión?

- Capacidad de abrir múltiples sesiones de trabajo simultáneas
- Cada sesión tiene su propio contexto y historial
- Ideal para trabajar en diferentes partes del proyecto
- Sesiones child para tareas especializadas (subagentes)
- Disponible en TUI y Desktop App

### Crear y Gestionar Sesiones

```bash
# Nueva sesión
/new    o    Ctrl+X N

# Listar sesiones
/sessions    o    Ctrl+X L

# Reanudar sesión anterior
/resume <session-id>
```

- Cada sesión se guarda automáticamente
- Persisten entre reinicios de OpenCode
- Nombrar sesiones ayuda a identificarlas
- Exportar sesión: /export

### Trabajo en Paralelo

- Sesión A: Refactor del backend API
- Sesión B: Implementación de tests unitarios
- Sesión C: Revisión de seguridad con agente custom
- Cambiar entre sesiones sin perder contexto
- Child sessions para tareas profundas con @mention

### Casos de Uso

- **Microservicios:** Una sesión por servicio
- **Frontend + Backend:** Trabajar ambos en paralelo
- **Bug fixes urgentes:** Nueva sesión sin perder el feature actual
- **Code review:** Sesión dedicada a revisar PR de compañero
- **Investigación:** Explorar librería nueva sin contaminar sesión principal

## Guía Paso a Paso

### Paso 1: ¿Qué es Multi-sesión?

- Capacidad de abrir múltiples sesiones de trabajo simultáneas
- Cada sesión tiene su propio contexto y historial
- Ideal para trabajar en diferentes partes del proyecto
- Sesiones child para tareas especializadas (subagentes)
- Disponible en TUI y Desktop App

### Paso 2: Crear y Gestionar Sesiones

```bash
# Nueva sesión
/new    o    Ctrl+X N

# Listar sesiones
/sessions    o    Ctrl+X L

# Reanudar sesión anterior
/resume <session-id>
```

- Cada sesión se guarda automáticamente
- Persisten entre reinicios de OpenCode
- Nombrar sesiones ayuda a identificarlas
- Exportar sesión: /export

### Paso 3: Trabajo en Paralelo

- Sesión A: Refactor del backend API
- Sesión B: Implementación de tests unitarios
- Sesión C: Revisión de seguridad con agente custom
- Cambiar entre sesiones sin perder contexto
- Child sessions para tareas profundas con @mention

### Paso 4: Casos de Uso

- **Microservicios:** Una sesión por servicio
- **Frontend + Backend:** Trabajar ambos en paralelo
- **Bug fixes urgentes:** Nueva sesión sin perder el feature actual
- **Code review:** Sesión dedicada a revisar PR de compañero
- **Investigación:** Explorar librería nueva sin contaminar sesión principal

## Referencia Rápida

_Esta clase no introduce comandos nuevos; se trabaja sobre configuración y buenas prácticas._

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de ¿qué es multi-sesión? paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica crear y gestionar sesiones en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina trabajo en paralelo con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (¿qué es multi-sesión?, crear y gestionar sesiones, trabajo en paralelo). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/35-multi-sesion.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/35-multi-sesion.pptx`

## Autoevaluación

- [ ] Puedo explicar ¿qué es multi-sesión? sin consultar apuntes
- [ ] Puedo explicar crear y gestionar sesiones sin consultar apuntes
- [ ] Puedo explicar trabajo en paralelo sin consultar apuntes
- [ ] Puedo explicar casos de uso sin consultar apuntes
