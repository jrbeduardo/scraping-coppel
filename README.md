# Proyecto de Web Scraping - Análisis Competitivo Coppel

## Descripción del Proyecto

Este proyecto contiene el análisis de datos obtenidos mediante web scraping de competidores de Coppel México, enfocándose en la comparación de atributos de productos electrónicos, específicamente refrigeradores.

## Estructura del Proyecto

```
scraping-coppel/
├── config/
│   └── environment.yml            # Configuración del ambiente conda
├── data/
│   ├── raw/                       # Datos originales sin procesar
│   │   ├── exact_match_data_*.csv
│   │   └── analyse_item_list_*.csv
│   └── processed/                 # Datos procesados y limpios
├── docs/
│   ├── CHANGELOG.md               # Historial de cambios
│   ├── DICCIONARIO_DATOS.md       # Diccionario de campos
│   ├── ESTRUCTURA_PROYECTO.txt    # Estructura detallada
│   ├── mvp_scraping_platform.md   # Especificaciones de la plataforma
│   ├── mvp_update.md              # Actualización MVP
│   ├── PROYECTO_COMPLETO.md       # Proyecto completo detallado
│   ├── PROYECTO_RESUMEN.md        # Resumen ejecutivo del proyecto
│   └── propuesta_solucion.md      # Propuesta técnica completa (29 páginas)
├── latex_mvp/                     # Documentos LaTeX profesionales
│   ├── assets/                    # Recursos compartidos (logos)
│   ├── mvp_update/                # Documento LaTeX MVP Update
│   │   ├── mvp_update.tex         # Código fuente LaTeX
│   │   ├── mvp_update.pdf         # PDF compilado (93KB)
│   │   ├── Makefile               # Compilación automatizada
│   │   └── assets/                # Recursos locales
│   ├── propuesta_solucion/        # Propuesta Técnica Completa
│   │   ├── propuesta_solucion.tex # Código fuente LaTeX
│   │   ├── propuesta_solucion.pdf # PDF compilado (140KB, 29 páginas)
│   │   ├── Makefile               # Compilación automatizada
│   │   └── assets/                # Recursos locales
│   └── README.md                  # Documentación LaTeX
├── notebooks/
│   └── analysis_notebook.ipynb    # Notebook de análisis exploratorio
├── propuesta_latex/               # Propuesta LaTeX con variables ROI
│   ├── propuesta_scraping*.tex    # Versiones de propuesta
│   ├── *.pdf                      # PDFs compilados
│   └── VARIABLES_ROI.md           # Plantilla cálculo ROI
├── scripts/
│   ├── quick_analysis.py          # Script de análisis rápido
│   └── start_jupyter.sh           # Script de inicio de Jupyter
├── .gitignore
└── README.md                      # Documentación principal
```

## Archivos de Datos

Para información detallada de todos los campos, consulta el [Diccionario de Datos](docs/DICCIONARIO_DATOS.md).

### 1. `exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv`
**Ubicación**: `data/raw/`
- **Registros**: 200 productos
- **Columnas**: 10
- **Tamaño**: ~50 KB
- **Contenido**: Datos de productos con match exacto entre competidores
- **Campos principales**:
  - `Sku_id`: Identificador del producto
  - `Name`: Nombre del producto
  - `Category`: Categoría jerárquica
  - `Brand`: Marca del producto (24 marcas únicas)
  - `Price`: Precio original ($4,599 - $91,999 MXN)
  - `Discount`: Descuento aplicado (86% con descuento)
  - `Out`: Disponibilidad (46% fuera de stock)
  - `Status`: Estado competitivo (Out Of Stock, No Competitor)
  - `Difference`: Diferencia de precio con competencia

### 2. `analyse_item_list_Coppel Mx (8).csv`
**Ubicación**: `data/raw/`
- **Registros**: 107 productos
- **Columnas**: 52
- **Tamaño**: ~79 KB
- **Contenido**: Análisis detallado de productos con múltiples atributos técnicos
- **Secciones de información**:
  - **Identificación**: `Mongo_id`, `Sku`, `Name`
  - **Pricing**: `Price`, `Discount`, `Discount_Percent`
  - **Características visuales**: `Color` (7 colores disponibles)
  - **Especificaciones técnicas**:
    - `Refrigerator_type` (top mount, french door, side-by-side, bottom mount)
    - `Capacity_in_feet` (7-32 pies cúbicos)
    - `No_of_doors` (1-4 puertas)
    - `Freezer_location` (top, bottom, side)
  - **Tecnología**:
    - `Control_panel` (manual, digital, touch panel)
    - `Refrigeration_and_cooling_technology` (inverter, multi air flow, frost free)
    - `Saving_energy_or_water` (certificaciones)
  - **Comercial**:
    - `Seller` (Coppel, marketplace partners)
    - `Shipping_time` y `Shipping_fees`
    - `Product_emi_plan` (planes de financiamiento)

**Documentación completa**: Ver [docs/DICCIONARIO_DATOS.md](docs/DICCIONARIO_DATOS.md) para descripción detallada de cada campo, tipos de datos, valores posibles y ejemplos.

## Instalación del Ambiente

### Opción 1: Usando Conda (Recomendado)

```bash
# Crear el ambiente desde el archivo environment.yml
conda env create -f config/environment.yml

# Activar el ambiente
conda activate webscraping-analysis

# Verificar instalación
python -c "import pandas; print(f'Pandas: {pandas.__version__}')"
```

### Opción 2: Actualizar ambiente existente

```bash
# Actualizar ambiente existente
conda env update -f config/environment.yml --prune
```

## Uso del Proyecto

### Opción 1: Análisis Rápido (Recomendado para inicio)

```bash
# Ejecutar análisis rápido en terminal
python scripts/quick_analysis.py

# O con el ambiente conda
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis
python scripts/quick_analysis.py
```

Este script genera un reporte ejecutivo rápido con:
- Métricas generales de precios
- Análisis de descuentos
- Top marcas
- Productos fuera de stock
- Recomendaciones estratégicas

### Opción 2: Análisis Detallado con Jupyter Notebook

```bash
# Opción A: Usar script de inicio
bash scripts/start_jupyter.sh

# Opción B: Inicio manual
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis
jupyter notebook notebooks/analysis_notebook.ipynb
```

El notebook incluye:
- Análisis exploratorio completo
- Visualizaciones interactivas con Plotly
- Análisis de atributos técnicos
- Exportación de resultados
- Insights avanzados

## Análisis Implementados

El notebook incluye los siguientes análisis:

1. **Carga y limpieza de datos**
   - Validación de tipos de datos
   - Manejo de valores nulos
   - Normalización de campos

2. **Análisis Exploratorio de Datos (EDA)**
   - Estadísticas descriptivas
   - Distribución de precios por marca
   - Análisis de disponibilidad de productos
   - Comparación de descuentos

3. **Análisis de Competitividad**
   - Comparación de precios entre competidores
   - Análisis de diferencias de precio
   - Productos fuera de stock vs competencia

4. **Visualizaciones**
   - Distribución de precios por categoría
   - Heatmap de correlaciones
   - Análisis de atributos técnicos
   - Comparativa de marcas

5. **Insights y Recomendaciones**
   - Oportunidades de pricing
   - Productos sin competencia identificada
   - Análisis de brechas en el catálogo

## Dependencias Principales

- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualizaciones estáticas
- **plotly**: Visualizaciones interactivas
- **scikit-learn**: Análisis estadístico y clustering
- **ydata-profiling**: Generación de reportes automáticos

## Mejores Prácticas

1. **Versionamiento de datos**: Los archivos CSV incluyen timestamp en el nombre
2. **Reproducibilidad**: Ambiente conda especificado con versiones fijas
3. **Documentación**: Código documentado con docstrings y comentarios
4. **Modularidad**: Funciones reutilizables para análisis recurrentes

## Próximos Pasos

- [ ] Automatizar la actualización de datos
- [ ] Implementar alertas de cambios de precio
- [ ] Crear dashboard interactivo con Plotly Dash
- [ ] Integrar con base de datos MongoDB
- [ ] Implementar modelos predictivos de pricing

## Solución de Problemas

Si encuentras algún error al ejecutar el análisis, consulta la [Guía de Troubleshooting](docs/TROUBLESHOOTING.md) que incluye:

- ✅ Soluciones a errores comunes en Jupyter
- ✅ Problemas con el ambiente conda
- ✅ Errores de carga de datos
- ✅ Problemas de visualización
- ✅ Comandos útiles de diagnóstico

**Error corregido:** `AttributeError: 'float' object has no attribute 'round'` - Ya resuelto en la versión actual del notebook.

## Contacto y Soporte

Para preguntas o sugerencias sobre este proyecto, por favor contactar al equipo de Data Science.

---
**Última actualización**: Noviembre 2025
**Versión**: 2.0.0
# scraping-coppel
# scraping-coppel
