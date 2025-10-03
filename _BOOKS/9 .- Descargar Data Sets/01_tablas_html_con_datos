from __future__ import annotations

from io import StringIO
from typing import List, Optional

import pandas as pd
import requests
# Necesitas instalar esta librería: pip install tabulate
from tabulate import tabulate 


def ejemplo_tablas_html(url: str = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_poblaci%C3%b3n") -> List[pd.DataFrame]:
    """
    Descarga el HTML de forma segura (usando un User-Agent) y usa pandas.read_html 
    para extraer todas las tablas de la página.
    """
    print(f"[HTML] Descargando tablas desde: {url}")
    
    # Definir un User-Agent para simular un navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Usar requests para obtener el contenido con los headers (evita Error 403)
        respuesta = requests.get(url, headers=headers)
        respuesta.raise_for_status() 
        
        # Leemos todas las tablas
        tablas = pd.read_html(StringIO(respuesta.text))
        
        print(f"[HTML] Tablas encontradas: {len(tablas)}")
        
        return tablas
    
    except requests.exceptions.HTTPError as err_h:
        print(f"[HTML][ERROR] Error HTTP (Verificación de Bot/403): {err_h}")
        return []
    except Exception as e:
        print(f"[HTML][ERROR] Error al leer o procesar las tablas: {e}")
        return []

# ----------------------------------------------------------------------
# --- Ejecución y Extracción de Datos Específicos (Proyecciones) ---
# ----------------------------------------------------------------------

dataframes = ejemplo_tablas_html()

if dataframes:
    # 1. Identificación de la Tabla Principal de Proyecciones:
    tabla_proyeccion: Optional[pd.DataFrame] = None
    
    for df in dataframes:
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(0)
            
        if any('Proyección' in str(col) for col in df.columns):
            tabla_proyeccion = df
            break 

    if tabla_proyeccion is not None:
        
        # 2. Búsqueda y mapeo de los nombres de las columnas que queremos mostrar:
        columnas_mapeadas = {}
        
        for col in tabla_proyeccion.columns:
            col_str = str(col)
            col_lower = col_str.lower().replace(" ", "")

            if 'país' in col_lower:
                columnas_mapeadas['País'] = col_str
            elif 'proyecciónexponencial' in col_lower:
                columnas_mapeadas['Proyección exponencial'] = col_str
            elif 'totalmundial' in col_lower:
                columnas_mapeadas['Total mundial (%)'] = col_str
            elif 'cambio' in col_lower and 'anual' in col_lower:
                 columnas_mapeadas[col_str] = col_str

        # 3. Definir el orden final de las columnas:
        columnas_ordenadas = [
            columnas_mapeadas.get('País'),
            columnas_mapeadas.get('Proyección exponencial'),
            columnas_mapeadas.get('Total mundial (%)'),
            next((col for name, col in columnas_mapeadas.items() if 'Cambio medio' in name), None),
            next((col for name, col in columnas_mapeadas.items() if 'Cambio absoluto' in name), None),
        ]
        
        columnas_finales = [col for col in columnas_ordenadas if col is not None]

        if columnas_finales:
            # Seleccionamos las columnas y excluimos la fila 'Mundo' (iloc[1:])
            df_filtrado = tabla_proyeccion.iloc[1:][columnas_finales]
            
            # Mostramos las 4 primeras filas de países
            df_resultado = df_filtrado.head(10).copy() 

            # 4. Formateo de los datos:
            # Convertimos las columnas numéricas a string para evitar la notación científica y aplicar separadores.
            col_poblacion = columnas_mapeadas.get('Proyección exponencial')
            
            if col_poblacion in df_resultado.columns:
                 # Intentamos limpiar los valores (quitando comas/espacios/etc.) y convertirlos a entero.
                def clean_and_format_number(x):
                    try:
                        # Limpia cualquier carácter que no sea dígito ni punto decimal
                        cleaned = str(x).replace('.', '').replace(',', '').replace(' ', '')
                        # Formatea el número con separadores de miles
                        return f"{int(cleaned):,}".replace(',', '.')
                    except ValueError:
                        return x # Devuelve el valor original si no se puede convertir

                df_resultado[col_poblacion] = df_resultado[col_poblacion].apply(clean_and_format_number)


            # 5. Generación de la salida con tabulate:
            
            # Generamos la tabla formateada con el estilo 'fancy_grid'
            # (Puedes probar 'grid', 'simple', 'html', etc.)
            tabla_formateada = tabulate(
                df_resultado, 
                headers="keys", 
                tablefmt="fancy_grid", 
                showindex=False  # Oculta el índice de Pandas (0, 1, 2, 3...)
            )
            
            # 6. Mostrar el resultado
            print("\n" + "="*60)
            print("NOMBRES DE LAS COLUMNAS UTILIZADAS (Nombres originales de Pandas):")
            print(columnas_finales)
            print("-" * 60)
            print("RESULTADO SOLICITADO (Formato con 'fancy_grid'):")
            print("="*60)
            print(tabla_formateada)
            print("="*60)
        else:
            print("\n[INFO] La tabla de proyección fue encontrada, pero no se pudo identificar las columnas de datos.")

    else:
        print("\n[INFO] No se pudo encontrar la tabla de Proyección Exponencial en la página.")
else:
    print("\n[INFO] No se pudo obtener ninguna tabla de la página (fallo de conexión o lectura).")