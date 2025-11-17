# Makefile para compilar la propuesta de scraping

# Variables
TEX_FILE = propuesta_scraping.tex
PDF_FILE = propuesta_scraping.pdf
LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode

# Objetivo principal
all: $(PDF_FILE)

# Compilar el documento (dos pasadas para TOC)
$(PDF_FILE): $(TEX_FILE)
	@echo "Compilando documento LaTeX..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "Segunda pasada para tabla de contenidos..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "✓ Documento generado: $(PDF_FILE)"

# Limpiar archivos auxiliares
clean:
	@echo "Limpiando archivos auxiliares..."
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb
	@echo "✓ Archivos auxiliares eliminados"

# Limpiar todo incluyendo el PDF
cleanall: clean
	@echo "Eliminando PDF..."
	rm -f $(PDF_FILE)
	@echo "✓ Todos los archivos generados eliminados"

# Ver el PDF (requiere un visor de PDF)
view: $(PDF_FILE)
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(PDF_FILE); \
	elif command -v evince > /dev/null; then \
		evince $(PDF_FILE) & \
	elif command -v okular > /dev/null; then \
		okular $(PDF_FILE) & \
	else \
		echo "No se encontró un visor de PDF. Abre manualmente: $(PDF_FILE)"; \
	fi

# Recompilar (limpiar y compilar)
rebuild: cleanall all

# Ayuda
help:
	@echo "Makefile para compilar propuesta_scraping.tex"
	@echo ""
	@echo "Objetivos disponibles:"
	@echo "  make          - Compilar el documento PDF"
	@echo "  make all      - Igual que 'make'"
	@echo "  make clean    - Eliminar archivos auxiliares"
	@echo "  make cleanall - Eliminar todos los archivos generados"
	@echo "  make view     - Abrir el PDF en el visor predeterminado"
	@echo "  make rebuild  - Limpiar y recompilar desde cero"
	@echo "  make help     - Mostrar esta ayuda"

.PHONY: all clean cleanall view rebuild help
