# Plataforma de Web Scraping y Análisis Competitivo - Coppel MX

**Versión:** 1.0  
**Fecha:** Noviembre 2025  
**Patrocinador:** Luis Acosta / Dirección Estrategia  
**Equipo responsable:** Ruíz / Lozas  
**Status:** RECOMENDADO - GO

---

## Resumen Ejecutivo

Plataforma interna que extrae información pública de competidores (precio, promoción, disponibilidad y vendedor), la normaliza y la disponibiliza mediante una interfaz simple, descargas y API.

**Alcance MVP (3-4 meses):** 3-4 competidores, 2-3 categorías, frecuencia diaria, comparación por SKU con matching básico (exacto/variante).

**Beneficio esperado:** Habilitar playbooks de precio, reacción táctica ante movimientos de mercado, trazabilidad histórica para negociación con marcas, reducir dependencia de proveedor actual con bajo desempeño.

### Situación Actual del Proveedor

Análisis de datos actuales revela deficiencias críticas:

**Métricas del Proveedor:**
- Cobertura efectiva: 46% (54% productos sin competidor identificado)
- 46% productos fuera de stock en muestra
- Matching limitado a coincidencias exactas
- Sin evidencia de trazabilidad histórica robusta

**Hallazgos del Análisis:**
- Total productos analizados: 200 refrigeradores
- Precio promedio: $13,385 MXN (rango: $4,599 - $91,999 MXN)
- 86% productos con descuento (promedio 36.2%)
- Oportunidad perdida por OOS: $1,126,237 MXN
- Top marcas: Samsung (41), LG (31), Mabe (25), Whirlpool (24)

### Ventajas Competitivas del MVP

| Métrica | Proveedor Actual | Target MVP | Mejora |
|---------|------------------|------------|--------|
| Cobertura efectiva | 46% | ≥70% | +52% |
| Frescura (<24h) | Semanal | ≥90% | ✓ |
| Precisión precio | Desconocida | ≥97% | ✓ |
| Disponibilidad | Desconocida | ≥97% | ✓ |
| MTTR cambios | Desconocido | <24h | ✓ |
| Control | Nulo | Total | ✓ |

**ROI:** Break-even en 2-4 meses si proveedor cobra >$5,000/mes. Ahorro anual desde Año 2: $18,840-78,840 USD.

---

## Objetivo del Proyecto

### Fase Actual: Análisis de Datos

Analizar datos obtenidos mediante web scraping de competidores de Coppel México, identificando oportunidades de optimización de precios, gestión de inventario y estrategia competitiva.

**Archivos analizados:**

1. **exact_match_data** (200 productos):
   - Datos de productos con match exacto entre competidores
   - Campos: SKU, nombre, categoría, marca, precio, descuento, disponibilidad, diferencia precio
   - Problema: 54% sin competidor, 46% OOS

2. **analyse_item_list** (107 productos):
   - Análisis detallado con ~50 atributos técnicos
   - Incluye: especificaciones, seller, envío, planes EMI
   - Ventaja temporal del proveedor actual

### Fase MVP: Plataforma Propia

1. Snapshots programados (diarios; sub-diarios cuando sea viable)
2. Comparar por SKU: precio, precio lista, descuento, envío, disponibilidad, tipo vendedor (1P/3P)
3. UI simple (filtros, tabla comparativa, series tiempo) + CSV/Parquet + API + alertas
4. Matching v1 (exacto/variante) usando EAN/UPC/MPN/SKU y reglas simples

**KPIs objetivo:**

| KPI | Target MVP | Método Medición |
|-----|------------|-----------------|
| Cobertura | ≥70% SKUs prioritarios | matched_skus / golden_set |
| Frescura | ≥90% datos <24h | timestamp > NOW()-24h / total |
| Precisión | ≥97% | Muestreo estratificado semanal (50 SKUs) |
| Disponibilidad | ≥97% | Uptime procesos extracción |
| MTTR | <24h | Tiempo detección → fix |

---

## Alcance del Proyecto

### Incluye (MVP)

**Funcionalidad core:**
- Extracción de listados y páginas de producto en 3-4 competidores y 2-3 categorías
- Normalización de moneda, marca, pack/talla, categoría estándar
- Matching v1: exacto/variante
- UI con filtros, tabla comparativa, serie de tiempo y detalle con evidencias (URL y captura)
- API/exports y alertas (caída/subida precio >x%, cambio disponibilidad)

**Atributos a extraer:**
- Precio actual
- Precio lista/tachado
- Descuento porcentual
- Disponibilidad (In Stock/Out of Stock)
- Vendedor (1P/3P + nombre)
- URL producto
- Marca, categoría, SKU competidor

### No Incluye (Fase 2)

**Fuera de alcance MVP:**
- Similaridad avanzada (texto/imagen con ML)
- Share of search
- Ratings/reviews
- Cobertura masiva de todos sitios y categorías
- Sitios con alta fricción (algunos marketplaces globales)
- Atributos técnicos detallados (capacidad, color, tecnología)

**Recomendación Fase 2 (Semanas 13-20):**
- Implementar extracción de especificaciones por categoría
- Usar selectores CSS + plantillas configurables
- Considerar LLM API (GPT-4o/Claude) para atributos no estructurados
- Prioridad: Solo si el negocio lo requiere para decisiones comerciales

---

## Casos de Uso Habilitados

### Playbooks Operativos

1. **Playbooks de precio:** Detectar gaps y definir respuesta (mantener/igualar/contraatacar)
2. **Oportunidad por OOS competidor:** Cuando competidor queda sin stock
3. **Negociación con marcas:** Evidencia histórica de movimientos precio/promoción
4. **Alertas operativas:** Eventos relevantes para equipos comerciales

### Casos de Uso Adicionales (del análisis)

**Basados en datos actuales:**
- Detección de cambios de seller (competidor cambia 1P → 3P)
- Alertas de reposición (competidor recupera stock después OOS)
- Análisis de planes de financiamiento (MSI, planes EMI agresivos)
- Monitoreo de envío (cambios en costos/tiempos)

**Ejemplo de alertas configurables:**

```yaml
alertas:
  - nombre: "Caída precio >10% refrigeradores"
    condicion: "price_change < -10%"
    categoria: "Refrigeradores"
    competidores: ["Liverpool", "Elektra"]
    
  - nombre: "Competidor sin stock"
    condicion: "out_of_stock = true"
    skus: [golden_set_prioritario]
```

---

## Requerimientos y Supuestos

### Alcance Inicial

**Competidores:** 3-4 (sugerencia: Liverpool, Elektra, Palacio de Hierro)
- Evitar Mercado Libre/Amazon en MVP (cambios frecuentes)
- Empezar con retailers directos

**Categorías:** 2-3 (sugerencia: Línea Blanca, Electrónicos)
- Basado en datos del proveedor

**SKUs:** 5,000-15,000 canónicos priorizados
- Golden set inicial: 500-1,000 para QA

**Frecuencia:** Diaria 01:00/06:00
- Menor a diario solo si el sitio lo permite y es responsable

### Cumplimiento y Ética

**Cumplimiento:**
- Solo información pública
- Revisión de términos y robots.txt por dominio
- Límites de ritmo por sitio

**Anti-bot:**
- Cadencia conservadora
- Variación de agente de navegador
- Rotación de IP dentro de límites prudentes

**Seguridad:**
- Sin PII
- Acceso por roles
- Registro de fuente (URL) y timestamp por dato

---

## Arquitectura Técnica

### Componentes Principales

```
EXTRACCIÓN
├── Playwright (recomendado sobre Puppeteer)
├── Pool de workers con límites por dominio
├── Proxy rotatorio (Bright Data/Smartproxy)
└── Detección de cambios (hash estructura HTML)
    ↓
ORQUESTACIÓN
├── Prefect/Dagster (recomendado sobre Airflow)
├── DAGs por competidor/categoría
├── Retry logic inteligente
└── Rate limiting por dominio
    ↓
PROCESAMIENTO Y MATCHING
├── Normalización (precios, moneda, unidades)
├── Matching v1: exacto (EAN/UPC) + variante
├── Fuzzy matching (rapidfuzz)
└── Validaciones (precios, outliers)
    ↓
ALMACENAMIENTO
├── Raw: S3/GCS + Parquet (fecha/competidor)
├── Procesado: DuckDB/ClickHouse
└── Histórico: retención 12-24 meses
    ↓
PUBLICACIÓN
├── API: FastAPI (endpoints REST)
├── UI: Streamlit/Retool
└── Alertas: Email/Slack
```

### Stack Tecnológico Recomendado

| Componente | Opción A | Opción B | Recomendado | Justificación |
|------------|----------|----------|-------------|---------------|
| Scraping | Puppeteer | Playwright | **Playwright** | Mejor manejo SPA, APIs limpias |
| Orquestación | Airflow | Prefect/Dagster | **Prefect** | Moderno, mejor DX, Python-native |
| Storage raw | S3 + Parquet | GCS + Parquet | **S3 + Parquet** | Costo, integración |
| Storage queries | PostgreSQL | DuckDB | **DuckDB** | OLAP sobre Parquet, zero-config |
| API | Flask | FastAPI | **FastAPI** | Performance, docs auto, async |
| UI | Retool | Streamlit | **Streamlit** | Prototipado rápido, Python-only |
| Proxies | Smartproxy | Bright Data | **Bright Data** | Mejor uptime, más IPs residenciales |
| Matching | Custom | fuzzywuzzy | **rapidfuzz** | Más rápido que fuzzywuzzy |
| Monitoring | Datadog | Grafana + Loki | **Grafana + Loki** | Open-source, menor costo |

---

## Modelo de Datos

### Dimensiones

**dim_producto:**
```sql
producto_id (PK)
ean / upc / mpn
marca, familia, clase, departamento
pack / talla / color
categoria_estandar
```

**dim_competidor:**
```sql
competidor_id (PK)
nombre, dominio
tipo (retailer/marketplace)
limite_rpm
```

**dim_vendedor:**
```sql
vendedor_id (PK)
nombre, tipo (1P/3P)
competidor_id (FK)
```

**dim_tiempo:**
```sql
fecha_id (PK)
fecha, semana, mes, año, dia_semana
```

### Hechos

**fact_precio:**
```sql
precio_id (PK)
producto_id, competidor_id, vendedor_id, fecha_id (FKs)
precio_actual, precio_lista
descuento_monto, descuento_porcentaje
disponibilidad (boolean)
moneda, url
timestamp_extraccion
hash_evidencia
```

**fact_extraccion_log:**
```sql
log_id (PK)
competidor_id, producto_id (FKs)
timestamp, estado (success/retry/fail)
codigo_respuesta, latencia_ms
captcha_detectado (boolean)
error_mensaje
```

### Matching

**rel_matching:**
```sql
matching_id (PK)
producto_canonico_id, competidor_id (FKs)
sku_competidor
tipo_match (exacto/variante/fuzzy)
score_similitud (0-100)
fecha_validacion
validado_manualmente (boolean)
```

---

## Plan de Trabajo (12 Semanas)

### Semanas 0-2: Descubrimiento y Base

**Objetivos:**
- Validar competidores y categorías
- Levantar golden set (500-1,000 SKUs)
- Diseñar modelo de datos y mockups UI
- Revisar términos y robots por dominio

**Entregables:**
- [ ] Lista 3-4 competidores aprobada
- [ ] Lista 2-3 categorías con palabras búsqueda
- [ ] Golden set con EAN/UPC/MPN
- [ ] Mockups UI
- [ ] Matriz legal (ToS y robots.txt)

**Quick win:** Presentación mockups a usuarios finales

---

### Semanas 3-4: Infraestructura y Primer Sitio

**Objetivos:**
- Configurar repos, planificador, logs, storage
- Implementar primer sitio (búsquedas + producto)
- Normalización básica
- UI v0 (tabla + filtros)

**Entregables:**
- [ ] Repo + CI/CD básico
- [ ] Primer scraper funcional (1 competidor, 1 categoría)
- [ ] Storage Parquet funcionando
- [ ] UI v0 con tabla comparativa

**Hito crítico (Semana 4):** Demo funcional con datos reales 1 competidor

---

### Semanas 5-6: Más Sitios y Matching

**Objetivos:**
- Implementar sitio 2 y 3
- Control de calidad por muestreo
- Matching v1 (exacto/variante)
- API y UI v1 (serie tiempo)

**Entregables:**
- [ ] 3 competidores scraped diariamente
- [ ] Matching exacto por EAN/UPC
- [ ] Matching variantes (talla/color/pack)
- [ ] API endpoints básicos
- [ ] UI con serie tiempo

**KPI checkpoint:** Cobertura >50% en golden set

---

### Semanas 7-8: Robustez y Alertas

**Objetivos:**
- Detector de cambios de página
- Reintentos inteligentes
- Alertas por umbrales
- Demo con usuarios comerciales

**Entregables:**
- [ ] Detector cambios estructura
- [ ] Sistema alertas configurables
- [ ] Retry logic inteligente
- [ ] Demo usuarios comerciales
- [ ] Feedback documentado

**Validación usuarios:** 5 usuarios clave validan plataforma

---

### Semanas 9-12: Ampliación y Cierre MVP

**Objetivos:**
- Sumar categoría #2 (y #3 si aplica)
- Pruebas de carga
- Monitoreo KPIs 4 semanas
- Decisión Go/No-Go Fase 2

**Entregables:**
- [ ] 2-3 categorías operativas
- [ ] 4 semanas continuas cumpliendo KPIs
- [ ] Documentación completa
- [ ] Plan Fase 2
- [ ] Decisión Go/No-Go escalamiento

**Decisión final:** ¿Proceder Fase 2 o ajustar?

---

## Equipo y Recursos

### Equipo Mínimo

| Rol | Dedicación | Responsabilidades |
|-----|------------|-------------------|
| Líder técnico/Datos Sr | 1.0 FTE | Arquitectura, orquestación, observabilidad |
| Ingeniero datos | 1.0 FTE | Extracción, normalización, matching |
| Ingeniero back/frontend | 1.0 FTE | API, autenticación, interfaz, alertas |
| PM/PO | 0.75 FTE | Roadmap, riesgos, relación usuarios |

**Total MVP:** 3.75 FTE

**Fase 2 (opcional):** +0.5-1.0 analista/ML para similaridad avanzada

### Perfil Ideal

**Líder técnico:**
- Experiencia pipelines datos a escala
- Web scraping y anti-bot
- Arquitectura datos (lakehouse, warehouses)

**Ingeniero datos:**
- Python avanzado (Playwright/Scrapy)
- Regex, parsing, normalización
- Proxies y rate limiting

**Ingeniero full-stack:**
- FastAPI + React/Streamlit
- Autenticación (SSO)
- Dashboards

**PM:**
- Productos de datos
- Gestión stakeholders comerciales
- Pricing/ecommerce (deseable)

---

## Riesgos y Mitigaciones

| # | Riesgo | Prob. | Impacto | Mitigación | Status |
|---|--------|-------|---------|------------|--------|
| 1 | Defensas anti-extracción | Alta | Alto | Proxies residenciales + cadencia conservadora + headers realistas. Horarios valle. Pausas automáticas. | ⚠️ |
| 2 | Cambios estructura páginas | Media | Alto | Detector cambios automático. Plantillas por sitio. MTTR <24h. | ✓ |
| 3 | Calidad matching baja | Media | Medio | Golden set robusto (500-1K). Muestreo estratificado semanal. Fuzzy matching. | ✓ |
| 4 | Cumplimiento legal | Baja | Alto | Matriz ToS/robots.txt. Solo info pública. Ritmos responsables documentados. | ✓ |
| 5 | Costo conectividad/IPs | Media | Medio | Medición por dominio (GB/mes). Priorización categorías. Cacheo. Budget cap. | ⚠️ |
| 6 | Scope creep | Alta | Medio | Stick to MVP. Decir NO features. Documentar backlog Fase 2. Validar con sponsor. | 🚨 |
| 7 | Cambios marketplaces | Alta | Alto | Empezar retailers directos. Dejar ML/Amazon para Fase 2. | ✓ |
| 8 | Equipo incompleto | Media | Alto | Pre-asignar antes Sprint 0. Contratar/transferir 2 semanas anticipación. | ⚠️ |

**Leyenda:** ✓ Bien mitigado | ⚠️ Requiere atención | 🚨 Crítico - monitorear semanalmente

### Plan Contingencia Anti-bot

**Síntomas:** HTTP 403/429, CAPTCHAs frecuentes, bloqueos IP

**Acciones:**
1. Reducir frecuencia (diario → semanal temporal)
2. Aumentar pool proxies residenciales
3. Agregar delays aleatorios (3-10 seg entre requests)
4. Rotar User-Agents realistas
5. Si persiste: evaluar cambiar competidor en MVP

---

## Costos y ROI

### Drivers de Costo

**CAPEX (one-time):**
- Desarrollo MVP: 3.75 FTE × 3 meses × $10,000 USD promedio
- **Total CAPEX: $112,500 USD**

**OPEX (mensual recurrente):**

| Concepto | Conservador | Base | Ambicioso |
|----------|-------------|------|-----------|
| Cómputo/workers | $150 | $300 | $500 |
| Almacenamiento | $50 | $100 | $200 |
| Proxies/IPs | $300 | $800 | $1,500 |
| Monitoreo | $50 | $100 | $150 |
| Orquestación | $0 | $0 | $200 |
| Contingencia (10%) | $55 | $130 | $255 |
| **TOTAL MENSUAL** | **$605** | **$1,430** | **$2,805** |
| **TOTAL ANUAL** | **$7,260** | **$17,160** | **$33,660** |

### Comparativa Financiera

| Concepto | Proveedor Actual | MVP Año 1 | MVP Año 2+ |
|----------|------------------|-----------|------------|
| Costo total | $36,000-96,000 | $129,660 | $17,160 |
| Control | ❌ Nulo | ✓ Total | ✓ Total |
| Cobertura | 46% | 70-85% | 70-85%+ |

**Break-even:** Si proveedor cobra >$5,000/mes → ROI positivo en 2-4 meses

**Ahorro anual (desde Año 2):** $18,840-78,840 USD/año

### Ejemplo ROI (ilustrativo)

```
Supuestos:
- Categorías objetivo: 15% ventas totales ($100M anuales)
- Gap detectable: 40% del tiempo
- Mejora margen: 50 bps al reaccionar
- Reacción 2x más rápida con plataforma propia

Beneficio anual:
= $100M × 15% × 40% × 0.5% × 2
= $60,000 USD/año

ROI = ($60K - $17K OPEX) / $112K CAPEX
= 38% anual (conservador)
```

---

## Gobierno y Seguridad

### Comité Quincenal

**Participantes:**
- Sponsor (Luis Acosta)
- PM/PO
- Líder técnico
- Representante usuarios comerciales
- Representante legal (compliance)

**Agenda:**
- Avance vs plan (semáforo)
- KPIs actuales
- Riesgos top 3
- Decisiones requeridas
- Budget burn rate

### Tablero de Salud (actualización diaria)

```
SALUD DEL SISTEMA (last 24h)
Cobertura:          76% ✓
Frescura (<24h):    92% ✓
Precisión:          98% ✓
Uptime:             99.2% ✓

Fallos por sitio:
  - Liverpool:      2 (403 errors)
  - Elektra:        0 ✓
  - Palacio:        1 (timeout)

Consumo:
  - GB/mes:         180 / 300 (60%)
  - Costo proxies:  $620 / $800
```

### Auditoría y Trazabilidad

**Cada registro incluye:**
- URL original
- Timestamp extracción
- User-Agent usado
- IP/proxy utilizado
- Hash SHA-256 página (evidencia)
- Usuario que ejecutó proceso

**Mini-capturas:**
- Screenshot precio/disponibilidad (casos críticos)
- Almacenamiento: S3 con lifecycle (30-90 días)
- Uso: resolución disputas, validación cambios

### Seguridad

**Acceso:**
- SSO corporativo (Azure AD/Okta)
- RBAC (admin, comercial, analista, auditor)
- MFA obligatorio para admins

**Datos:**
- Cifrado en tránsito (TLS 1.3)
- Cifrado en reposo (S3 server-side encryption)
- Sin PII de clientes
- Logs de acceso a datos sensibles

**Compliance:**
- Revisión legal ToS por dominio (cada 6 meses)
- Respeto robots.txt
- Rate limiting documentado
- Proceso opt-out si competidor lo solicita

---

## Análisis de Datos Actual

### Herramientas de Análisis

**Estructura del proyecto:**
```
scraping-coppel/
├── config/
│   └── environment.yml
├── data/
│   ├── raw/
│   │   ├── exact_match_data_*.csv
│   │   └── analyse_item_list_*.csv
│   └── processed/
├── docs/
├── notebooks/
│   └── analysis_notebook.ipynb
└── scripts/
    ├── quick_analysis.py
    └── start_jupyter.sh
```

### Análisis Disponibles

**1. Análisis Rápido (Terminal)**
```bash
python scripts/quick_analysis.py
```

**Output:**
- Métricas generales de precios
- Análisis de descuentos por marca
- Productos fuera de stock
- Productos sin competencia
- Top 10 marcas

**2. Análisis Detallado (Jupyter Notebook)**
```bash
bash scripts/start_jupyter.sh
```

**Secciones:**
1. Configuración y carga de datos
2. Limpieza y validación
3. Análisis exploratorio (EDA)
4. Análisis de competitividad
5. Análisis de atributos técnicos
6. Visualizaciones avanzadas (Plotly)
7. Insights y recomendaciones

### Tecnologías Utilizadas

**Core:**
- Python 3.11
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly

**Análisis:**
- Scikit-learn
- Statsmodels
- ydata-profiling

**Tools:**
- Jupyter
- Conda
- Git

### Instalación

```bash
# Crear ambiente
conda env create -f config/environment.yml

# Activar ambiente
conda activate webscraping-analysis

# Ejecutar análisis
python scripts/quick_analysis.py
```

---

## Recomendaciones Estratégicas

### Basadas en Análisis Actual

**1. Optimización de Precios**
- Revisar productos con descuentos >30%
- Implementar dynamic pricing
- Analizar elasticidad por segmento

**2. Gestión de Inventario**
- Reabastecimiento prioritario (92 productos OOS)
- Alertas automáticas de stock
- Evaluar productos de baja rotación

**3. Inteligencia Competitiva**
- Monitoreo semanal de precios
- Tracking de nuevos productos
- Análisis de gaps en catálogo

**4. Análisis Continuo**
- Dashboard en tiempo real
- Actualización automática de datos
- Modelos predictivos de demanda

### Roadmap Recomendado

**Corto Plazo (1-2 semanas):**
- [ ] Ejecutar análisis con datos actualizados
- [ ] Validar hallazgos con equipo de negocio
- [ ] Implementar recomendaciones prioritarias

**Mediano Plazo (1-2 meses):**
- [ ] Automatizar scraping y actualización de datos
- [ ] Desarrollar dashboard interactivo (Streamlit/Dash)
- [ ] Implementar alertas de precio

**Largo Plazo (3-6 meses):**
- [ ] Modelos predictivos de demanda
- [ ] Sistema de dynamic pricing
- [ ] Integración con sistemas de inventario
- [ ] Expansión a otras categorías

---

## Checklist para Arrancar

### Pre-Sprint 0

**Negocio:**
- [ ] Aprobar presupuesto ($112K CAPEX + $17K/año OPEX)
- [ ] Asignar equipo (3.75 FTE)
- [ ] Definir competidores (3-4)
- [ ] Definir categorías (2-3)
- [ ] Identificar usuarios clave validación (5 nombres)

**Técnico:**
- [ ] Acceso cloud provider (AWS/GCP/Azure)
- [ ] Cuenta proxies (Bright Data trial)
- [ ] Repo git configurado
- [ ] Slack/Teams channel

### Sprint 0 (Semanas 0-2)

**Datos:**
- [ ] Golden set 500-1,000 SKUs con EAN/UPC/MPN
- [ ] Palabras búsqueda por categoría
- [ ] URLs ejemplo productos por competidor

**Legal:**
- [ ] Matriz compliance (ToS y robots.txt)
- [ ] Aprobación legal interna
- [ ] Definir límites frecuencia responsables

**Usuario:**
- [ ] Mockups UI validados
- [ ] Casos uso priorizados
- [ ] Definición alertas críticas

---

## Decisiones Requeridas

### Críticas (esta semana)

1. ✓ Aprobación alcance MVP
2. 🔴 Definición competidores y categorías
   - Propuesta: Liverpool, Elektra, Palacio de Hierro
   - Categorías: Línea Blanca, Electrónicos
3. 🟡 Inicio Sprint 0 (2 semanas)
4. 🟡 Primer hito visible (Semana 4): tabla comparativa funcional 1 sitio

### Secundarias (2 semanas)

5. Plan comunicación a equipos comerciales
6. Proceso feedback usuarios durante MVP
7. Criterios éxito aprobar Fase 2

---

## Glosario

| Término | Definición |
|---------|------------|
| Extracción (scraping) | Obtención automatizada de información pública de páginas web |
| Snapshot | Captura de estado (precio/stock) en fecha/hora específica |
| SKU canónico | Identificador interno para comparar entre competidores |
| Matching exacto | Mismo producto identificado por EAN/UPC/MPN |
| Matching variante | Misma referencia con diferencias (talla, color, pack) |
| Matching fuzzy | Similitud aproximada basada en texto (>85% similitud) |
| 1P (First Party) | Producto vendido directamente por retailer |
| 3P (Third Party) | Producto vendido por seller externo en marketplace |
| Sitio alta fricción | Página con defensas técnicas que requieren ritmos bajos |
| Golden set | Conjunto SKUs prioritarios para QA y validación |
| MTTR | Mean Time To Recovery - tiempo recuperación ante fallas |
| SLO | Service Level Objective - objetivo nivel servicio |

---

## Próximos Pasos Inmediatos

### Esta Semana
1. Sponsor aprueba documento y presupuesto
2. Definir competidores finales
3. Definir categorías finales
4. Pre-asignar equipo (4 personas con nombres)

### Próxima Semana (Semana 0)
5. Kickoff del proyecto con equipo completo
6. Construir golden set (500 SKUs)
7. Revisar ToS y robots.txt de competidores
8. Setup técnico inicial (repo, cloud, proxies trial)

### Semana 4 (primer hito)
9. Demo funcional con datos reales 1 competidor
10. Validación con usuarios (5 personas comerciales)

---

## Contactos del Proyecto

**Patrocinador:**
- Luis Acosta / Dirección Estrategia
- Email: luis.acosta@empresa.com

**Equipo responsable:**
- Ruíz (PM) - ruiz@empresa.com
- Lozas (Tech Lead) - lozas@empresa.com

**Stakeholders clave:**
- Comercial: [Definir]
- Legal: [Definir]
- Finanzas: [Definir]

---

## Firma de Aprobación

| Rol | Nombre | Aprobación | Fecha |
|-----|--------|------------|-------|
| Sponsor | Luis Acosta | ☐ Apruebo | __/__/__ |
| Tech Lead | Lozas | ☐ Apruebo | __/__/__ |
| PM | Ruíz | ☐ Apruebo | __/__/__ |
| Legal | [Nombre] | ☐ Apruebo | __/__/__ |

---

## Recomendación Final

**Status:** RECOMENDADO - GO

Este MVP es técnicamente viable, financieramente justificable, y estratégicamente necesario dado el desempeño deficiente del proveedor actual (54% sin matching).

**Confianza en éxito:** Alta (80%)  
**Riesgo principal:** Scope creep y anti-bot en sitios complejos  
**Mitigación clave:** Disciplina en MVP, empezar con retailers simples

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Próxima revisión:** Semana 4 (hito de demo funcional)
