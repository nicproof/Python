# 📘 Ejercicios propuestos de Pandas (sin resolver)

import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

COLOR = '\033[33m'
DEFECTO = '\033[0m'


# 1. Crear un DataFrame
# 👉 Crea un DataFrame con 5 productos que tenga las columnas: Producto, Precio, Stock, Categoría.

datos = {
    'Producto': ['Laptop Pro', 'Smartphone X', 'Auriculares BT', 'Monitor Curvo', 'Teclado Mecánico'],
    'Precio': [1200.50, 799.99, 45.00, 350.75, 85.90],
    'Stock': [15, 30, 150, 8, 45],
    'Categoría': ['Electrónica', 'Electrónica', 'Accesorios', 'Electrónica', 'Accesorios']
}

df = pd.DataFrame(datos)
print(f"{COLOR}\n\n1.- Listado de productos:{DEFECTO}")
print("----------------------------------------------------------------")
print(df)
print("----------------------------------------------------------------\n")


# 2. Explorar el DataFrame
# 👉 Muestra las primeras 3 filas, info() y describe().

print(f"{COLOR}2.- Primeras 3 filas, info() y describe():{DEFECTO}")
print("----------------------------------------------------------------")
print("Primeras 3 filas:\n")
print(df.head(3))
print("\nInformación del DataFrame:\n")
print(df.info())
print("\nEstadísticas descriptivas:\n")
print(df.describe())
print("----------------------------------------------------------------\n")


# 3. Selección de columnas
# 👉 Obtén únicamente las columnas Producto y Precio.

print(f"{COLOR}3.- Columnas Producto y Precio:{DEFECTO}")
print("----------------------------------------------------------------")
print(df[['Producto', 'Precio']])
print("----------------------------------------------------------------\n") 


# 4. Filtrado de filas
# 👉 Filtra los productos con precio > 100 y los de categoría "Electrónica".

print(f"{COLOR}4.- Productos con precio > 100:{DEFECTO}")
print("----------------------------------------------------------------")
print(df[df['Precio'] > 100])
print("----------------------------------------------------------------\n")


# 5. Operaciones con columnas
# 👉 Crea la columna Valor_Total = Precio * Stock.

df['Valor_Total'] = df['Precio'] * df['Stock']
print(f"{COLOR}5.- DataFrame con columna Valor_Total:{DEFECTO}")
print("----------------------------------------------------------------")
print(df)
print("----------------------------------------------------------------\n")


# 6. Ordenar datos
# 👉 Ordena por Precio (ascendente) y por Stock (descendente).

print(f"{COLOR}6.- DataFrame ordenado por Precio (ascendente):{DEFECTO}")
print("----------------------------------------------------------------")
print(df.sort_values(by='Precio'))
print("----------------------------------------------------------------\n")

print(f"{COLOR}DataFrame ordenado por Stock (descendente):{DEFECTO}")
print("----------------------------------------------------------------")
print(df.sort_values(by='Stock', ascending=False))
print("----------------------------------------------------------------\n")


# 7. Agrupaciones
# 👉 Calcula precio medio y stock total por categoría.

print(f"{COLOR}7.- Precio medio y stock total por categoría:{DEFECTO}")
print("----------------------------------------------------------------")
# precio_medio = df.groupby('Categoría')['Precio'].mean()
# stock_total = df.groupby('Categoría')['Stock'].sum()
print(df.groupby('Categoría').agg({'Precio': 'mean', 'Stock': 'sum'}))
print("----------------------------------------------------------------\n")



# 8. Valores nulos y limpieza
# 👉 Introduce un valor nulo en Precio y rellénalo con la media.

df.loc[1, 'Precio'] = None
print(f"{COLOR}8.- DataFrame con valor nulo en Precio:{DEFECTO}")
print("----------------------------------------------------------------")
print(df)
print("\nNúmero de valores nulos por columna:")
print(df.isnull().sum())
df['Precio'] = df['Precio'].fillna(df['Precio'].mean())
#df['Precio'].fillna(df['Precio'].mean(), inplace=True)
print("\nDataFrame tras rellenar nulos en Precio con la media:")
print(df)
print("----------------------------------------------------------------\n") 


# 9. Exportar a CSV
# 👉 Guarda tu DataFrame final como productos.csv.

df.to_csv('productos.csv', index=False)
print(f"{COLOR}9.- DataFrame exportado a productos.csv:{DEFECTO}")
print("----------------------------------------------------------------\n")
print(df)
print("----------------------------------------------------------------\n")

# Buscar en df el producto "Monitor Curvo" y mostrar su precio y stock.
print(f"{COLOR}EXTRA 1.- Precio y stock del 'Monitor Curvo':{DEFECTO}")
print("----------------------------------------------------------------")
monitor = df[df['Producto'] == 'Monitor Curvo']
precio_monitor = monitor['Precio'].values[0]
stock_monitor = monitor['Stock'].values[0]
print(f"El precio del 'Monitor Curvo' es: {precio_monitor}")
print(f"El stock del 'Monitor Curvo' es: {stock_monitor}")
precio_monitor = 666.66
stock_monitor = 66
df.loc[df['Producto'] == 'Monitor Curvo', 'Precio'] = precio_monitor
df.loc[df['Producto'] == 'Monitor Curvo', 'Stock'] = stock_monitor
print("\nDataFrame tras actualizar el precio del 'Monitor Curvo':")
print(f"{df}")
print("----------------------------------------------------------------\n")

# Buscar en df el producto "Monitor Curvo" y mostrar su precio y stock.
print(f"{COLOR}EXTRA 2.- Precio y stock del 'Monitor Curvo':{DEFECTO}")
print("----------------------------------------------------------------")
monitor = df[df['Producto'] == 'Monitor Curvo']
precio_monitor = monitor['Precio'].values[0]
stock_monitor = monitor['Stock'].values[0]

# --- MODIFICACIÓN CLAVE AQUÍ ---
print(f"El precio del 'Monitor Curvo' es: {precio_monitor}")
print(f"El stock del 'Monitor Curvo' es: {COLOR}{stock_monitor}{DEFECTO}")
# --------------------------------

precio_monitor = 666.66
stock_monitor = 66
df.loc[df['Producto'] == 'Monitor Curvo', 'Precio'] = precio_monitor
df.loc[df['Producto'] == 'Monitor Curvo', 'Stock'] = stock_monitor

print("\nDataFrame tras actualizar el precio del 'Monitor Curvo':")

# --- MODIFICACIÓN CLAVE PARA COLOREAR EN EL PRINT FINAL ---

# 1. Obtenemos la fila del Monitor Curvo
fila_monitor = df[df['Producto'] == 'Monitor Curvo']

# 2. Obtenemos el resto del DataFrame
df_resto = df[df['Producto'] != 'Monitor Curvo']

# 3. Imprimimos el resto
print(df_resto.to_string())

# 4. Imprimimos la fila del Monitor Curvo con el código de color
# Usamos to_string() para obtener la representación de texto de la fila y le añadimos el color.
# Colocamos el código de color al inicio y el reset al final de la línea.
print(f"{COLOR}{fila_monitor.to_string(header=False)}{DEFECTO}") 
# Usamos header=False para evitar que se repitan los nombres de las columnas.

print("----------------------------------------------------------------\n")