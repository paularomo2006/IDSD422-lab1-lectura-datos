# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se analizaron los reportes de ventas recibidos en los formatos CSV, JSON y XSLX. Se identificó que los archivos contienen cinco registros y cuatro variables, con una estructura adecuada para su análisis. Los indicadores muestran que Guayaquil Centro registra la mayor venta y la región Sierra acumula el mayor total. Se recomienda mantener un control de calidad de los datos y utilizar estos resultados para apoyar las decisiones comerciales.

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales |5 |4 |pd.read_csv() / read.csv() |
| JSON | API de fidelización |5 |4 |pd.read_json() / fromJSON() |
| Excel | Consolidado de finanzas |5 |4 |pd.read_excel() / read_excel() |

*Responde: ¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*

No. Aunque CSV utiliza texto separado por comas, JSON almacena información mediante objetos y Excel utiliza un formato de hoja de cálculo, los tres pueden representar los mismos datos, mostar la misma información. La diferencia está en cómo se almacena y se lee la información, no en los datos que contiene.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` |int64 |integer / numeric |Valores numéricos de las ventas |
| `clientes` |int64 |integer / numeric |Cantidad de clientes registrados |
| `sucursal` |object |character |Nombre de cada sucursal |
| `region` |object |character |Región a la que pertenece la sucursal |

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*
Podría indicar errores en el registro, como símbolos, espacios o caracteres no numéricos. Esto impediría realizar operaciones matemáticas y generaría resultados incorrectos, por lo que se debería limpiar y convertir los datos antes del análisis.

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*

CSV: Su lectura fue fácil porque los datos estaban organizados en filas y columnas separadas por comas. Python y R identificaron directamente las variables y sus tipos.

JSON: La información estaba organizada como una lista de objetos. Al utilizar las funciones correspondientes, fue posible representarla como una tabla para analizar los registros.

XSLX: Para leer el archivo se utilizó la hoja ventas, lo que permitió acceder directamente a los datos. Su estructura en forma de tablas o tabular facilitó la inspección de filas, columnas y variables.

En cuanto a las variables categóricas, Python las representa como object y R como character en este ejercicio. Con ambos lenguajes de programción se puede trabahar con estos valores para agrupar información por sucursal o región.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal |Quito Norte: 12.450; Quito Sur: 9.870; Guayaquil Centro: 15.200; Guayaquil Norte: 13.980; Cuenca: 8.540 |
| Ticket promedio (ventas ÷ clientes) |38,07 |
| Sucursal con mayor venta |Guayaquil Centro |
| Sucursal con menor venta |Cuenca |
| Región con mayor venta total |Sierra |

## 5. Conclusiones y recomendación

1.Los tres formatos presentan la misma cantidad de registros y variables. Esto demuestra que es posible integrar información de diferentes sistemas para realizar un análisis conjunto.
2.Python y R permiten leer, organizar y analizar los reportes, aunque utilizan funciones y tipos de datos diferentes. Es importante revisar la calidad de la información para evitar errores en los cálculos.
3.Guayaquil Centro presentó las mayores ventas y Cuenca las menores, mientras que Sierra fue la región con mayor venta total. Se recomienda revisar continuamente estos indicadores para identificar oportunidades de mejora y apoyar la toma de decisiones.
