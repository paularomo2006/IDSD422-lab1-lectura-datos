# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total



# TODO 1: Cargar data/ventas.csv
ventas <- read.csv("data/ventas.csv")

# TODO 2: Imprimir los tipos de cada columna
str(ventas)

# TODO 3: Crear la columna derivada ticket = ventas / clientes
ventas$ticket <- ventas$ventas / ventas$clientes

print(head(ventas))

# TODO 4: Calcular e imprimir los indicadores

# Venta promedio por sucursal
print("Venta promedio por sucursal")
venta_promedio <- aggregate(ventas ~ sucursal, data = ventas, FUN = mean)
print(venta_promedio)

# Ticket promedio general (ventas totales / clientes totales)
print("Ticket promedio general")
ticket_promedio <- sum(ventas$ventas) / sum(ventas$clientes)
print(ticket_promedio)

# Sucursal con mayor venta total
ventas_sucursal <- aggregate(ventas ~ sucursal, data = ventas, FUN = sum)

sucursal_mayor <- ventas_sucursal$sucursal[
  which.max(ventas_sucursal$ventas)
]

print("Sucursal con mayor venta:")
print(sucursal_mayor)

# Sucursal con menor venta total
sucursal_menor <- ventas_sucursal$sucursal[
  which.min(ventas_sucursal$ventas)
]

print("Sucursal con menor venta:")
print(sucursal_menor)

# Región con mayor venta total
ventas_region <- aggregate(ventas ~ region, data = ventas, FUN = sum)

region_mayor <- ventas_region$region[
  which.max(ventas_region$ventas)
]