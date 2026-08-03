# Caso de Uso 3: OpenCode + Docker

## Descripción
Crear, optimizar y mantener contenedores Docker y docker-compose usando OpenCode como asistente.

## Escenario
Un equipo necesita contenerizar sus aplicaciones pero no son expertos en Docker.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Crear Dockerfile multi-stage:**
```
@opencode Create an optimized multi-stage Dockerfile for:
- Node.js 20 backend with TypeScript
- Multi-stage build for smaller image
- Security best practices (non-root user)
- Health checks included
```

**Docker-compose completo:**
```
@opencode Create docker-compose.yml with:
- PostgreSQL 15 with persistent volume
- Redis for caching
- Node.js API backend
- Nginx reverse proxy
- Environment variables for all services
```

**Optimizar imagen existente:**
```
@opencode Optimize this Dockerfile:
- Reduce image size
- Improve layer caching
- Add .dockerignore
- Security hardening
```

### 2. Flujo de Trabajo
1. OpenCode analiza tu aplicación
2. Genera Dockerfile optimizado
3. Crea docker-compose con servicios
4. Incluye .dockerignore apropiado
5. Documenta comandos útiles

## Beneficios
- Imágenes 40-60% más pequeñas
- Mejores prácticas de seguridad
- Configuración consistente
- Menos tiempo de debugging

## Archivos del Caso
- `03-docker/Dockerfile`
- `03-docker/docker-compose.yml`
- `03-docker/.dockerignore`
