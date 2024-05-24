"""

pandas:

. Libreria python para realizar análisis de datos
. Permite manejar los datos como si estuvieramos manejando una hoja de excel

Dataframe: 

. Datos en forma tabular
. Cada dataframe esta formado por filas y columnas

Datasets: https://datos.gob.ar/dataset
Datasets: https://www.yvera.tur.ar/sinta/
"""

import pandas as pd
from matplotlib import pyplot as plt

"""
Si entre los datos ya hay un id, especificarlo
pd.read_csv("datasets/visitas.csv", index_col="id")

Sino pandas agrega en forma automática una col id
numérico secuencial iniciando en 0
"""

df = pd.read_csv("datasets/visitas.csv")

print(df)
print(df.head(10))    # Muestra las primeras 10 filas
print(df.tail(10))    # Muestra las últimas 10 filas
print(df.describe())  # Muestra estadísticas de las columnas numéricas

# Limpieza de datos vacios o incompletos
df_limpiado = df.dropna()                                   # Borrado filas NaN
df_limpiado = df.fillna("")                                 # Relleno NaN con ""
df_limpiado = df.fillna({"visitas":0, "observaciones":""})  # Relleno NaN segun columna

# Filtrado de datos
df_filtrado = df['visitas']
df_filtrado = df[['origen_visitantes', 'visitas']]

df_filtrado = df.iloc[0]      # Filtro por índice de fila 0
df_filtrado = df.iloc[0:5]    # Filtro por índice de fila 0 hasta 4
df_filtrado = df.iloc[[0, 2]] # Filtro por índice de fila 0 y 2
df_filtrado = df.loc[[0, 2], ['region_de_destino', 'visitas']]  # Filtro por id y columnas
df_filtrado = df[df['visitas'] > 100000]                        # Filtro por condición
df_filtrado = df[(df['origen_visitantes'] == 'residentes') & (df['visitas'] > 100000)]
df_filtrado = df[df['region_de_destino'].str.contains('cordoba')]

# Transformación de datos

print(df_filtrado)


#plt.plot(df.letters, df.frecuency)
#plt.show()
