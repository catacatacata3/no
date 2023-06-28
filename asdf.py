# NOMBRE_DEL_DUEÑO_CODIGO: JuanPerez789
# TEMATICA_DEL_CODIGO: Análisis de datos con pandas
# IEM_ESCUELA_NORMAL_PASTO: IEM Normal de Pasto
# CURSO: Ciencia de Datos

import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro', 'Luis'],
        'Edad': [25, 30, 28, 35],
        'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla']}

df = pd.DataFrame(data)
print(df)
