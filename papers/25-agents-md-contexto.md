---
title: "AGENTS.md y Contexto"
module: 25
duration: "35 min"
prerequisites: "Módulo 24 - Agent Skills"
---

# Clase 25: AGENTS.md y Contexto

## Resumen Ejecutivo

AGENTS.md es un archivo de contexto del proyecto que proporciona a los agentes de OpenCode información esencial sobre la estructura, convenciones y patrones del código fuente. Este archivo se crea automáticamente con el comando `/init` o se puede editar manualmente para incluir detalles específicos del proyecto. AGENTS.md se carga como contexto inicial cada vez que se inicia una nueva conversación, permitiendo a los agentes comprender mejor el proyecto desde el primer momento.

El contenido de AGENTS.md puede incluir estructura del proyecto, convenciones de nomenclatura, patrones arquitectónicos, comandos de build y test, y cualquier otra información relevante para el desarrollo. Este archivo se commitea al repositorio Git, lo que garantiza que todos los miembros del equipo y los agentes tengan acceso a la misma información contextual.

## Objetivos de Aprendizaje
- Crear AGENTS.md usando el comando `/init`
- Editar manualmente AGENTS.md para incluir contexto específico
- Entender qué información incluir en AGENTS.md
- Comprender cómo AGENTS.md mejora el rendimiento de los agentes
- Gestionar AGENTS.md en el repositorio Git

## Conceptos Clave

### ¿Qué es AGENTS.md?

AGENTS.md es un archivo de texto plano que contiene información contextual sobre el proyecto. Los agentes de OpenCode leen este archivo al inicio de cada conversación para comprender:

- Estructura del proyecto
- Convenciones de codificación
- Patrones arquitectónicos
- Comandos disponibles
- Dependencias principales
- Decisiones de diseño

### Creación con /init

El comando `/init` crea automáticamente un AGENTS.md analizando el proyecto:

```
/init
```

Este comando:
1. Analiza la estructura del directorio
2. Identifica archivos de configuración (package.json, tsconfig.json, etc.)
3. Detecta el lenguaje y frameworks utilizados
4. Genera un AGENTS.md con la información básica

### Contenido Recomendado para AGENTS.md

```markdown
# Project Context

## Project Structure
```
src/
├── components/    # UI Components
├── services/      # Business logic
├── utils/         # Utility functions
├── types/         # TypeScript types
└── index.ts       # Entry point
tests/
├── unit/          # Unit tests
└── integration/   # Integration tests
```

## Tech Stack
- Language: TypeScript
- Runtime: Node.js
- Framework: Express
- Testing: Jest
- Linting: ESLint + Prettier

## Naming Conventions
- Files: kebab-case (user-service.ts)
- Classes: PascalCase (UserService)
- Functions: camelCase (getUserById)
- Constants: UPPER_SNAKE_CASE (API_URL)

## Commands
- `npm run dev`: Start development server
- `npm run build`: Build for production
- `npm run test`: Run tests
- `npm run lint`: Run linter

## Architecture Patterns
- Repository Pattern for data access
- Service Layer for business logic
- Controller Pattern for HTTP handlers

## Important Notes
- Always add tests for new features
- Update documentation when changing APIs
- Follow conventional commits for Git
```

### Edición Manual

AGENTS.md se puede editar manualmente para agregar contexto específico que el análisis automático no detecta:

1. **Decisiones de diseño:** Por qué se eligió cierta arquitectura
2. **Configuraciones especiales:** Variables de entorno, feature flags
3. **Procesos del equipo:** Code review, deployment, branching strategy
4. **Conocimiento tácito:** Información que no está documentada en otro lugar

### Commiteo a Git

AGENTS.md se debe commitear al repositorio para que:
- Todos los agentes tengan acceso al mismo contexto
- El contexto persista entre sesiones
- Los miembros del equipo puedan editarlo
- Se mantenga sincronizado con los cambios del proyecto

```bash
# Agregar AGENTS.md al repositorio
git add AGENTS.md
git commit -m "docs: add project context for AI agents"
git push
```

### Instrucciones Adicionales en Config

Además de AGENTS.md, se pueden agregar instrucciones adicionales en `opencode.json`:

```json
{
  "instructions": [
    "Siempre usa TypeScript estricto",
    "Sigue el patrón de repositorio para acceso a datos",
    "Ejecuta lint después de cada cambio",
    "Actualiza los tests cuando modifiques funciones existentes"
  ]
}
```

Estas instrucciones se concatenan al contexto de AGENTS.md.

### Persistencia del Contexto

El contexto de AGENTS.md persiste durante toda la conversación. Los agentes pueden:
- Referenciar información del contexto en sus respuestas
- Tomar decisiones basadas en las convenciones del proyecto
- Evitar contradecir el contexto existente
- Sugerir cambios que respeten la arquitectura actual

## Guía Paso a Paso

### Paso 1: Crear AGENTS.md con /init

```bash
# Navega al directorio raíz de tu proyecto
cd mi-proyecto

# Ejecuta el comando init
opencode

# En el chat de OpenCode:
/init
```

### Paso 2: Revisar el AGENTS.md Generado

```bash
# El comando crea automáticamente AGENTS.md
cat AGENTS.md
```

### Paso 3: Editar Manualmente AGENTS.md

```markdown
# Agregar información específica del proyecto

## Database
- PostgreSQL 14
- Migrations en db/migrations/
- Seeds en db/seeds/

## API Design
- RESTful API
- Versioning: /api/v1/
- Auth: JWT tokens

## Deployment
- Platform: Vercel
- Environment variables en .env.local
- CI/CD: GitHub Actions
```

### Paso 4: Commitear a Git

```bash
git add AGENTS.md
git commit -m "docs: add AGENTS.md with project context"
git push origin main
```

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `/init` | Crear AGENTS.md automáticamente | En chat de OpenCode |
| `AGENTS.md` | Archivo de contexto del proyecto | En raíz del proyecto |
| `instructions` | Instrucciones adicionales en config | En opencode.json |
| `git add AGENTS.md` | Agregar a repositorio | Terminal |

## Ejercicios Guiados

### Ejercicio 1: Crear AGENTS.md con /init
**Objetivo:** Generar automáticamente un AGENTS.md para un proyecto existente.

**Instrucciones:**
1. Navega al directorio raíz de tu proyecto
2. Abre OpenCode
3. Ejecuta el comando `/init`
4. Revisa el archivo AGENTS.md generado
5. Verifica que contiene la información correcta del proyecto

**Solución Esperada:**
```bash
# Después de ejecutar /init, el archivo debería contener
# información similar a esto (adaptada a tu proyecto):
cat AGENTS.md

# Output esperado:
# # Project Context
# 
# ## Tech Stack
# - Language: TypeScript
# - Framework: Next.js
# ...
```

### Ejercicio 2: Editar AGENTS.md Manualmente
**Objetivo:** Agregar contexto específico que el análisis automático no detecta.

**Instrucciones:**
1. Abre AGENTS.md en tu editor de código
2. Agrega una sección sobre la estrategia de base de datos
3. Documenta los comandos de deployment
4. Incluye convenciones específicas del equipo
5. Guarda los cambios

**Solución Esperada:**
```markdown
# Agregar al final de AGENTS.md

## Database Strategy
- ORM: Prisma
- Migrations: Prisma Migrate
- Seeding: ts-node db/seed.ts

## Deployment Process
1. Create PR with changes
2. Wait for CI to pass
3. Get code review approval
4. Merge to main
5. Auto-deploy to Vercel

## Team Conventions
- PR titles follow conventional commits
- Max 400 lines per PR
- Required reviewers: 2
- Squash merge on completion
```

### Ejercicio 3: Verificar Persistencia del Contexto
**Objetivo:** Confirmar que los agentes utilizan el contexto de AGENTS.md en sus respuestas.

**Instrucciones:**
1. Asegúrate de que AGENTS.md existe y tiene contenido
2. Inicia una nueva conversación en OpenCode
3. Pregunta al agente sobre la estructura del proyecto
4. Verifica que la respuesta refleja el contenido de AGENTS.md
5. Cambia algo en AGENTS.md y verifica que se actualiza

**Solución Esperada:**
```
# En el chat de OpenCode:
¿Cuál es la estructura del proyecto?

# Respuesta esperada:
# Basándome en el contexto del proyecto, la estructura es:
# - src/: Código fuente principal
# - tests/: Pruebas unitarias y de integración
# ...
# (La respuesta debería reflejar el contenido de AGENTS.md)
```

## Ejercicio Desafío

**Reto:** Crea un AGENTS.md completo para un proyecto real que incluya:
1. Estructura detallada del proyecto
2. Stack tecnológico completo
3. Convenciones de nomenclatura
4. Patrones arquitectónicos
5. Comandos de desarrollo
6. Procesos del equipo
7. Decisiones de diseño importantes
8. Configuraciones especiales

Luego, verifica que los agentes utilizan correctamente este contexto en sus respuestas.

**Pistas:**
- Incluye tanto información técnica como de proceso
- Documenta decisiones de diseño y sus razones
- Mantén el archivo actualizado con los cambios del proyecto
- Usa formato claro y fácil de escanear

## Recursos Adicionales
- [Documentación oficial de OpenCode - AGENTS.md](https://opencode.ai/docs/agents-md)
- [Guía de creación de AGENTS.md](https://opencode.ai/docs/agents-md/creating)
- [Mejores prácticas para AGENTS.md](https://opencode.ai/docs/agents-md/best-practices)

## Autoevaluación
- [ ] Puedo crear AGENTS.md usando el comando `/init`
- [ ] Sé editar manualmente AGENTS.md para agregar contexto específico
- [ ] Entiendo qué información incluir en AGENTS.md
- [ ] Comprendo cómo AGENTS.md mejora el rendimiento de los agentes
- [ ] Puedo commitear AGENTS.md a Git correctamente
- [ ] Verifico que los agentes utilizan el contexto de AGENTS.md
