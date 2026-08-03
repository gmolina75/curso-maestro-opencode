---
title: "Flujo de Trabajo Plan → Build"
module: 21
duration: "60 minutos"
prerequisites: "Módulo 20: Modo Plan"
---

# Clase 21: Flujo de Trabajo Plan → Build

## Resumen Ejecutivo

El flujo de trabajo Plan → Build es la metodología recomendada para usar OpenCode de manera efectiva. Consiste en planificar primero en modo Plan (solo lectura) y luego implementar en modo Build (acceso completo). Este enfoque reduce errores, mejora la calidad del código, y hace el desarrollo más predecible y controlado.

Este módulo integra todo lo aprendido en módulos anteriores en un flujo de trabajo completo y práctico. Aprenderás a pasar de una idea o problema a una implementación completa y verificada, usando la alternancia entre modos de forma fluida y eficiente.

## Objetivos de Aprendizaje

- Ejecutar el flujo completo Plan → Build
- Planificar features de manera efectiva
- Iterar sobre planes hasta tener la mejor solución
- Implementar cambios de forma sistemática
- Usar referencias de archivos con @
- Verificar cambios con tests y linting
- Documentar el proceso de desarrollo

## Conceptos Clave

### El Flujo Completo

```
┌─────────────────────────────────────────────────────────┐
│                     FLUJO PLAN → BUILD                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. IDENTIFICAR  →  2. PLANEAR  →  3. IMPLEMENTAR      │
│                                                         │
│  Plan Mode          Plan Mode       Build Mode          │
│  (lectura)          (análisis)      (escritura)         │
│                                                         │
│  4. VERIFICAR  →  5. DOCUMENTAR  →  6. ENTREGAR        │
│                                                         │
│  Build Mode         Build Mode       Build Mode         │
│  (tests)           (docs)           (commit)            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Paso 1: Identificar el Problema o Feature

```bash
# Activa Plan mode
Tab

# Explora el codebase para entender el contexto
glob(pattern="src/**/*.ts")
read("src/app.ts")
grep(pattern="TODO|FIXME", include="*.ts")

# Define el objetivo
> Necesito agregar autenticación JWT a la API REST

# Pide análisis inicial
> Analiza la estructura actual de la API y dime qué archivos necesito modificar
```

### Paso 2: Planear la Solución

```bash
# En Plan mode, pide un plan detallado
> Crea un plan paso a paso para implementar JWT auth

# El asistente proporcionará:
# - Lista de archivos a crear/modificar
# - Orden de implementación
# - Dependencias entre cambios
# - Estimación de tiempo
# - Riesgos potenciales

# Itera sobre el plan
> El plan es bueno, pero ¿cómo manejarías la renovación de tokens?

> Agrega manejo de errores para tokens expirados

> ¿Qué tests necesitaríamos?
```

### Paso 3: Usar Referencias con @

```bash
# En Plan mode, referencia archivos para dar contexto
@src/routes/api.ts Analiza esta ruta y propón cómo protegerla

@src/middleware/ Existe algún middleware de auth que pueda reutilizar?

@package.json ¿Qué dependencias necesito instalar para JWT?

# El asistente cargará los archivos automáticamente
# y los usará como contexto para su análisis
```

### Paso 4: Cambiar a Build Mode

```bash
# Cuando el plan esté completo y aprobado
Tab    # Cambiar a Build mode

# Verifica que estás en Build mode
# La barra de estado mostrará "Build Mode"
```

### Paso 5: Implementar Sistemáticamente

```bash
# Sigue el plan paso a paso

# 1. Crear archivos nuevos
write(
  filePath="src/middleware/auth.ts",
  content="import jwt from 'jsonwebtoken';\n\nexport function authMiddleware(req, res, next) {\n  // implementation\n}"
)

# 2. Modificar archivos existentes
edit(
  filePath="src/routes/api.ts",
  oldString="import express from 'express';",
  newString="import express from 'express';\nimport { authMiddleware } from '../middleware/auth';"
)

# 3. Ejecutar comandos de build
bash("npm install jsonwebtoken @types/jsonwebtoken")
```

### Paso 6: Verificar los Cambios

```bash
# Ejecutar tests
bash("npm test")

# Ejecutar linting
bash("npm run lint")

# Verificar build
bash("npm run build")

# Revisar cambios
bash("git diff")
bash("git status")
```

### Paso 7: Documentar

```bash
# Actualizar documentación
edit(
  filePath="README.md",
  oldString="## API Endpoints",
  newString="## API Endpoints\n\n### Autenticación\nTodas las rutas requieren JWT token en header Authorization"
)

# Crear documentación específica
write(
  filePath="docs/authentication.md",
  content="# Autenticación JWT\n\n## Uso\n1. Obtener token via POST /auth/login\n2. Incluir en header: Authorization: Bearer <token>"
)
```

### Paso 8: Entregar (Commit)

```bash
# Agregar archivos
bash("git add src/middleware/auth.ts src/routes/api.ts docs/authentication.md")

# Commitear con mensaje descriptivo
bash("git commit -m 'feat: add JWT authentication

- Add auth middleware for token validation
- Protect API routes with JWT
- Add token renewal endpoint
- Include error handling for expired tokens
- Add documentation for authentication'")

# Verificar commit
bash("git log --oneline -1")
```

## Flujo Completo de Ejemplo

### Ejemplo: Agregar Sistema de Logging

```bash
# ========== FASE 1: PLAN ==========

# 1. Activar Plan mode
Tab

# 2. Explorar codebase
glob(pattern="src/**/*.ts")
read("src/app.ts")
read("src/services/")

# 3. Definir objetivo
> Necesito agregar logging estructurado para debugging en producción

# 4. Pedir plan
> Crea un plan para implementar logging con niveles (debug, info, warn, error)

# 5. Iterar sobre el plan
> El plan es bueno. ¿Cómo manejarías logging async para no bloquear?

> Agrega rotación de archivos de log

> ¿Qué tests necesitamos para el logger?

# 6. Aprobación final
> Perfecto, el plan está listo. Procedamos a implementar.

# ========== FASE 2: BUILD ==========

# 7. Cambiar a Build mode
Tab

# 8. Crear módulo de logging
write(
  filePath="src/utils/logger.ts",
  content=`import fs from 'fs';
import path from 'path';

export enum LogLevel {
  DEBUG = 'debug',
  INFO = 'info',
  WARN = 'warn',
  ERROR = 'error'
}

const LOG_DIR = path.join(process.cwd(), 'logs');
const LOG_FILE = path.join(LOG_DIR, 'app.log');

export function log(level: LogLevel, message: string, data?: unknown) {
  const timestamp = new Date().toISOString();
  const logEntry = JSON.stringify({ timestamp, level, message, data });
  
  fs.appendFileSync(LOG_FILE, logEntry + '\\n');
  
  if (level === LogLevel.ERROR) {
    console.error(\`[\${level}] \${message}\`, data);
  } else {
    console.log(\`[\${level}] \${message}\`, data);
  }
}`
)

# 9. Integrar en la app
edit(
  filePath="src/app.ts",
  oldString="const app = express();",
  newString="import { log, LogLevel } from './utils/logger';\n\nconst app = express();\n\nlog(LogLevel.INFO, 'Application starting');"
)

# 10. Verificar
bash("npm test")
bash("npm run build")

# 11. Documentar
write(
  filePath="docs/logging.md",
  content="# Sistema de Logging\n\n## Uso\nimport { log, LogLevel } from '../utils/logger';\n\nlog(LogLevel.INFO, 'Evento importante', { userId: 123 });"
)

# 12. Commitear
bash("git add -A")
bash("git commit -m 'feat: add structured logging system

- Create logger module with log levels
- Add file rotation support
- Integrate with application startup
- Include documentation'")
```

## Referencia Rápida

| Fase | Modo | Acciones | Herramientas |
|------|------|----------|--------------|
| Identificar | Plan | Explorar, definir | read, glob, grep |
| Planear | Plan | Analizar, proponer | read, glob, grep, question |
| Implementar | Build | Crear, modificar | write, edit, bash, apply_patch |
| Verificar | Build | Testear, validar | bash (npm test, lint) |
| Documentar | Build | Escribir docs | write, edit |
| Entregar | Build | Commitear | bash (git) |

## Ejercicios Guiados

### Ejercicio 1: Feature Completa con Plan → Build

**Objetivo:** Implementar una feature completa siguiendo el flujo Plan → Build.

**Instrucciones:**
1. Elige una feature simple (ej: paginación de resultados)
2. En Plan mode, analiza el codebase
3. Crea un plan detallado
4. Evalúa y ajusta el plan
5. Cambia a Build mode
6. Implementa cada paso del plan
7. Verifica con tests
8. Documenta la feature
9. Crea un commit

**Solución Esperada:**
```bash
# FASE 1: PLAN
Tab
glob(pattern="src/**/*.ts")
read("src/routes/api.ts")
> Crea un plan para agregar paginación a los endpoints de lista

# FASE 2: BUILD
Tab
write(filePath="src/utils/pagination.ts", content="...")
edit(filePath="src/routes/api.ts", oldString="...", newString="...")
bash("npm test")
write(filePath="docs/pagination.md", content="...")
bash("git commit -m 'feat: add pagination'")
```

### Ejercicio 2: Corregir Bug Crítico

**Objetivo:** Usar Plan → Build para corregir un bug de manera sistemática.

**Instrucciones:**
1. Identifica el bug (ej: error en producción)
2. En Plan mode, analiza el código problemático
3. Identifica la causa raíz
4. Propón una solución
5. Evalúa impactos colaterales
6. Cambia a Build mode
7. Implementa la corrección
8. Agrega test para prevenir regresión
9. Verifica todo funciona

**Solución Esperada:**
```bash
# PLAN
Tab
grep(pattern="undefined.*property", include="*.ts")
read("src/services/api.ts")
> El bug está en la línea 45. ¿Cuál es la causa raíz?

# BUILD
Tab
edit(filePath="src/services/api.ts", oldString="...", newString="...")
write(filePath="src/__tests__/api.test.ts", content="...")
bash("npm test")
bash("git commit -m 'fix: handle undefined response data'")
```

### Ejercicio 3: Refactorización Grande

**Objetivo:** Realizar una refactorización compleja usando el flujo completo.

**Instrucciones:**
1. Identifica código a refactorizar (ej: módulo monolítico)
2. En Plan mode, analiza dependencias
3. Diseña la nueva arquitectura
4. Crea un plan por fases
5. Estima tiempo y riesgos
6. Cambia a Build mode
7. Implementa por fases (un commit por fase)
8. Verifica después de cada fase
9. Documenta la nueva arquitectura

**Solución Esperada:**
```bash
# PLAN
Tab
read("src/services/monolith.ts")
grep(pattern="export.*function", include="monolith.ts")
> Diseña una nueva arquitectura modular para este módulo
> Crea un plan por fases con commits separados

# BUILD
Tab
# Fase 1: Crear estructura
write(filePath="src/services/user/index.ts", content="...")
bash("git commit -m 'refactor: create user service structure'")

# Fase 2: Migrar funciones
edit(filePath="...", oldString="...", newString="...")
bash("git commit -m 'refactor: migrate user functions'")

# Fase 3: Actualizar importaciones
edit(filePath="...", oldString="...", newString="...")
bash("git commit -m 'refactor: update imports'")
```

## Ejercicio Desafío

**Reto:** Ejecuta el flujo completo para una feature compleja:
1. Planifica una feature que toque 5+ archivos
2. Usa referencias @ para dar contexto
3. Itera el plan al menos 3 veces
4. Implementa con commits separados por lógica
5. Ejecuta tests después de cada commit
6. Documenta todo el proceso
7. Crea un PR con descripción detallada

**Pistas:**
- No te apresures en la fase de plan
- Un buen plan ahorra horas de implementación
- Usa todowrite para trackear progreso
- Documenta decisiones de diseño

## Recursos Adicionales

- [Guía completa de flujo de trabajo](https://opencode.ai/docs/workflow)
- [Planificación de features](https://opencode.ai/docs/feature-planning)
- [Mejores prácticas de commit](https://opencode.ai/docs/git-best-practices)

## Autoevaluación

- [ ] Ejecuto el flujo completo Plan → Build sin saltarme pasos
- [ ] Planifico antes de implementar cada feature
- [ ] Uso referencias @ para dar contexto efectivo
- [ ] Itero sobre planes hasta tener la mejor solución
- [ ] Implemento de forma sistemática y organizada
- [ ] Verifico cambios con tests después de cada implementación
- [ ] Documento todo el proceso de desarrollo
- [ ] Crea commits descriptivos y organizados
