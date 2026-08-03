# Caso de Uso 5: OpenCode + Python Data Science

## Descripción
Crear scripts de análisis de datos, modelos ML y dashboards usando OpenCode con Python.

## Escenario
Un equipo de data science necesita prototipar análisis rápidamente pero pasar mucho tiempo escribiendo código repetitivo.

## Solución con OpenCode

### 1. Ejemplos de Uso

**Análisis exploratorio:**
```
@opencode Create an EDA script for this dataset:
- Load CSV with pandas
- Handle missing values
- Generate statistical summary
- Create visualizations (histograms, correlations)
- Export report as HTML
```

**Modelo de ML:**
```
@opencode Create a machine learning pipeline:
- Data preprocessing
- Feature engineering
- Train/test split
- Model training (Random Forest, XGBoost)
- Cross-validation
- Model evaluation metrics
- Save model as pickle
```

**Limpieza de datos:**
```
@opencode Clean this messy dataset:
- Remove duplicates
- Standardize date formats
- Normalize text columns
- Handle outliers
- Export clean CSV
```

### 2. Flujo de Trabajo
1. Proporciona los datos o describe el dataset
2. OpenCode genera el script completo
3. Incluye visualizaciones
4. Documenta cada paso
5. Exporta resultados

## Beneficios
- Scripts más rápidos de crear
- Mejores prácticas de ML
- Código documentado
- Reproducibilidad

## Archivos del Caso
- `05-data-science/eda_script.py`
- `05-data-science/ml_pipeline.py`
- `05-data-science/data_cleaning.py`
