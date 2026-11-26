---
title: "Clase 40: Testing y Calidad de Código"
module: 40
duration: "1.5 horas"
prerequisites: "Módulo 39 - Clase 39: Personalización de System Prompts"
---

# Clase 40: Testing y Calidad de Código

## Resumen Ejecutivo

Esta clase cubre testing y calidad de código. Red-Green-Refactor asistido por IA Escribir tests primero, luego implementar OpenCode genera tests basados en requisitos.

A lo largo de la sesión se exploran los siguientes temas: tdd con opencode, generación de tests, análisis de cobertura, revisión de calidad. Al finalizar, el estudiante tendrá una base práctica para aplicar estos conceptos en sus propios proyectos con OpenCode.

## Objetivos de Aprendizaje

- Red-Green-Refactor asistido por IA
- Escribir tests primero, luego implementar
- OpenCode genera tests basados en requisitos
- Iterar: tests fallan → implementar → tests pasan → refactor
- Plan mode para diseñar suite de tests completa

## Conceptos Clave

### TDD con OpenCode

- Red-Green-Refactor asistido por IA
- Escribir tests primero, luego implementar
- OpenCode genera tests basados en requisitos
- Iterar: tests fallan → implementar → tests pasan → refactor
- Plan mode para diseñar suite de tests completa

### Generación de Tests

```bash
# Generar tests para función existente
"Write unit tests for @src/utils/auth.ts
covering edge cases and error paths"

# Generar tests de integración
"Create integration tests for the /api/users
endpoints using the existing test setup"
```

- Especificar framework: Jest, Vitest, Pytest, Go test
- Incluir casos edge y errores
- Referenciar código fuente con @

### Análisis de Cobertura

- "Run test coverage and identify untested paths"
- OpenCode puede interpretar reportes de cobertura
- Sugerir tests adicionales para branches no cubiertos
- Objetivo común: 80%+ cobertura en lógica crítica
- No perseguir 100% ciegamente; priorizar calidad sobre cantidad

### Revisión de Calidad

- Agente custom "code-reviewer" para revisión automática
- Linter integration: ESLint, Ruff, golangci-lint
- Type checking: TypeScript, mypy, Go vet
- "Review this code for security best practices"
- Usar skills para estandarizar criterios de calidad

## Guía Paso a Paso

### Paso 1: TDD con OpenCode

- Red-Green-Refactor asistido por IA
- Escribir tests primero, luego implementar
- OpenCode genera tests basados en requisitos
- Iterar: tests fallan → implementar → tests pasan → refactor
- Plan mode para diseñar suite de tests completa

### Paso 2: Generación de Tests

```bash
# Generar tests para función existente
"Write unit tests for @src/utils/auth.ts
covering edge cases and error paths"

# Generar tests de integración
"Create integration tests for the /api/users
endpoints using the existing test setup"
```

- Especificar framework: Jest, Vitest, Pytest, Go test
- Incluir casos edge y errores
- Referenciar código fuente con @

### Paso 3: Análisis de Cobertura

- "Run test coverage and identify untested paths"
- OpenCode puede interpretar reportes de cobertura
- Sugerir tests adicionales para branches no cubiertos
- Objetivo común: 80%+ cobertura en lógica crítica
- No perseguir 100% ciegamente; priorizar calidad sobre cantidad

### Paso 4: Revisión de Calidad

- Agente custom "code-reviewer" para revisión automática
- Linter integration: ESLint, Ruff, golangci-lint
- Type checking: TypeScript, mypy, Go vet
- "Review this code for security best practices"
- Usar skills para estandarizar criterios de calidad

## Referencia Rápida

| Comando | Descripción |
|---------|-------------|
| `covering edge cases and error paths"` | Ejemplo de generación de tests |
| `endpoints using the existing test setup"` | Ejemplo de generación de tests |

## Ejercicios Guiados

1. **Práctica inicial:** sigue la guía de tdd con opencode paso a paso y verifica que el resultado coincida con lo esperado.
2. **Práctica intermedia:** aplica generación de tests en un proyecto propio, documentando cada paso y los problemas encontrados.
3. **Práctica avanzada:** combina análisis de cobertura con lo aprendido en clases anteriores en un escenario integrador.

## Ejercicio Desafío

Diseña un caso de uso real que integre todos los temas de esta clase (tdd con opencode, generación de tests, análisis de cobertura). Implementa una solución completa, documenta la configuración utilizada y presenta una comparativa de antes y después de aplicar estas técnicas.

## Recursos Adicionales

- [Documentación oficial de OpenCode](https://opencode.ai/docs)
- Presentación de la clase: `presentaciones/nuevas-clases/40-testing-calidad.pptd`
- Presentación exportada: `presentaciones/nuevas-clases/40-testing-calidad.pptx`

## Autoevaluación

- [ ] Puedo explicar tdd con opencode sin consultar apuntes
- [ ] Puedo explicar generación de tests sin consultar apuntes
- [ ] Puedo explicar análisis de cobertura sin consultar apuntes
- [ ] Puedo explicar revisión de calidad sin consultar apuntes
