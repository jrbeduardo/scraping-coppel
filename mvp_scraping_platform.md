# Plataforma interna de scraping y análisis competitivo de precios (MVP)

**Versión:** 0.2 (análisis técnico de viabilidad integrado)  
**Fecha:** 15/oct/2025  
**Patrocinador:** Luis Acosta / Dirección Estrategia  
**Equipo responsable:** Ruíz / Lozas  
**Status:** ✅ **RECOMENDADO - GO**

---

## 📊 Resumen Ejecutivo

Construiremos una plataforma interna que extrae de forma programada información pública de competidores (precio, promoción, disponibilidad y vendedor), la normaliza y la disponibiliza en una interfaz simple y mediante descargas/API.

El MVP (3/4 meses) se acota a 3/4 competidores y 2/3 categorías con frecuencia diaria (o menor solo si es responsable y viable), y comparación por SKU con matching básico (exacto/variante). Sitios de alta fricción entran en Fase 2 con ventanas y frecuencia reducidas.

**Beneficio esperado (direccional):** habilitar playbooks de precio y reacción táctica ante movimientos de mercado, ganar trazabilidad histórica para negociar con marcas, reducir dependencia de un proveedor que hoy no cumple capacidades/SLAs.

### ✅ Evaluación de Viabilidad Técnica

**Status:** ALTAMENTE VIABLE - Se recomienda proceder

**Análisis del proveedor actual:**
- 📉 **Cobertura deficiente:** 54% de productos sin competidor identificado (archivo exact_match)
- 📉 **Matching limitado:** Solo coincidencias exactas, sin variantes
- ✅ **Extracción rica:** ~50 atributos por producto (ventaja temporal)
- ❌ **Sin trazabilidad:** No hay evidencia de históricos robustos

**Ventajas competitivas del MVP:**
- 🎯 **Matching mejorado:** Target 70-85% vs 46% actual
- 📈 **Frescura garantizada:** Datos <24h en >90% SKUs
- 🔧 **Control total:** Pipeline propio, sin dependencias
- 💰 **ROI positivo:** Break-even en 2-4 meses

---

## 1) Antecedentes y problema

### Situación actual
- Dependencia de un tercero con resultados irregulares en frescura, cobertura y precisión
- Decisiones comerciales con latencia y poca evidencia histórica
- Necesitamos un pipeline propio con alcance realista, riesgos controlados y KPIs claros

### 🔍 Análisis de datos del proveedor actual

**Archivo 1 - `analyse_item_list` (107 productos):**
- Extracción detallada con ~50 atributos específicos por categoría
- Incluye: precio, descuento, marca, seller, disponibilidad, envío, planes EMI
- Atributos técnicos: capacidad, modelo, tecnología, certificaciones

**Archivo 2 - `exact_match_data` (200 productos de electrónicos):**
- ⚠️ **46% productos "Out Of Stock"**
- ⚠️ **54% productos "No Competitor"** ← Principal problema
- Solo matching básico (campo "Difference" = 0 en todos los casos)
- Categoría: Refrigeradores (Samsung 41, LG 31, Mabe 25, Whirlpool 24)
- Rango de precios: $4,599 - $91,999 MXN

**Conclusión:** El proveedor actual NO está cumpliendo con las expectativas de cobertura y matching.

---

## 2) Objetivo del MVP (3/4 meses)

1. Disponibilizar snapshots programados (diarios; sub-diarios cuando sea viable)
2. Comparar por SKU: precio, precio lista, % descuento, envío (si es visible), disponibilidad y tipo de vendedor (1P/3P)
3. UI simple (filtros, tabla comparativa, series de tiempo) + descargar (CSV/Parquet) + API interna + alertas por umbrales
4. Matching v1 (exacto/variante) usando claves duras (EAN/UPC/MPN/SKU) y reglas simples (pack/talla/color)

### 🎯 KPIs objetivo vs proveedor actual

| Métrica | Proveedor Actual | Target MVP | Mejora |
|---------|------------------|------------|--------|
| Cobertura efectiva | ~46% | ≥70% | +52% |
| Frescura (<24h) | ¿Semanal? | ≥90% | ✅ |
| Precisión precio | ¿? | ≥97% | ✅ |
| Disponibilidad sistema | ¿? | ≥97% | ✅ |

---

## 3) Alcance del MVP (incluye / no incluye)

### ✅ Incluye

**Funcionalidad core:**
- Extracción de listados de búsqueda y páginas de producto en 3/4 competidores y 2/3 categorías
- Normalización de moneda, marca, pack/talla, categoría estándar
- Matching v1: exacto/variante
- UI con filtros, tabla comparativa, serie de tiempo y detalle con evidencias (URL y mini-captura)
- API/exports y alertas (p. ej., caída/subida de precio >x% o cambio de disponibilidad)

**Atributos a extraer (MVP):**
- Precio actual
- Precio lista / precio tachado
- % Descuento
- Disponibilidad (In Stock / Out of Stock)
- Vendedor (1P / 3P + nombre si aplica)
- URL del producto
- Marca
- Categoría
- SKU del competidor

### ⚠️ No incluye (Fase 2)

**Fuera de alcance MVP:**
- Similaridad avanzada (texto/imagen con ML)
- Share of search
- Ratings/reviews
- Cobertura masiva de todos los sitios y categorías
- Sitios con alta fricción (ej.: algunos marketplaces globales)
- **Atributos técnicos detallados** (capacidad, color, tecnología, etc.) ← El proveedor actual los tiene

### 📋 Recomendación: Plan para Fase 2

**Atributos técnicos (Semanas 13-20):**
- Implementar extracción de especificaciones por categoría
- Usar selectores CSS específicos + plantillas configurables
- Considerar LLM API (GPT-4o/Claude) para extracción de atributos no estructurados
- **Prioridad:** Solo si el negocio lo requiere para decisiones comerciales

---

## 4) Casos de uso habilitados

### Playbooks operativos
- **Playbooks de precio:** detectar gaps y definir respuesta (mantener/igualar/contraatacar)
- **Oportunidad por OOS competidor:** cuando el competidor queda sin stock
- **Negociación con marcas:** evidencia histórica de movimientos de precio/promoción
- **Alertas operativas:** eventos relevantes para equipos comerciales

### 🔍 Casos de uso adicionales identificados

**Basados en el análisis de datos:**
- **Detección de cambios de seller:** Competidor cambia de 1P a 3P (ejemplo: Coppel vs Bomssa en análisis)
- **Alertas de reposición:** Competidor recupera stock después de OOS
- **Análisis de planes de financiamiento:** Si competidor ofrece MSI o planes EMI más agresivos
- **Monitoreo de envío:** Cambios en costos/tiempos de envío

---

## 5) Requerimientos y supuestos

### Alcance inicial
- **Competidores iniciales:** 3/4 (definir con negocio)
  - 💡 **Sugerencia:** Liverpool, Elektra, Palacio de Hierro (evitar Mercado Libre/Amazon en MVP)
- **Categorías iniciales:** 2/3 (definir con negocio)
  - 💡 **Sugerencia:** Línea Blanca, Electrónicos (basado en datos del proveedor)
- **SKUs canónicos priorizados:** 5,000/15,000 (con golden set inicial de 500/1,000 para QA)
- **Frecuencia:** diaria 01:00/06:00, menor a diario solo si el sitio lo permite y es responsable

### Cumplimiento y ética
- **Cumplimiento:** solo información pública; revisión de términos y robots.txt por dominio; límites de ritmo por sitio
- **Anti-bot:** cadencia conservadora, variación de agente de navegador y rotación de IP dentro de límites prudentes
- **Seguridad:** sin PII; acceso por roles; registro de fuente (URL) y timestamp por dato

### ⚠️ Riesgo adicional identificado
- **Cambios frecuentes en marketplaces:** Mercado Libre y Amazon cambian estructura constantemente
- **Mitigación:** Empezar con retailers directos (Liverpool, Coppel competencia, etc.)

---

## 6) Entrega de datos y disponibilidad

### Interfaces disponibles
- **Interfaz web:** filtros (competidor, categoría, marca, SKU, fecha), tabla comparativa y tendencias
- **Descarga:** CSV/Parquet del resultado filtrado
- **API interna:** endpoints para consulta programática
- **Alertas:** reglas simples (condición, umbral, destinatarios) con historial
- **Acuerdos operativos:** ventana de actualización nocturna; tiempos de reintento ante fallas

### 📊 Ejemplo de alertas configurables

```yaml
alertas:
  - nombre: "Caída de precio >10% en refrigeradores"
    condicion: "price_change < -10%"
    categoria: "Refrigeradores"
    competidores: ["Liverpool", "Elektra"]
    destinatarios: ["comercial@empresa.com"]
    
  - nombre: "Competidor sin stock"
    condicion: "out_of_stock = true"
    skus: [golden_set_prioritario]
    destinatarios: ["operaciones@empresa.com"]
```

---

## 7) Arquitectura

### Componentes principales

```
┌─────────────────────────────────────────────────────┐
│  CAPA DE EXTRACCIÓN                                  │
│  - Playwright/Puppeteer                              │
│  - Pool de workers con límites por dominio           │
│  - Proxy rotatorio (Bright Data/Smartproxy)          │
│  - Detección de cambios (hash estructura HTML)       │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  ORQUESTACIÓN                                        │
│  - Prefect/Dagster/Airflow                           │
│  - DAGs por competidor/categoría                     │
│  - Retry logic inteligente                           │
│  - Rate limiting por dominio                         │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  PROCESAMIENTO Y MATCHING                            │
│  - Normalización (precios, moneda, unidades)        │
│  - Matching v1: exacto (EAN/UPC) + variante         │
│  - Fuzzy matching (fuzzywuzzy/rapidfuzz)            │
│  - Validaciones (precios, outliers)                  │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  ALMACENAMIENTO                                      │
│  - Raw: S3/GCS + Parquet (fecha/competidor)         │
│  - Procesado: DuckDB/ClickHouse                      │
│  - Histórico: retención 12-24 meses                 │
└─────────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────────┐
│  CAPA DE PUBLICACIÓN                                 │
│  - API: FastAPI (endpoints REST)                     │
│  - UI: Streamlit/Retool                              │
│  - Alertas: Email/Slack                              │
└─────────────────────────────────────────────────────┘
```

### Descripción de componentes

**Extracción:**
- Automatización de navegador (capaz de cargar páginas dinámicas)
- Plantillas por sitio y reintentos
- **Recomendación:** Playwright sobre Puppeteer (mejor manejo de SPA)

**Orquestación:**
- Planificador de tareas y cola de trabajos con límites por dominio
- **Recomendación:** Prefect (más moderno) o Dagster

**Procesamiento:**
- Limpieza, normalización y validaciones (precios, moneda, disponibilidad)
- **Adicional:** Fuzzy matching para mejorar cobertura (70-85% target)

**Almacenamiento:**
- Archivos columnados (Parquet/Delta) por fecha/sitio
- Repositorio analítico (tipo warehouse) para consultas
- **Recomendación:** DuckDB para queries rápidas en Parquet

**Publicación:**
- API interna, descargas y UI

**Observabilidad:**
- Bitácoras, métricas, mini-capturas como evidencia y tableros de salud

---

## 8) Modelo de datos

### Dimensiones (catálogos)

**Producto canónico:**
```sql
dim_producto:
  - producto_id (PK)
  - ean / upc / mpn
  - marca
  - familia
  - clase
  - departamento
  - pack / talla / color
  - categoria_estandar
```

**Competidor:**
```sql
dim_competidor:
  - competidor_id (PK)
  - nombre
  - dominio
  - tipo (retailer/marketplace)
  - limite_rpm (rate limit)
```

**Vendedor:**
```sql
dim_vendedor:
  - vendedor_id (PK)
  - nombre
  - tipo (1P/3P)
  - competidor_id (FK)
```

**Tiempo:**
```sql
dim_tiempo:
  - fecha_id (PK)
  - fecha
  - semana
  - mes
  - año
  - dia_semana
```

### Hechos (mediciones)

**Precio histórico:**
```sql
fact_precio:
  - precio_id (PK)
  - producto_id (FK)
  - competidor_id (FK)
  - vendedor_id (FK)
  - fecha_id (FK)
  - precio_actual
  - precio_lista
  - descuento_monto
  - descuento_porcentaje
  - disponibilidad (boolean)
  - moneda
  - url
  - timestamp_extraccion
  - hash_evidencia (mini-captura)
```

**Metadata del proceso:**
```sql
fact_extraccion_log:
  - log_id (PK)
  - competidor_id (FK)
  - producto_id (FK)
  - timestamp
  - estado (success/retry/fail)
  - codigo_respuesta
  - latencia_ms
  - captcha_detectado (boolean)
  - error_mensaje
```

### Vínculo de matching (MVP)

**Tabla de matching:**
```sql
rel_matching:
  - matching_id (PK)
  - producto_canonico_id (FK)
  - competidor_id (FK)
  - sku_competidor
  - tipo_match (exacto/variante/fuzzy)
  - score_similitud (0-100)
  - fecha_validacion
  - validado_manualmente (boolean)
```

**Tipos de match:**
- **Exacto:** EAN/UPC/MPN coincide 100%
- **Variante:** Mismo producto, diferente talla/color/pack
- **Fuzzy:** Similitud >85% en nombre normalizado (Fase MVP tardía)

---

## 9) KPIs y criterios de éxito (SLOs)

### Métricas core del MVP

| KPI | Target MVP | Método de medición |
|-----|------------|-------------------|
| **Cobertura** | ≥70% de SKUs prioritarios con ≥1 coincidencia | `COUNT(DISTINCT matched_skus) / COUNT(golden_set)` |
| **Frescura** | ≥90% de SKUs con datos de las últimas 24h | `COUNT(WHERE timestamp > NOW()-24h) / total_skus` |
| **Precisión (precio/promo)** | ≥97% en muestreo estratificado | Validación manual semanal (50 SKUs) |
| **Disponibilidad de procesos** | ≥97% | Uptime de procesos de extracción |
| **Tiempo de recuperación ante cambio de página** | <24h | MTTR desde detección hasta fix |

### Definición de éxito del MVP

Cumplir estos indicadores en **≥2 competidores** y **≥2 categorías** durante **4 semanas continuas**.

### 📊 Comparativa con proveedor actual

| Aspecto | Proveedor Actual | Target MVP | Mejora |
|---------|------------------|------------|--------|
| Matching efectivo | ~46% | ≥70% | **+52%** |
| Frescura | Semanal (?) | Diaria (>90%) | **✅** |
| Precisión | Desconocida | ≥97% | **✅** |
| MTTR cambios | Desconocido | <24h | **✅** |
| Trazabilidad | Limitada | Completa | **✅** |

---

## 10) Plan de trabajo (12 semanas)

### Semanas 0-2: Descubrimiento y base
**Objetivos:**
- Validar competidores y categorías; levantar golden set (500/1,000 SKUs)
- Diseñar modelo de datos y mockups de UI; revisar términos y robots por dominio
- Definir KPIs y "Definition of Done"

**Entregables:**
- [ ] Lista de 3-4 competidores aprobada
- [ ] Lista de 2-3 categorías con palabras de búsqueda
- [ ] Golden set con EAN/UPC/MPN cuando exista
- [ ] Mockups de UI
- [ ] Matriz legal (ToS y robots.txt por dominio)

**🎯 Quick win:** Presentación de mockups a usuarios finales

---

### Semanas 3-4: Infraestructura y primer sitio
**Objetivos:**
- Configurar repos, planificador, bitácoras y almacenamiento
- Implementar primer sitio (búsquedas + producto) y normalización
- UI v0 (tabla + filtros) y descarga básica

**Entregables:**
- [ ] Repo configurado + CI/CD básico
- [ ] Primer scraper funcional (1 competidor, 1 categoría)
- [ ] Storage en Parquet funcionando
- [ ] UI v0 con tabla comparativa básica

**🎯 Hito crítico (Semana 4):** Demo funcional con datos reales de 1 competidor

---

### Semanas 5-6: Más sitios y matching
**Objetivos:**
- Implementar sitio 2 y sitio 3; control de calidad por muestreo
- Matching v1 (exacto/variante); API y UI v1 (serie de tiempo)

**Entregables:**
- [ ] 3 competidores scraped diariamente
- [ ] Matching exacto por EAN/UPC
- [ ] Matching de variantes (talla/color/pack)
- [ ] API endpoints básicos
- [ ] UI con serie de tiempo

**🎯 KPI checkpoint:** Cobertura >50% en golden set

---

### Semanas 7-8: Robustez y alertas
**Objetivos:**
- Detector de cambios de página; reintentos inteligentes; alertas por umbrales
- Demostración con usuarios comerciales y ajustes

**Entregables:**
- [ ] Detector de cambios de estructura
- [ ] Sistema de alertas configurables
- [ ] Retry logic inteligente
- [ ] Demo con usuarios comerciales
- [ ] Feedback documentado

**🎯 Validación de usuarios:** 5 usuarios clave validan la plataforma

---

### Semanas 9-12: Ampliación y cierre del MVP
**Objetivos:**
- Sumar categoría #2 (y #3 si aplica); pruebas de carga
- Monitoreo de KPIs 4 semanas; decisión Go/No-Go y backlog de Fase 2

**Entregables:**
- [ ] 2-3 categorías completamente operativas
- [ ] 4 semanas continuas cumpliendo KPIs
- [ ] Documentación completa
- [ ] Plan de Fase 2
- [ ] Decisión Go/No-Go para escalamiento

**🎯 Decisión final:** ¿Proceder con Fase 2 o ajustar?

---

## 11) Equipo mínimo y roles

| Rol | Dedicación | Responsabilidades |
|-----|------------|-------------------|
| **Líder técnico / Datos Sr** | 1.0 FTE | Arquitectura, orquestación, observabilidad, robustez |
| **Ingeniero/a de datos** | 1.0 FTE | Extracción, normalización, procesos, matching |
| **Ingeniero/a back/frontend** | 1.0 FTE | API, autenticación, interfaz, descargas, alertas |
| **PM/PO** | 0.75 FTE | Roadmap, riesgos, relación con usuarios y sponsors |

**Total estimado:** 3.75 FTE para el MVP

**Fase 2 (opcional):** +0.5–1.0 analista/ML para similaridad avanzada

### Perfil ideal del equipo

**Líder técnico:**
- Experiencia con pipelines de datos a escala
- Conocimiento de web scraping y anti-bot
- Experiencia con arquitectura de datos (lakehouse, warehouses)

**Ingeniero de datos:**
- Python avanzado (Playwright/Scrapy)
- Regex, parsing, normalización de datos
- Experiencia con proxies y rate limiting

**Ingeniero full-stack:**
- FastAPI + React/Streamlit
- Autenticación (SSO)
- Desarrollo de dashboards

**PM:**
- Experiencia con productos de datos
- Gestión de stakeholders comerciales
- Conocimiento de pricing/ecommerce (deseable)

---

## 12) Riesgos y mitigaciones

### Matriz de riesgos

| # | Riesgo | Prob. | Impacto | Mitigación | Status |
|---|--------|-------|---------|------------|--------|
| 1 | **Defensas anti-extracción en sitios** | Alta | Alto | Proxies residenciales + cadencia conservadora + headers realistas. Horarios valle. Pausas automáticas ante bloqueos. | ⚠️ |
| 2 | **Cambios en estructura de páginas** | Media | Alto | Detector de cambios automático. Plantillas por sitio. MTTR <24h con alertas. | ✅ |
| 3 | **Calidad de matching baja** | Media | Medio | Golden set robusto (500-1K SKUs). Muestreo estratificado semanal. Validación manual inicial. Fuzzy matching en caso necesario. | ✅ |
| 4 | **Cumplimiento legal/operativo** | Baja | Alto | Matriz por dominio (ToS y robots.txt). Solo info pública. Ritmos responsables documentados. | ✅ |
| 5 | **Costo de conectividad/IPs** | Media | Medio | Medición por dominio (GB/mes). Priorización de categorías. Cacheo selectivo. Budget cap mensual. | ⚠️ |
| 6 | **Scope creep (features adicionales)** | Alta | Medio | **Stick to MVP.** Decir NO a features. Documentar en backlog Fase 2. Validar con sponsor antes de agregar. | 🚨 |
| 7 | **Cambios frecuentes en marketplaces** | Alta | Alto | Empezar con retailers directos. Dejar marketplaces (ML/Amazon) para Fase 2. | ✅ |
| 8 | **Equipo no completo a tiempo** | Media | Alto | Pre-asignar equipo antes de Sprint 0. Contratar/transferir con 2 semanas de anticipación. | ⚠️ |

**Leyenda:**
- ✅ Bien mitigado en documento original
- ⚠️ Requiere atención activa
- 🚨 Riesgo crítico - monitorear semanalmente

### Plan de contingencia para riesgo #1 (Anti-bot)

**Síntomas:**
- HTTP 403/429
- CAPTCHAs frecuentes
- Bloqueos de IP

**Acciones:**
1. Reducir frecuencia de scraping (diario → semanal temporal)
2. Aumentar pool de proxies residenciales
3. Agregar delays aleatorios (3-10 segundos entre requests)
4. Rotar User-Agents realistas
5. Si persiste: evaluar cambiar de competidor en MVP

---

## 13) Costos (drivers y escenarios)

### Drivers de costo

**CAPEX (one-time):**
- Desarrollo del MVP: 3.75 FTE × 3 meses × $10,000 USD promedio
- **Total CAPEX: ~$112,500 USD**

**OPEX (mensual recurrente):**

| Concepto | Conservador | Base | Ambicioso |
|----------|-------------|------|-----------|
| **Cómputo/workers** | $150 | $300 | $500 |
| **Almacenamiento (S3/GCS)** | $50 | $100 | $200 |
| **Proxies/IPs rotatorias** | $300 | $800 | $1,500 |
| **Monitoreo (logs/métricas)** | $50 | $100 | $150 |
| **Orquestación (Prefect Cloud)** | $0 | $0 | $200 |
| **Contingencia (10%)** | $55 | $130 | $255 |
| **TOTAL MENSUAL** | **$605** | **$1,430** | **$2,805** |
| **TOTAL ANUAL** | **$7,260** | **$17,160** | **$33,660** |

### Escenarios de alcance

**Conservador:**
- 2 competidores × 2 categorías
- Frecuencia: solo diaria
- 3,000 SKUs monitoreados

**Base (recomendado):**
- 3-4 competidores × 2-3 categorías
- Frecuencia: diaria (menor a diaria selectiva en 1 competidor)
- 5,000-8,000 SKUs

**Ambicioso:**
- 4 competidores × 3 categorías
- Frecuencia: diaria + sub-diaria en 2 competidores
- 10,000-15,000 SKUs

### 💰 Comparativa financiera

| Concepto | Proveedor Actual | MVP Propio (Año 1) | MVP Propio (Año 2+) |
|----------|------------------|-------------------|-------------------|
| **Costo total** | $36,000-96,000 | $112,500 + $17,160 = **$129,660** | **$17,160** |
| **Control** | ❌ Nulo | ✅ Total | ✅ Total |
| **Cobertura** | ~46% | 70-85% | 70-85%+ |

**Break-even:** Si el proveedor cobra >$5,000/mes → **ROI positivo en 2-4 meses**

**Ahorro anual (desde Año 2):** $36,000-96,000 - $17,160 = **$18,840-78,840 USD/año**

---

## 14) Gobierno, auditoría y seguridad

### Gobierno del proyecto

**Comité quincenal:**
- Sponsor (Luis Acosta)
- PM/PO
- Líder técnico
- Representante usuarios comerciales
- Representante legal (Q&A sobre compliance)

**Agenda estándar:**
- Avance vs plan (semáforo)
- KPIs actuales
- Riesgos top 3
- Decisiones requeridas
- Budget burn rate

### Tablero de salud (actualización diaria)

**Métricas operativas:**
```
┌─────────────────────────────────────────┐
│ SALUD DEL SISTEMA (last 24h)            │
├─────────────────────────────────────────┤
│ Cobertura:          76% ✅               │
│ Frescura (<24h):    92% ✅               │
│ Precisión:          98% ✅               │
│ Uptime:             99.2% ✅             │
│                                          │
│ Fallos por sitio:                        │
│   - Liverpool:      2 (403 errors)      │
│   - Elektra:        0 ✅                 │
│   - Palacio:        1 (timeout)          │
│                                          │
│ Consumo:                                 │
│   - GB/mes:         180 / 300 (60%)     │
│   - Costo proxies:  $620 / $800         │
└─────────────────────────────────────────┘
```

### Auditoría y trazabilidad

**Cada registro incluye:**
- URL original
- Timestamp de extracción
- User-Agent usado
- IP/proxy utilizado
- Hash SHA-256 de la página (evidencia)
- Usuario que ejecutó el proceso

**Mini-capturas:**
- Screenshot de precio/disponibilidad en casos críticos
- Almacenamiento: S3 con lifecycle policy (30-90 días)
- Uso: resolución de disputas, validación de cambios

### Seguridad

**Acceso:**
- SSO corporativo (Azure AD / Okta)
- RBAC (roles: admin, comercial, analista, auditor)
- MFA obligatorio para admins

**Datos:**
- Cifrado en tránsito (TLS 1.3)
- Cifrado en reposo (S3 server-side encryption)
- Sin PII de clientes
- Logs de acceso a datos sensibles

**Compliance:**
- Revisión legal de ToS por dominio (cada 6 meses)
- Respeto de robots.txt
- Rate limiting documentado
- Proceso de opt-out si un competidor lo solicita

---

## 15) Stack tecnológico recomendado

### Comparativa de opciones

| Componente | Opción A | Opción B | Recomendado | Justificación |
|------------|----------|----------|-------------|---------------|
| **Scraping** | Puppeteer | Playwright | **Playwright** | Mejor manejo de SPA, APIs más limpias |
| **Orquestación** | Airflow | Prefect/Dagster | **Prefect** | Más moderno, mejor DX, Python-native |
| **Storage (raw)** | S3 + Parquet | GCS + Parquet | **S3 + Parquet** | Costo, integración |
| **Storage (queries)** | PostgreSQL | DuckDB | **DuckDB** | OLAP sobre Parquet, zero-config |
| **API** | Flask | FastAPI | **FastAPI** | Performance, docs automáticas, async |
| **UI** | Retool | Streamlit | **Streamlit** | Prototipado rápido, Python-only |
| **Proxies** | Smartproxy | Bright Data | **Bright Data** | Mejor uptime, más IPs residenciales |
| **Matching** | Custom | fuzzywuzzy | **rapidfuzz** | Más rápido que fuzzywuzzy |
| **Monitoring** | Datadog | Grafana + Loki | **Grafana + Loki** | Open-source, menor costo |

### Arquitectura de despliegue recomendada

**Opción Cloud (recomendada):**
```
┌──────────────────────────────────────┐
│ AWS / GCP / Azure                     │
├──────────────────────────────────────┤
│ Scrapers: ECS/Cloud Run (containers) │
│ Orquestación: Prefect Cloud (SaaS)  │
│ Storage: S3/GCS (Parquet)            │
│ Queries: DuckDB (serverless)         │
│ API: Cloud Run / Lambda + API GW     │
│ UI: Cloud Run / App Engine           │
│ Monitoring: Grafana Cloud            │
└──────────────────────────────────────┘
```

**Ventajas:**
- Escalabilidad automática
- Menor OpEx (sin servidores 24/7)
- Managed services

---

## 16) Checklist para arrancar

### Pre-Sprint 0 (antes de Semana 0)

**Negocio:**
- [ ] Aprobar presupuesto ($112K CAPEX + $17K/año OPEX)
- [ ] Asignar equipo (3.75 FTE comprometidos)
- [ ] Definir lista de competidores (3-4)
- [ ] Definir lista de categorías (2-3)
- [ ] Identificar usuarios clave para validación (5 nombres)

**Técnico:**
- [ ] Acceso a cloud provider (AWS/GCP/Azure)
- [ ] Cuenta de proxies (Bright Data trial)
- [ ] Repo git configurado
- [ ] Slack/Teams channel para equipo

### Sprint 0 (Semanas 0-2)

**Datos:**
- [ ] Golden set de 500-1,000 SKUs con EAN/UPC/MPN
- [ ] Palabras de búsqueda por categoría
- [ ] Ejemplo de URLs de productos por competidor

**Legal:**
- [ ] Matriz de compliance (ToS y robots.txt por dominio)
- [ ] Aprobación de legal interna para scraping
- [ ] Definir límites de frecuencia responsables

**Usuario:**
- [ ] Mockups de UI validados
- [ ] Casos de uso priorizados
- [ ] Definición de alertas críticas

---

## 17) Decisiones solicitadas al sponsor

### Decisiones críticas (requieren respuesta esta semana)

1. ✅ **Aprobación del alcance del MVP** (secciones 3, 4 y 8-11)
2. 🔴 **Definición de competidores y categorías** (deadline: esta semana)
   - Propuesta: Liverpool, Elektra, Palacio de Hierro
   - Categorías: Línea Blanca, Electrónicos
3. 🟡 **Inicio del Sprint 0** (2 semanas): descubrimiento, legal y base técnica
4. 🟡 **Primer hito visible** (Semana 4): tabla comparativa funcional con 1 sitio

### Decisiones secundarias (pueden esperar 2 semanas)

5. Plan de comunicación a equipos comerciales
6. Proceso de feedback de usuarios durante MVP
7. Criterios de éxito para aprobar Fase 2

---

## 18) Glosario breve

| Término | Definición |
|---------|------------|
| **Extracción (scraping)** | Obtención automatizada de información pública mostrada en páginas web |
| **Snapshot** | Captura de estado (precio/stock) en una fecha/hora específica |
| **SKU canónico** | Identificador interno para comparar "manzanas con manzanas" entre competidores |
| **Matching exacto** | Mismo producto identificado por EAN/UPC/MPN |
| **Matching variante** | Misma referencia con diferencias (talla, color, pack) |
| **Matching fuzzy** | Similitud aproximada basada en texto (>85% similitud) |
| **1P (First Party)** | Producto vendido directamente por el retailer |
| **3P (Third Party)** | Producto vendido por un seller externo en marketplace |
| **Sitio de alta fricción** | Página con defensas técnicas que requieren ritmos más bajos o ventanas acotadas |
| **Golden set** | Conjunto de SKUs prioritarios para QA y validación |
| **MTTR** | Mean Time To Recovery - tiempo promedio de recuperación ante fallas |
| **SLO** | Service Level Objective - objetivo de nivel de servicio |

---

## 19) Anexo A - Variables para estimar ROI

**Completar con equipo de negocio:**

| Variable | Valor | Fuente |
|----------|-------|--------|
| **Ventas de categorías objetivo** | ___% del total | Finanzas |
| **Unidades/SKUs críticos** | ___ SKUs | Comercial |
| **Ticket promedio** | $____ MXN | Finanzas |
| **Elasticidad de precio** | ___% | Comercial/Pricing |
| **% tiempo con gap vs competidor** | ___% | Estimado |
| **Mejora de margen/venta al reaccionar** | ___ bps | Comercial |
| **Frecuencia de reacción (días)** | ___ días | Comercial |

**Ejemplo de cálculo ROI (ilustrativo):**

```
Supuestos:
- Categorías objetivo: 15% de ventas totales ($100M anuales)
- Gap detectable: 40% del tiempo
- Mejora de margen: 50 bps al reaccionar
- Reacción 2x más rápida con plataforma propia

Beneficio anual estimado:
= $100M × 15% × 40% × 0.5% × 2 (factor velocidad)
= $60,000 USD/año

ROI = ($60K - $17K OPEX) / $112K CAPEX
= 38% anual (muy conservador)
```

---

## 20) Anexo B - Análisis del proveedor actual

### 📊 Evaluación detallada

**Fortalezas identificadas:**
- ✅ Extracción rica de atributos (~50 campos)
- ✅ Atributos específicos por categoría
- ✅ Información de envío y financiamiento

**Debilidades críticas:**
- ❌ **54% sin competidor identificado** (archivo exact_match)
- ❌ **46% productos Out of Stock** en muestra
- ❌ Matching solo exacto (no variantes)
- ❌ Sin evidencia de trazabilidad histórica robusta
- ❌ Dependencia total (vendor lock-in)

### Recomendación estratégica

**Fase MVP (meses 1-4):**
- Enfocarse en cobertura y matching (superar 46% del proveedor)
- Extraer solo atributos esenciales (precio, stock, seller)
- Validar que podemos hacerlo mejor en lo básico

**Fase 2 (meses 5-8, si MVP exitoso):**
- Añadir atributos técnicos específicos por categoría
- Implementar matching avanzado (ML/visión)
- Igualar/superar extracción rica del proveedor

**Decisión de migración (mes 6-8):**
- Si MVP cumple KPIs → reducir dependencia del proveedor gradualmente
- Mantener proveedor en paralelo 3-6 meses como backup
- Migración completa solo cuando cobertura >80% y precision >97%

---

## 21) Próximos pasos inmediatos

### Esta semana (Semana actual)
1. **Sponsor aprueba documento y presupuesto**
2. **Definir competidores finales** (Liverpool, Elektra, Palacio + 1?)
3. **Definir categorías finales** (Línea Blanca, Electrónicos + 1?)
4. **Pre-asignar equipo** (4 personas con nombres)

### Semana próxima (Semana 0 - inicio)
5. **Kickoff del proyecto** con equipo completo
6. **Construir golden set** (500 SKUs prioritarios)
7. **Revisar ToS y robots.txt** de competidores
8. **Setup técnico inicial** (repo, cloud, proxies trial)

### Semana 4 (primer hito)
9. **Demo funcional** con datos reales de 1 competidor
10. **Validación con usuarios** (5 personas comerciales)

---

## 📞 Contactos del proyecto

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

## ✅ Firma de aprobación

| Rol | Nombre | Aprobación | Fecha |
|-----|--------|------------|-------|
| **Sponsor** | Luis Acosta | ☐ Apruebo | __/__/__ |
| **Tech Lead** | Lozas | ☐ Apruebo | __/__/__ |
| **PM** | Ruíz | ☐ Apruebo | __/__/__ |
| **Legal** | [Nombre] | ☐ Apruebo | __/__/__ |

---

**Versión:** 0.2  
**Última actualización:** 15/oct/2025  
**Próxima revisión:** Semana 4 (hito de demo funcional)

---

# 🚀 RECOMENDACIÓN FINAL: GO

Este MVP es técnicamente viable, financieramente justificable, y estratégicamente necesario dado el desempeño deficiente del proveedor actual (54% sin matching). 

**Confianza en éxito:** Alta (80%)  
**Riesgo principal:** Scope creep y anti-bot en sitios complejos  
**Mitigación clave:** Disciplina en MVP, empezar con retailers simples  

**¡Es momento de construir!** 🛠️