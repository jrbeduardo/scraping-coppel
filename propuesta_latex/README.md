# Propuesta de Plataforma de Scraping - Documento LaTeX

Este directorio contiene dos versiones de la propuesta en formato LaTeX basada en el documento MVP de scraping.

## ⭐ Versiones Disponibles

### Versión 2 (Ejecutiva) - **RECOMENDADA PARA PRESENTACIÓN**
- **Archivo:** `propuesta_scraping_v2_ejecutiva.tex`
- **PDF:** `propuesta_scraping_v2_ejecutiva.pdf` (17 páginas, 171KB)
- **Audiencia:** Ejecutivos, sponsors, tomadores de decisión
- **Características:**
  - Decisiones críticas al inicio
  - Página de highlights con 5 beneficios
  - Análisis de costo de inacción (\$386K-896K/año)
  - Casos de éxito cuantificados
  - Lenguaje ejecutivo (detalles técnicos en anexo)
  - ROI claro: 476%-1,409% en año 2

### Versión 1 (Técnica)
- **Archivo:** `propuesta_scraping.tex`
- **PDF:** `propuesta_scraping.pdf` (18 páginas, 175KB)
- **Audiencia:** Equipos técnicos y de implementación
- **Características:**
  - Arquitectura detallada
  - Stack tecnológico completo
  - Modelo de datos SQL
  - Especificaciones de implementación

📄 **Ver [COMPARACION_VERSIONES.md](COMPARACION_VERSIONES.md) para análisis detallado de diferencias**

## Archivos en este Directorio

- `propuesta_scraping_v2_ejecutiva.tex` ⭐ - Versión ejecutiva
- `propuesta_scraping_v2_ejecutiva.pdf` ⭐ - PDF ejecutivo
- `propuesta_scraping.tex` - Versión técnica
- `propuesta_scraping.pdf` - PDF técnico
- `Makefile` - Automatización de compilación
- `COMPARACION_VERSIONES.md` - Comparativa de versiones
- `README.md` - Este archivo

## Compilación

### Opción 1: Usando pdflatex (recomendado)

```bash
cd propuesta_latex
pdflatex propuesta_scraping.tex
pdflatex propuesta_scraping.tex  # Segunda pasada para TOC
```

### Opción 2: Usando latexmk (automático)

```bash
cd propuesta_latex
latexmk -pdf propuesta_scraping.tex
```

### Opción 3: Overleaf

1. Sube el archivo `propuesta_scraping.tex` a Overleaf
2. Compila automáticamente

## Requisitos

Paquetes LaTeX necesarios:
- inputenc
- babel (español)
- geometry
- graphicx
- xcolor
- hyperref
- enumitem
- tabularx
- booktabs
- longtable
- fancyhdr
- listings
- amsmath
- tikz

En sistemas Ubuntu/Debian:
```bash
sudo apt-get install texlive-full
```

## Estructura del Documento

1. Resumen Ejecutivo
2. Antecedentes y Problema
3. Objetivo del MVP
4. Alcance del MVP
5. Casos de Uso
6. Arquitectura del Sistema
7. Modelo de Datos
8. KPIs y Criterios de Éxito
9. Plan de Trabajo (12 semanas)
10. Equipo y Roles
11. Riesgos y Mitigaciones
12. Costos y ROI
13. Gobierno y Seguridad
14. Decisiones Solicitadas
15. Próximos Pasos
16. Glosario
17. Recomendación Final
18. Firma de Aprobación

## Personalización

Puedes personalizar:
- Colores en la sección `\definecolor`
- Márgenes en `\geometry`
- Encabezado y pie de página en `\fancyhdr`

## Salida

El comando generará:
- `propuesta_scraping.pdf` - Documento final
- `propuesta_scraping.aux` - Archivos auxiliares
- `propuesta_scraping.log` - Log de compilación
- `propuesta_scraping.toc` - Tabla de contenidos
