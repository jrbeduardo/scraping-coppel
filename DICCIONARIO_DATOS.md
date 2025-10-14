# 📚 Diccionario de Datos - Proyecto Web Scraping Coppel MX

**Fecha de creación**: 2025-10-13
**Versión**: 1.0
**Autor**: Equipo de Data Science

---

## 📋 Tabla de Contenidos

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Dataset 1: Exact Match Data](#dataset-1-exact-match-data)
3. [Dataset 2: Detailed Analysis](#dataset-2-detailed-analysis)
4. [Relaciones entre Datasets](#relaciones-entre-datasets)
5. [Notas Técnicas](#notas-técnicas)
6. [Glosario](#glosario)

---

## Resumen Ejecutivo

Este documento describe la estructura y contenido de los datasets generados mediante web scraping de productos de la categoría de electrónica (refrigeradores) de Coppel México y sus competidores.

### Archivos Incluidos

| Archivo | Registros | Columnas | Tamaño | Descripción |
|---------|-----------|----------|--------|-------------|
| `exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv` | 200 | 10 | ~50 KB | Productos con match exacto entre competidores |
| `analyse_item_list_Coppel Mx (8).csv` | 107 | 52 | ~79 KB | Análisis detallado con atributos técnicos |

---

## Dataset 1: Exact Match Data

**Archivo**: `exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv`
**Registros**: 200 productos
**Fecha de extracción**: 2025-10-10

### Descripción General

Dataset que contiene productos identificados con match exacto entre Coppel y sus competidores, enfocado en información básica de precio, disponibilidad y status competitivo.

### Estructura de Columnas

#### 1. **Sku_id**
- **Tipo de dato**: Text (String)
- **Nulos**: 64 registros (32.0%)
- **Valores únicos**: 136
- **Descripción**: Identificador único del producto (SKU - Stock Keeping Unit)
- **Formato**: Alfanumérico, puede incluir prefijos como "MKP-" o números puros
- **Ejemplos**:
  - `MKP-74381260`
  - `632724`
  - `625711`
- **Notas**: Algunos productos no tienen SKU asignado (valores nulos)
- **Uso**: Clave primaria para identificación y matching de productos

---

#### 2. **Name**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 200 (todos únicos)
- **Descripción**: Nombre completo del producto incluyendo marca, modelo y características principales
- **Longitud**: Variable (típicamente 50-150 caracteres)
- **Formato**: Texto libre con mayúsculas/minúsculas mixtas
- **Ejemplos**:
  - `Refrigerador Tcl 6 Pies Cúbicos Con Dispensador De Agua TSD60BW-NEGRO`
  - `Refrigerador Hisense RR63D6WWX Una Puerta 7 Pies Blanco`
- **Componentes típicos**:
  - Tipo de producto (Refrigerador)
  - Marca
  - Capacidad (en pies cúbicos)
  - Características especiales
  - Modelo
  - Color
- **Uso**: Descripción principal del producto para matching y visualización

---

#### 3. **Category**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Categoría jerárquica del producto en formato breadcrumb
- **Valor**: `IN > Electronics > Kitchen Appliances > Refrigerators`
- **Formato**: Jerarquía separada por " > "
- **Niveles**:
  1. `IN` (India/International - prefijo del sistema)
  2. `Electronics` (Categoría principal)
  3. `Kitchen Appliances` (Subcategoría)
  4. `Refrigerators` (Tipo específico)
- **Uso**: Clasificación y filtrado de productos

---

#### 4. **Brand**
- **Tipo de dato**: Text (String)
- **Nulos**: 1 registro (0.5%)
- **Valores únicos**: 24 marcas
- **Descripción**: Marca del fabricante del refrigerador
- **Formato**: Lowercase (minúsculas)
- **Principales marcas**:
  - Samsung (41 productos)
  - LG (31 productos)
  - Mabe (25 productos)
  - Whirlpool (24 productos)
  - Midea (20 productos)
  - Hisense (16 productos)
  - TCL (8 productos)
  - Aspix (7 productos)
  - Daewoo (5 productos)
  - Otros (23 productos)
- **Uso**: Análisis competitivo por marca, segmentación de mercado

---

#### 5. **Url**
- **Tipo de dato**: Text (String - URL)
- **Nulos**: 0 (0%)
- **Valores únicos**: 200 (todas únicas)
- **Descripción**: URL completa del producto en el sitio web de Coppel
- **Formato**: `https://www.coppel.com/[slug]-[sku]`
- **Dominio**: `www.coppel.com`
- **Ejemplo**:
  ```
  https://www.coppel.com/refrigerador-tcl-6-pies-cubicos-con-dispensador-de-agua-tsd60bw-negro-mkp-74381260
  ```
- **Componentes**:
  - Protocolo: HTTPS
  - Dominio: www.coppel.com
  - Slug: Nombre del producto en formato URL-friendly
  - SKU: Al final del slug precedido por `pm-` o `mkp-`
- **Uso**: Acceso directo al producto, tracking, validación de scraping

---

#### 6. **Price**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 0 (0%)
- **Valores únicos**: 153
- **Descripción**: Precio original del producto en pesos mexicanos (MXN)
- **Rango**: $4,599 - $91,999 MXN
- **Media**: $19,264.69 MXN
- **Mediana**: $16,842.50 MXN
- **Desviación estándar**: $12,380.75
- **Distribución**:
  - Q1 (25%): $11,999
  - Q2 (50%): $16,842.50
  - Q3 (75%): $22,524
- **Formato**: Número decimal sin formato de moneda
- **Uso**: Análisis de precios, comparativas competitivas, segmentación por rango

---

#### 7. **Discount**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 0 (0%)
- **Valores únicos**: 123
- **Descripción**: Monto de descuento aplicado en pesos mexicanos (MXN)
- **Rango**: $0 - $69,800 MXN
- **Media**: $5,879.25 MXN
- **Mediana**: $3,650 MXN
- **Productos sin descuento**: 28 (14%)
- **Productos con descuento**: 172 (86%)
- **Descuento promedio (productos con desc.)**: $6,836.34 MXN
- **Uso**:
  - Cálculo de precio final: `Final_Price = Price - Discount`
  - Análisis de estrategia promocional
  - Comparación de agresividad comercial

---

#### 8. **Out**
- **Tipo de dato**: Boolean (True/False)
- **Nulos**: 0 (0%)
- **Valores únicos**: 2
- **Descripción**: Indicador de disponibilidad del producto
- **Valores**:
  - `True`: Producto fuera de stock (92 productos - 46%)
  - `False`: Producto en stock (108 productos - 54%)
- **Distribución**:
  ```
  False: 108 productos (en stock)
  True:   92 productos (fuera de stock)
  ```
- **Interpretación**:
  - `True` = Out of Stock = No disponible
  - `False` = In Stock = Disponible
- **Uso**:
  - Análisis de disponibilidad de inventario
  - Identificación de oportunidades de venta perdidas
  - Comparación con competencia

---

#### 9. **Status**
- **Tipo de dato**: Text (String - Categorical)
- **Nulos**: 0 (0%)
- **Valores únicos**: 2
- **Descripción**: Estado del producto en relación con la competencia
- **Valores posibles**:
  1. **`Out Of Stock`** (92 productos - 46%)
     - Producto identificado en competencia pero actualmente sin stock
     - Oportunidad de captura de mercado

  2. **`No Competitor`** (108 productos - 54%)
     - No se encontró match exacto con competidores
     - Producto único de Coppel o sin competencia directa identificada
     - Oportunidad de pricing premium

- **Distribución**:
  ```
  No Competitor:  108 productos (54%)
  Out Of Stock:    92 productos (46%)
  ```
- **Uso**:
  - Análisis de posicionamiento competitivo
  - Identificación de productos exclusivos
  - Estrategia de pricing diferenciado

---

#### 10. **Difference**
- **Tipo de dato**: Numeric (Integer)
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Diferencia de precio con competidores
- **Valor**: 0 (constante en todos los registros)
- **Interpretación**: Campo calculado para diferencias de precio vs competencia
- **Estado actual**: No hay datos de diferencia (posiblemente porque no hay match de competidores o está pendiente de cálculo)
- **Uso esperado**:
  - Comparación directa de precios con competencia
  - Identificación de ventajas/desventajas de precio
  - Alertas de competitividad

---

### Métricas Agregadas del Dataset

| Métrica | Valor |
|---------|-------|
| **Total de productos** | 200 |
| **Precio promedio** | $19,264.69 MXN |
| **Precio mediano** | $16,842.50 MXN |
| **Descuento promedio** | $5,879.25 MXN (30.5%) |
| **Productos con descuento** | 172 (86%) |
| **Productos fuera de stock** | 92 (46%) |
| **Productos sin competencia** | 108 (54%) |
| **Marcas únicas** | 24 |
| **Precio más bajo** | $4,599 MXN |
| **Precio más alto** | $91,999 MXN |

---

## Dataset 2: Detailed Analysis

**Archivo**: `analyse_item_list_Coppel Mx (8).csv`
**Registros**: 107 productos
**Columnas**: 52

### Descripción General

Dataset detallado con información extendida de productos, incluyendo atributos técnicos, características de envío, especificaciones del refrigerador y datos del vendedor. Contiene 52 columnas con información granular.

### Estructura de Columnas

#### **Sección 1: Identificación del Producto**

##### 1. **Mongo_id**
- **Tipo de dato**: Text (String - ObjectId)
- **Nulos**: 0 (0%)
- **Valores únicos**: 107 (todos únicos)
- **Descripción**: Identificador único de MongoDB
- **Formato**: Hexadecimal de 24 caracteres
- **Ejemplo**: `682b2858e635c648ff03f414`
- **Uso**: Clave primaria en base de datos MongoDB

##### 2. **Sku**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 107
- **Descripción**: Código SKU del producto
- **Formato**: Numérico con separadores de miles (comas)
- **Ejemplos**: `660,582`, `74,381,197`
- **Uso**: Identificación y búsqueda de productos

##### 3. **Name**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 107
- **Descripción**: Nombre completo del producto
- **Ejemplo**: `Refrigerador Mabe Top Mount 10 Pies Negro RMA250PVMRP0`
- **Uso**: Identificación visual del producto

---

#### **Sección 2: Información de Precio**

##### 4. **Price**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 92
- **Descripción**: Precio en formato texto con separadores de miles
- **Rango**: $6,999 - $75,199 MXN
- **Formato**: `XX,XXX.0` con coma como separador de miles
- **Ejemplos**: `12,499.0`, `38,999.0`
- **Nota**: Requiere conversión a numérico para análisis
- **Uso**: Precio original del producto

##### 9. **Discount**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 77
- **Descripción**: Descuento aplicado en formato texto
- **Formato**: `X,XXX.0`
- **Ejemplos**: `3,700.0`, `14,500.0`
- **Uso**: Cálculo de precio final

##### 10. **Discount_Percent**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 0 (0%)
- **Valores únicos**: 97
- **Descripción**: Porcentaje de descuento
- **Rango**: 0% - 30.33%
- **Media**: 17.41%
- **Uso**: Análisis de estrategia promocional

---

#### **Sección 3: Información del Host y Vendedor**

##### 5. **Host**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Sitio web de origen
- **Valor**: `Coppel Mx`
- **Uso**: Identificación de la fuente de datos

##### 6. **Brand**
- **Tipo de dato**: Text (String)
- **Nulos**: 1 (0.9%)
- **Valores únicos**: 16
- **Descripción**: Marca del fabricante (con capitalización)
- **Ejemplos**: `Mabe`, `Samsung`, `Midea`
- **Principales marcas**:
  - Samsung: 22 productos
  - Mabe: 16 productos
  - Hisense: 12 productos
  - Midea: 12 productos
  - LG: 11 productos
  - Whirlpool: 10 productos
- **Diferencia vs Dataset 1**: Capitalización correcta

##### 51. **Seller**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Descripción**: Vendedor del producto en marketplace
- **Valores**:
  - Coppel (mayoría)
  - Bomssa
  - Tienda Oficial Samsung
  - Whirlpool México
  - Midea Mexico
  - Otros vendedores del marketplace
- **Uso**: Análisis de marketplace vs venta directa

##### 7. **Currency**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Moneda de los precios
- **Valor**: `peso`
- **Uso**: Referencia de moneda (MXN)

---

#### **Sección 4: Categorización**

##### 8. **Category**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 2
- **Descripción**: Categoría en formato navegacional español
- **Valores**:
  1. `Inicio > Línea Blanca > Refrigeradores y congeladores > Refrigeradores`
  2. `Inicio > Línea Blanca > Refrigeradores y congeladores > Frigobares`
- **Uso**: Navegación y filtrado por categoría

##### 12. **Category.1**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Categoría internacional estandarizada
- **Valor**: `IN > Electronics > Kitchen Appliances > Refrigerators`
- **Uso**: Categorización internacional

---

#### **Sección 5: Características Visuales**

##### 13. **Color**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Valores únicos**: 7
- **Descripción**: Color principal del refrigerador
- **Valores**:
  - `black` (negro)
  - `grey` (gris/grafito)
  - `silver` (plateado/acero)
  - `white` (blanco)
  - `blue` (azul)
  - Combinaciones: `silver,blue`
- **Distribución aproximada**:
  - Grey/Grafito: ~35%
  - Silver/Plateado: ~30%
  - Black/Negro: ~20%
  - White/Blanco: ~10%
  - Otros: ~5%
- **Uso**: Filtrado por preferencias estéticas, análisis de tendencias

---

#### **Sección 6: Especificaciones Técnicas del Refrigerador**

##### 18. **Refrigerator_model**
- **Tipo de dato**: Text (String)
- **Nulos**: 13 (12.1%)
- **Valores únicos**: 90
- **Descripción**: Código de modelo del refrigerador
- **Formato**: Alfanumérico, generalmente lowercase
- **Ejemplos**: `rma250pvmrp0`, `rf32cg5n10b1em`, `lt57bpsx.astfmxm`
- **Uso**: Identificación técnica precisa, búsqueda de manuales

##### 43. **Capacity_in_feet**
- **Tipo de dato**: Text (String)
- **Nulos**: 1 (0.9%)
- **Valores únicos**: 34
- **Descripción**: Capacidad del refrigerador
- **Formatos**:
  - `X feet` (ej: `10 feet`, `32 feet`)
  - `X.XX cubic feet` (ej: `12.71 cubic feet`)
- **Rango**: 7 - 32 pies cúbicos
- **Promedio**: ~16 pies cúbicos
- **Uso**: Segmentación por tamaño, análisis precio/capacidad

##### 44. **Refrigerator_type**
- **Tipo de dato**: Text (String)
- **Nulos**: 22 (20.6%)
- **Valores únicos**: 5
- **Descripción**: Tipo de configuración del refrigerador
- **Valores**:
  1. **`top mount`** - Congelador arriba (más común, ~50%)
  2. **`french door`** - Doble puerta con congelador abajo (~20%)
  3. **`side-by-side`** - Puertas lado a lado (~15%)
  4. **`bottom mount`** - Congelador abajo (~10%)
  5. **Otros/Sin especificar** (~5%)
- **Uso**: Segmentación por tipo, análisis de preferencias

##### 34. **No_of_doors**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 27 (25.2%)
- **Valores únicos**: 5
- **Descripción**: Número de puertas del refrigerador
- **Valores**:
  - `1.0` - Una puerta (frigobares, pequeños)
  - `2.0` - Dos puertas (top mount, bottom mount) - Más común
  - `3.0` - Tres puertas (french door con drawer)
  - `4.0` - Cuatro puertas (french door premium)
- **Distribución**:
  - 2 puertas: ~60%
  - 1 puerta: ~20%
  - 3-4 puertas: ~20%
- **Uso**: Clasificación de complejidad y premium

##### 40. **No_of_drawers**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 56 (52.3%)
- **Valores únicos**: 4
- **Descripción**: Número de cajones/gavetas internas
- **Valores**: 1, 2, 4
- **Uso**: Indicador de organización interna

##### 42. **Freezer_location**
- **Tipo de dato**: Text (String)
- **Nulos**: 24 (22.4%)
- **Valores únicos**: 3
- **Descripción**: Ubicación del congelador
- **Valores**:
  - `top` - Arriba (top mount) - ~60%
  - `bottom` - Abajo (bottom mount, french door) - ~30%
  - `side` - Al lado (side-by-side) - ~10%
- **Uso**: Clasificación de tipo de refrigerador

##### 45. **Semiautomatic**
- **Tipo de dato**: Text (String)
- **Nulos**: 105 (98.1%)
- **Valores únicos**: 2
- **Descripción**: Indicador de descongelamiento semiautomático
- **Valores**: `yes` (muy pocos casos)
- **Uso**: Característica de descongelamiento

---

#### **Sección 7: Tecnología y Control**

##### 24. **Control_panel**
- **Tipo de dato**: Text (String)
- **Nulos**: 56 (52.3%)
- **Valores únicos**: 3
- **Descripción**: Tipo de panel de control
- **Valores**:
  - `manual` - Control mecánico tradicional (~40%)
  - `digital` - Panel digital con display (~50%)
  - `touch panel` - Panel táctil (~10%)
- **Uso**: Indicador de modernidad y facilidad de uso

##### 32. **Control_panel.1**
- **Tipo de dato**: Text (String)
- **Descripción**: Campo duplicado de Control_panel
- **Nota**: Columna redundante

##### 39. **Display**
- **Tipo de dato**: Text (String)
- **Nulos**: 100 (93.5%)
- **Valores únicos**: 2
- **Descripción**: Presencia de pantalla/display
- **Valores**: `yes` (cuando está presente)
- **Uso**: Característica premium

##### 35. **Refrigeration_and_cooling_technology**
- **Tipo de dato**: Text (String)
- **Nulos**: 35 (32.7%)
- **Valores únicos**: 10
- **Descripción**: Tecnología de refrigeración utilizada
- **Valores principales**:
  - `smart inverter` - Compresor inverter inteligente
  - `inverter` - Compresor inverter estándar
  - `multi air flow` - Flujo de aire múltiple
  - `door cooling` - Enfriamiento de puerta
  - `all around cooling` - Enfriamiento envolvente
  - `frost free` - Libre de escarcha
  - `compressor cooling` - Enfriamiento por compresor
  - Combinaciones: `smart inverter,inverter`
- **Uso**:
  - Eficiencia energética
  - Característica de valor agregado
  - Posicionamiento premium

##### 38. **Temperature_control**
- **Tipo de dato**: Text (String)
- **Nulos**: 103 (96.3%)
- **Valores únicos**: 2
- **Descripción**: Tipo de control de temperatura
- **Valores**: `manual`, `digital`
- **Uso**: Precisión de control

##### 41. **Type_of_thaw**
- **Tipo de dato**: Text (String)
- **Nulos**: 61 (57.0%)
- **Valores únicos**: 2
- **Descripción**: Tipo de descongelamiento
- **Valores**:
  - `automatic` - Descongelamiento automático (frost-free)
  - `manual` - Requiere descongelamiento manual
- **Distribución**: Majority automatic
- **Uso**: Conveniencia y mantenimiento

---

#### **Sección 8: Eficiencia y Características Especiales**

##### 31. **Saving_energy_or_water**
- **Tipo de dato**: Text (String)
- **Nulos**: 47 (43.9%)
- **Valores únicos**: 2
- **Descripción**: Certificación de ahorro de energía/agua
- **Valores**:
  - `yes` - Tiene certificación de ahorro (~75% de los no-nulos)
  - `no` - No tiene certificación (~25%)
- **Uso**:
  - Eficiencia energética
  - Cumplimiento normativo
  - Valor agregado ecológico

##### 33. **Special_features**
- **Tipo de dato**: Numeric (Float)
- **Nulos**: 107 (100.0%)
- **Descripción**: Características especiales adicionales
- **Estado**: Sin datos en este dataset
- **Uso esperado**: Características únicas o premium

---

#### **Sección 9: Información de Envío y Logística**

##### 36. **Shipping_time**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Descripción**: Tiempo estimado de entrega
- **Formato**: Texto descriptivo en español
- **Valor típico**:
  ```
  *Dependerá del domicilio de entrega
  Recíbelo entre 2 y 7 días hábiles
  ```
  ```
  *Dependerá del domicilio de entrega
  Recíbelo entre 3 y 10 días hábiles
  ```
- **Variantes**:
  - 2-7 días hábiles (productos Coppel directo)
  - 3-10 días hábiles (marketplace/terceros)
- **Uso**:
  - Expectativa de entrega
  - Análisis de logística
  - Diferenciación por vendedor

##### 37. **Shipping_fees**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Descripción**: Costo de envío
- **Valor dominante**: `Envío gratis*`
- **Formato**: Texto con asterisco indicando condiciones
- **Condición**: Envío gratis con asterisco (aplican términos)
- **Uso**:
  - Costo total al cliente
  - Estrategia de envío

---

#### **Sección 10: Información Comercial**

##### 11. **Availability**
- **Tipo de dato**: Boolean
- **Nulos**: 0 (0%)
- **Valores únicos**: 1
- **Descripción**: Disponibilidad del producto
- **Valor**: `false` (todos los registros)
- **Interpretación**: Todos marcados como no disponibles al momento del scraping
- **Uso**: Control de inventario

##### 46. **Product_emi_plan**
- **Tipo de dato**: Text (String)
- **Nulos**: 0 (0%)
- **Descripción**: Plan de pagos a meses sin intereses (EMI - Equated Monthly Installment)
- **Formato**: Texto descriptivo con detalles de financiamiento
- **Ejemplo**:
  ```
  Desde $492 quincenales 11791 pesos en 24 quincenas
  ( $11,791 en 24 quincenas* )
  ```
- **Componentes**:
  - Pago quincenal mínimo
  - Total a pagar
  - Número de quincenas (típicamente 24)
  - Total con financiamiento
- **Uso**:
  - Opciones de financiamiento
  - Estrategia comercial
  - Accesibilidad del producto

##### 9. **Url**
- **Tipo de dato**: Text (String - URL)
- **Nulos**: 0 (0%)
- **Valores únicos**: 107
- **Descripción**: URL completa del producto
- **Formato**: Similar al Dataset 1
- **Dominio**: `www.coppel.com`
- **Tipos de URL**:
  - `/refrigerador-...pm-XXXXXX` (productos marketplace)
  - `/refrigerador-...mkp-XXXXXX` (marketplace partner)
  - `/pdp/refrigerador-...` (product detail page)
- **Uso**: Acceso directo, tracking, verificación

---

#### **Sección 11: Columnas Vacías (Sin Datos)**

Las siguientes columnas no contienen datos en este dataset (100% nulos), reservadas para otros tipos de productos:

##### Electrodomésticos de Lavado
- **14. Washing_machine_type** - Tipo de lavadora
- **15. Washing_machine_capacity** - Capacidad de lavadora
- **16. Washing_machine_model** - Modelo de lavadora
- **17. Dryer_model** - Modelo de secadora
- **23. Washing_program** - Programas de lavado

##### Dispositivos Móviles
- **19. Phone_model** - Modelo de teléfono
- **21. Storage** - Almacenamiento
- **22. Operating_system** - Sistema operativo

##### Estufas y Parrillas
- **20. Cooktop_model** - Modelo de parrilla
- **25. Cooktop_size** - Tamaño de parrilla
- **26. Stove_type** - Tipo de estufa
- **27. Ignition** - Tipo de encendido
- **28. No_of_burners** - Número de quemadores
- **29. Cooktop_type** - Tipo de cocina
- **30. Glass_stove_cover** - Cubierta de vidrio

##### Vehículos
- **47. Engine_displacement** - Cilindraje de motor
- **48. Motorcycle_type** - Tipo de motocicleta
- **49. Helmet_type** - Tipo de casco
- **50. Certification** - Certificación

**Nota**: Estas columnas existen porque el sistema de scraping es genérico y captura múltiples categorías de productos. En este dataset de refrigeradores, naturalmente están vacías.

---

### Métricas Agregadas del Dataset Detallado

| Métrica | Valor |
|---------|-------|
| **Total de productos** | 107 |
| **Precio promedio** | $18,645.78 MXN |
| **Precio mediano** | $16,499 MXN |
| **Descuento promedio** | $4,269.79 MXN (17.41%) |
| **Productos con descuento** | 96 (89.7%) |
| **Marcas únicas** | 16 |
| **Colores disponibles** | 7 |
| **Tipos de refrigerador** | 5 |
| **Vendedores únicos** | ~15 |
| **Precio más bajo** | $6,999 MXN |
| **Precio más alto** | $75,199 MXN |
| **Capacidad promedio** | ~16 pies cúbicos |
| **Tipo más común** | Top Mount (~50%) |

---

## Relaciones entre Datasets

### Campos Comunes

| Campo | Dataset 1 | Dataset 2 | Notas |
|-------|-----------|-----------|-------|
| **Name** | ✅ | ✅ | Nombres pueden variar ligeramente |
| **Brand** | ✅ (lowercase) | ✅ (capitalized) | Mismo contenido, diferente formato |
| **Price** | ✅ (numeric) | ✅ (string) | Requiere normalización |
| **Discount** | ✅ (numeric) | ✅ (string) | Requiere normalización |
| **Url** | ✅ | ✅ | Puede usarse para matching |
| **Category** | ✅ | ✅ | Formato internacional vs español |

### Estrategias de Join

#### 1. Por URL (Recomendado)
```python
# Más confiable, URLs son únicas
merged = pd.merge(df1, df2, on='Url', how='outer')
```

#### 2. Por Name (Fuzzy Matching)
```python
# Requiere similitud de strings
from fuzzywuzzy import fuzz
# Matching con threshold > 90%
```

#### 3. Por Brand + Model
```python
# Normalizar marcas primero
df1['Brand_norm'] = df1['Brand'].str.lower()
df2['Brand_norm'] = df2['Brand'].str.lower()
```

### Complementariedad

| Información | Dataset 1 | Dataset 2 |
|-------------|-----------|-----------|
| **Precio y descuento** | ✅ Completo | ✅ Completo |
| **Disponibilidad** | ✅ (Out, Status) | ✅ (Availability) |
| **Características técnicas** | ❌ | ✅ Completo |
| **Información de envío** | ❌ | ✅ |
| **Competencia** | ✅ (Status) | ❌ |
| **Vendedor marketplace** | ❌ | ✅ |

---

## Notas Técnicas

### Calidad de Datos

#### Dataset 1 (Exact Match)
- **Completitud**: Alta (>95%)
- **Valores nulos**: Mínimos, principalmente en Sku_id (32%)
- **Consistencia**: Excelente
- **Duplicados**: No detectados

#### Dataset 2 (Detailed)
- **Completitud**: Variable por columna
  - Campos core: >95%
  - Campos técnicos: 40-80%
  - Campos de otras categorías: 0%
- **Valores nulos**: Significativos en campos opcionales
- **Consistencia**: Buena, requiere limpieza de formatos

### Tipos de Datos que Requieren Conversión

| Campo | Tipo Actual | Tipo Objetivo | Acción |
|-------|-------------|---------------|--------|
| Price (Dataset 2) | String | Float | Remover comas, convertir |
| Discount (Dataset 2) | String | Float | Remover comas, convertir |
| Capacity_in_feet | String | Float | Extraer número |
| No_of_doors | Float | Integer | Convertir |
| Discount_Percent | Float | Float | OK |

### Procesamiento Recomendado

```python
# Limpieza de precios (Dataset 2)
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['Discount'] = df['Discount'].str.replace(',', '').astype(float)

# Extracción de capacidad
df['Capacity_Numeric'] = df['Capacity_in_feet'].str.extract(r'(\d+(?:\.\d+)?)')

# Normalización de marcas
df['Brand'] = df['Brand'].str.lower().str.strip()

# Cálculo de precio final
df['Final_Price'] = df['Price'] - df['Discount']
```

### Consideraciones de Encoding

- **Encoding de archivo**: UTF-8
- **Caracteres especiales**: Presentes en nombres (tildes, ñ)
- **Separador CSV**: Coma (,)
- **Delimitador de texto**: Comillas dobles (")
- **Formato de números**: Punto decimal, coma separador de miles

---

## Glosario

### Términos de E-commerce

| Término | Definición |
|---------|-----------|
| **SKU** | Stock Keeping Unit - Código único de producto |
| **EMI** | Equated Monthly Installment - Cuotas mensuales sin intereses |
| **Marketplace** | Plataforma donde terceros venden productos |
| **Out of Stock** | Producto sin inventario disponible |
| **Breadcrumb** | Navegación jerárquica (Categoría > Subcategoría > Producto) |

### Términos de Refrigeración

| Término | Definición |
|---------|-----------|
| **Top Mount** | Congelador ubicado en la parte superior |
| **Bottom Mount** | Congelador ubicado en la parte inferior |
| **French Door** | Doble puerta con congelador abajo |
| **Side-by-Side** | Refrigerador y congelador lado a lado |
| **Frost Free** | Sistema de descongelamiento automático |
| **Inverter** | Compresor de velocidad variable (ahorro energético) |
| **Multi Air Flow** | Sistema de circulación de aire múltiple |
| **Cubic Feet** | Unidad de capacidad (pies cúbicos) |

### Acrónimos

| Acrónimo | Significado |
|----------|-------------|
| **MXN** | Peso Mexicano (Mexican Peso) |
| **PM** | Product Model (en URL) |
| **MKP** | Marketplace Product (en URL) |
| **IN** | International (prefijo de categoría) |
| **PDP** | Product Detail Page |
| **CSV** | Comma-Separated Values |
| **UTF-8** | Formato de codificación de caracteres |

---

## Control de Versiones del Documento

| Versión | Fecha | Autor | Cambios |
|---------|-------|-------|---------|
| 1.0 | 2025-10-13 | Equipo Data Science | Creación inicial del diccionario |

---

## Referencias

- [Pandas Data Types](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)
- [Data Dictionary Best Practices](https://dataedo.com/kb/data-dictionary)
- [ISO 8601 Date Format](https://www.iso.org/iso-8601-date-and-time-format.html)

---

**Fin del Diccionario de Datos**

Para preguntas o actualizaciones, contactar al equipo de Data Science.
