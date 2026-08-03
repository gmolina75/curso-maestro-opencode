# Caso de Uso 9: OpenCode + API REST

## Descripción
Crear APIs REST completas con autenticación, documentación y tests usando OpenCode.

## Escenario
Un equipo necesita crear una API REST rápida pero bien documentada y con tests.

## Solución con OpenCode

### 1. Ejemplos de Uso

**API completa:**
```
@opencode Create a REST API with:
- Express.js + TypeScript
- JWT authentication
- Input validation with Zod
- Error handling middleware
- Swagger documentation
- Unit and integration tests
```

**Endpoints específicos:**
```
@opencode Create CRUD endpoints for:
- User management (register, login, profile)
- Role-based access control
- Password reset flow
- Email verification
```

**Documentación:**
```
@opencode Generate OpenAPI/Swagger docs for:
- All existing endpoints
- Request/response schemas
- Authentication examples
- Error codes
```

### 2. Flujo de Trabajo
1. Describe los endpoints que necesitas
2. OpenCode genera la API completa
3. Incluye validación y errores
4. Genera documentación OpenAPI
5. Crea tests automáticos

## Beneficios
- API más rápida de crear
- Documentación siempre actualizada
- Tests comprehensivos
- Mejores prácticas de seguridad

## Archivos del Caso
- `09-api-rest/src/routes/`
- `09-api-rest/src/middleware/`
- `09-api-rest/swagger.json`
