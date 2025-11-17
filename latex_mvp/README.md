# LaTeX Documents - Scraping Coppel MVP

Esta carpeta contiene los documentos técnicos en formato LaTeX para el proyecto de plataforma de scraping.

## 📁 Estructura de Carpetas

```
latex_mvp/
├── assets/                      # Recursos compartidos (logos, imágenes)
│   └── logo-coppel.png
├── mvp_update/                  # Documento: Plataforma Interna de Scraping MVP
│   ├── assets/                  # Copia local de recursos
│   ├── mvp_update.tex          # Código fuente LaTeX
│   ├── mvp_update.pdf          # PDF compilado (93KB)
│   └── mvp_update.*            # Archivos auxiliares de compilación
└── propuesta_solucion/          # Documento: Propuesta Técnica Completa
    ├── assets/                  # Copia local de recursos
    ├── propuesta_solucion.tex  # Código fuente LaTeX
    ├── propuesta_solucion.pdf  # PDF compilado (140KB, 29 páginas)
    └── propuesta_solucion.*    # Archivos auxiliares de compilación
```

## 📄 Documentos Disponibles

### 1. MVP Update (mvp_update/)
- **Archivo**: `mvp_update.pdf`
- **Tamaño**: 93KB
- **Descripción**: Plataforma Interna de Scraping - Análisis Competitivo de Precios
- **Versión**: 0.1 (para socializar con equipo y usuario final)
- **Fecha**: 15/oct/2025

### 2. Propuesta Solución (propuesta_solucion/)
- **Archivo**: `propuesta_solucion.pdf`
- **Tamaño**: 140KB (29 páginas)
- **Descripción**: Plataforma de Monitoreo de Precios Competitivos - Hoja de Ruta MVP 3-4 Meses
- **Versión**: 1.0 (Propuesta Técnica Completa)
- **Fecha**: Noviembre 2025
- **Contenido**:
  - Resumen ejecutivo
  - 8 secciones técnicas detalladas
  - 20 referencias con código accesible
  - Stack tecnológico completo
  - Cronograma de implementación

## 🔧 Compilación

Para recompilar cualquier documento LaTeX:

```bash
cd latex_mvp/<nombre_documento>
xelatex <nombre_documento>.tex
xelatex <nombre_documento>.tex  # Segunda pasada para TOC
```

**Ejemplo para propuesta_solucion:**
```bash
cd latex_mvp/propuesta_solucion
xelatex propuesta_solucion.tex
xelatex propuesta_solucion.tex
```

## 📋 Requisitos

- **XeLaTeX**: Compilador LaTeX (incluido en TeX Live)
- **Fuentes**: DejaVu Sans (disponible en la mayoría de sistemas Linux)
- **Paquetes LaTeX**: geometry, xcolor, fontspec, babel, hyperref, titlesec, tabularx, booktabs, multirow, listings, etc.

## 🎨 Estilo Corporativo

Todos los documentos utilizan la paleta de colores corporativa de Coppel:

- **Brand Blue**: #1C42E8
- **Brand Yellow**: #F0D224
- **Brand Medium Blue**: #05297A
- **Brand Dark Blue**: #081754
- **Brand Light Blue**: #1CA8F7

## 📝 Notas

- Los archivos `.aux`, `.log`, `.out`, `.toc` son archivos auxiliares generados durante la compilación
- La carpeta `assets/` se copia en cada subcarpeta para mantener independencia de recursos
- Se recomienda usar XeLaTeX en lugar de pdfLaTeX para mejor soporte de fuentes y Unicode

## 🔄 Actualización de Documentos

Cuando se modifiquen los archivos markdown fuente en `docs/`:
1. Actualizar el archivo `.tex` correspondiente
2. Recompilar con XeLaTeX (2 pasadas)
3. Verificar el PDF generado

---

**Última actualización**: Noviembre 2025
