---
title: "Modo Plan"
module: 20
duration: "45 minutos"
prerequisites: "Módulo 19: Modo Build"
---

# Clase 20: Modo Plan

## Resumen Ejecutivo

El modo Plan es un modo de solo lectura de OpenCode diseñado para análisis seguro del codebase. En este modo, el asistente solo puede leer archivos, buscar contenido y analizar código, pero no puede modificar nada. Esto lo hace ideal para explorar proyectos unfamiliar, planificar cambios complejos, y recibir sugerencias sin riesgo de alterar el código existente.

Plan mode es tu primera línea de defensa al trabajar con código nuevo. Te permite entender la arquitectura, identificar áreas de mejora, y crear un plan de implementación antes de tocar una sola línea de código. La alternancia fluida entre Plan y Build es clave para un flujo de trabajo efectivo.

## Objetivos de Aprendizaje

- Activar y usar el modo Plan correctamente
- Analizar codebases de forma segura
- Proponer cambios sin implementarlos
- Evaluar sugerencias del asistente
- Alternar efectivamente entre Plan y Build
- Crear planes de implementación detallados

## Conceptos Clave

### Activación del Modo Plan

Hay varias formas de entrar en modo Plan:

```bash
# Usando Tab (más rápido)
Tab    # Alterna entre Build y Plan

# Usando tecla líder
Ctrl+X → p    # Entrar a Plan mode

# Usando comando slash
/plan    # Cambiar a Plan mode
```

La barra de estado mostrará "Plan Mode" cuando esté activo.

### Capacidades en Plan Mode

| Herramienta | Disponible | Uso |
|-------------|------------|-----|
| `read` | Sí | Leer archivos |
| `glob` | Sí | Buscar archivos |
| `grep` | Sí | Buscar contenido |
| `webfetch` | Sí | Obtener documentación |
| `websearch` | Sí | Buscar en internet |
| `question` | Sí | Preguntar al usuario |
| `todowrite` | Sí | Organizar tareas |
| `write` | **No** | Crear archivos |
| `edit` | **No** | Modificar archivos |
| `bash` | **No** | Ejecutar comandos |
| `apply_patch` | **No** | Aplicar parches |

### Análisis de Codebase

En Plan mode puedes:

1. **Explorar estructura**
```bash
glob(pattern="src/**/*.ts")
read("src/")
```

2. **Entender arquitectura**
```bash
read("src/app.ts")
read("src/routes/")
read("src/services/")
```

3. **Identificar patrones**
```bash
grep(pattern="export.*class")
grep(pattern="import.*from")
```

4. **Evaluar calidad**
```bash
grep(pattern="TODO|FIXME")
grep(pattern="any", include="*.ts")
```

### Propuesta de Cambios

El asistente puede proponer cambios detallados:

```markdown
## Propuesta de Cambio

### Archivos a modificar:
1. `src/types/user.ts` - Agregar interfaz Profile
2. `src/services/user.ts` - Implementar función getProfile
3. `src/routes/user.ts` - Agregar endpoint GET /profile

### Cambios específicos:

**En `src/types/user.ts`:**
```typescript
export interface Profile {
  id: string;
  name: string;
  email: string;
}
```

**En `src/services/user.ts`:**
```typescript
export async function getProfile(userId: string): Promise<Profile> {
  // implementation
}
```

### Dependencias:
- Requiere auth middleware existente
- Usa base de datos configurada

### Riesgos:
- Bajo riesgo: cambios aditivos
- No afecta código existente
```

### Evaluación de Sugerencias

Puedes pedir al asistente que evalúe sus propias sugerencias:

```markdown
> Evalúa los pros y contras de esta implementación

> ¿Hay alternativas más simples?

> ¿Qué tests necesitaríamos?

> ¿Esto cumple con los estándares del proyecto?
```

### Flujo Plan → Build

```
1. Activar Plan mode (Tab)
2. Explorar codebase
3. Definir objetivo
4. Recibir propuesta del asistente
5. Evaluar y ajustar
6. Cambiar a Build mode (Tab)
7. Implementar cambios
8. Verificar
```

### Crear Planes Detallados

El asistente puede crear planes estructurados:

```markdown
## Plan de Implementación: [Feature Name]

### Fase 1: Preparación (10 min)
- [ ] Explorar codebase existente
- [ ] Identificar archivos relevantes
- [ ] Revisar tests existentes

### Fase 2: Modelos (15 min)
- [ ] Definir interfaces TypeScript
- [ ] Crear tipos de datos
- [ ] Agregar validaciones

### Fase 3: Servicios (20 min)
- [ ] Implementar lógica de negocio
- [ ] Agregar manejo de errores
- [ ] Implementar logging

### Fase 4: API (15 min)
- [ ] Crear endpoints
- [ ] Agregar middleware
- [ ] Documentar con OpenAPI

### Fase 5: Testing (20 min)
- [ ] Tests unitarios
- [ ] Tests de integración
- [ ] Tests de error

### Total: ~80 minutos
```

## Guía Paso a Paso

### Paso 1: Activar Plan Mode

```bash
# Opción 1: Tab (más rápido)
Tab

# Opción 2: Tecla líder
Ctrl+X
p

# Verificar que estás en Plan mode
# La barra de estado mostrará "Plan Mode"
```

### Paso 2: Explorar el Codebase

```bash
# Ver estructura general
glob(pattern="**/*.ts")

# Leer archivos principales
read("package.json")
read("README.md")
read("src/app.ts")

# Identificar áreas clave
grep(pattern="export.*class", include="*.ts")
grep(pattern="router\\.", include="*.ts")
```

### Paso 3: Analizar un Problema

```markdown
> Estoy viendo errores de tipo en el módulo de usuarios.
> ¿Puedes analizar src/services/user.ts y找出 los problemas?

# El asistente leerá el archivo y proporcionará:
# - Lista de errores de tipo
# - Sugerencias de corrección
# - Prioridad de cada problema
```

### Paso 4: Recibir Propuesta de Cambio

```markdown
> Proponme una solución para refactorizar el módulo de autenticación

# El asistente proporcionará:
# - Análisis del código actual
# - Propuesta de nueva estructura
# - Lista de archivos a modificar
# - Estimación de esfuerzo
# - Riesgos y mitigaciones
```

### Paso 5: Evaluar y Ajustar

```markdown
> ¿Esta propuesta cumple con los estándares de seguridad del proyecto?

> ¿Hay una forma más simple de lograr lo mismo?

> ¿Qué tests necesitaríamos agregar?

# El asistente ajustará la propuesta según tus feedback
```

### Paso 6: Cambiar a Build Mode

```bash
# Cuando estés satisfecho con el plan
Tab    # Volver a Build mode

# Implementar los cambios propuestos
# Seguir el plan creado en Plan mode
```

## Referencia Rápida

| Acción | Comando | Descripción |
|--------|---------|-------------|
| Activar Plan | `Tab` | Cambiar a Plan mode |
| Activar Plan | `Ctrl+X → p` | Alternativa |
| Activar Plan | `/plan` | Comando slash |
| Volver a Build | `Tab` | Cambiar a Build mode |
| Leer archivo | `read(path)` | Disponible en Plan |
| Buscar archivos | `glob(pattern)` | Disponible en Plan |
| Buscar contenido | `grep(pattern)` | Disponible en Plan |
| Crear archivo | `write(path, content)` | **NO** disponible |
| Modificar archivo | `edit(path, old, new)` | **NO** disponible |
| Ejecutar comando | `bash(cmd)` | **NO** disponible |

## Ejercicios Guiados

### Ejercicio 1: Explorar un Proyecto Nuevo

**Objetivo:** Usar Plan mode para entender un proyecto unfamiliar.

**Instrucciones:**
1. Activa Plan mode con Tab
2. Lee el README.md del proyecto
3. Explora la estructura de directorios
4. Identifica los módulos principales
5. Entiende las dependencias
6. Crea un resumen de la arquitectura
7. Vuelve a Build mode

**Solución Esperada:**
```bash
# 1. Activar Plan
Tab

# 2-4. Explorar
read("README.md")
glob(pattern="src/**/*.ts")
read("src/")
read("package.json")

# 5. Dependencias
grep(pattern="import.*from", include="src/**/*.ts")

# 6. Resumen
> Crea un resumen de la arquitectura de este proyecto

# 7. Volver a Build
Tab
```

### Ejercicio 2: Planificar una Feature

**Objetivo:** Crear un plan detallado antes de implementar.

**Instrucciones:**
1. Define la feature a implementar
2. En Plan mode, analiza el codebase existente
3. Identifica archivos afectados
4. Pide al asistente que cree un plan
5. Evalúa el plan y pide ajustes
6. Documenta el plan final
7. Cambia a Build mode para implementar

**Solución Esperada:**
```bash
# 1-2. Definir y analizar
Tab    # Plan mode
> Necesito agregar sistema de notificaciones por email

# 3-4. Planificar
read("src/services/")
grep(pattern="send.*email", include="*.ts")
> Crea un plan detallado para implementar notificaciones

# 5-6. Ajustar
> El plan es bueno, pero agrega manejo de cola de mensajes
> Documenta el plan en docs/notifications-plan.md

# 7. Implementar
Tab    # Build mode
> Implementa el plan que acabamos de crear
```

### Ejercicio 3: Revisar Cambios Propuestos

**Objetivo:** Evaluar sugerencias del asistente antes de implementar.

**Instrucciones:**
1. Describe un problema o área de mejora
2. Pide análisis y sugerencias en Plan mode
3. Evalúa cada sugerencia
4. Pide alternativas
5. Selecciona la mejor opción
6. Crea un plan de implementación
7. Cambia a Build mode

**Solución Esperada:**
```bash
# 1-2. Análisis
Tab    # Plan mode
> El módulo de pagas tiene código duplicado y es difícil de mantener

# 3-4. Evaluar
> ¿Cuáles son las 3 mejores formas de refactorizar esto?
> ¿Qué contras tiene cada opción?

# 5-6. Seleccionar y planificar
> La opción 2 parece mejor. Crea un plan detallado

# 7. Implementar
Tab    # Build mode
> Implementa la refactorización seleccionada
```

## Ejercicio Desafío

**Reto:** Realiza un análisis completo de un proyecto usando solo Plan mode:
1. Documenta la arquitectura general
2. Identifica 5 áreas de mejora
3. Prioriza las mejoras por impacto y esfuerzo
4. Crea un plan de implementación para cada una
5. Evalúa riesgos y dependencias
6. Prepara un roadmap de 3 meses
7. Cambia a Build mode solo cuando tengas todo planificado

**Pistas:**
- Tómate tu tiempo en Plan mode
- No tengas prisa por implementar
- Un buen plan ahorra horas de desarrollo
- Documenta TODO para referencia futura

## Recursos Adicionales

- [Guía de Plan mode](https://opencode.ai/docs/modes#plan)
- [Técnicas de análisis de código](https://opencode.ai/docs/code-analysis)
- [Planificación de features](https://opencode.ai/docs/feature-planning)

## Autoevaluación

- [ ] Puedo activar y desactivar Plan mode
- [ ] Entiendo qué herramientas están disponibles en Plan
- [ ] Analizo codebases de forma sistemática
- [ ] Recibo y evalúo propuestas de cambio
- [ ] Creo planes detallados antes de implementar
- [ ] Alterno efectivamente entre Plan y Build
- [ ] Documento planes para referencia futura
