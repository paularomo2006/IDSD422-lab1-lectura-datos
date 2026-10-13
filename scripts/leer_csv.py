import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
print(ventas.head())
#imprimir las dimensiones
print("Dimensiones:", ventas.shape)
#imprimir loa tipos de columna
print("\nTipos por columna")
print(ventas.dtypes)