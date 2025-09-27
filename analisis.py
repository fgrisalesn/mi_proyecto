import pandas as pd
from modulo_limpieza import cargar_datos, manejar_nulos, estandarizar_texto, limpiar_precios

def main():
    # 1. Cargar datos
    productos = cargar_datos("data/productos.csv")
    ventas = cargar_datos("data/ventas.csv")

    # 2. Limpiar datos
    productos = limpiar_precios(productos, "precio")
    productos = manejar_nulos(productos, metodo="rellenar", valor=0)
    ventas = manejar_nulos(ventas, metodo="rellenar", valor=0)

    productos = estandarizar_texto(productos, ["nombre", "categoria"])
    ventas = estandarizar_texto(ventas, ["cliente"])

    # 3. Unir tablas
    df = ventas.merge(productos, on="id_producto", how="left")

    print("\n--- Vista de datos combinados ---")
    print(df)

    # 4. Análisis
    # a) Frecuencia: producto más vendido
    mas_vendido = df["nombre"].value_counts().idxmax()
    print(f"\nProducto más vendido: {mas_vendido}")

    # b) Agregación: total de unidades por categoría
    unidades_categoria = df.groupby("categoria")["cantidad"].sum()
    print("\nUnidades totales por categoría:")
    print(unidades_categoria)

    # c) Filtrado: cuántas ventas tienen cantidad > 2
    ventas_mayor_2 = df[df["cantidad"] > 2].shape[0]
    print(f"\nNúmero de ventas con más de 2 unidades: {ventas_mayor_2}")

if __name__ == "__main__":
    main()
