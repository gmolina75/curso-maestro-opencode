# Caso de Uso 8: OpenCode + Bases de Datos

## Descripción
Crear esquemas de base de datos, migraciones, queries optimizadas y ORMs usando OpenCode.

## Escenario
Un equipo necesita diseñar una base de datos completa pero no tiene tiempo para escribir cada query y migración manualmente.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Esquema de base de datos:**
```
@opencode Design a PostgreSQL database schema for:
- E-commerce platform
- Users with roles and permissions
- Products with categories and inventory
- Orders with payments
- Include indexes for performance
```

**Migraciones:**
```
@opencode Create Prisma migrations for:
- Add new table 'reviews'
- Modify 'users' table to add 'avatar_url'
- Create many-to-many relationship
- Include seed data
```

**Query optimizada:**
```
@opencode Optimize this SQL query:
- It's taking 5 seconds on 1M rows
- Add proper indexes
- Rewrite for better performance
- Explain the execution plan
```

### 2. Flujo de Trabajo
1. Describe el dominio de tu aplicación
2. OpenCode genera el esquema completo
3. Incluye índices optimizados
4. Crea migraciones versionadas
5. Documenta relaciones y constraints

## Beneficios
- Esquemas mejor diseñados
- Queries más rápidas
- Migraciones sin errores
- Documentación automática

## Archivos del Caso
- `08-database/schema.sql`
- `08-database/migrations/`
- `08-database/queries/optimized.sql`
