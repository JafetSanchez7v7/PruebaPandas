import pandas as pd
import random

random.seed(42)

n = 100
nombres_pool = ['Roberto Silva', 'Carmen Morales', 'José Torres', 'Patricia Vargas', 'Manuel Castro',
                'Laura Ortiz', 'Francisco Mendoza', 'Isabel Reyes', 'Antonio Morales', 'Teresa Aguilar',
                'Ricardo Ruiz', 'Beatriz Hernández', 'Sergio Díaz', 'Claudia Sánchez', 'Alberto Ramírez']

niveles_actividad = ['Sedentario', 'Ligero', 'Moderado', 'Activo', 'Muy Activo']

df = pd.DataFrame({
    'id_paciente': range(1, n+1),
    'nombre': [random.choice(nombres_pool) for _ in range(n)],
    'edad': [random.randint(18, 85) for _ in range(n)],
    'genero': [random.choice(['Masculino', 'Femenino']) for _ in range(n)],
    'peso': [round(random.uniform(45.0, 120.0), 1) for _ in range(n)],
    'altura': [round(random.uniform(1.45, 2.05), 2) for _ in range(n)],
    'presion_sistolica': [random.randint(90, 180) for _ in range(n)],
    'presion_diastolica': [random.randint(60, 120) for _ in range(n)],
    'colesterol': [random.randint(120, 300) for _ in range(n)],
    'fumador': [random.choice([True, False]) for _ in range(n)],
    'nivel_actividad': [random.choice(niveles_actividad) for _ in range(n)],
    'consultas_anio': [random.randint(0, 20) for _ in range(n)]
})
