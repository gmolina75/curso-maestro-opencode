---
title: "Configuración de Permisos"
module: 18
duration: "50 minutos"
prerequisites: "Módulo 17: Herramientas Principales - Parte 2"
---

# Clase 18: Configuración de Permisos

## Resumen Ejecutivo

El sistema de permisos de OpenCode controla qué herramientas pueden ejecutarse automáticamente, cuáles requieren confirmación, y cuáles están bloqueadas. Este control es fundamental para mantener la seguridad del proyecto mientras permites que OpenCode trabaje de manera eficiente. Los permisos se configuran en `opencode.json` y se pueden ajustar por herramienta, por tipo de operación, o por proyecto.

Un sistema de permisos bien configurado equilibra automatización y control. Puedes permitir operaciones seguras como lectura de archivos mientras solicitás confirmación para escritura, o bloquear completamente operaciones peligrosas como eliminación de archivos.

## Objetivos de Aprendizaje

- Comprender los valores de permisos (allow, deny, ask)
- Configurar permisos por herramienta
- Usar patrones glob para múltiples herramientas
- Gestionar permisos de servidores MCP
- Establecer comportamientos por defecto
- Crear configuraciones de seguridad por proyecto

## Conceptos Clave

### Valores de Permisos

OpenCode usa tres valores para permisos:

| Valor | Comportamiento |
|-------|----------------|
| `allow` | Ejecuta automáticamente sin preguntar |
| `deny` | Bloquea la operación completamente |
| `ask` | Pide confirmación al usuario antes de ejecutar |

```json
{
  "permissions": {
    "tool_name": "allow"
  }
}
```

### Permisos por Herramienta

Cada herramienta tiene su propio permiso:

```json
{
  "permissions": {
    "read": "allow",
    "write": "ask",
    "edit": "ask",
    "bash": "ask",
    "glob": "allow",
    "grep": "allow",
    "webfetch": "allow",
    "websearch": "allow",
    "apply_patch": "ask",
    "skill": "allow",
    "todowrite": "allow",
    "question": "allow"
  }
}
```

### Configuración de Bash

Bash tiene configuración avanzada por tipo de comando:

```json
{
  "permissions": {
    "bash": {
      "default": "ask",
      "allow": [
        "ls",
        "pwd",
        "echo",
        "cat",
        "git status",
        "git log",
        "npm test",
        "npm run lint"
      ],
      "deny": [
        "rm -rf",
        "sudo",
        "chmod 777",
        "curl | bash"
      ]
    }
  }
}
```

### Patrones Glob para Múltiples Herramientas

Usa `*` para aplicar permisos a múltiples herramientas:

```json
{
  "permissions": {
    "*": "ask",
    "read": "allow",
    "glob": "allow",
    "grep": "allow"
  }
}
```

Esto configura:
- Todas las herramientas en "ask" por defecto
- Lectura y búsqueda en "allow" (automático)

### Permisos de Servidores MCP

Los servidores MCP tienen permisos separados:

```json
{
  "permissions": {
    "mcp": {
      "filesystem": {
        "read": "allow",
        "write": "ask"
      },
      "database": {
        "query": "allow",
        "modify": "ask",
        "drop": "deny"
      },
      "github": {
        "read": "allow",
        "write": "ask",
        "admin": "deny"
      }
    }
  }
}
```

### Comportamiento por Defecto

Si no se especifica un permiso, OpenCode usa valores por defecto seguros:

```json
{
  "permissions": {
    // Herramientas de lectura: allow por defecto
    "read": "allow",
    "glob": "allow",
    "grep": "allow",
    
    // Herramientas de escritura: ask por defecto
    "write": "ask",
    "edit": "ask",
    "bash": "ask",
    "apply_patch": "ask"
  }
}
```

### Configuración por Proyecto

Cada proyecto puede tener su propia configuración de permisos en `.opencode/permissions.json`:

```json
{
  "permissions": {
    "bash": {
      "default": "ask",
      "allow": [
        "npm *",
        "yarn *",
        "pnpm *",
        "git *"
      ],
      "deny": [
        "rm -rf *",
        "sudo *"
      ]
    },
    "write": "ask",
    "edit": "ask"
  }
}
```

## Guía Paso a Paso

### Paso 1: Configurar Permisos Básicos

```bash
# Crea o edita opencode.json en la raíz del proyecto
cat > opencode.json << EOF
{
  "permissions": {
    "read": "allow",
    "write": "ask",
    "edit": "ask",
    "bash": "ask",
    "glob": "allow",
    "grep": "allow"
  }
}
EOF
```

### Paso 2: Configurar Permisos de Bash

```json
{
  "permissions": {
    "bash": {
      "default": "ask",
      "allow": [
        "ls",
        "pwd",
        "echo",
        "git status",
        "git log --oneline",
        "git diff",
        "npm test",
        "npm run lint",
        "npm run build"
      ],
      "deny": [
        "rm -rf /",
        "sudo *",
        "chmod 777 *",
        "curl | bash",
        "wget | bash"
      ]
    }
  }
}
```

### Paso 3: Configurar Permisos de MCP

```json
{
  "permissions": {
    "mcp": {
      "filesystem": {
        "read": "allow",
        "write": "ask",
        "delete": "deny"
      },
      "database": {
        "query": "allow",
        "insert": "ask",
        "update": "ask",
        "delete": "ask",
        "drop": "deny"
      }
    }
  }
}
```

### Paso 4: Usar Patrones Glob

```json
{
  "permissions": {
    "*": "ask",
    "read": "allow",
    "glob": "allow",
    "grep": "allow",
    "webfetch": "allow",
    "websearch": "allow",
    "todowrite": "allow",
    "skill": "allow"
  }
}
```

### Paso 5: Configuración Completa de Ejemplo

```json
{
  "permissions": {
    "*": "ask",
    "read": "allow",
    "glob": "allow",
    "grep": "allow",
    "webfetch": "allow",
    "websearch": "allow",
    "todowrite": "allow",
    "skill": "allow",
    "question": "allow",
    "write": "ask",
    "edit": "ask",
    "apply_patch": "ask",
    "bash": {
      "default": "ask",
      "allow": [
        "ls",
        "pwd",
        "cat",
        "head",
        "tail",
        "git *",
        "npm test",
        "npm run *",
        "yarn *",
        "pnpm *"
      ],
      "deny": [
        "rm -rf *",
        "sudo *",
        "chmod 777 *",
        "curl | bash",
        "wget | bash"
      ]
    },
    "mcp": {
      "filesystem": {
        "read": "allow",
        "write": "ask"
      }
    }
  }
}
```

## Referencia Rápida

| Herramienta | Valor por Defecto | Recomendación |
|-------------|-------------------|---------------|
| `read` | allow | Mantener allow |
| `glob` | allow | Mantener allow |
| `grep` | allow | Mantener allow |
| `write` | ask | Mantener ask |
| `edit` | ask | Mantener ask |
| `bash` | ask | Configurar allow/deny específicos |
| `apply_patch` | ask | Mantener ask |
| `webfetch` | allow | Mantener allow |
| `websearch` | allow | Mantener allow |
| `skill` | allow | Mantener allow |
| `todowrite` | allow | Mantener allow |
| `question` | allow | Mantener allow |

## Ejercicios Guiados

### Ejercicio 1: Configurar Permisos de Desarrollo

**Objetivo:** Crear una configuración de permisos equilibrada para desarrollo.

**Instrucciones:**
1. Analiza las herramientas que usas frecuentemente
2. Configura "allow" para operaciones de lectura seguras
3. Configura "ask" para operaciones de escritura
4. Configura "deny" para operaciones destructivas
5. Prueba cada configuración
6. Ajusta según tu flujo de trabajo

**Solución Esperada:**
```json
{
  "permissions": {
    "read": "allow",
    "glob": "allow",
    "grep": "allow",
    "write": "ask",
    "edit": "ask",
    "bash": {
      "default": "ask",
      "allow": ["ls", "git *", "npm *"],
      "deny": ["rm -rf", "sudo *"]
    }
  }
}
```

### Ejercicio 2: Configurar Permisos para Equipo

**Objetivo:** Crear permisos que sean seguros para un equipo de desarrollo.

**Instrucciones:**
1. Considera diferentes niveles de experiencia del equipo
2. Bloquea comandos destructivos comunes
3. Permite operaciones de lectura y búsqueda
4. Solicita confirmación para escritura
5. Documenta cada decisión de permiso
6. Comparte la configuración con el equipo

**Solución Esperada:**
```json
{
  "permissions": {
    "*": "ask",
    "read": "allow",
    "glob": "allow",
    "grep": "allow",
    "webfetch": "allow",
    "bash": {
      "default": "ask",
      "allow": [
        "git status",
        "git log",
        "git diff",
        "npm test",
        "npm run lint",
        "npm run build",
        "ls",
        "pwd"
      ],
      "deny": [
        "rm -rf *",
        "sudo *",
        "chmod 777 *",
        "curl | bash",
        "wget | bash",
        "dd *",
        "mkfs *"
      ]
    }
  }
}
```

### Ejercicio 3: Configurar Permisos por Proyecto

**Objetivo:** Crear configuraciones diferentes para diferentes tipos de proyecto.

**Instrucciones:**
1. Proyecto frontend: permisos más abiertos para build tools
2. Proyecto backend: permisos más restrictivos para base de datos
3. Proyecto de datos: permisos para ejecutar scripts de procesamiento
4. Documenta las diferencias entre proyectos
5. Crea un template reutilizable

**Solución - Frontend:**
```json
{
  "permissions": {
    "bash": {
      "allow": ["npm *", "yarn *", "npx *"],
      "deny": ["rm -rf node_modules"]
    }
  }
}
```

**Solución - Backend:**
```json
{
  "permissions": {
    "bash": {
      "allow": ["npm test", "npm run migrate"],
      "deny": ["npm run db:drop", "sudo *"]
    },
    "mcp": {
      "database": {
        "query": "allow",
        "modify": "ask",
        "drop": "deny"
      }
    }
  }
}
```

## Ejercicio Desafío

**Reto:** Diseña un sistema de permisos completo:
1. Analiza un proyecto real y sus necesidades de seguridad
2. Crea una configuración de permisos por defecto
3. Agrega permisos específicos para cada herramienta
4. Configura permisos MCP para servicios externos
5. Documenta cada decisión de seguridad
6. Crea un script para validar la configuración
7. Prueba con diferentes escenarios de uso

**Pistas:**
- Piensa en el peor caso posible para cada permiso
- Usa deny para operaciones que nunca deberían ejecutarse
- Documenta TODO para auditorías futuras
- Revisa permisos regularmente

## Recursos Adicionales

- [Documentación de permisos](https://opencode.ai/docs/permissions)
- [Guía de seguridad](https://opencode.ai/docs/security)
- [Configuración MCP](https://opencode.ai/docs/mcp)

## Autoevaluación

- [ ] Entiendo los tres valores de permisos (allow, deny, ask)
- [ ] Puedo configurar permisos por herramienta
- [ ] Uso patrones glob para configuraciones amplias
- [ ] Configuro permisos de bash con allow/deny
- [ ] Gestión permisos de servidores MCP
- [ ] Creo configuraciones por proyecto
- [ ] Documento mis decisiones de permisos
