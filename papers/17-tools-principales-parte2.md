---
title: "Herramientas Principales - Parte 2"
module: 17
duration: "55 minutos"
prerequisites: "Módulo 16: Herramientas Principales - Parte 1"
---

# Clase 17: Herramientas Principales - Parte 2

## Resumen Ejecutivo

Continuando con las herramientas fundamentales de OpenCode, este módulo cubre herramientas más especializadas: apply_patch para cambios complejos, skill para cargar instrucciones específicas, todowrite para gestión de tareas, webfetch y websearch para contenido web, question para interacción con el usuario, y lsp para soporte de lenguaje.

Estas herramientas complementan las básicas del módulo anterior, permitiendo operaciones más sofisticadas. apply_patch es especialmente útil para cambios grandes, skill permite cargar conhecimento especializado, y las herramientas web conectan OpenCode con información externa en tiempo real.

## Objetivos de Aprendizaje

- Aplicar parches complejos con apply_patch
- Cargar y usar skills especializadas
- Gestionar tareas con todowrite
- Obtener contenido web con webfetch
- Buscar en internet con websearch
- Hacer preguntas al usuario con question
- Entender el soporte LSP experimental

## Conceptos Clave

### apply_patch - Aplicar Parches

La herramienta `apply_patch` aplica cambios múltiples a archivos de forma atómica. Es ideal para refactorizaciones grandes o cambios que afectan múltiples archivos.

```bash
# Parche básico
apply_patch(
  patch=`--- a/src/main.ts
+++ b/src/main.ts
@@ -10,7 +10,7 @@
 import { helper } from './utils';
 
-function oldFunction() {
+function newFunction() {
   // implementation
 }
`
)

# Parche multi-archivo
apply_patch(
  patch=`--- a/src/app.ts
+++ b/src/app.ts
@@ -5,3 +5,4 @@
 import { oldFunction } from './utils';
+import { newHelper } from './helpers';
 
-oldFunction();
+newFunction();
--- a/src/utils.ts
+++ b/src/utils.ts
@@ -1,3 +1,3 @@
-export function oldFunction() {
+export function newFunction() {
`
)
```

**Ventajas sobre edit:**
- Cambios atómicos (todo o nada)
- Múltiples archivos en una operación
- Manejo de contexto con líneas @@ 
- Ideal para cambios grandes

### skill - Cargar Skills

La herramienta `skill` carga archivos SKILL.md con instrucciones especializadas para tareas específicas.

```bash
# Cargar una skill
skill(name="testing")

# Cargar skill de un proyecto específico
skill(name="react-component")

# La skill se carga y da contexto adicional
# al asistente para esa tarea específica
```

**Skills comunes:**
- `testing`: Pruebas unitarias y de integración
- `refactoring`: Mejores prácticas de refactorización
- `documentation`: Generación de documentación
- `security`: Auditoría de seguridad

### todowrite - Gestión de Tareas

La herramienta `todowrite` crea y gestiona listas de tareas para organizar el trabajo.

```bash
# Crear lista de tareas
todowrite(
  tasks=[
    "Analizar código existente",
    "Identificar áreas de mejora",
    "Crear tests para funciones críticas",
    "Refactorizar módulo de autenticación",
    "Actualizar documentación"
  ]
)

# Marcar tarea como completada
todowrite(
  tasks=["Analizar código existente"],
  completed=true
)

# Obtener estado actual
todowrite()
```

### webfetch - Obtener Contenido Web

La herramienta `webfetch` descarga y analiza contenido de páginas web.

```bash
# Obtener documentación
webfetch(
  url="https://docs.ejemplo.com/api",
  format="markdown"
)

# Obtener datos de API
webfetch(
  url="https://api.ejemplo.com/data",
  format="text"
)

# Obtener HTML completo
webfetch(
  url="https://ejemplo.com",
  format="html"
)
```

**Formatos disponibles:**
- `markdown` (predeterminado): Convierte a markdown legible
- `text`: Solo texto sin formato
- `html`: HTML completo

### websearch - Búsqueda Web

La herramienta `websearch` busca en internet usando Exa AI.

```bash
# Búsqueda básica
websearch(query="cómo implementar autenticación JWT")

# Búsqueda con filtros
websearch(
  query="mejores prácticas React hooks",
  numResults=5
)

# Búsqueda profunda
websearch(
  query="migración PostgreSQL a MongoDB",
  type="deep",
  numResults=10
)
```

**Parámetros:**
- `query`: Términos de búsqueda
- `numResults`: Número de resultados (default: 8)
- `type`: auto, fast, deep
- `livecrawl`: fallback, preferred

### question - Preguntar al Usuario

La herramienta `question` hace preguntas interactivas al usuario para obtener información o confirmaciones.

```bash
# Pregunta simple
question(
  question="¿Qué framework de testing prefieres?",
  options=["Jest", "Vitest", "Mocha"]
)

# Pregunta con confirmación
question(
  question="¿Deseas eliminar este archivo?",
  options=["Sí, eliminar", "No, cancelar"]
)

# Pregunta abierta
question(
  question="Describe el problema que encuentras:",
  options=["Problema de rendimiento", "Bug visual", "Error de tipado", "Otro"]
)
```

### lsp - Language Server Protocol (Experimental)

La herramienta `lsp` proporciona soporte de lenguaje en tiempo real: autocompletado, errores, y navegación de código.

```bash
# Obtener errores del archivo
lsp(
  command="textDocument/diagnostic",
  filePath="src/main.ts"
)

# Obtener información de símbolo
lsp(
  command="textDocument/hover",
  filePath="src/main.ts",
  position={"line": 10, "character": 5}
)

# Formatear archivo
lsp(
  command="textDocument/formatting",
  filePath="src/main.ts"
)
```

**NOTA:** El soporte LSP es experimental y puede no estar disponible en todas las configuraciones.

## Guía Paso a Paso

### Paso 1: Aplicar Parche Complejo

```bash
# Primero, analiza los archivos afectados
glob(pattern="src/**/*.ts")
grep(pattern="function oldName", include="*.ts")

# Lee cada archivo para entender el contexto
read("src/utils.ts")
read("src/services/api.ts")

# Aplica el parche multi-archivo
apply_patch(
  patch=`--- a/src/utils.ts
+++ b/src/utils.ts
@@ -1,5 +1,5 @@
-export function oldName() {
+export function newName() {
   // implementation
 }
--- a/src/services/api.ts
+++ b/src/services/api.ts
@@ -3,3 +3,3 @@
-import { oldName } from '../utils';
+import { newName } from '../utils';
`
)

# Verifica los cambios
bash("git diff")
```

### Paso 2: Usar Skills para Tareas Especializadas

```bash
# Carga la skill de testing antes de crear tests
skill(name="testing")

# Ahora el asistente tiene contexto de mejores prácticas
> Crea tests unitarios para la función calculate

# La skill proporciona:
# - Estructura de archivos de test
# - Patrones de naming
# - Casos de prueba comunes
```

### Paso 3: Gestionar Proyecto con todowrite

```bash
# Crea una lista de tareas para una feature
todowrite(
  tasks=[
    "Diseñar API del endpoint",
    "Implementar controlador",
    "Crear modelos de datos",
    "Escribir tests unitarios",
    "Documentar endpoints",
    "Revisar código"
  ]
)

# A medida que avanzas, marca tareas
todowrite(
  tasks=["Diseñar API del endpoint"],
  completed=true
)

# Consulta el progreso
todowrite()
```

### Paso 4: Obtener Información Web

```bash
# Busca documentación oficial
websearch(query="Node.js express middleware documentation")

# Obtén contenido específico
webfetch(
  url="https://expressjs.com/en/guide/routing.html",
  format="markdown"
)

# Usa la información en tu código
> Basándote en la documentación, crea un middleware de autenticación
```

### Paso 5: Interacción con el Usuario

```bash
# Pregunta sobre preferencias
question(
  question="¿Qué base de datos usarás?",
  options=["PostgreSQL", "MySQL", "MongoDB", "SQLite"]
)

# Confirmación antes de cambios destructivos
question(
  question="Voy a eliminar el archivo old.ts. ¿Confirmas?",
  options=["Sí, eliminar", "No, mantener"]
)
```

## Referencia Rápida

| Herramienta | Uso | Ejemplo |
|-------------|-----|---------|
| `apply_patch` | Parches multi-archivo | `apply_patch(patch="...")` |
| `skill` | Cargar skill | `skill(name="testing")` |
| `todowrite` | Crear tareas | `todowrite(tasks=[...])` |
| `todowrite` | Completar tarea | `todowrite(tasks=["t"], completed=true)` |
| `webfetch` | Obtener URL | `webfetch(url="...", format="markdown")` |
| `websearch` | Buscar web | `websearch(query="...")` |
| `question` | Preguntar usuario | `question(question="...", options=[...])` |
| `lsp` | Soporte lenguaje | `lsp(command="...", filePath="...")` |

## Ejercicios Guiados

### Ejercicio 1: Refactorización con apply_patch

**Objetivo:** Realizar una refactorización multi-archivo usando parches.

**Instrucciones:**
1. Identifica un patrón de código duplicado
2. Analiza todos los archivos afectados
3. Diseña la solución (extraer función, cambiar nombre, etc.)
4. Crea un parche que modifique todos los archivos
5. Aplica el parche de forma atómica
6. Verifica que todos los cambios se aplicaron correctamente

**Solución Esperada:**
```bash
# 1-2. Análisis
grep(pattern="duplicatePattern", include="*.ts")
read("src/a.ts")
read("src/b.ts")
read("src/c.ts")

# 3-4. Crear parche
apply_patch(
  patch=`--- a/src/shared.ts
+++ b/src/shared.ts
@@ -1,0 +1,5 @@
+export function extractedFunction() {
+  // lógica común
+}
--- a/src/a.ts
+++ b/src/a.ts
@@ -5,3 +5,3 @@
-import { duplicatePattern } from './b';
+import { extractedFunction } from './shared';
`
)

# 5-6. Verificar
bash("git diff --stat")
bash("npm test")
```

### Ejercicio 2: Investigar con Web Tools

**Objetivo:** Usar webfetch y websearch para resolver un problema técnico.

**Instrucciones:**
1. Identifica un problema o duda técnica
2. Usa websearch para encontrar soluciones
3. Usa webfetch para leer documentación específica
4. Analiza la información obtenida
5. Implementa la solución basándote en lo aprendido
6. Documenta la investigación

**Solución Esperada:**
```bash
# 1. Problema: "¿Cómo manejar rate limiting en Express?"

# 2. Buscar
websearch(query="express rate limiting middleware best practices")

# 3. Obtener docs
webfetch(
  url="https://www.npmjs.com/package/express-rate-limit",
  format="markdown"
)

# 4-5. Implementar
> Implementa rate limiting basándote en la documentación

# 6. Documentar
write(
  filePath="docs/rate-limiting.md",
  content="# Rate Limiting\n\nImplementado con express-rate-limit..."
)
```

### Ejercicio 3: Gestión de Proyecto con todowrite

**Objetivo:** Organizar un proyecto completo usando la herramienta de tareas.

**Instrucciones:**
1. Crea una lista de tareas para una feature completa
2. Divide las tareas grandes en subtareas
3. Marca tareas completadas a medida que avanzas
4. Consulta el progreso regularmente
5. Reorganiza tareas si es necesario
6. Genera un reporte final del proyecto

**Solución Esperada:**
```bash
# 1. Lista inicial
todowrite(
  tasks=[
    "Diseñar schema de base de datos",
    "Crear migraciones",
    "Implementar modelos",
    "Crear endpoints CRUD",
    "Implementar autenticación",
    "Escribir tests",
    "Documentar API",
    "Configurar CI/CD"
  ]
)

# 2. Subtareas
todowrite(
  tasks=[
    "Diseñar schema de base de datos",
    "Crear tabla usuarios",
    "Crear tabla posts",
    "Crear tabla comentarios"
  ]
)

# 3-5. Avanzar y consultar
todowrite(tasks=["Diseñar schema de base de datos"], completed=true)
todowrite()  # Ver progreso

# 6. Reporte
bash("echo 'Proyecto completado al 25%' > reporte.txt")
```

## Ejercicio Desafío

**Reto:** Crea un flujo de investigación e implementación:
1. Usa websearch para encontrar mejores prácticas para una tecnología específica
2. Usa webfetch para obtener documentación detallada
3. Crea una skill personalizada con los patrones encontrados
4. Usa todowrite para planificar la implementación
5. Implementa usando apply_patch para cambios multi-archivo
6. Usa question para validar decisiones de diseño
7. Documenta todo el proceso

**Pistas:**
- Combina múltiples fuentes de información
- Valida la información con múltiples búsquedas
- Documenta cada paso del proceso

## Recursos Adicionales

- [Documentación de apply_patch](https://opencode.ai/docs/tools#apply-patch)
- [Guía de skills](https://opencode.ai/docs/skills)
- [Integración con LSP](https://opencode.ai/docs/lsp)

## Autoevaluación

- [ ] Puedo usar apply_patch para cambios multi-archivo
- [ ] Sé cargar skills para tareas especializadas
- [ ] Gestiono tareas eficientemente con todowrite
- [ ] Obtengo información web con webfetch
- [ ] Busco documentación con websearch
- [ ] Hago preguntas al usuario con question
- [ ] Entiendo el propósito del soporte LSP
