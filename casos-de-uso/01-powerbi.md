# Caso de Uso 1: OpenCode + PowerBI

## Descripción
Automatizar la creación de reportes PowerBI, modelos de datos DAX y consultas M usando OpenCode como asistente de IA.

## Escenario
Un equipo de business intelligence necesita crear reportes PowerBI recurrentemente pero no tiene tiempo para escribir fórmulas DAX complejas ni configurar modelos de datos manualmente.

## Solución con OpenCode

### 1. Conexión via MCP
```json
{
  "mcp": {
    "powerbi": {
      "type": "remote",
      "url": "https://mcp.powerbi.com/mcp",
      "enabled": true
    }
  }
}
```

### 2. Ejemplos de Uso

**Crear modelo de datos:**
```
@opencode Create a PowerBI data model connecting to our SQL Server 
database with tables: Sales, Products, Customers. 
Define relationships and create DAX measures for:
- Total Revenue
- Monthly Growth Rate
- Top 10 Products by Sales
```

**Generar consultas M:**
```
@opencode Write Power Query M code to:
1. Import data from SharePoint folder
2. Clean null values
3. Merge with reference table
4. Export to staging table
```

**Crear medidas DAX:**
```
@opencode Create DAX measures for time intelligence:
- YTD Sales
- Same Period Last Year
- Rolling 3 Month Average
- % Change vs Previous Month
```

### 3. Flujo de Trabajo
1. OpenCode analiza la estructura de datos existente
2. Genera el modelo de datos con relaciones
3. Crea medidas DAX optimizadas
4. Exporta como archivo .pbix o script
5. Validación automática de fórmulas

## Beneficios
- Ahorro de 60-70% en tiempo de desarrollo
- Fórmulas DAX optimizadas y documentadas
- Modelos de datos consistentes
- Reducción de errores humanos

## Requisitos
- PowerBI Desktop o Service
- Acceso a fuentes de datos
- OpenCode con MCP PowerBI (o sin él, usando scripts)

## Archivos del Caso
- `01-powerbi/modelo-datos-ejemplo.dax`
- `01-powerbi/consulta-m-ejemplo.m`
- `01-powerbi/reporte-ventas.pbix`
