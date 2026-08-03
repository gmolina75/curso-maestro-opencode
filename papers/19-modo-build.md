---
title: "Modo Build"
module: 19
duration: "55 minutos"
prerequisites: "Módulo 18: Configuración de Permisos"
---

# Clase 19: Modo Build

## Resumen Ejecutivo

El modo Build es el modo de operación principal de OpenCode donde el asistente tiene acceso completo a todas las herramientas. En este modo, OpenCode puede leer, escribir y editar archivos, ejecutar comandos shell, buscar en el codebase, y realizar cualquier operación necesaria para implementar cambios en tu proyecto.

Build mode es donde ocurre la magia de la implementación. Después de planificar en Plan mode, switches a Build mode para ejecutar los cambios. Este módulo cubre las mejores prácticas para usar Build mode de manera efectiva, segura y productiva.

## Objetivos de Aprendizaje

- Entender las capacidades completas del modo Build
- Ejecutar operaciones de archivos de forma segura
- Implementar features y refactorizaciones
- Usar herramientas de búsqueda en el codebase
- Seguir mejores prácticas de seguridad
- Alternar efectivamente entre Build y Plan

## Conceptos Clave

### Capacidades del Modo Build

En modo Build, OpenCode tiene acceso a:

| Herramienta | Capacidad | Uso |
|-------------|-----------|-----|
| `read` | Leer archivos | Análisis de código |
| `write` | Crear/sobrescribir archivos | Crear nuevos archivos |
| `edit` | Modificar archivos | Ediciones precisas |
| `bash` | Ejecutar comandos | Build, test, git |
| `glob` | Buscar archivos | Encontrar archivos |
| `grep` | Buscar contenido | Encontrar código |
| `apply_patch` | Parches complejos | Cambios multi-archivo |
| `skill` | Cargar skills | Contexto especializado |
| `todowrite` | Gestionar tareas | Organizar trabajo |
| `webfetch` | Obtener contenido web | Documentación |
| `websearch` | Buscar en internet | Investigación |
| `question` | Preguntar usuario | Decisiones |

### Flujo de Trabajo Típico

```
Plan Mode → Análisis → Cambios Propuestos
    ↓
Build Mode → Implementación → Verificación
    ↓
Verificación → Tests → Deploy
```

### Operaciones de Archivos

**Leer archivos:**
```bash
# Leer archivo completo
read("src/main.ts")

# Leer porciones específicas
read("src/main.ts", offset=10, limit=50)

# Leer directorio
read("src/")
```

**Crear archivos:**
```bash
# Crear nuevo archivo
write(
  filePath="src/components/NewComponent.tsx",
  content="export const NewComponent = () => {}"
)
```

**Modificar archivos:**
```bash
# Reemplazo exacto
edit(
  filePath="src/utils.ts",
  oldString="function oldName(",
  newString="function newName("
)
```

### Ejecución de Comandos

```bash
# Comandos de build
bash("npm run build")
bash("yarn build")
bash("pnpm build")

# Comandos de test
bash("npm test")
bash("yarn test:unit")
bash("pnpm test:integration")

# Comandos de git
bash("git status")
bash("git diff")
bash("git add .")
bash("git commit -m 'feat: add new feature'")
```

### Búsqueda en el Codebase

```bash
# Encontrar archivos
glob(pattern="src/**/*.ts")

# Buscar contenido
grep(pattern="function.*calculate")

# Buscar en tipos específicos
grep(pattern="TODO|FIXME", include="*.ts")
```

### Mejores Prácticas de Seguridad

1. **Siempre lee antes de modificar**
   - Entiende el código existente antes de cambiarlo
   - Identifica dependencias y efectos secundarios

2. **Usa edit en lugar de write para modificaciones**
   - write sobrescribe el archivo completo
   - edit es más seguro y preciso

3. **Verifica cambios antes de commitear**
   - Revisa diffs con `git diff`
   - Ejecuta tests después de cambios

4. **No ejecutes comandos destructivos sin confirmar**
   - rm -rf, sudo, chmod 777 son peligrosos
   - Usa permisos para bloquear comandos peligrosos

### Implementación de Features

```bash
# 1. Entender la需求
> Necesito agregar autenticación JWT a la API

# 2. Explorar codebase existente
glob(pattern="src/**/*.ts")
read("src/app.ts")
read("src/routes/")

# 3. Planificar (puede ser en Plan mode)
> Propongo crear middleware de auth, rutas protegidas, y utils de JWT

# 4. Implementar en Build mode
write(filePath="src/middleware/auth.ts", content="...")
edit(filePath="src/routes/api.ts", oldString="...", newString="...")

# 5. Verificar
bash("npm test")
bash("npm run lint")
```

### Refactorización

```bash
# 1. Identificar código a refactorizar
grep(pattern="duplicate.*code", include="*.ts")

# 2. Analizar dependencias
grep(pattern="import.*from.*utils")

# 3. Crear nuevas abstracciones
write(filePath="src/utils/newHelper.ts", content="...")

# 4. Actualizar importaciones
edit(filePath="src/components/Comp.tsx", oldString="...", newString="...")

# 5. Verificar que todo funciona
bash("npm test")
```

## Guía Paso a Paso

### Paso 1: Evaluar el Codebase

```bash
# Antes de hacer cambios, entiende la estructura
bash("ls -la")
bash("find . -type f -name '*.ts' | head -20")
read("package.json")
read("README.md")

# Identificar áreas relevantes
glob(pattern="src/**/*.ts")
grep(pattern="export.*function")
```

### Paso 2: Hacer Cambios Seguros

```bash
# SIEMPRE lee el archivo primero
read("src/services/api.ts")

# Usa edit para cambios precisos
edit(
  filePath="src/services/api.ts",
  oldString="function fetchData() {",
  newString="async function fetchData(): Promise<Data> {"
)

# Verifica el cambio
bash("git diff src/services/api.ts")
```

### Paso 3: Implementar Feature Completa

```bash
# Ejemplo: Agregar logging

# 1. Crear módulo de logging
write(
  filePath="src/utils/logger.ts",
  content=`export enum LogLevel {
  DEBUG = 'debug',
  INFO = 'info',
  WARN = 'warn',
  ERROR = 'error'
}

export function log(level: LogLevel, message: string, data?: unknown) {
  console.log(\`[\${level}] \${message}\`, data);
}`
)

# 2. Usar en archivos existentes
edit(
  filePath="src/app.ts",
  oldString="import express from 'express';",
  newString="import express from 'express';\nimport { log, LogLevel } from './utils/logger';"
)

# 3. Agregar logging
edit(
  filePath="src/app.ts",
  oldString="app.listen(port);",
  newString="log(LogLevel.INFO, \`Server starting on port \${port}\`);\napp.listen(port);"
)
```

### Paso 4: Ejecutar Tests y Verificar

```bash
# Ejecutar tests
bash("npm test")

# Ejecutar lint
bash("npm run lint")

# Verificar build
bash("npm run build")

# Revisar cambios
bash("git status")
bash("git diff --stat")
```

### Paso 5: Commitear Cambios

```bash
# Agregar archivos
bash("git add src/utils/logger.ts src/app.ts")

# Commitear con mensaje descriptivo
bash("git commit -m 'feat: add logging utility

- Create logger module with log levels
- Add logging to app startup
- Include data parameter for structured logging'")

# Verificar commit
bash("git log --oneline -1")
```

## Referencia Rápida

| Operación | Comando | Ejemplo |
|-----------|---------|---------|
| Leer archivo | `read(path)` | `read("src/main.ts")` |
| Crear archivo | `write(path, content)` | `write("f.ts", "code")` |
| Editar archivo | `edit(path, old, new)` | `edit("f.ts", "old", "new")` |
| Ejecutar comando | `bash(cmd)` | `bash("npm test")` |
| Buscar archivos | `glob(pattern)` | `glob("**/*.ts")` |
| Buscar contenido | `grep(pattern)` | `grep("TODO")` |
| Parche complejo | `apply_patch(patch)` | `apply_patch("...")` |
| Cargar skill | `skill(name)` | `skill("testing")` |
| Gestionar tareas | `todowrite(tasks)` | `todowrite([...])` |
| Obtener URL | `webfetch(url)` | `webfetch("https://...")` |
| Buscar web | `websearch(query)` | `websearch("query")` |
| Preguntar | `question(q, opts)` | `question("...", [...])` |

## Ejercicios Guiados

### Ejercicio 1: Implementar Feature Completa

**Objetivo:** Implementar una feature completa usando solo Build mode.

**Instrucciones:**
1. Elige una feature simple (ej: agregar campo a un formulario)
2. Explora el codebase para entender la estructura
3. Lee los archivos relevantes
4. Implementa los cambios necesarios
5. Crea archivos nuevos si es necesario
6. Ejecuta tests para verificar
7. Limpia código innecesario

**Solución Esperada:**
```bash
# 1. Explorar
glob(pattern="src/**/*.tsx")
read("src/components/Form.tsx")
read("src/types/form.ts")

# 2. Implementar
edit(
  filePath="src/types/form.ts",
  oldString="interface FormData {\n  name: string;\n}",
  newString="interface FormData {\n  name: string;\n  email: string;\n}"
)

edit(
  filePath="src/components/Form.tsx",
  oldString="<input name='name' />",
  newString="<input name='name' />\n<input name='email' type='email' />"
)

# 3. Verificar
bash("npm test")
bash("npm run build")
```

### Ejercicio 2: Refactorizar Código Duplicado

**Objetivo:** Identificar y eliminar código duplicado.

**Instrucciones:**
1. Usa grep para encontrar código duplicado
2. Analiza todas las ocurrencias
3. Crea una función auxiliar
4. Reemplaza todas las ocurrencias
5. Verifica que nada se rompió
6. Documenta el cambio

**Solución Esperada:**
```bash
# 1. Encontrar duplicación
grep(pattern="function formatDate", include="*.ts")
# Encuentra en: utils.ts, helpers.ts, lib.ts

# 2. Leer cada archivo
read("src/utils.ts")
read("src/helpers.ts")
read("src/lib.ts")

# 3. Crear función centralizada
write(
  filePath="src/shared/date.ts",
  content=`export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}`
)

# 4. Actualizar importaciones
edit(filePath="src/utils.ts", oldString="...", newString="import { formatDate } from '../shared/date';")
edit(filePath="src/helpers.ts", oldString="...", newString="import { formatDate } from '../shared/date';")
edit(filePath="src/lib.ts", oldString="...", newString="import { formatDate } from '../shared/date';")

# 5. Verificar
bash("npm test")
```

### Ejercicio 3: Corregir Bug Crítico

**Objetivo:** Encontrar y corregir un bug de manera sistemática.

**Instrucciones:**
1. Identifica el bug (ej: error en consola)
2. Usa grep para encontrar el código problemático
3. Lee el archivo para entender el contexto
4. Implementa la corrección
5. Verifica con tests
6. Agrega test para prevenir regresión

**Solución Esperada:**
```bash
# 1-2. Encontrar bug
grep(pattern="undefined.*property")
# Encuentra: src/services/api.ts:45

# 3. Leer contexto
read("src/services/api.ts", offset=40, limit=20)

# 4. Corregir
edit(
  filePath="src/services/api.ts",
  oldString="const data = response.data;",
  newString="const data = response.data ?? {};"
)

# 5. Verificar
bash("npm test")

# 6. Agregar test
write(
  filePath="src/services/__tests__/api.test.ts",
  content=`import { fetchData } from '../api';

test('handles null response data', async () => {
  const result = await fetchData();
  expect(result).toBeDefined();
});`
)
```

## Ejercicio Desafío

**Reto:** Implementa una feature completa en Build mode:
1. Crea un nuevo módulo con múltiples archivos
2. Integra con el codebase existente
3. Agrega tests unitarios y de integración
4. Documenta la feature
5. Crea un commit descriptivo
6. Prepara un PR con descripción completa

**Pistas:**
- Planifica antes de implementar
- Usa skills para contexto de testing
- Verifica TODO antes de commitear
- Documenta decisiones de diseño

## Recursos Adicionales

- [Guía de Build mode](https://opencode.ai/docs/modes#build)
- [Mejores prácticas de código](https://opencode.ai/docs/best-practices)
- [Flujo de trabajo de desarrollo](https://opencode.ai/docs/workflow)

## Autoevaluación

- [ ] Entiendo las capacidades del modo Build
- [ ] Leo archivos antes de modificarlos
- [ ] Uso edit en lugar de write para modificaciones
- [ ] Ejecuto tests después de cambios
- [ ] Implemento features completas de forma sistemática
- [ ] Refactorizo código de manera segura
- [ ] Commiteo con mensajes descriptivos
