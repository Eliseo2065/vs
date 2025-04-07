# %%
# Creamos objeto cliente
class Clientes:
    def __init__(self, nombre, rut, direccion, kpan, kprecio):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion
        self.kpan = kilos
        self.kprecio = precio


# %%
# Solicitar datos al usuario y almacenarlos en variables
nombre = input("Por favor, ingresa tu nombre: ")  # Solicitar el nombre del usuario
rut = input("Por favor, ingresa tu rut: ")  # Solicitar el rut del usuario
direccion = input("Por favor, ingresa tu dirección: ")  # Solicitar la dirección del usuario
kilos = float(input("Por favor, ingresa cuántos kilos compraste: "))  # Convertir a float para cálculos

# Mostrar los datos ingresados para confirmación
print(f"RUT ingresado: {rut}")
print(f"Nombre ingresado: {nombre}")
print(f"Dirección ingresada: {direccion}")

# Calcular el precio total multiplicando por el precio por kilo
precio_por_kilo = 1000
precio_total = kilos * precio_por_kilo

# Mostrar el valor de la compra
print(f"El valor de tu compra es: {precio_total} pesos")

# %%
# GENERAMOS UN DATAFRAME DE CLIENTES DE NUESTRA PANADERIA

# %%
import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Configuración
PRECIO_KILO_PAN = 1000  # Precio por kilo de pan en pesos chilenos
TOTAL_REGISTROS = 1000000  # Número de registros a generar

# Listas de datos para generación aleatoria
nombres = ['Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Carmen', 'Diego', 'Isabel', 'Carlos', 'Laura',
            'José', 'Andrea', 'Miguel', 'Patricia', 'Fernando', 'Daniela', 'Roberto', 'Francisca', 'Sergio', 'Valentina']
apellidos = ['González', 'Muñoz', 'Rojas', 'Díaz', 'Pérez', 'Soto', 'Contreras', 'Silva', 'Martínez', 'Sepúlveda',
             'Morales', 'Rodríguez', 'López', 'Fuentes', 'Hernández', 'Torres', 'Araya', 'Flores', 'Espinoza', 'Castillo']

comunas_chile = ['Santiago', 'Providencia', 'Las Condes', 'Ñuñoa', 'La Reina', 'Macul', 'Peñalolén', 'La Florida',
                 'Puente Alto', 'Maipú', 'San Bernardo', 'La Cisterna', 'El Bosque', 'Recoleta', 'Independencia',
                 'Quilicura', 'Huechuraba', 'Vitacura', 'Lo Barnechea', 'San Miguel']

# Función para generar RUT chileno válido
def generar_rut():
    num = random.randint(1, 25000000)
    digito = generar_digito_verificador(num)
    return f"{num}-{digito}"

def generar_digito_verificador(numero):
    reversed_digits = map(int, reversed(str(numero)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    mod = (-s) % 11
    return 'K' if mod == 10 else str(mod)

def cycle(iterable):
    while True:
        for x in iterable:
            yield x

# Función para generar dirección aleatoria
def generar_direccion():
    calle = random.choice(['Calle', 'Avenida', 'Pasaje'])
    nombre_calle = random.choice(['Los Aromos', 'Las Acacias', 'Los Plátanos', 'Los Olivos', 'Los Laureles',
                                 'Alameda', 'Principal', '5 de Abril', '21 de Mayo', 'Arturo Prat'])
    numero = random.randint(1, 9999)
    comuna = random.choice(comunas_chile)
    return f"{calle} {nombre_calle} {numero}, {comuna}"

# Generar los datos
data = {
    'nombre': [],
    'rut': [],
    'direccion': [],
    'kilos_comprados': [],
    'valor_total': [],
    'fecha_compra': [],
    'valor_venta_diaria': []  # Nueva columna
}

for _ in range(TOTAL_REGISTROS):
    # Nombre completo
    nombre = f"{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}"
    data['nombre'].append(nombre)
    
    # RUT
    data['rut'].append(generar_rut())
    
    # Dirección
    data['direccion'].append(generar_direccion())
    
    # Kilos comprados (distribución normal con media en 2kg)
    kilos = min(20, max(0.1, random.gauss(2, 1.5)))
    data['kilos_comprados'].append(round(kilos, 1))
    
    # Valor total
    valor_total = int(kilos * PRECIO_KILO_PAN)
    data['valor_total'].append(valor_total)
    
    # Fecha (últimos 3 años)
    dias_atras = random.randint(1, 365*3)
    fecha = datetime.now() - timedelta(days=dias_atras)
    data['fecha_compra'].append(fecha.strftime('%Y-%m-%d %H:%M:%S'))
    
    # Valor venta diaria (simulación de ventas diarias)
    valor_venta_diaria = valor_total * random.uniform(0.8, 1.2)  # Variación del 80% al 120%
    data['valor_venta_diaria'].append(round(valor_venta_diaria, 2))

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar información del DataFrame
print("Información del DataFrame:")
print(df.info())

# Mostrar primeras filas
print("\nPrimeras 5 filas:")
display(df.head())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
display(df.describe())

# %%
# CREAMOS FUNCION PARA VISUALIZAR VENTAS POR FECHA
def visualizar_ventas_por_fecha(df):
    # Solicitar al usuario una fecha
    fecha_usuario = input("Ingrese una fecha en formato 'YYYY-MM-DD' (por ejemplo, 2025-03-31): ")
    
    # Filtrar las ventas para la fecha ingresada
    ventas_fecha = df[df['fecha_compra'].str.startswith(fecha_usuario)]
    
    # Verificar si hay v
    # entas para la fecha ingresada
    if ventas_fecha.empty:
        print(f"No se encontraron ventas para la fecha {fecha_usuario}.")
    else:
        # Calcular el valor total de ventas para la fecha
        valor_total_ventas = ventas_fecha['valor_total'].sum()
        
        # Mostrar las ventas y el valor total
        print(f"\nVentas para la fecha {fecha_usuario}:")
        display(ventas_fecha)
        print(f"\nValor total de ventas para la fecha {fecha_usuario}: {valor_total_ventas} pesos")

# Llamar a la función para visualizar las ventas por fecha
visualizar_ventas_por_fecha(df)

# %%


# CREAMOS UN FILTRO PARA VER LAS VENTAS DEL MES DE MARZO 2025 Y DIFERENCIAR POR COLROES
import pandas as pd
df['fecha_compra'] = pd.to_datetime(df['fecha_compra'])  # Asegurarse de que la columna sea de tipo datetime
marzo_2025 = df[(df['fecha_compra'].dt.year == 2025) & (df['fecha_compra'].dt.month == 3)]

# Agrupar por día y calcular el valor total de ventas
ventas_por_dia = marzo_2025.groupby(marzo_2025['fecha_compra'].dt.day)['valor_total'].sum()

# Crear un gráfico de barras para visualizar los días con más ventas
dias = ventas_por_dia.index
valores_ventas = ventas_por_dia.values

# Asignar colores según el valor total de ventas
colores = []
for v in valores_ventas:
    if v < 1800000:  # Ventas bajas
        colores.append('yellow')
    elif 1800000 < v < 1950000:  # Ventas medias
        colores.append('green')
    else:  # Ventas altas
        colores.append('red')

# Crear el gráfico
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))
bars = plt.bar(dias, valores_ventas, color=colores, edgecolor='black')

# Personalizar el gráfico
plt.title('Días con Más Ventas de Pan - Marzo 2025', fontsize=16)
plt.xlabel('Día del Mes', fontsize=14)
plt.ylabel('Valor Total de Ventas (pesos)', fontsize=14)
plt.xticks(dias)  # Mostrar todos los días en el eje X
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Añadir etiquetas a las barras
for bar, valor in zip(bars, valores_ventas):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10000, f'{int(valor)}', ha='center', fontsize=10)

# Mostrar el gráfico
plt.show()


