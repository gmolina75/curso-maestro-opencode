# Caso de Uso 7: OpenCode + GitLab CI/CD

## Descripción
Configurar pipelines GitLab CI/CD, Auto DevOps y integración con GitLab usando OpenCode.

## Escenario
Un equipo usa GitLab y necesita configurar pipelines completos para múltiples proyectos.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Pipeline completo:**
```
@opencode Create .gitlab-ci.yml with:
- Build stage (Docker)
- Test stage (parallel jobs)
- Security scanning (SAST, DAST, dependency)
- Deploy to staging
- Manual deploy to production
- Cache configuration
```

**Auto DevOps:**
```
@opencode Configure Auto DevOps for:
- Node.js application
- Helm chart for Kubernetes
- Canary deployments
- Automatic rollback
```

**Integración con GitLab:**
```
@opencode Create GitLab CI for:
- Merge request approvals
- Code quality checks
- Performance testing
- Container registry push
```

### 2. Flujo de Trabajo
1. OpenCode analiza tu proyecto
2. Genera pipeline optimizado
3. Incluye stages paralelos
4. Configura cache y artifacts
5. Documenta variables necesarias

## Beneficios
- Pipelines más rápidos
- Menos configuración manual
- Mejores prácticas CI/CD
- Integración completa con GitLab

## Archivos del Caso
- `07-gitlab/.gitlab-ci.yml`
- `07-gitlab/Dockerfile`
- `07-gitlab/helm/values.yaml`
