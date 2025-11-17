# Variables para Cálculo de ROI - Plataforma de Scraping

Este documento lista todas las variables que deben completarse para calcular el ROI real del proyecto.

## 📋 Resumen de Variables

**Total de variables:** 25+
**Responsables:** IT/Finanzas (10), Comercial/Pricing (10), Otros (5)
**Deadline sugerido:** Semanas 1-2 antes de presentación final

---

## 💰 Variables de Costos (IT/Finanzas)

### CAPEX (Inversión Única)

| Variable | Descripción | Responsable | Ejemplo |
|----------|-------------|-------------|---------|
| `[N_FTE]` | Número de FTEs requeridos | IT/PMO | 3.75 |
| `[N_MESES]` | Duración del proyecto | Definido | 3-4 |
| `[COSTO_FTE]` | Costo promedio por FTE/mes | Finanzas | $10,000 |
| `[CAPEX_SETUP]` | Setup inicial (infraestructura, licencias) | IT | $5,000 |
| `[CAPEX_DESARROLLO]` | N_FTE × N_MESES × COSTO_FTE | Calculado | $112,500 |
| `[CAPEX_TOTAL]` | CAPEX_DESARROLLO + CAPEX_SETUP | Calculado | $117,500 |

### OPEX (Operación Mensual)

| Variable | Descripción | Responsable | Ejemplo |
|----------|-------------|-------------|---------|
| `[OPEX_COMPUTO]` | Cómputo / Workers cloud | IT/Cloud | $300 |
| `[OPEX_STORAGE]` | Almacenamiento (S3/GCS, Parquet) | IT/Cloud | $100 |
| `[OPEX_PROXIES]` | Proxies / IPs rotatorias | IT | $800 |
| `[OPEX_MONITOR]` | Monitoreo (logs/métricas) | IT | $100 |
| `[OPEX_ORQUESTACION]` | Orquestación (Prefect/alternativa) | IT | $0-200 |
| `[OPEX_CONTINGENCIA]` | Contingencia 10% de suma | Calculado | $130 |
| `[OPEX_MENSUAL]` | Suma de todos los OPEX | Calculado | $1,430 |
| `[OPEX_ANUAL]` | OPEX_MENSUAL × 12 | Calculado | $17,160 |

### Proveedor Actual

| Variable | Descripción | Responsable | Fuente |
|----------|-------------|-------------|--------|
| `[COSTO_PROVEEDOR_MENSUAL]` | Costo mensual del proveedor actual | Finanzas | Contrato |
| `[COSTO_PROVEEDOR_ANUAL]` | Costo anual del proveedor actual | Finanzas | Contrato |

---

## 📈 Variables de Beneficios (Comercial/Pricing)

### Beneficio 1: Reacciones Más Rápidas

| Variable | Descripción | Responsable | Ejemplo |
|----------|-------------|-------------|---------|
| `[VENTAS_CATEGORIAS]` | Ventas anuales de categorías objetivo | Finanzas | $120M |
| `[PCT_GAPS]` | % de tiempo con gap de precio vs competidor | Pricing | 40% |
| `[MEJORA_MARGEN_BPS]` | Mejora de margen en bps al reaccionar | Comercial | 50 bps |
| `[FACTOR_VELOCIDAD]` | Factor de mejora en velocidad de reacción | Estimado | 2x |
| `[BENEFICIO_REACCION]` | Beneficio calculado (ver fórmula abajo) | Calculado | TBD |

**Fórmula:**
```
[BENEFICIO_REACCION] = [VENTAS_CATEGORIAS] × [PCT_GAPS] × ([MEJORA_MARGEN_BPS]/10000) × [FACTOR_VELOCIDAD]
```

### Beneficio 2: Negociación con Marcas

| Variable | Descripción | Responsable | Ejemplo |
|----------|-------------|-------------|---------|
| `[COMPRAS_MARCAS_CLAVE]` | Compras anuales a marcas clave | Finanzas | $50M |
| `[PCT_MEJORA_TERMINOS]` | % de mejora en términos de negociación | Comercial | 0.5% |
| `[BENEFICIO_NEGOCIACION]` | Beneficio calculado (ver fórmula abajo) | Calculado | TBD |

**Fórmula:**
```
[BENEFICIO_NEGOCIACION] = [COMPRAS_MARCAS_CLAVE] × ([PCT_MEJORA_TERMINOS]/100)
```

### Beneficio 3: Costo de Inacción

| Variable | Descripción | Responsable | Ejemplo |
|----------|-------------|-------------|---------|
| `[PERDIDA_MARGEN_RETRASOS]` | Pérdida anual por retrasos en detectar cambios | Comercial | TBD |
| `[COSTO_NEGOCIACION_DEBIL]` | Costo anual de negociaciones débiles | Comercial | TBD |
| `[COSTO_INFO_INCOMPLETA]` | Costo de decisiones con información incompleta | Estimado | TBD |
| `[OTROS_BENEFICIOS]` | Suma de beneficios adicionales | Calculado | TBD |

### Totales

| Variable | Descripción | Fórmula |
|----------|-------------|---------|
| `[SUMA_BENEFICIOS]` | Total de beneficios anuales | BENEFICIO_REACCION + BENEFICIO_NEGOCIACION + OTROS_BENEFICIOS |
| `[SUMA_TOTAL]` | Costo total de inacción | COSTO_PROVEEDOR_ANUAL + PERDIDA_MARGEN + COSTO_NEGOCIACION + COSTO_INFO |

---

## 📊 Variables para Casos de Éxito

Estas variables se usan para personalizar los casos de éxito en el documento:

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `[X%]` | Porcentaje de bajada de precio del competidor | 15% |
| `[Y horas]` | Tiempo de reacción | 2 horas |
| `[AHORRO_MARGEN]` | Ahorro en margen por reacción rápida | $50K/mes |
| `[N_SKUs]` | Número de SKUs con oportunidad | 200 |
| `[BENEFICIO_OOS]` | Beneficio por oportunidad de stock out | $30K/trimestre |
| `[N]` | Número de competidores con MAP violation | 3 |

---

## 🧮 Fórmulas de Cálculo de ROI

### ROI Porcentual
```
ROI (%) = ([SUMA_BENEFICIOS] - [OPEX_ANUAL]) / [CAPEX_TOTAL] × 100
```

### Break-even (meses)
```
Break-even = [CAPEX_TOTAL] / (([SUMA_BENEFICIOS] - [OPEX_ANUAL]) / 12)
```

### Beneficio Neto Anual (desde Año 2)
```
Beneficio Neto = [SUMA_BENEFICIOS] - [OPEX_ANUAL]
```

### Ahorro vs Proveedor Actual
```
Ahorro Anual = [COSTO_PROVEEDOR_ANUAL] - [OPEX_ANUAL]
```

---

## 📅 Plan de Completado

### Semana 1: Variables de Costos

**Responsable:** IT/Finanzas
**Reunión:** 1 hora

Completar:
- [ ] Todos los CAPEX
- [ ] Todos los OPEX
- [ ] Costos del proveedor actual

### Semana 2: Variables de Beneficios

**Responsable:** Comercial/Pricing
**Reunión:** 2 horas (puede requerir análisis previo)

Completar:
- [ ] Ventas de categorías objetivo
- [ ] Estimación de gaps de precio
- [ ] Mejora de margen por reacción
- [ ] Compras a marcas clave
- [ ] Mejora en términos de negociación

### Semana 2: Validación Conjunta

**Responsable:** Equipo completo
**Reunión:** 1 hora

Actividades:
- [ ] Validar fórmulas de cálculo
- [ ] Revisar supuestos
- [ ] Calcular ROI final
- [ ] Aprobar cifras para presentación

---

## 💡 Ejemplo Ilustrativo (No Vinculante)

**Supuestos ejemplo:**
- Categorías objetivo: 15% de ventas totales ($10M/mes = $120M/año)
- Gap detectable: 40% del tiempo
- Mejora de margen: 50 bps al reaccionar
- Reacción 2x más rápida con plataforma propia

**Cálculo de beneficio por reacciones:**
```
= $120M × 40% × (50/10000) × 2
= $120M × 0.40 × 0.005 × 2
= $240,000 + $120,000
= $360,000/año
```

**Nota:** Este es solo un ejemplo para ilustrar el método. Los valores reales deben calcularse con datos específicos de la empresa.

---

## 📋 Checklist de Documentación

Antes de presentar al sponsor:

- [ ] Todas las variables de costos completadas
- [ ] Todas las variables de beneficios estimadas
- [ ] Fórmulas aplicadas correctamente
- [ ] ROI calculado y validado
- [ ] Break-even determinado
- [ ] Supuestos documentados y justificados
- [ ] Casos de éxito personalizados con cifras reales (si disponibles)
- [ ] Análisis de sensibilidad preparado (escenario conservador/base/optimista)

---

## 🎯 Resultado Esperado

Al completar todas las variables, el documento final incluirá:

1. **Inversión total clara** (CAPEX + OPEX)
2. **Beneficios cuantificados** con metodología transparente
3. **ROI específico** para el contexto de la empresa
4. **Break-even calculado** en meses
5. **Comparativa vs proveedor actual** con cifras reales
6. **Análisis de costo de inacción** cuantificado

Esto permitirá al sponsor tomar una decisión informada basada en datos reales del negocio, no en estimaciones genéricas.

---

**Ubicación en el documento:** Ver **Anexo B** del PDF para tablas completas y fórmulas detalladas.
