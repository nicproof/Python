import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chisquare
            

# FUNCIÓN ORIGINAL obtener_info_dataset

def obtener_info_dataset(nombre_archivo, separador=';'):
    # ... (El código de la función obtener_info_dataset permanece sin cambios) ...
    # Nota: He añadido 'separador' como argumento para mayor flexibilidad.

    ruta_archivo = Path(nombre_archivo)
    if not ruta_archivo.exists():
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Verifica la ruta.")
        return None

    try:
        df = pd.read_csv(ruta_archivo, sep=separador, on_bad_lines='skip') 
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None
    
    # 2. Encabezado informativo
    print("=" * 60)
    print(f"INFORMACIÓN DEL DATASET: '{nombre_archivo}'")
    print("=" * 60)

    # 3. Información básica
    print(f"| Número Total de Sorteos (Filas): {df.shape[0]:,}")
    print(f"| Número Total de Variables (Columnas): {df.shape[1]}")
    print("-" * 60)

    # 4. Nombres de las columnas
    print("Nombres de las Columnas:")
    for i, col in enumerate(df.columns):
        print(f"  [{i+1}] {col}")
    print("-" * 60)

    # 5. Tipos de datos y valores perdidos
    print("Tipos de Datos y Estado de Valores Perdidos:")
    df_info = pd.DataFrame({
        'Tipo de Dato': df.dtypes,
        'Valores Perdidos': df.isnull().sum(),
        '% Perdidos': (df.isnull().sum() / len(df) * 100).round(2),
        'Valores Únicos': df.nunique()
    })
    print(df_info.to_markdown(numalign="left", stralign="left"))
    print("-" * 60)
    
    # 6. Descripción estadística para variables numéricas (si las hay)
    bolas_y_estrellas = df.select_dtypes(include=np.number).filter(regex='(Bola|Estrella)') # Ajustado para compatibilidad si ya tienen el nombre
    if not bolas_y_estrellas.empty:
        print("Descripción Estadística (Números Numéricos):")
        print(bolas_y_estrellas.describe().loc[['count', 'mean', 'std', 'min', 'max']].T.to_markdown(numalign="left", stralign="left"))
        print("-" * 60)

    # 7. Primeras 5 filas (Vista previa)
    print("Vista Previa (Primeros 5 Sorteos):")
    print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
    print("=" * 60)

    return df # Retorna el DF original para ser usado por la función de procesamiento


#  NUEVA FUNCIÓN procesar_euromillon

def procesar_euromillon(df_original: pd.DataFrame) -> pd.DataFrame:
    """
    Selecciona las columnas relevantes, parsea la combinación ganadora 
    y limpia los tipos de datos para crear el DataFrame final de análisis.
    """
    print("\n" + "=" * 60)
    print("INICIANDO PROCESAMIENTO Y LIMPIEZA DE DATOS CLAVE")
    print("=" * 60)

    # 1. Definir columnas de interés
    columnas_interes = [
        'fecha_sorteo',
        'dia_semana',
        'anyo',
        'recaudacion',
        'premio_bote',
        'combinacion',
        'categoria_1',
        'categoria_2',
        'categoria_3',
        'categoria_4',
        'categoria_5',
        'categoria_6',
        'categoria_7',
        'categoria_8',
        'categoria_9',
        'categoria_10'
    ]

    # Verificar que las columnas clave existan antes de seleccionarlas
    columnas_faltantes = [col for col in columnas_interes if col not in df_original.columns]
    if columnas_faltantes:
        print(f"ADVERTENCIA: Faltan columnas clave para el análisis: {columnas_faltantes}. No se puede procesar.")
        return pd.DataFrame()

    # Crear el nuevo DataFrame
    df_procesado = df_original[columnas_interes].copy()

    # 2. Parsing de la columna 'combinacion' (ejemplo: "16 - 29 - 32 - 36 - 41 - 7 - 9")
    try:
        # Separar la cadena por el patrón de separación
        combinaciones_separadas = df_procesado['combinacion'].str.split(' - ', expand=True)

        # Definir los nombres de las 7 nuevas columnas numéricas
        nombres_nuevas_columnas = [
            'Bola_1', 'Bola_2', 'Bola_3', 'Bola_4', 'Bola_5', 
            'Estrella_1', 'Estrella_2'
        ]

        # Asignar y convertir a numérico
        df_procesado[nombres_nuevas_columnas] = combinaciones_separadas
        for col in nombres_nuevas_columnas:
            # Convierte a entero, tratando errores como NaN
            df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce', downcast='integer')

        # 3. Eliminamos la columna de texto original y las filas incompletas por el parsing
        df_procesado = df_procesado.drop(columns=['combinacion']).dropna(subset=nombres_nuevas_columnas)
        print(f"--> Columna 'combinacion' parseada en 7 columnas numéricas. Filas con errores eliminadas: {df_original.shape[0] - df_procesado.shape[0]}")
    except Exception as e:
        print(f"ERROR al parsear la columna 'combinacion'. Revisa el formato: {e}")
        return df_procesado

    # 4. Transformación y Limpieza de Tipos
    df_procesado['fecha_sorteo'] = pd.to_datetime(df_procesado['fecha_sorteo'], errors='coerce')
    
    # Asumimos que las columnas económicas ya están limpias o aplicamos una limpieza básica
    for col in ['recaudacion', 'premio_bote']:
         if df_procesado[col].dtype == object:
             df_procesado[col] = df_procesado[col].astype(str).str.replace(r'[^0-9.]', '', regex=True) # Elimina comas y símbolos
             df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce')
    
    print("--> Conversión de 'fecha_sorteo' a datetime y limpieza de columnas económicas completada.")
    print("-" * 60)
    print("INFO: DataFrame Limpio (df_analisis)")
    # print(df_procesado.info())
    # print("\nVista Previa:")
    # print(df_procesado.head().to_markdown(index=False, numalign="left", stralign="left"))
    # print("=" * 60)

    return df_procesado


if __name__ == "__main__":
    nombre_csv = "! JCDA_básico\\scrap_euromillones.csv" # Ajusta si necesitas la ruta completa de tu ejemplo
    
    # PASO 1: Obtener información y cargar el DF original
    df_original = obtener_info_dataset(nombre_csv, separador=',') # Usamos ',' ya que los nombres de columna del ejemplo se veían separados por coma.

    # PASO 2: Procesar el DataFrame si la carga fue exitosa
    if df_original is not None and not df_original.empty:
        df_analisis = procesar_euromillon(df_original)
        
# Imprimir el DataFrame final para verificación
        print("\nDataFrame Final para Análisis (df_analisis):")
        print(df_analisis.head().to_markdown(index=False, numalign="left", stralign="left"))

# buscar los núeros más frecuentes en las bolas

        print("\nNúmeros más frecuentes en las Bolas:")
        bolas = pd.concat([df_analisis[f'Bola_{i}'] for i in range(1, 6)])
        frecuencias_bolas = bolas.value_counts().head(10)
        
        print(frecuencias_bolas.to_markdown(numalign="left", stralign="left"))
        
# buscar los números más frecuentes en las estrellas

        print("\nNúmeros más frecuentes en las Estrellas:")
        estrellas = pd.concat([df_analisis[f'Estrella_{i}'] for i in range(1, 3)])
        frecuencias_estrellas = estrellas.value_counts().head(10)       
        
        print(frecuencias_estrellas.to_markdown(numalign="left", stralign="left"))
        
# buscar los numeros más frecuentes en las bolas cuando ha tocado bote

        print("\nNumeros más frecuentes en las Bolas cuando ha tocado Bote:")
        df_bote = df_analisis[df_analisis['premio_bote'] > 0]
        bolas_bote = pd.concat([df_bote[f'Bola_{i}']
                                for i in range(1, 6)])  
        frecuencias_bolas_bote = bolas_bote.value_counts().head(10)
        
        print(frecuencias_bolas_bote.to_markdown(numalign="left", stralign="left"))
        
# Generar un gráfico donde se reflejen las 6 bolas que con más frecuencia salen cuando ha tocado bote
        plt.figure(figsize=(10, 6))
        sns.barplot(x=frecuencias_bolas_bote.index.astype(int), y=frecuencias_bolas_bote.values, palette="viridis")
        plt.title('Números más frecuentes en las Bolas cuando ha tocado Bote')
        plt.xlabel('Número de Bola')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()



# buscar los números más frecuentes en las estrellas cuando ha tocado bote

        print("\nNúmeros más frecuentes en las Estrellas cuando ha tocado Bote:")
        estrellas_bote = pd.concat([df_bote[f'Estrella_{i}']
                                for i in range(1, 3)])
        frecuencias_estrellas_bote = estrellas_bote.value_counts().head(10)
        
        print(frecuencias_estrellas_bote.to_markdown(numalign="left", stralign="left"))
        
# AÑADIR ESTO AL FINAL DEL SCRIPT
if 'df_analisis' in locals() and not df_analisis.empty:
    print("\n" + "=" * 60)
    print("ANÁLISIS ESTADÍSTICO DE ALEATORIEDAD (TEST Chi-cuadrado)")
    print("=" * 60)
    
    # 1. Preparar las frecuencias observadas
    bolas_apiladas = pd.concat([df_analisis[f'Bola_{i}'] for i in range(1, 6)]).dropna()
    frecuencias_observadas = bolas_apiladas.value_counts().sort_index()

    # Rango completo de números del 1 al 50
    rango_bolas = pd.Series(range(1, 51))
    
    # Asegurar que todas las 50 bolas estén en el conteo (los no salidos tienen 0)
    frecuencias_completas = frecuencias_observadas.reindex(rango_bolas, fill_value=0)
    
    # 2. Calcular la frecuencia esperada
    # En un sorteo aleatorio, la frecuencia esperada es la misma para todas las bolas.
    total_observaciones = frecuencias_completas.sum()
    num_posibles_valores = 50
    frecuencia_esperada = total_observaciones / num_posibles_valores
    
    # El array de frecuencias esperadas es el mismo valor para los 50 números
    f_esperada_array = np.full(num_posibles_valores, frecuencia_esperada)
    
    # 3. Aplicar el Test Chi-Cuadrado (Bondad de Ajuste)
    # Se compara la distribución observada (frecuencias_completas) con la esperada (uniforme)
    chi2_stat, p_value = chisquare(f_obs=frecuencias_completas.values, f_exp=f_esperada_array)
    
    print(f"Número total de apariciones de bolas: {total_observaciones:,}")
    print(f"Frecuencia Esperada por Bola (si fuera perfectamente uniforme): {frecuencia_esperada:.2f}")
    print("-" * 60)
    print(f"Estadístico Chi-cuadrado (Chi2): {chi2_stat:.2f}")
    print(f"Valor P (p-value): {p_value:.4f}")
    
    # 4. Interpretación de la Relevancia
    alpha = 0.05
    if p_value < alpha:
        print(f"\nCONCLUSIÓN: Rechazamos la hipótesis nula (p-value < {alpha}).")
        print("La distribución de las bolas NO es perfectamente uniforme/aleatoria. Hay un sesgo estadísticamente significativo.")
    else:
        print(f"\nCONCLUSIÓN: No podemos rechazar la hipótesis nula (p-value >= {alpha}).")
        print("La distribución de las bolas NO se desvía significativamente de la aleatoriedad esperada.")
        
    print("=" * 60)
    
    
# Asegúrate de que df_analisis esté disponible y limpio
if 'df_analisis' not in locals() or df_analisis.empty:
    print("Error: df_analisis no está disponible. Ejecuta las funciones de carga y procesamiento primero.")
    exit()

# 1. Preparación de Datos
# Apilar todas las 5 columnas de bolas para contar la frecuencia
bolas_apiladas = pd.concat([df_analisis[f'Bola_{i}'] for i in range(1, 6)]).dropna()
frecuencias_observadas = bolas_apiladas.value_counts().sort_index()

# Rellenar con 0 las bolas que nunca han salido (del 1 al 50)
rango_bolas = pd.Series(range(1, 51))
frecuencias_completas = frecuencias_observadas.reindex(rango_bolas, fill_value=0)

# Calcular la frecuencia esperada (la media)
total_observaciones = frecuencias_completas.sum()
num_posibles_valores = 50
frecuencia_esperada = total_observaciones / num_posibles_valores

# 2. Creación del DataFrame de Plotting
df_plot = pd.DataFrame({
    'Bola': frecuencias_completas.index,
    'Frecuencia Observada': frecuencias_completas.values
})
df_plot['Desviacion'] = df_plot['Frecuencia Observada'] - frecuencia_esperada

# Definir el color basado en la desviación
df_plot['Color'] = df_plot['Desviacion'].apply(lambda x: 'g' if x > 0 else 'r')

# 3. Generación del Gráfico
plt.figure(figsize=(18, 7))
sns.barplot(
    x='Bola', 
    y='Desviacion', 
    data=df_plot, 
    palette=df_plot['Color'].tolist()
)

# Añadir la línea de referencia cero (Frecuencia Esperada)
plt.axhline(0, color='blue', linestyle='--', linewidth=1.5, label=f'Frecuencia Esperada ({frecuencia_esperada:.1f})')

plt.title('Desviación de la Frecuencia de las 50 Bolas Principales respecto a la Aleatoriedad', fontsize=16)
plt.xlabel('Número de Bola (1 a 50)', fontsize=14)
plt.ylabel(f'Desviación de la Frecuencia (Obs. - Esp.)', fontsize=14)
plt.xticks(rotation=0, ha='center', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# Lista de las 6 bolas más frecuentes por cada categoría
print("\n" + "=" * 60)
print("LAS 6 BOLAS MÁS FRECUENTES POR CATEGORÍA")
print("=" * 60)
print("\n1. Bolas Más Frecuentes (General):")
print(frecuencias_bolas.head(6).to_markdown(numalign="left", stralign="left"))
print("\n2. Bolas Más Frecuentes (Cuando ha Tocada Bote):")
print(frecuencias_bolas_bote.head(6).to_markdown(numalign="left", stralign="left"))
print("=" * 60)