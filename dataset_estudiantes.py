import pandas as pd
import random

random.seed(42)

n = 100
nombres_pool = ['Ana', 'Luis', 'María', 'Carlos', 'Sofía', 'Pedro', 'Lucía', 'Jorge',
                'Elena', 'Miguel', 'Andrea', 'Diego', 'Valentina', 'Fernando', 'Camila',
                'Javier', 'Gabriela', 'Alejandro', 'Paula', 'Daniel']
carreras = ['Informática', 'Matemáticas', 'Física', 'Biología', 'Literatura']

df = pd.DataFrame({
    'id': range(1, n+1),
    'nombre': [random.choice(nombres_pool) for _ in range(n)],
    'edad': [random.randint(18, 25) for _ in range(n)],
    'carrera': [random.choice(carreras) for _ in range(n)],
    'semestre': [random.randint(1, 10) for _ in range(n)],
    'promedio': [round(random.uniform(5.0, 10.0), 2) for _ in range(n)],
    'asistencia': [round(random.uniform(0.5, 1.0), 2) for _ in range(n)],
    'creditos_aprobados': [random.randint(10, 180) for _ in range(n)],
    'materias_reprobadas': [random.randint(0, 3) for _ in range(n)],
    'tiene_beca': [random.choice([True, False]) for _ in range(n)],
    'horas_estudio_semana': [random.randint(0, 20) for _ in range(n)],
    'participacion_clase': [random.randint(1, 5) for _ in range(n)]
})

print(df)