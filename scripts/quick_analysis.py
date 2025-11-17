#!/usr/bin/env python3
"""
Script de Análisis Rápido
==========================
Genera un reporte rápido de los datos de web scraping.

Uso:
    python quick_analysis.py
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


def print_header(title):
    """Imprime un encabezado formateado."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def load_data():
    """Carga los archivos CSV."""
    print_header("CARGANDO DATOS")

    df_exact = pd.read_csv(
        '../data/raw/exact_match_data_2025-10-10_Coppel Mx_ELECTRONICS.csv',
        encoding='utf-8'
    )

    df_items = pd.read_csv(
        '../data/raw/analyse_item_list_Coppel Mx (8).csv',
        encoding='utf-8'
    )

    print(f"✓ Exact Match: {df_exact.shape[0]} filas x {df_exact.shape[1]} columnas")
    print(f"✓ Detailed: {df_detailed.shape[0]} filas x {df_detailed.shape[1]} columnas")

    return df_exact, df_detailed


def clean_data(df_exact, df_detailed):
    """Limpia y prepara los datos."""
    print_header("LIMPIANDO DATOS")

    # Limpiar exact match
    df_exact['Price'] = pd.to_numeric(df_exact['Price'], errors='coerce')
    df_exact['Discount'] = pd.to_numeric(df_exact['Discount'], errors='coerce')
    df_exact['Final_Price'] = df_exact['Price'] - df_exact['Discount']
    df_exact['Discount_Percent'] = (
        (df_exact['Discount'] / df_exact['Price']) * 100
    ).round(2)

    # Limpiar detailed
    df_detailed['Price'] = (
        df_detailed['Price']
        .astype(str)
        .str.replace(',', '')
        .str.replace('$', '')
        .str.strip()
    )
    df_detailed['Price'] = pd.to_numeric(df_detailed['Price'], errors='coerce')

    df_detailed['Discount'] = (
        df_detailed['Discount']
        .astype(str)
        .str.replace(',', '')
        .str.replace('$', '')
        .str.strip()
    )
    df_detailed['Discount'] = pd.to_numeric(df_detailed['Discount'], errors='coerce')

    df_detailed['Final_Price'] = df_detailed['Price'] - df_detailed['Discount'].fillna(0)

    print("✓ Datos limpiados correctamente")

    return df_exact, df_detailed


def generate_summary(df_exact, df_detailed):
    """Genera resumen ejecutivo."""
    print_header("RESUMEN EJECUTIVO")

    print("\n📊 MÉTRICAS GENERALES")
    print(f"  • Total productos analizados: {len(df_exact)}")
    print(f"  • Precio promedio: ${df_exact['Final_Price'].mean():,.2f} MXN")
    print(f"  • Precio mediano: ${df_exact['Final_Price'].median():,.2f} MXN")
    print(f"  • Rango de precios: ${df_exact['Final_Price'].min():,.2f} - ${df_exact['Final_Price'].max():,.2f} MXN")

    print("\n💰 ANÁLISIS DE DESCUENTOS")
    productos_con_descuento = df_exact[df_exact['Discount'] > 0]
    print(f"  • Productos con descuento: {len(productos_con_descuento)} ({len(productos_con_descuento)/len(df_exact)*100:.1f}%)")
    print(f"  • Descuento promedio: ${productos_con_descuento['Discount'].mean():,.2f} MXN")
    print(f"  • Descuento promedio (%): {productos_con_descuento['Discount_Percent'].mean():.2f}%")

    print("\n🏆 TOP 5 MARCAS")
    top_brands = df_exact['Brand'].value_counts().head(5)
    for i, (brand, count) in enumerate(top_brands.items(), 1):
        print(f"  {i}. {brand.title()}: {count} productos")

    print("\n⚠️  PRODUCTOS FUERA DE STOCK")
    out_of_stock = df_exact[df_exact['Out'] == True]
    print(f"  • Total: {len(out_of_stock)} productos ({len(out_of_stock)/len(df_exact)*100:.1f}%)")
    print(f"  • Valor de oportunidad perdida: ${out_of_stock['Final_Price'].sum():,.2f} MXN")

    print("\n🎯 PRODUCTOS SIN COMPETENCIA")
    no_competitor = df_exact[df_exact['Status'] == 'No Competitor']
    print(f"  • Total: {len(no_competitor)} productos ({len(no_competitor)/len(df_exact)*100:.1f}%)")
    print(f"  • Valor del inventario: ${no_competitor['Final_Price'].sum():,.2f} MXN")


def generate_brand_analysis(df_exact):
    """Genera análisis por marca."""
    print_header("ANÁLISIS POR MARCA")

    brand_stats = df_exact.groupby('Brand').agg({
        'Price': ['mean', 'count'],
        'Discount': 'mean',
        'Final_Price': 'mean'
    }).round(2)

    brand_stats.columns = ['Precio_Promedio', 'Num_Productos', 'Descuento_Promedio', 'Precio_Final_Promedio']
    brand_stats = brand_stats.sort_values('Num_Productos', ascending=False).head(10)

    print("\nTop 10 Marcas por Número de Productos:\n")
    print(brand_stats.to_string())


def generate_recommendations():
    """Genera recomendaciones estratégicas."""
    print_header("RECOMENDACIONES ESTRATÉGICAS")

    print("""
1. OPTIMIZACIÓN DE PRECIOS
   • Revisar productos con descuentos superiores al 30%
   • Implementar dynamic pricing para productos sin competencia
   • Analizar elasticidad de precio por categoría

2. GESTIÓN DE INVENTARIO
   • Priorizar reabastecimiento de productos con alta demanda
   • Evaluar descontinuación de productos con baja rotación
   • Implementar alertas automáticas de stock

3. INTELIGENCIA COMPETITIVA
   • Monitoreo semanal de precios de competidores
   • Tracking de productos nuevos en el mercado
   • Análisis de gaps en el catálogo

4. ANÁLISIS CONTINUO
   • Actualizar datos de scraping regularmente
   • Desarrollar dashboard de visualización en tiempo real
   • Implementar modelos predictivos de demanda
    """)


def main():
    """Función principal."""
    print("\n" + "=" * 80)
    print("  ANÁLISIS RÁPIDO DE WEB SCRAPING - COPPEL MX")
    print("=" * 80)
    print(f"  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    try:
        # Cargar datos
        df_exact, df_detailed = load_data()

        # Limpiar datos
        df_exact, df_detailed = clean_data(df_exact, df_detailed)

        # Generar análisis
        generate_summary(df_exact, df_detailed)
        generate_brand_analysis(df_exact)
        generate_recommendations()

        print("\n" + "=" * 80)
        print("  ✓ ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("=" * 80)
        print("\nPara un análisis más detallado, ejecuta el notebook:")
        print("  ./start_jupyter.sh")
        print("\n")

    except Exception as e:
        print(f"\n❌ Error durante el análisis: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
