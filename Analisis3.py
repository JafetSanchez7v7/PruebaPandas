import pandas as pd
import numpy as np
from dataset_recursos_humanos import obtenerEmpleados

#EJERCICIO 1
df = obtenerEmpleados()
print(df)

# EJER 2
print("Dimensiones e info del dataset")
print(df.shape)
print(df.info())

# EJER 3
print("estadisticas descriptivas")
print(df.describe().round(2))

#EJER 4
print("trabajadores con horario extra mayor a 8 horas")
print(df[df['horas_extra'] > 12])

#5
print("Empleados con sueldo mayor a 100000 y puesto correspondiente")
print(df.loc[df['salario'] > 100000, ['nombre', 'salario', 'puesto']])

#6

print("Primeros 5 empleados")
print(df.iloc[0:5])

#7

print("estadisticas salarial por puesto")
print(df.groupby('puesto').agg({
    'salario' : ['mean', 'min', 'max']
}).round(2))

print("por meses antiguedad")
print(df.groupby('antigüedad_meses').agg({
    'salario' : ['mean', 'min', 'max']
}).round(2))

#8
print("Dataset con nueva columna  promedio por antiguedad")
df['promedio_antiguedad '] = df.groupby('antigüedad_meses')['salario'].mean()
df['promedio_antiguedad '] = df['promedio_antiguedad '].fillna(df['promedio_antiguedad '].mean().round(2))
print(df)

# 9
top_salarios = df.sort_values(by='salario', ascending=False).head(5)

print("Top 5 Empleados mejor pagados:")
print(top_salarios[['nombre', 'salario', 'puesto']])

# 10

print("cantidad de empleados por puesto")
print(df['puesto'].value_counts())

#11
print("promedio antiguedad")
promedio_ant = df.groupby('puesto')['antigüedad_meses'].agg(['mean', 'min', 'max']).round(2)
print(promedio_ant)

#12 promedio ausencias
print("promedio ausencias")
print(df.groupby('puesto')['ausencias'].agg(['mean', 'std', 'count']).round(2))

#13
categorias = ['Bajo', 'Medio', 'Alto']
df['rango_salarial'] = pd.cut(df['salario'], bins=3, labels=categorias)

print("Tabla cruzada: Cantidad de empleados por Puesto y Rango Salarial")
print(pd.crosstab(df['puesto'], df['rango_salarial']))\

#14
def categorizar_empleado(fila):
    if fila['salario'] > 200000 and fila['antigüedad_meses'] > 24:
        return 'Senior'
    elif fila['salario'] > 100000:
        return 'Estandar'
    else:
        return 'Junior'


df['categoria'] = df.apply(categorizar_empleado, axis=1)

print(df)

