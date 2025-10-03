"""
web_to_dataframe_examples.py
--------------------------------
Ejemplos prácticos para descargar DataFrames de páginas web en Python.

Casos cubiertos:
1) Tablas HTML con pandas.read_html
2) CSV remotos con pandas.read_csv
3) JSON (APIs públicas) con pandas.read_json / requests
4) Scraping ligero con requests + BeautifulSoup + pandas

Requisitos sugeridos (instálalos si hace falta):
    pip install pandas requests beautifulsoup4 lxml html5lib
"""

from __future__ import annotations

import json
import sys
from typing import List, Dict, Any

import pandas as pd
import requests
from bs4 import BeautifulSoup


# ===============
# 1) Tablas HTML
# ===============
def ejemplo_tablas_html(url: str = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_poblaci%C3%B3n") -> List[pd.DataFrame]:
    """
    Descarga todas las tablas de una página HTML usando pandas.read_html.
    Devuelve una lista de DataFrames.
    """
    print(f"[HTML] Descargando tablas desde: {url}")
    try:
        tablas = pd.read_html(url)  # requiere lxml o html5lib
        print(f"[HTML] Tablas encontradas: {len(tablas)}")
        if tablas:
            print("[HTML] Vista previa de la primera tabla:")
            print(tablas[0].head())
        return tablas
    except Exception as e:
        print(f"[HTML][ERROR] No se pudieron leer las tablas: {e}")
        return []


# =====================
# 2) CSV remoto (URL)
# =====================
def ejemplo_csv(url: str = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv") -> pd.DataFrame | None:
    """
    Lee un CSV remoto directamente con pandas.read_csv.
    """
    print(f"[CSV] Descargando CSV desde: {url}")
    try:
        df = pd.read_csv(url)
        print("[CSV] Vista previa:")
        print(df.head())
        return df
    except Exception as e:
        print(f"[CSV][ERROR] No se pudo leer el CSV: {e}")
        return None


# ===================
# 3) Datos en JSON
# ===================
def ejemplo_json(
    url: str = "https://jsonplaceholder.typicode.com/posts",
    normalizar: bool = False,
) -> pd.DataFrame | None:
    """
    Lee datos JSON desde una URL. Puedes usar pandas.read_json o requests + json.
    Si 'normalizar' es True, intenta normalizar estructuras anidadas.
    """
    print(f"[JSON] Descargando JSON desde: {url}")
    try:
        # Opción A: directamente con pandas
        df = pd.read_json(url)
        print("[JSON] Leído con pandas.read_json")
    except Exception as e:
        print(f"[JSON] read_json falló ({e}). Probando con requests...")
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                # Si es un dict, intentamos normalizar
                df = pd.json_normalize(data)
        except Exception as e2:
            print(f"[JSON][ERROR] No se pudo leer el JSON: {e2}")
            return None

    if normalizar:
        try:
            # Intento de normalización adicional por si hay campos anidados
            registros = json.loads(df.to_json(orient="records"))
            df = pd.json_normalize(registros)
            print("[JSON] Estructura normalizada.")
        except Exception as e:
            print(f"[JSON] No se pudo normalizar: {e}")

    print("[JSON] Vista previa:")
    print(df.head())
    return df


# =========================================
# 4) Scraping ligero: requests + BeautifulSoup
# =========================================
def ejemplo_scraping(
    url: str = "https://www.worldometers.info/world-population/population-by-country/",
    selector_tabla: str | None = None,
) -> pd.DataFrame | None:
    """
    Descarga el HTML con requests, localiza una tabla con BeautifulSoup y la convierte a DataFrame.
    Si 'selector_tabla' es None, toma la primera <table> encontrada.
    """
    print(f"[SCRAPING] Descargando HTML desde: {url}")
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        tabla = soup.select_one(selector_tabla) if selector_tabla else soup.find("table")
        if tabla is None:
            print("[SCRAPING][ERROR] No se encontró ninguna tabla en la página.")
            return None

        # Convertimos esa tabla a DataFrame usando read_html sobre el HTML de la tabla
        df_list = pd.read_html(str(tabla))
        if not df_list:
            print("[SCRAPING][ERROR] pandas no pudo parsear la tabla.")
            return None

        df = df_list[0]
        print("[SCRAPING] Vista previa:")
        print(df.head())
        return df
    except Exception as e:
        print(f"[SCRAPING][ERROR] {e}")
        return None


def main():
    print("=" * 80)
    print("1) Tablas HTML")
    print("=" * 80)
    _ = ejemplo_tablas_html()

    print("\n" + "=" * 80)
    print("2) CSV remoto")
    print("=" * 80)
    _ = ejemplo_csv()

    print("\n" + "=" * 80)
    print("3) JSON")
    print("=" * 80)
    _ = ejemplo_json(normalizar=False)

    print("\n" + "=" * 80)
    print("4) Scraping ligero")
    print("=" * 80)
    _ = ejemplo_scraping()

    print("\nListo. Edita las URLs según tus necesidades y ejecuta de nuevo.")

if __name__ == "__main__":
    # Permite pasar URLs por argumentos opcionalmente:
    #   python web_to_dataframe_examples.py html <url>
    #   python web_to_dataframe_examples.py csv <url>
    #   python web_to_dataframe_examples.py json <url>
    #   python web_to_dataframe_examples.py scrape <url> [<selector_css>]
    if len(sys.argv) > 1:
        modo = sys.argv[1].lower()
        if modo == "html":
            url = sys.argv[2] if len(sys.argv) > 2 else None
            ejemplo_tablas_html(url) if url else ejemplo_tablas_html()
        elif modo == "csv":
            url = sys.argv[2] if len(sys.argv) > 2 else None
            ejemplo_csv(url) if url else ejemplo_csv()
        elif modo == "json":
            url = sys.argv[2] if len(sys.argv) > 2 else None
            ejemplo_json(url) if url else ejemplo_json()
        elif modo == "scrape":
            url = sys.argv[2] if len(sys.argv) > 2 else None
            selector = sys.argv[3] if len(sys.argv) > 3 else None
            ejemplo_scraping(url, selector) if url else ejemplo_scraping()
        else:
            print("Modo no reconocido. Usa: html | csv | json | scrape")
    else:
        main()
