import pandas as pd
import random


def obtenerEmpleados():
    random.seed(42)

    n = 100
    nombres_pool = ['Ana García', 'Luis Martínez', 'María Rodríguez', 'Carlos López', 'Sofía Hernández', 
                'Pedro González', 'Lucía Díaz', 'Jorge Pérez', 'Elena Sánchez', 'Miguel Ramírez',
                'Andrea Torres', 'Diego Vargas', 'Valentina Castro', 'Fernando Ortiz', 'Camila Silva',
                'Javier Mendoza', 'Gabriela Reyes', 'Alejandro Morales', 'Paula Aguilar', 'Daniel Ruiz']

    departamentos = ['Recursos Humanos', 'Ventas', 'Marketing', 'Finanzas', 'TI', 'Operaciones', 'Calidad']
    puestos = ['Analista', 'Supervisor', 'Gerente', 'Coordinador', 'Especialista', 'Director', 'Asistente']

    df = pd.DataFrame({
        'id_empleado': range(1, n+1),
        'nombre': [random.choice(nombres_pool) for _ in range(n)],
        'departamento': [random.choice(departamentos) for _ in range(n)],
        'puesto': [random.choice(puestos) for _ in range(n)],
        'salario': [random.randint(25000, 120000) for _ in range(n)],
        'antigüedad_meses': [random.randint(1, 120) for _ in range(n)],
        'horas_extra': [random.randint(0, 40) for _ in range(n)],
        'evaluacion': [round(random.uniform(1.0, 5.0), 1) for _ in range(n)],
        'ausencias': [random.randint(0, 15) for _ in range(n)],
        'capacitaciones': [random.randint(0, 10) for _ in range(n)],
        'es_remoto': [random.choice([True, False]) for _ in range(n)],
        'satisfaccion': [round(random.uniform(1.0, 5.0), 1) for _ in range(n)]
    })
    return df


