---
title: "Herramientas Principales - Parte 1"
module: 16
duration: "60 minutos"
prerequisites: "Módulo 12: Navegación en la Interfaz TUI"
---

# Clase 16: Herramientas Principales - Parte 1

## Resumen Ejecutivo

OpenCode dispone de un conjunto de herramientas fundamentales que permiten interactuar con el sistema de archivos, ejecutar comandos y buscar contenido. Estas herramientas son la base de todas las operaciones que el asistente puede realizar. Dominarlas es esencial para aprovechar al máximo la capacidad de OpenCode.

Las herramientas se dividen en dos categorías principales: las que interactúan con archivos (read, write, edit, glob, grep) y las que ejecutan comandos (bash). Cada una tiene un propósito específico y mejores prácticas de uso. Este módulo cubre las herramientas más utilizadas en detalle práctico.

## Objetivos de Aprendizaje

- Ejecutar comandos shell con bash
- Leer archivos con read
- Crear y sobrescribir archivos con write
- Modificar archivos con edit usando reemplazo exacto
- Buscar contenido con grep
- Encontrar archivos con glob

## Conceptos Clave

### bash - Ejecutar Comandos Shell

La herramienta `bash` ejecuta comandos del sistema operativo. Es la forma de interactuar con git, npm, docker, y cualquier otra herramienta de línea de comandos.

```bash
# Uso básico
bash("ls -la")

# Con working directory
bash("npm test", workdir="/ruta/a/proyecto")

# Comandos con pipe
bash("git log --oneline | head -10")

# Verificar exit code
bash("docker build . -t mi-app")
```

**Buenas prácticas:**
- Siempre verifica el resultado antes de continuar
- Usa workdir para ejecutar en directorios específicos
- Evita comandos destructivos sin confirmación

### read - Leer Archivos

La herramienta `read` lee el contenido de archivos. Es fundamental para entender el código antes de modificarlo.

```bash
# Leer archivo completo
read("src/main.ts")

# Leer con líneas específicas
read("src/main.ts", offset=10, limit=50)

# Leer directorio
read("src/")
```

**Parámetros importantes:**
- `filePath`: Ruta absoluta del archivo
- `offset`: Línea de inicio (1-indexed)
- `limit`: Número máximo de líneas

### write - Crear/Sobrescribir Archivos

La herramienta `write` crea nuevos archivos o sobrescribe existentes completamente.

```bash
# Crear archivo nuevo
write(
  filePath="src/utils.ts",
  content="export const helper = () => {};"
)

# Sobrescribir archivo existente (requiere read previo)
write(
  filePath="config.json",
  content="{ \"key\": \"value\" }"
)
```

**IMPORTANTE:** Siempre lee el archivo primero antes de sobrescribir. Esto evita perder contenido importante.

### edit - Modificar Archivos con Reemplazo

La herramienta `edit` realiza reemplazos exactos en archivos. Es la forma más segura de modificar código.

```bash
# Reemplazo exacto
edit(
  filePath="src/app.ts",
  oldString="function oldName(",
  newString="function newName("
)

# Reemplazo con contexto (para hacer único)
edit(
  filePath="src/app.ts",
  oldString="  const x = 1;\n  console.log(x);",
  newString="  const x = 1;\n  const y = 2;\n  console.log(x, y);"
)

# Reemplazar todas las ocurrencias
edit(
  filePath="src/app.ts",
  oldString="deprecated",
  newString="updated",
  replaceAll=true
)
```

**Reglas importantes:**
- El oldString debe ser EXACTAMENTE como aparece en el archivo
- Incluye suficiente contexto para que sea único
- Si hay múltiples coincidencias, necesitas más contexto
- Siempre lee el archivo antes de editar

### grep - Búsqueda de Contenido con Regex

La herramienta `grep` busca patrones de texto en archivos usando expresiones regulares.

```bash
# Búsqueda básica
grep(pattern="function")

# Búsqueda en archivos específicos
grep(pattern="TODO", include="*.ts")

# Regex avanzado
grep(pattern="import.*from ['\"]react['\"]")

# Contar coincidencias
bash("rg -c 'function' src/")
```

**Características:**
- Soporta regex completo
- Filtra por tipo de archivo con include
- Retorna ruta, línea y contenido

### glob - Búsqueda de Archivos por Patrón

La herramienta `glob` encuentra archivos usando patrones de comodín.

```bash
# Todos los archivos TypeScript
glob(pattern="**/*.ts")

# Archivos en directorio específico
glob(pattern="src/**/*.tsx")

# Archivos de configuración
glob(pattern="*.json")

# Combinar patrones
glob(pattern="src/**/*.{ts,tsx}")
```

**Patrones comunes:**
- `*` - Cualquier cosa excepto `/`
- `**` - Cualquier cosa incluyendo `/`
- `?` - Un solo carácter
- `[abc]` - Cualquier carácter del conjunto

## Guía Paso a Paso

### Paso 1: Explorar un Proyecto con bash y read

```bash
# Ver estructura del proyecto
bash("ls -la")

# Ver estructura de directorios
bash("find . -type f -name '*.ts' | head -20")

# Leer package.json para entender dependencias
read("package.json")

# Leer archivo principal
read("src/index.ts")
```

### Paso 2: Buscar Código con grep y glob

```bash
# Encontrar todos los archivos TypeScript
glob(pattern="**/*.ts")

# Buscar todas las funciones exportadas
grep(pattern="export (function|const|class)")

# Buscar TODOs pendientes
grep(pattern="TODO|FIXME|HACK", include="*.ts")

# Encontrar importaciones de React
grep(pattern="import.*React", include="*.{ts,tsx}")
```

### Paso 3: Modificar Archivos con edit

```bash
# Primero lee el archivo
read("src/utils.ts")

# Encuentra la función a modificar
grep(pattern="function calculate", include="*.ts")

# Realiza el reemplazo exacto
edit(
  filePath="src/utils.ts",
  oldString="function calculate(a, b) {",
  newString="function calculate(a: number, b: number): number {"
)
```

### Paso 4: Crear Archivos con write

```bash
# Crear un nuevo componente
write(
  filePath="src/components/Button.tsx",
  content=`import React from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
}

export const Button: React.FC<ButtonProps> = ({ label, onClick }) => {
  return (
    <button onClick={onClick}>
      {label}
    </button>
  );
};`
)
```

### Paso 5: Flujo Completo de Edición

```bash
# 1. Explora la estructura
glob(pattern="src/**/*.ts")

# 2. Lee el archivo objetivo
read("src/services/api.ts")

# 3. Busca el patrón a modificar
grep(pattern="fetch\\(", include="api.ts")

# 4. Modifica con edit
edit(
  filePath="src/services/api.ts",
  oldString="fetch(url)",
  newString="fetch(url, { headers: { 'Content-Type': 'application/json' } })"
)

# 5. Verifica el cambio
bash("git diff src/services/api.ts")
```

## Referencia Rápida

| Herramienta | Uso | Ejemplo |
|-------------|-----|---------|
| `bash` | Ejecutar comando shell | `bash("ls -la")` |
| `read` | Leer archivo | `read("src/main.ts")` |
| `read` | Leer con líneas | `read("f.ts", offset=10, limit=50)` |
| `write` | Crear/sobrescribir | `write("f.ts", "content")` |
| `edit` | Reemplazo exacto | `edit("f.ts", "old", "new")` |
| `edit` | Reemplazar todo | `edit("f.ts", "a", "b", replaceAll=true)` |
| `grep` | Buscar contenido | `grep(pattern="TODO")` |
| `grep` | Buscar en tipo | `grep(pattern="fn", include="*.ts")` |
| `glob` | Encontrar archivos | `glob(pattern="**/*.ts")` |
| `glob` | Patrón complejo | `glob(pattern="src/**/*.{ts,tsx}")` |

## Ejercicios Guiados

### Ejercicio 1: Explorar un Proyecto Desconocido

**Objetivo:** Usar las herramientas de lectura y búsqueda para entender un proyecto nuevo.

**Instrucciones:**
1. Navega a un proyecto que no conozcas
2. Usa bash para ver la estructura de directorios
3. Lee el README.md para entender el proyecto
4. Usa glob para encontrar todos los archivos de código fuente
5. Usa grep para encontrar las exportaciones principales
6. Lee los archivos más importantes
7. Documenta la arquitectura del proyecto

**Solución Esperada:**
```bash
# 1. Estructura
bash("ls -la")
bash("find . -type d | head -20")

# 2. README
read("README.md")

# 3. Archivos fuente
glob(pattern="src/**/*.{ts,tsx,js,jsx}")

# 4. Exportaciones
grep(pattern="export (default|function|class|const)")

# 5-6. Archivos clave
read("src/index.ts")
read("src/App.tsx")
```

### Ejercicio 2: Corregir un Error de Tipado

**Objetivo:** Usar grep para encontrar errores y edit para corregirlos.

**Instrucciones:**
1. Usa grep para buscar tipos `any` en el proyecto
2. Identifica dónde se usan incorrectamente
3. Lee el archivo con el error
4. Usa edit para agregar tipos correctos
5. Verifica el cambio con bash

**Solución Esperada:**
```bash
# 1. Buscar any
grep(pattern=": any", include="*.ts")

# 2. Identificar
# Encuentra: src/utils.ts:15 - const data: any = {}

# 3. Leer
read("src/utils.ts", offset=10, limit=20)

# 4. Corregir
edit(
  filePath="src/utils.ts",
  oldString="const data: any = {}",
  newString="const data: Record<string, unknown> = {}"
)

# 5. Verificar
bash("git diff src/utils.ts")
```

### Ejercicio 3: Crear Archivo de Configuración

**Objetivo:** Usar write para crear un archivo de configuración completo.

**Instrucciones:**
1. Lee existentes archivos de configuración del proyecto
2. Usa grep para entender el formato esperado
3. Crea un nuevo archivo de configuración con write
4. Verifica que el formato sea correcto con bash
5. Valida con un linter si existe

**Solución Esperada:**
```bash
# 1. Leer configs existentes
read("tsconfig.json")
read("package.json")

# 2. Entender formato
grep(pattern="\"compilerOptions\"", include="tsconfig.json")

# 3. Crear nuevo config
write(
  filePath="tsconfig.build.json",
  content=`{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./dist",
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}`
)

# 4-5. Verificar
bash("cat tsconfig.build.json")
bash("npx tsc --showConfig")
```

## Ejercicio Desafío

**Reto:** Realiza una refactorización completa usando todas las herramientas:
1. Usa glob para encontrar todos los archivos afectados
2. Usa grep para identificar el patrón a refactorizar
3. Usa read para entender cada archivo
4. Usa edit para hacer cambios precisos en cada archivo
5. Usa write si necesitas crear archivos nuevos
6. Usa bash para ejecutar tests y verificar que todo funciona

**Pistas:**
- Trabaja en orden lógico (archivos dependientes primero)
- Haz un commit antes de empezar por si necesitas revertir
- Usa bash para ejecutar linters después de cambios

## Recursos Adicionales

- [Documentación de herramientas](https://opencode.ai/docs/tools)
- [Guía de expresiones regulares](https://opencode.ai/docs/regex)
- [Mejores prácticas de refactorización](https://opencode.ai/docs/refactoring)

## Autoevaluación

- [ ] Puedo ejecutar comandos bash correctamente
- [ ] Sé leer archivos con read usando offset y limit
- [ ] Puedo crear archivos con write preservando formato
- [ ] Uso edit para reemplazos exactos sin errores
- [ ] Busco contenido eficientemente con grep
- [ ] Encuentro archivos con glob usando patrones
- [ ] Combino múltiples herramientas en flujos de trabajo
