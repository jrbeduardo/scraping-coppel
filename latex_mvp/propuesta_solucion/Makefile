# Makefile para compilar propuesta_solucion.tex

# Variables
LATEX = xelatex
DOCUMENT = propuesta_solucion
FLAGS = -interaction=nonstopmode

# Compilar el documento (2 pasadas para TOC)
all: $(DOCUMENT).pdf

$(DOCUMENT).pdf: $(DOCUMENT).tex
	@echo "Compilando $(DOCUMENT).tex (primera pasada)..."
	$(LATEX) $(FLAGS) $(DOCUMENT).tex
	@echo "Compilando $(DOCUMENT).tex (segunda pasada para TOC)..."
	$(LATEX) $(FLAGS) $(DOCUMENT).tex
	@echo "PDF generado: $(DOCUMENT).pdf"

# Limpiar archivos auxiliares
clean:
	@echo "Limpiando archivos auxiliares..."
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb

# Limpiar todo incluyendo el PDF
cleanall: clean
	@echo "Eliminando PDF..."
	rm -f $(DOCUMENT).pdf

# Ver el PDF
view: $(DOCUMENT).pdf
	@echo "Abriendo $(DOCUMENT).pdf..."
	xdg-open $(DOCUMENT).pdf || open $(DOCUMENT).pdf || evince $(DOCUMENT).pdf

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make          - Compila el documento LaTeX"
	@echo "  make clean    - Elimina archivos auxiliares"
	@echo "  make cleanall - Elimina archivos auxiliares y PDF"
	@echo "  make view     - Abre el PDF generado"
	@echo "  make help     - Muestra esta ayuda"

.PHONY: all clean cleanall view help
