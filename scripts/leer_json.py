import json
import pandas as pd

with open("data/ventas.json", encoding = "utf-8") as f:
  datos = json.load(f)

ventas = pd.json_normalize(datos)
print(ventas.head())
#imprimir las dimensiones
print("Dimensiones:", ventas.shape)
#imprimir loa tipos de columna
print("\nTipos por columna")
print(ventas.dtypes)
