import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

n = 100
productos = ['Laptop Dell', 'iPhone 14', 'Samsung TV', 'iPad Pro', 'MacBook Air', 
             'Monitor LG', 'Teclado Logitech', 'Mouse Microsoft', 'Auriculares Sony', 'Impresora HP']
categorias = ['Electrónica', 'Computación', 'Telefonía', 'Accesorios', 'Oficina']
vendedores = ['Carlos Ruiz', 'María López', 'Juan Pérez', 'Ana Martínez', 'Luis García']
regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
clientes_tipo = ['Individual', 'Empresa', 'Gobierno', 'Educación']
metodos_pago = ['Tarjeta', 'Transferencia', 'Efectivo', 'Crédito', 'PayPal']

fecha_inicio = datetime.now() - timedelta(days=365)
fechas = [fecha_inicio + timedelta(days=random.randint(0, 365)) for _ in range(n)]

df = pd.DataFrame({
    'id_venta': range(1, n+1),
    'fecha': [fecha.strftime('%Y-%m-%d') for fecha in fechas],
    'producto': [random.choice(productos) for _ in range(n)],
    'categoria': [random.choice(categorias) for _ in range(n)],
    'cantidad': [random.randint(1, 10) for _ in range(n)],
    'precio_unitario': [random.randint(100, 5000) for _ in range(n)],
    'costo': [random.randint(50, 3000) for _ in range(n)],
    'vendedor': [random.choice(vendedores) for _ in range(n)],
    'region': [random.choice(regiones) for _ in range(n)],
    'cliente_tipo': [random.choice(clientes_tipo) for _ in range(n)],
    'descuento': [round(random.uniform(0.0, 0.3), 2) for _ in range(n)],
    'metodo_pago': [random.choice(metodos_pago) for _ in range(n)]
})

print(df)
