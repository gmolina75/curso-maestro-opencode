# Caso de Uso 4: OpenCode + React/Frontend

## Descripción
Desarrollar componentes React, hooks personalizados y arquitectura frontend usando OpenCode.

## Escenario
Un equipo frontend necesita crear componentes reutilizables y mantener consistencia en el código.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Crear componente completo:**
```
@opencode Create a React component for a Data Table with:
- Sorting by columns
- Pagination
- Search/filter
- Row selection
- Export to CSV
- TypeScript types
- Storybook stories
```

**Hook personalizado:**
```
@opencode Create a custom hook useApi that:
- Handles loading, error, success states
- Supports caching
- Auto-retry on failure
- TypeScript generic support
```

**Refactorizar código:**
```
@opencode Refactor this component to:
- Extract custom hooks
- Improve performance with useMemo/useCallback
- Add proper TypeScript types
- Follow SOLID principles
```

### 2. Flujo de Trabajo
1. Describe el componente que necesitas
2. OpenCode genera el código
3. Incluye tests y storybook
4. Optimiza rendimiento
5. Documenta el componente

## Beneficios
- Componentes más reutilizables
- Código más mantenible
- Tests automáticos
- Documentación incluida

## Archivos del Caso
- `04-react/DataTable.tsx`
- `04-react/useApi.ts`
- `04-react/DataTable.stories.tsx`
