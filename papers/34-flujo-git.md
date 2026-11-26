---
title: "Clase 34: Flujo de Trabajo con Git"
module: 34
duration: "1.5 horas"
prerequisites: "Módulo 33 - Clase 33: Gestión de Contexto y Tokens"
---

# Clase 34: Flujo de Trabajo con Git

## Resumen Ejecutivo

Esta clase cubre flujo de trabajo con git. OpenCode detecta automáticamente repositorios Git /undo y /redo dependen de Git para revertir cambios El agente puede ejecutar comandos git vía tool bash.

A lo largo de la sesión se exploran los siguientes temas: git en opencode, commits y branches, resolución de conflictos, preparación de pull requests. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- OpenCode detecta automáticamente repositorios Git
- /undo y /redo dependen de Git para revertir cambios
- El agente puede ejecutar comandos git vía tool bash
- Recomendado: siempre trabajar dentro de un repo Git
- OpenCode respeta .gitignore y no expone secrets

## Conceptos Clave

### Git en OpenCode

- OpenCode detecta automáticamente repositorios Git
- /undo y /redo dependen de Git para revertir cambios
- El agente puede ejecutar comandos git vía tool bash
- Recomendado: siempre trabajar dentro de un repo Git
- OpenCode respeta .gitignore y no expone secrets

### Commits y Branches

```bash
# Crear branch para feature
git checkout -b feature/auth-refactor

# Después de cambios de OpenCode
git add .
git commit -m "refactor: extract auth logic"

# O dejar que OpenCode haga el commit
"Create a commit with a descriptive message"
```

- Trabajar en branches protege el código principal
- OpenCode puede sugerir mensajes de commit
- Revisar siempre antes de hacer push

### Resolución de Conflictos

- Pull frecuente para mantenerse actualizado
- Si hay conflictos, OpenCode puede analizarlos
- Referenciar ambas versiones con @archivo
- Usar Plan mode primero para entender el conflicto
- Luego Build mode para aplicar la resolución
- Siempre verificar los cambios antes de commit

### Preparación de Pull Requests

- Usar /init para generar contexto del proyecto
- AGENTS.md ayuda a mantener consistencia en reviews
- OpenCode puede generar descripciones de PR automáticamente
- Solicitar review con agentes custom (code-reviewer)
- Verificar tests pasan antes de solicitar merge

## Guía Paso a Paso

### Paso 1: Git en OpenCode

- OpenCode detecta automáticamente repositorios Git
- /undo y /redo dependen de Git para revertir cambios
- El agente puede ejecutar comandos git vía tool bash
- Recomendado: siempre trabajar dentro de un repo Git
- OpenCode respeta .gitignore y no expone secrets

### Paso 2: Commits y Branches

```bash
# Crear branch para feature
git checkout -b feature/auth-refactor

# Después de cambios de OpenCode
git add .
git commit -m "refactor: extract auth logic"

# O dejar que OpenCode haga el commit
"Create a commit with a descriptive message"
```

- Trabajar en branches protege el código principal
- OpenCode puede sugerir mensajes de commit
- Revisar siempre antes de hacer push

### Paso 3: Resolución de Conflictos

- Pull frecuente para mantenerse actualizado
- Si hay conflictos, OpenCode puede analizarlos
- Referenciar ambas versiones con @archivo
- Usar Plan mode primero para entender el conflicto
- Luego Build mode para aplicar la resolución
- Siempre verificar los cambios antes de commit

### Paso 4: Preparación de Pull Requests

- Usar /init para generar contexto del proyecto
- AGENTS.md ayuda a mantener consistencia en reviews
- OpenCode puede generar descripciones de PR automáticamente
- Solicitar review con agentes custom (code-reviewer)
- Verificar tests pasan antes de solicitar merge

## Referencia Rápida

| Comando | Descripción |
|---------|-------------|
| `git checkout -b feature/auth-refactor` | Ejemplo de commits y branches |
| `git add .` | Ejemplo de commits y branches |
| `git commit -m "refactor: extract auth logic"` | Ejemplo de commits y branches |

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de git en opencode paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica commits y branches en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina resolución de conflictos con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (git en opencode, commits y branches, resolución de conflictos). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/34-flujo-git.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/34-flujo-git.pptx`

## Autoevaluación

- [ ] Puedo explicar git en opencode sin consultar apuntes
- [ ] Puedo explicar commits y branches sin consultar apuntes
- [ ] Puedo explicar resolución de conflictos sin consultar apuntes
- [ ] Puedo explicar preparación de pull requests sin consultar apuntes
