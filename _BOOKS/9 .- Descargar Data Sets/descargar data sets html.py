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

ejemplo_tablas_html()



