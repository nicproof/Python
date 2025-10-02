# 📘 Ejercicio guiado con Pandas

import pandas as pd

# 1. Crear un DataFrame con datos ficticios
datos = {
    "Nombre": ["Ana", "Luis", "María", "Pedro", "Lucía", "Jorge"],
    "Edad": [23, 35, 29, 41, 30, 22],
    "Ciudad": ["Madrid", "Barcelona", "Madrid", "Sevilla", "Bilbao", "Madrid"],
    "Salario": [2200, 2500, 2700, 3000, 2600, 2100]
}

df = pd.DataFrame(datos)
print(df)

# 2. Explorar datos
print(df.head())       # Primeras filas
print(df.info())       # Información general
print(df.describe())   # Estadísticas descriptivas

# 3. Selección de columnas
print(df["Nombre"])                # Una columna
print(df[["Nombre", "Ciudad"]])    # Varias columnas

# 4. Filtrado de filas
print(df[df["Edad"] > 30])         # Mayores de 30 años
print(df[df["Ciudad"] == "Madrid"]) # Personas de Madrid

# 5. Operaciones con columnas
df["Salario_Anual"] = df["Salario"] * 12
print(df)

# 6. Ordenar datos
print(df.sort_values(by="Edad"))
print(df.sort_values(by="Salario", ascending=False))

# 7. Agrupaciones
print(df.groupby("Ciudad")["Salario"].mean())

# 8. Valores nulos y limpieza
df.loc[2, "Salario"] = None
print(df.isnull().sum())
df["Salario"].fillna(df["Salario"].mean(), inplace=True)
print(df)

# 9. Exportar a CSV
df.to_csv("empleados.csv", index=False)
