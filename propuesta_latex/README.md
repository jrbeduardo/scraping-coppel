# Propuesta de Plataforma de Scraping - Documento LaTeX

Este directorio contiene la propuesta técnica en formato LaTeX basada en el documento MVP de scraping.

## Archivos

- `propuesta_scraping.tex` - Documento principal en LaTeX
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
