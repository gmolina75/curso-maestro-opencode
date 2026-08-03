# Caso de Uso 2: OpenCode + GitHub Actions (CI/CD)

## Descripción
Configurar pipelines de CI/CD automatizados usando OpenCode para generar, mantener y optimizar GitHub Actions workflows.

## Escenario
Un equipo de desarrollo necesita crear pipelines de CI/CD para múltiples proyectos pero cada uno tiene requisitos diferentes.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Crear workflow de testing:**
```
@opencode Create a GitHub Actions workflow that:
1. Triggers on push to main and PRs
2. Runs tests for Python 3.10 and 3.11
3. Caches pip dependencies
4. Uploads coverage to Codecov
5. Posts test summary as PR comment
```

**Optimizar workflow existente:**
```
@opencode Analyze this workflow and optimize it:
- Reduce build time
- Add parallel jobs where possible
- Improve caching strategy
- Add failure notifications to Slack
```

**Agregar seguridad:**
```
@opencode Add security scanning to our CI:
- SAST with CodeQL
- Dependency scanning with Dependabot
- Secret scanning
- Container scanning with Trivy
```

### 2. Flujo de Trabajo
1. Describe el pipeline que necesitas
2. OpenCode genera el workflow YAML
3. Validación automática de sintaxis
4. Sugerencias de optimización
5. Commit directo o PR

## Beneficios
- Configuración 5x más rápida
- Workflows optimizados y consistentes
- Menos configuración manual
- Mejores prácticas incluidas

## Archivos del Caso
- `02-github-actions/workflow-testing.yml`
- `02-github-actions/workflow-deploy.yml`
- `02-github-actions/workflow-security.yml`
