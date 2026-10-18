# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"]/ventas["clientes"]
print(ventas.head())

print(ventas["ventas"].max())

venta_promedio = ventas.groupby("sucursal")["ventas"].mean()
print("Venta promedio por sucursal:")
print(venta_promedio)


print("Sucursal con mayor venta:",
      ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
#localizar una tupla en base al identificador, idxmax me retorna el identificador basandose en la cantidad maxima de ventas

print("Sucursal con menor venta:",
      ventas.loc[ventas["ventas"].idxmin(), "sucursal"])

ventas_per_region = ventas.groupby("region").sum("ventas")

region_mayor = ventas_per_region["ventas"].idxmax()
total_mayor = ventas_per_region.loc[region_mayor, "ventas"]

print(f"Región con mayor venta total: {region_mayor} con un total de {total_mayor}")

