import pandas as pd
import random

random.seed(42)

n = 100
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Sedán', 'SUV', 'Camioneta', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 'Pickup']
tipos_combustible = ['Gasolina', 'Diésel', 'Híbrido', 'Eléctrico', 'Gas']
transmisiones = ['Manual', 'Automática', 'CVT', 'Semi-automática']

df = pd.DataFrame({
    'id_vehiculo': range(1, n+1),
    'marca': [random.choice(marcas) for _ in range(n)],
    'modelo': [random.choice(modelos) for _ in range(n)],
    'año': [random.randint(2015, 2024) for _ in range(n)],
    'kilometraje': [random.randint(0, 150000) for _ in range(n)],
    'precio': [random.randint(150000, 800000) for _ in range(n)],
    'tipo_combustible': [random.choice(tipos_combustible) for _ in range(n)],
    'transmision': [random.choice(transmisiones) for _ in range(n)],
    'num_puertas': [random.choice([2, 3, 4, 5]) for _ in range(n)],
    'potencia': [random.randint(80, 400) for _ in range(n)],
    'consumo_ciudad': [round(random.uniform(8.0, 25.0), 1) for _ in range(n)],
    'consumo_carretera': [round(random.uniform(6.0, 20.0), 1) for _ in range(n)]
})

print(df)
