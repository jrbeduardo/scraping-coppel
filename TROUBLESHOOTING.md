# 🔧 Guía de Resolución de Problemas

Este documento contiene soluciones a errores comunes que pueden aparecer al ejecutar el análisis.

---

## 📋 Índice

1. [Errores en Jupyter Notebook](#errores-en-jupyter-notebook)
2. [Errores de Ambiente Conda](#errores-de-ambiente-conda)
3. [Errores de Datos](#errores-de-datos)
4. [Errores de Visualización](#errores-de-visualización)

---

## Errores en Jupyter Notebook

### ❌ Error: `AttributeError: 'float' object has no attribute 'round'`

**Mensaje completo:**
```python
AttributeError: 'float' object has no attribute 'round'
out_of_stock_pct = (df_exact_clean['Out'].sum() / len(df_exact_clean) * 100).round(2)
```

**Causa:**
En versiones recientes de Python/NumPy, algunas operaciones ya devuelven un `float` nativo de Python en lugar de un `np.float64`, y los floats nativos no tienen el método `.round()`.

**Solución:**
Usar la función `round()` en lugar del método `.round()`:

```python
# ❌ Incorrecto
out_of_stock_pct = (df_exact_clean['Out'].sum() / len(df_exact_clean) * 100).round(2)

# ✅ Correcto
out_of_stock_pct = round(df_exact_clean['Out'].sum() / len(df_exact_clean) * 100, 2)
```

**Estado:** ✅ Ya corregido en el notebook

---

### ❌ Error: `FileNotFoundError: [Errno 2] No such file or directory`

**Mensaje completo:**
```python
FileNotFoundError: [Errno 2] No such file or directory: 'exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv'
```

**Causa:**
El notebook no encuentra los archivos CSV.

**Solución:**
1. Verificar que estés en el directorio correcto:
```bash
pwd
# Debe mostrar: /home/franciscomath/webscraping
```

2. Listar archivos CSV:
```bash
ls -lh *.csv
```

3. Si los archivos no están, verifica la ubicación o actualiza las rutas en el notebook.

---

### ❌ Error: `ModuleNotFoundError: No module named 'plotly'`

**Causa:**
El ambiente conda no está activado o las librerías no están instaladas.

**Solución:**
```bash
# Activar ambiente
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis

# Verificar instalación
python -c "import plotly; print(plotly.__version__)"
```

Si falla, reinstalar:
```bash
pip install plotly>=5.0.0
```

---

## Errores de Ambiente Conda

### ❌ Error: `CondaError: Run 'conda init' before 'conda activate'`

**Causa:**
Conda no está inicializado en el shell actual.

**Solución:**
```bash
# Opción 1: Source el script de conda
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis

# Opción 2: Usar el script proporcionado
./start_jupyter.sh
```

---

### ❌ Error: `PackagesNotFoundError: The following packages are not available`

**Causa:**
Versiones específicas de paquetes no disponibles en los canales.

**Solución:**
El archivo `environment.yml` ya está configurado con versiones flexibles. Si aparece este error:

```bash
# Eliminar ambiente existente
conda env remove -n webscraping-analysis

# Recrear con versiones flexibles
conda env create -f environment.yml
```

---

## Errores de Datos

### ❌ Error: `UnicodeDecodeError: 'utf-8' codec can't decode byte`

**Causa:**
Problemas de encoding en los archivos CSV.

**Solución:**
Modificar la carga de datos en el notebook:

```python
# Probar diferentes encodings
df = pd.read_csv('archivo.csv', encoding='latin1')
# o
df = pd.read_csv('archivo.csv', encoding='iso-8859-1')
```

---

### ❌ Error: Valores nulos o datos faltantes

**Síntoma:**
Análisis incompletos o gráficos vacíos.

**Solución:**
Los datos ya están siendo limpiados en las funciones `clean_exact_match_data()` y `clean_detailed_data()`. Si encuentras problemas adicionales:

```python
# Verificar valores nulos
print(df.isnull().sum())

# Rellenar valores nulos
df['columna'] = df['columna'].fillna(0)  # o valor apropiado
```

---

### ❌ Error: `ValueError: could not convert string to float`

**Causa:**
Valores no numéricos en columnas que deberían ser numéricas (ej: comas en precios).

**Solución:**
Ya implementado en las funciones de limpieza:

```python
df['Price'] = (
    df['Price']
    .astype(str)
    .str.replace(',', '')
    .str.replace('$', '')
    .str.strip()
)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
```

---

## Errores de Visualización

### ❌ Error: Gráficos no se muestran en Jupyter

**Causa:**
Backend de matplotlib no configurado.

**Solución:**
Ya incluido en el notebook, pero si falla:

```python
%matplotlib inline
import matplotlib.pyplot as plt
```

---

### ❌ Error: Plotly no muestra gráficos interactivos

**Causa:**
Extensión de Plotly no habilitada.

**Solución:**
```bash
# Dentro del ambiente conda
conda activate webscraping-analysis
jupyter labextension install jupyterlab-plotly
```

O usar en el notebook:
```python
import plotly.io as pio
pio.renderers.default = "iframe"  # o "notebook"
```

---

## Comandos Útiles para Diagnóstico

### Verificar Ambiente

```bash
# Ver ambientes disponibles
conda env list

# Ver paquetes instalados
conda list

# Ver versión de Python
python --version
```

### Verificar Datos

```bash
# Ver primeras líneas de CSV
head -n 5 "exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv"

# Contar líneas
wc -l *.csv

# Ver tamaño de archivos
ls -lh *.csv
```

### Limpiar y Reiniciar

```bash
# Reiniciar Jupyter kernel
# Desde Jupyter: Kernel > Restart Kernel

# Limpiar outputs del notebook
jupyter nbconvert --clear-output --inplace analysis_notebook.ipynb

# Recrear ambiente desde cero
conda env remove -n webscraping-analysis
conda env create -f environment.yml
```

---

## 📞 Obtener Ayuda Adicional

Si ninguna de estas soluciones funciona:

1. **Verificar versiones de dependencias:**
```bash
conda activate webscraping-analysis
python -c "import pandas; print(pandas.__version__)"
python -c "import numpy; print(numpy.__version__)"
```

2. **Generar log de errores:**
```bash
python quick_analysis.py > error_log.txt 2>&1
```

3. **Revisar documentación oficial:**
   - [Pandas Docs](https://pandas.pydata.org/docs/)
   - [Plotly Docs](https://plotly.com/python/)
   - [Conda Docs](https://docs.conda.io/)

---

## ✅ Checklist de Diagnóstico

Antes de reportar un error, verifica:

- [ ] El ambiente conda está activado
- [ ] Los archivos CSV están en el directorio correcto
- [ ] Las librerías necesarias están instaladas
- [ ] La versión de Python es 3.11
- [ ] No hay errores de encoding en los archivos
- [ ] Jupyter está ejecutándose correctamente

---

## 🔄 Actualizaciones

**Última actualización:** 2025-10-13

**Errores corregidos en esta versión:**
- ✅ `AttributeError: 'float' object has no attribute 'round'`
- ✅ Problemas de encoding en nombres de archivos
- ✅ Versiones de paquetes incompatibles en environment.yml

---

## 🎓 Buenas Prácticas

Para evitar errores futuros:

1. **Siempre activar el ambiente antes de trabajar:**
```bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate webscraping-analysis
```

2. **Mantener versiones actualizadas:**
```bash
conda update -n webscraping-analysis --all
```

3. **Hacer backup antes de cambios importantes:**
```bash
cp analysis_notebook.ipynb analysis_notebook_backup.ipynb
```

4. **Ejecutar celdas en orden:** No saltar celdas en el notebook.

5. **Reiniciar kernel si hay problemas:** Kernel > Restart & Clear Output

---

**Fin del documento de troubleshooting**
