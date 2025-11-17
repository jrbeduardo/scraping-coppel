# 📝 Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

---

## [1.0.1] - 2025-10-13

### 🐛 Corregido
- **Error crítico en Jupyter Notebook**: `AttributeError: 'float' object has no attribute 'round'`
  - **Celda afectada**: Análisis de Competitividad (celda 14)
  - **Línea problemática**: `out_of_stock_pct = (df_exact_clean['Out'].sum() / len(df_exact_clean) * 100).round(2)`
  - **Solución aplicada**: `out_of_stock_pct = round(df_exact_clean['Out'].sum() / len(df_exact_clean) * 100, 2)`
  - **Causa**: En versiones recientes de NumPy/Pandas, algunas operaciones devuelven float nativo de Python que no tiene método `.round()`

- **Error similar en función de análisis de valores nulos**
  - **Función afectada**: `analyze_missing_values()`
  - **Línea problemática**: `missing_pct = (missing / len(df) * 100).round(2)`
  - **Solución aplicada**: `missing_pct = round((missing / len(df) * 100), 2)`

### 📚 Agregado
- **Guía de Troubleshooting** ([TROUBLESHOOTING.md](TROUBLESHOOTING.md))
  - Soluciones a errores comunes en Jupyter
  - Problemas con ambiente conda
  - Errores de carga de datos
  - Problemas de visualización
  - Comandos útiles de diagnóstico

- **Registro de cambios** (este archivo)

### 📖 Actualizado
- [README.md](README.md) - Agregada sección de "Solución de Problemas"
- [analysis_notebook.ipynb](analysis_notebook.ipynb) - Corregidos errores de round()

---

## [1.0.0] - 2025-10-13

### ✨ Características Iniciales

#### 📊 Análisis de Datos
- Notebook completo de análisis exploratorio (EDA)
- Análisis de competitividad de precios
- Análisis de atributos técnicos de productos
- Visualizaciones interactivas con Plotly
- Exportación de resultados a CSV

#### 🐍 Scripts
- **quick_analysis.py**: Análisis rápido en terminal
- **start_jupyter.sh**: Script de inicio de Jupyter Notebook

#### 📚 Documentación
- **README.md**: Documentación técnica completa
- **PROYECTO_RESUMEN.md**: Resumen ejecutivo
- **ESTRUCTURA_PROYECTO.txt**: Estructura visual del proyecto

#### 🔧 Configuración
- **environment.yml**: Ambiente conda con todas las dependencias
- **.gitignore**: Configuración de archivos ignorados

#### 📈 Funcionalidades de Análisis

**Limpieza de Datos:**
- Normalización de tipos de datos
- Manejo de valores nulos
- Conversión de formatos de precio
- Extracción de atributos numéricos

**Análisis Exploratorio:**
- Estadísticas descriptivas completas
- Distribución de precios por marca
- Análisis de descuentos
- Productos fuera de stock
- Productos sin competencia

**Visualizaciones:**
- Histogramas y distribuciones
- Box plots por marca
- Gráficos de barras y pie charts
- Scatter plots interactivos (Plotly)
- Sunburst charts
- Heatmaps de correlación

**Insights Automáticos:**
- Oportunidades de mercado
- Análisis de disponibilidad
- Estrategia de precios
- Competencia por marca
- Características técnicas

**Exportación:**
- Productos sin competencia (CSV)
- Productos fuera de stock (CSV)
- Top descuentos (CSV)
- Estadísticas por marca (CSV)

#### 📦 Dependencias Principales
- Python 3.11
- Pandas 2.3.3
- NumPy 2.1.3
- Matplotlib 3.10.0
- Seaborn 0.13
- Plotly 6.3.1
- Jupyter
- Scikit-learn
- Statsmodels
- ydata-profiling

#### 📊 Datos Procesados
- **exact_match_data**: 200 productos con match exacto
- **analyse_item_list**: 107 productos con análisis detallado (52 atributos)

#### 🎯 Hallazgos Clave
- 200 productos analizados
- 86% con descuento (promedio 36.2%)
- 46% fuera de stock ($1.1M MXN en oportunidad perdida)
- 54% sin competencia identificada
- Top 5 marcas: Samsung, LG, Mabe, Whirlpool, Midea

---

## Tipos de Cambios

- **✨ Agregado**: para nuevas funcionalidades
- **🔄 Cambiado**: para cambios en funcionalidad existente
- **❌ Deprecado**: para funcionalidades que serán eliminadas
- **🗑️ Eliminado**: para funcionalidades eliminadas
- **🐛 Corregido**: para corrección de bugs
- **🔒 Seguridad**: en caso de vulnerabilidades

---

## Versionado

Este proyecto usa [Versionado Semántico](https://semver.org/lang/es/):
- **MAJOR**: Cambios incompatibles en la API
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs compatibles

---

## Próximas Versiones Planeadas

### [1.1.0] - Planeado
- [ ] Dashboard interactivo con Streamlit/Plotly Dash
- [ ] Automatización de actualización de datos
- [ ] Sistema de alertas de cambios de precio
- [ ] Análisis de series temporales

### [1.2.0] - Planeado
- [ ] Integración con base de datos MongoDB
- [ ] API REST para consultas
- [ ] Modelos predictivos de pricing
- [ ] Análisis de elasticidad de demanda

### [2.0.0] - Futuro
- [ ] Expansión a múltiples categorías de productos
- [ ] Sistema de recomendaciones
- [ ] Machine Learning para predicción de ventas
- [ ] Integración con sistemas de inventario

---

**Última actualización**: 2025-10-13
**Mantenedor**: Equipo de Data Science

---

## Enlaces Útiles

- [README Principal](README.md)
- [Guía de Troubleshooting](TROUBLESHOOTING.md)
- [Resumen del Proyecto](PROYECTO_RESUMEN.md)
- [Estructura del Proyecto](ESTRUCTURA_PROYECTO.txt)
