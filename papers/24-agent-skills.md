---
title: "Agent Skills"
module: 24
duration: "40 min"
prerequisites: "Módulo 23 - Agentes Custom"
---

# Clase 24: Agent Skills

## Resumen Ejecutivo

Los skills (habilidades) son instrucciones reutilizables que los agentes de OpenCode pueden descubrir y cargar bajo demanda. A diferencia de los prompts estáticos, los skills se activan dinámicamente cuando el agente detecta que una tarea requiere conocimientos especializados. Los skills se almacenan como archivos Markdown con frontmatter YAML en directorios específicos y pueden controlarse mediante permisos y configuración por agente.

El sistema de skills está diseñado para promover la reutilización de conocimiento especializado. Un skill bien diseñado puede ser compartido entre proyectos, miembros del equipo, o incluso la comunidad. Los skills permiten encapsular best practices, patrones de diseño, y procedimientos específicos sin duplicar información en cada agente.

## Objetivos de Aprendizaje
- Comprender qué son los skills y cómo se descubren automáticamente
- Crear skills personalizados con frontmatter YAML
- Configurar permisos de acceso por skill
- Controlar la carga de skills por agente
- Solucionar problemas comunes de descubrimiento de skills

## Conceptos Clave

### ¿Qué son los Skills?

Los skills son instrucciones reutilizables que se cargan bajo demanda cuando un agente detecta que una tarea requiere conocimientos especializados. Funcionan como módulos de conocimiento que se activan dinámicamente.

**Características principales:**
- Carga bajo demanda (on-demand loading)
- Descubrimiento automático por los agentes
- Frontmatter YAML para metadatos
- Control de permisos granular
- Reutilizabilidad entre proyectos

### Ubicaciones de Skills

OpenCode busca skills en múltiples ubicaciones siguiendo un orden de prioridad:

| Ubicación | Prioridad | Alcance |
|-----------|-----------|---------|
| `.opencode/skills/` | 1 (Mayor) | Proyecto actual |
| `.claude/skills/` | 2 | Proyecto actual (compatibilidad) |
| `.agents/skills/` | 3 | Proyecto actual (compatibilidad) |
| `~/.config/opencode/skills/` | 4 (Menor) | Global (todos los proyectos) |

Los skills en el directorio del proyecto tienen prioridad sobre los globales, permitiendo override por proyecto.

### Estructura de un Archivo de Skill

Cada skill se define como un archivo Markdown con frontmatter YAML:

```markdown
---
name: "security-audit"
description: "Realizar auditorías de seguridad en código"
version: "1.0.0"
author: "Equipo de Seguridad"
tags:
  - security
  - audit
  - best-practices
permission:
  tools:
    - read
    - grep
    - glob
  agents:
    - build
    - code-reviewer
---

# Auditoría de Seguridad

## Procedimiento de Auditoría

### 1. Análisis de Dependencias
Verifica las dependencias del proyecto en busca de vulnerabilidades conocidas.

### 2. Revisión de Código Sensible
Busca patrones de código que puedan representar riesgos:
- Inyección de SQL
- Cross-Site Scripting (XSS)
- Manejo inseguro de autenticación
- Exposición de datos sensibles

### 3. Validación de Entrada
Verifica que todos los puntos de entrada validen y sanitizen los datos.

### 4. Análisis de Permisos
Revisa la configuración de permisos y acceso.

## Formato del Reporte
Para cada hallazgo, incluye:
- Severidad (Crítica, Alta, Media, Baja)
- Ubicación exacta
- Descripción del problema
- Impacto potencial
- Recomendación de remediación
```

### Carga Bajo Demanda (On-Demand Loading)

Los skills se cargan cuando el agente detecta que una tarea requiere los conocimientos encapsulados en el skill. El agente utiliza el tool `skill` para cargar el skill apropiado.

```
# El agente detecta que necesita conocimientos de seguridad
# y carga el skill automáticamente
skill(name="security-audit")
```

### Control de Permisos por Skill

Los permisos controlan qué agentes pueden cargar un skill y qué herramientas tienen disponibles durante su ejecución:

```yaml
permission:
  tools:
    - read
    - grep
    - glob
  agents:
    - build
    - code-reviewer
```

- `tools`: Herramientas disponibles cuando el skill está activo
- `agents`: Agentes que pueden cargar el skill

### Override de Skills por Agente

Los agentes pueden configurar qué skills están disponibles o deshabilitados en su configuración:

```json
// En la configuración del agente
{
  "agent": {
    "skills": {
      "disabled": ["old-skill-1", "old-skill-2"],
      "priority": ["security-audit", "code-review"]
    }
  }
}
```

### Deshabilitar Skills

Para deshabilitar un skill específico, se puede:

1. **Por agente:** Agregar el skill a la lista `disabled` en la configuración del agente
2. **Por proyecto:** Eliminar o renombrar el archivo del skill
3. **Por permisos:** Configurar permisos que excluyan el agente actual

### Troubleshooting de Skills

Problemas comunes y soluciones:

| Problema | Causa | Solución |
|----------|-------|----------|
| Skill no se carga | Frontmatter YAML inválido | Verificar sintaxis YAML |
| Skill no se descubre | Archivo en ubicación incorrecta | Mover a `.opencode/skills/` |
| Permiso denegado | Agente no en lista de permitidos | Actualizar permisos del skill |
| Skill cargado incorrectamente | Nombre duplicado | Verificar unicidad de nombres |

## Guía Paso a Paso

### Paso 1: Crear el Directorio de Skills

```bash
# Crear directorio para skills del proyecto
mkdir -p .opencode/skills

# O para skills globales
mkdir -p ~/.config/opencode/skills
```

### Paso 2: Crear un Skill de Ejemplo

```markdown
<!-- .opencode/skills/testing-patterns.md -->
---
name: "testing-patterns"
description: "Patrones y best practices para testing"
version: "1.0.0"
author: "Equipo QA"
tags:
  - testing
  - patterns
  - best-practices
permission:
  tools:
    - read
    - grep
    - glob
    - bash
  agents:
    - build
    - testing-assistant
---

# Patrones de Testing

## Unit Testing

### Principios AAA (Arrange, Act, Assert)
```javascript
describe('UserService', () => {
  it('should create a new user', () => {
    // Arrange
    const userData = { name: 'John', email: 'john@example.com' };
    const mockRepository = { save: jest.fn() };
    
    // Act
    const result = await userService.createUser(userData);
    
    // Assert
    expect(result).toBeDefined();
    expect(mockRepository.save).toHaveBeenCalledWith(userData);
  });
});
```

### Testing de Excepciones
```javascript
it('should throw error for invalid email', async () => {
  // Arrange
  const invalidEmail = 'not-an-email';
  
  // Act & Assert
  await expect(userService.createUser({ email: invalidEmail }))
    .rejects.toThrow('Invalid email format');
});
```

## Integration Testing

### Setup y Teardown
```javascript
beforeAll(async () => {
  await database.connect();
});

afterAll(async () => {
  await database.disconnect();
});

beforeEach(async () => {
  await database.clear();
});
```
```

### Paso 3: Verificar el Descubrimiento del Skill

```bash
# Reiniciar OpenCode para cargar los nuevos skills
opencode

# En el chat, solicita una tarea que active el skill
Crea pruebas unitarias para el módulo de autenticación
```

### Paso 4: Verificar la Carga del Skill

El agente debería cargar automáticamente el skill `testing-patterns` cuando detecte que la tarea requiere conocimientos de testing.

## Referencia Rápida

| Comando/Config | Descripción | Ejemplo |
|----------------|-------------|---------|
| `.opencode/skills/` | Directorio de skills del proyecto | - |
| `~/.config/opencode/skills/` | Directorio global de skills | - |
| `name` | Nombre único del skill | `"security-audit"` |
| `description` | Descripción del skill | `"Auditorías de seguridad"` |
| `version` | Versión del skill | `"1.0.0"` |
| `permission.tools` | Herramientas disponibles | `["read", "grep"]` |
| `permission.agents` | Agentes permitidos | `["build"]` |
| `skill(name="...")` | Carga manual de skill | En conversación |

## Ejercicios Guiados

### Ejercicio 1: Crear un Skill de Documentación
**Objetivo:** Crear un skill que proporcione instrucciones para generar documentación de alta calidad.

**Instrucciones:**
1. Crea el directorio `.opencode/skills/` si no existe
2. Crea un archivo `documentation-generator.md` con frontmatter YAML
3. Define permisos para agentes de documentación
4. Incluye patrones de documentación para diferentes tipos de archivos
5. Verifica que el skill se descubre correctamente

**Solución Esperada:**
```markdown
---
name: "documentation-generator"
description: "Generar documentación técnica de alta calidad"
version: "1.0.0"
author: "Equipo de Documentación"
tags:
  - documentation
  - markdown
  - api-docs
permission:
  tools:
    - read
    - write
    - edit
    - grep
    - glob
  agents:
    - build
    - documenter
---

# Generador de Documentación

## Tipos de Documentación

### README.md
Estructura recomendada:
1. Título y descripción
2. Instalación
3. Uso rápido
4. API Reference
5. Contributing
6. License

### API Documentation
Para cada endpoint incluir:
- Método HTTP
- URL
- Parámetros
- Ejemplo de request/response
- Códigos de error

### Code Comments
Reglas para comentarios:
- Explicar POR QUÉ, no QUÉ
- Actualizar cuando cambie el código
- Usar formato JSDoc/TSDoc
```

### Ejercicio 2: Configurar Permisos de Skill
**Objetivo:** Configurar permisos granulares para controlar el acceso a un skill.

**Instrucciones:**
1. Crea un skill `database-operations.md` con permisos restringidos
2. Configura herramientas específicas para operaciones de base de datos
3. Limita el acceso a agentes específicos
4. Verifica que otros agentes no pueden cargar el skill

**Solución Esperada:**
```markdown
---
name: "database-operations"
description: "Operaciones seguras de base de datos"
version: "1.0.0"
author: "Equipo de Backend"
tags:
  - database
  - sql
  - operations
permission:
  tools:
    - read
    - grep
    - bash
  agents:
    - build
    - db-admin
  bash_commands:
    - "npm run db:migrate"
    - "npm run db:seed"
    - "npm run db:backup"
---

# Operaciones de Base de Datos

## Migraciones
Ejecutar migraciones de forma segura:
```bash
npm run db:migrate
```

## Seed Data
Poblar la base de datos con datos de prueba:
```bash
npm run db:seed
```

## Backup
Crear copias de seguridad:
```bash
npm run db:backup
```
```

### Ejercicio 3: Override de Skills por Proyecto
**Objetivo:** Crear un skill global y overridearlo con uno específico del proyecto.

**Instrucciones:**
1. Crea un skill global en `~/.config/opencode/skills/general-patterns.md`
2. Crea un skill del proyecto en `.opencode/skills/general-patterns.md`
3. Verifica que el skill del proyecto tiene prioridad
4. Modifica el skill del proyecto y verifica que se carga la versión local

**Solución Esperada:**
```markdown
<!-- ~/.config/opencode/skills/general-patterns.md (Global) -->
---
name: "general-patterns"
description: "Patrones generales de codificación"
version: "1.0.0"
---
# Patrones Generales
Contenido global...

<!-- .opencode/skills/general-patterns.md (Proyecto) -->
---
name: "general-patterns"
description: "Patrones específicos del proyecto"
version: "1.0.0"
---
# Patrones del Proyecto
Contenido específico del proyecto...
```

## Ejercicio Desafío

**Reto:** Crea un ecosistema completo de skills para un proyecto:
1. Un skill `security-audit` para auditorías de seguridad
2. Un skill `performance-analysis` para análisis de rendimiento
3. Un skill `accessibility-check` para verificación de accesibilidad
4. Un skill `api-design` para diseño de APIs RESTful

Cada skill debe tener permisos específicos, tags para descubrimiento, y contenido detallado con ejemplos de código. Configura los skills para que solo ciertos agentes puedan acceder a ellos.

**Pistas:**
- Usa tags consistentes para facilitar el descubrimiento
- Incluye ejemplos de código reales en cada skill
- Documenta claramente los permisos requeridos
- Considera la reutilizabilidad entre proyectos

## Recursos Adicionales
- [Documentación oficial de OpenCode - Skills](https://opencode.ai/docs/skills)
- [Guía de creación de skills](https://opencode.ai/docs/skills/creating)
- [Referencia de permisos de skills](https://opencode.ai/docs/skills/permissions)

## Autoevaluación
- [ ] Entiendo qué son los skills y cómo se cargan bajo demanda
- [ ] Puedo crear un skill con frontmatter YAML válido
- [ ] Sé configurar permisos de acceso por skill
- [ ] Comprendo las ubicaciones de skills y su prioridad
- [ ] Puedo solucionar problemas comunes de descubrimiento
- [ ] Sé hacer override de skills por proyecto
