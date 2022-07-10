import pandas as pd

# Importar .csv videojuegos
dfVideojuegos = pd.read_csv("videojuegos.csv")

# Importar .csv consolas
dfConsolas = pd.read_csv("consolas.csv")

# Unir los dos .csv
df = dfVideojuegos.merge(dfConsolas, on='ID_CONSOLA')


df2 = (df[(df['Año Publicación'] >= 2006) &  # Filtrar por año de publicación (Mayor o igual al 2006)
          (df['Rating'] > "")])               # Filtrar por Rating (Si no hay datos, lo excluye)

# Impresión de los primeros filtros
# print(df2)

df3 = (df2[(df2['Puntaje Críticos'] > 0) &  # Filtrar Puntaje Críticos (Quitar valores nulos)
           (df2['Puntaje Usuarios'] > 0)])  # Filtrar Puntaje Usuarios (Quitar valores nulos)

# Impresión de los segundos filtros
# print(df3)

# Crear variable con las columnas que queremos ver
columnas = ['ID_VIDEOJUEGO', 'Nombre Videojuego', 'Año Publicación',
            'Género', 'Siglas Consola', 'Nombre Consola', 'Familia Consolas',
            'Ventas Total', 'Puntaje Críticos', 'Puntaje Usuarios', 'Rating']

# Crear variable con las columnas seleccionadas
df4 = (df3[columnas])

# Imprimir datos con las columnas seleccionadas
print(df4)

# Exportar datos en un archivo .csv
df4.to_csv("Introducción a Hojas de cálculo para el Análisis de Datos.csv")
