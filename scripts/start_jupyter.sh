#!/bin/bash
#############################################
# Script para iniciar Jupyter Notebook
# con el ambiente de webscraping-analysis
#############################################

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}  Iniciando Jupyter Notebook${NC}"
echo -e "${BLUE}======================================${NC}"

# Activar ambiente conda
echo -e "\n${GREEN}✓ Activando ambiente: webscraping-analysis${NC}"
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis

# Verificar que el ambiente esté activo
if [[ "$CONDA_DEFAULT_ENV" == "webscraping-analysis" ]]; then
    echo -e "${GREEN}✓ Ambiente activado correctamente${NC}"
else
    echo -e "${RED}✗ Error al activar ambiente${NC}"
    exit 1
fi

# Mostrar información del ambiente
echo -e "\n${BLUE}Librerías instaladas:${NC}"
python -c "import pandas as pd; import numpy as np; import plotly; print(f'  - Pandas: {pd.__version__}'); print(f'  - NumPy: {np.__version__}'); print(f'  - Plotly: {plotly.__version__}')"

# Iniciar Jupyter
echo -e "\n${GREEN}✓ Iniciando Jupyter Notebook...${NC}"
echo -e "${BLUE}Presiona Ctrl+C para detener el servidor${NC}\n"

jupyter notebook ../notebooks/analysis_notebook.ipynb
