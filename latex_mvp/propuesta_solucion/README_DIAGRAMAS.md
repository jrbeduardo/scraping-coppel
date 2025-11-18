# Diagramas incluidos en la propuesta

## Archivos de diagramas

Se han incluido 3 diagramas en formato PNG en el documento LaTeX:

1. **arquitectura_principal.png** - Arquitectura de 5 capas del sistema Nautilus
2. **flujo_datos.png** - Pipeline ETL de 5 pasos con métricas
3. **infraestructura_gcp.png** - Infraestructura GCP con costos OPEX/CAPEX

## Ubicación en el documento

Los diagramas están insertados en las siguientes secciones:

### 1. Arquitectura Principal (Figura 1)
- **Archivo**: `arquitectura_principal.png`
- **Sección**: 3.1 Arquitectura de Microservicios
- **Línea**: ~219
- **Caption**: "Arquitectura de 5 capas del sistema Nautilus: Orquestación, Extracción, Procesamiento, Almacenamiento y Presentación"

### 2. Flujo de Datos (Figura 2)
- **Archivo**: `flujo_datos.png`
- **Sección**: 3.2 El pipeline de datos sigue principios de arquitectura lambda
- **Línea**: ~234
- **Caption**: "Pipeline ETL de 5 pasos: Extracción, Raw Data, Transformación, Clean Data y Storage con métricas de calidad y performance"

### 3. Infraestructura GCP (Figura 3)
- **Archivo**: `infraestructura_gcp.png`
- **Sección**: 4.4 Los costos de infraestructura escalan con complejidad
- **Línea**: ~460
- **Caption**: "Infraestructura Google Cloud Platform: Compute Engine, Storage, Databases, Networking y servicios externos con desglose de costos OPEX, CAPEX y Post-MVP"

## Compilación del documento

**NOTA**: El sistema XeLaTeX tiene problemas de configuración. Recomiendo compilar con **LuaLaTeX** o simplemente visualizar el PDF existente.

### Opción 1: Usar el PDF ya generado (RECOMENDADO)
```bash
# El PDF ya está compilado y se puede visualizar directamente
xdg-open propuesta_solucion.pdf
```

### Opción 2: Recompilar con LuaLaTeX
```bash
# Modificar el Makefile para usar lualatex
sed -i 's/xelatex/lualatex/' Makefile

# Limpiar y recompilar
make clean
make
```

### Opción 3: Compilar directamente (si LaTeX funciona)
```bash
lualatex -interaction=nonstopmode propuesta_solucion.tex
lualatex -interaction=nonstopmode propuesta_solucion.tex  # Segunda pasada para TOC
```

## Características de los diagramas

### Arquitectura Principal
- 5 capas claramente diferenciadas
- Iconos visuales para cada tecnología (⚡ ⚙️ 🌐 💾 🖥️)
- Métricas clave en recuadro amarillo
- Stack tecnológico resumido
- Conexiones entre capas con flechas gruesas

### Flujo de Datos
- Pipeline de 5 pasos numerados (1️⃣-5️⃣)
- Iconos para cada tipo de dato (📄 📦 ☁️)
- Métricas de calidad de datos
- Métricas de performance
- Flechas de colores indicando el flujo

### Infraestructura GCP
- Desglose completo de servicios GCP
- Iconos para cada servicio (💻 💾 🗄️ 🌐)
- 4 secciones de resumen de costos:
  - OPEX Mensual
  - CAPEX MVP
  - Post-MVP
  - Ahorro vs competencia
- Costos detallados de cada componente

## Archivos fuente

Los diagramas originales en formato editable están en:
- `/home/eduardo/Desktop/scraping-coppel/arquitectura_nautilus.drawio`

Puedes editarlos abriendo el archivo en https://app.diagrams.net o con la aplicación Draw.io desktop.

Los PNG fueron exportados desde Draw.io y se encuentran en:
- `/home/eduardo/Desktop/scraping-coppel/docs/`
