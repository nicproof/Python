"""
IFCD104 - Visualización con Matplotlib (PARA HACER)
---------------------------------------------------
Archivo para practicar en VS Code siguiendo las instrucciones (TODO).
Incluye enunciados y "huecos" para que completes el código.

Cómo usar:
- Rellena las partes con 'TODO' y ejecuta la función desde main.
- Requisitos: `pip install matplotlib numpy`
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize


# ======================================================
# 1) BARRAS: cada barra de un color
# ======================================================
def e1_barras_colores_por_barra():
    """
    Enunciado:
      Dibuja un gráfico de barras donde cada barra tenga un color distinto.
    Pasos:
      1) Crea listas x, y con 5 categorías y valores
      2) Define una lista de 5 colores
      3) Llama a plt.bar(x, y, color=...)
      4) Añade título, ejes y plt.show()
    """
    # TODO: datos
    x = ["A", "B", "C", "D", "E"]
    y = [5, 7, 3, 8, 4]
    colores = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]  # puedes cambiarlos

    # TODO: dibuja las barras con la lista de colores
    plt.figure("E1 - Barras", figsize=(7, 4))
    plt.bar(x, y, color=colores)

    # TODO: personaliza y muestra
    plt.title("E1: Barras - un color por barra")
    plt.xlabel("Categoría"); plt.ylabel("Valor")
    plt.tight_layout(); plt.show()


# ======================================================
# 2) BARRAS con colormap según el valor
# ======================================================
def e2_barras_colormap_segun_valor():
    """
    Enunciado:
      Colorea las barras automáticamente en función del valor.
    Pistas:
      - Usa Normalize(vmin, vmax)
      - Elige un colormap (viridis, plasma, inferno, magma...)
      - Crea ScalarMappable y añade colorbar
    """
    x = list("ABCDEFG")
    y = [14, 9, 22, 7, 12, 15, 18]

    # TODO: normaliza y crea colores por colormap
    norm = Normalize(vmin=min(y), vmax=max(y))
    cmap = cm.viridis
    colores = cmap(norm(y))

    plt.figure("E2 - Barras colormap", figsize=(7, 4))
    # TODO: dibuja las barras
    plt.bar(x, y, color=colores)

    # TODO: colorbar de referencia
    sm = cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
    plt.colorbar(sm, label="Valor")
    plt.title("E2: Barras con colormap")
    plt.tight_layout(); plt.show()


# ======================================================
# 3) LÍNEAS con estilos y leyenda
# ======================================================
def e3_lineas_basicas():
    """
    Enunciado:
      Pinta sin(x) y cos(x) con estilos distintos y leyenda.
    """
    # TODO: crea x con np.linspace
    x = np.linspace(0, 10, 200)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure("E3 - Líneas", figsize=(7, 4))
    # TODO: dos llamadas a plt.plot con marcadores/estilos diferentes
    plt.plot(x, y1, marker="o", linestyle="-", label="sin(x)")
    plt.plot(x, y2, marker="s", linestyle="--", label="cos(x)")

    plt.title("E3: Líneas con estilos")
    plt.xlabel("x"); plt.ylabel("y")
    # TODO: añade leyenda y grid
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.tight_layout(); plt.show()


# ======================================================
# 4) DISPERSIÓN con tamaño y color
# ======================================================
def e4_dispersion_tamano_color():
    """
    Enunciado:
      Crea un scatter donde:
        - 's' (tamaño) sea proporcional a una variable
        - 'c' (color) dependa de otra variable y tenga colorbar
    """
    rng = np.random.default_rng(42)
    x = rng.normal(50, 10, 120)
    y = rng.normal(30, 5, 120)
    tamanos = rng.integers(30, 200, size=120)
    colores = rng.normal(0, 1, 120)

    plt.figure("E4 - Dispersión", figsize=(7, 4))
    # TODO: scatter con tamaño y color + colorbar
    sc = plt.scatter(x, y, s=tamanos, c=colores, alpha=0.75, edgecolors="k", cmap="viridis")
    plt.colorbar(sc, label="Variable (color)")
    plt.title("E4: Dispersión con tamaño y color")
    plt.xlabel("X"); plt.ylabel("Y")
    plt.tight_layout(); plt.show()


# ======================================================
# 5) HISTOGRAMA con media y mediana
# ======================================================
def e5_histograma_estadisticos():
    """
    Enunciado:
      Genera 1000 datos N(10, 2.5) y dibuja:
        - Histograma con 25 bins
        - Línea vertical en media y en mediana
    """
    rng = np.random.default_rng(0)
    datos = rng.normal(10, 2.5, 1000)
    media = np.mean(datos); mediana = np.median(datos)

    plt.figure("E5 - Histograma", figsize=(7, 4))
    # TODO: histograma y líneas verticales
    plt.hist(datos, bins=25, edgecolor="black", alpha=0.7)
    plt.axvline(media, linestyle="--", label=f"Media={media:.2f}")
    plt.axvline(mediana, linestyle=":", label=f"Mediana={mediana:.2f}")
    plt.legend()
    plt.title("E5: Histograma con media y mediana")
    plt.tight_layout(); plt.show()


# ======================================================
# 6) PIE con buenas prácticas
# ======================================================
def e6_pie_buenas_practicas():
    """
    Enunciado:
      Crea un gráfico de sectores con 4 categorías, autopct y explode ligero.
    """
    valores = [45, 25, 18, 12]
    etiquetas = ["A", "B", "C", "D"]

    plt.figure("E6 - Pie", figsize=(5.5, 5.5))
    # TODO: gráfico de pie
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90, explode=[0.03, 0.03, 0, 0])
    plt.title("E6: Gráfico de sectores")
    plt.tight_layout(); plt.show()


# ======================================================
# 7) BOXPLOT multigrupo
# ======================================================
def e7_boxplot_multigrupo():
    """
    Enunciado:
      Genera 3 grupos con distribuciones diferentes y compáralos con boxplot.
    """
    rng = np.random.default_rng(123)
    g1 = rng.normal(50, 8, 200)
    g2 = rng.normal(55, 10, 200)
    g3 = rng.normal(48, 6, 200)

    plt.figure("E7 - Boxplot", figsize=(7, 4))
    # TODO: boxplot con etiquetas
    plt.boxplot([g1, g2, g3], labels=["G1", "G2", "G3"])
    plt.title("E7: Boxplot multigrupo")
    plt.tight_layout(); plt.show()


# ======================================================
# 8) HEATMAP simple
# ======================================================
def e8_heatmap():
    """
    Enunciado:
      Crea una matriz 8x10 de valores aleatorios y represéntala como mapa de calor
      con un colormap a tu elección y colorbar.
    """
    rng = np.random.default_rng(7)
    matriz = rng.random((8, 10))

    plt.figure("E8 - Heatmap", figsize=(7, 4))
    # TODO: imshow + colorbar
    im = plt.imshow(matriz, aspect="auto", cmap="magma")
    plt.colorbar(im, label="Intensidad")
    plt.title("E8: Heatmap")
    plt.tight_layout(); plt.show()


# ======================================================
# 9) RETO INTEGRADOR (para hacer)
# ======================================================
def e9_reto_integrador():
    """
    Enunciado:
      Con datos simulados, crea un mini dashboard con 3 subplots:
        - Barras por categoría (etiquetas encima)
        - Línea de ventas acumuladas mensuales
        - Dispersión precio vs unidades (tamaño=ingresos)
    Pistas:
      - Usa fig, axs = plt.subplots(1, 3, figsize=(14, 4))
      - Usa np.cumsum para acumuladas
      - Añade títulos y ejes claros
    """
    # TODO: genera datos
    categorias = ["A", "B", "C", "D", "E"]
    ventas_cat = np.array([120, 80, 45, 150, 95])
    colores = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

    meses = np.arange(1, 12 + 1)
    ventas_mensuales = np.array([20, 25, 18, 22, 24, 28, 26, 30, 27, 29, 31, 35])
    acumuladas = np.cumsum(ventas_mensuales)

    rng = np.random.default_rng(33)
    precios = rng.uniform(10, 40, 60)
    unidades = rng.integers(1, 30, 60)
    ingresos = precios * unidades

    # TODO: crea subplots y dibuja las 3 partes
    fig, axs = plt.subplots(1, 3, figsize=(14, 4))
    fig.suptitle("Mini Dashboard (para hacer)")

    axs[0].bar(categorias, ventas_cat, color=colores)
    for i, v in enumerate(ventas_cat):
        axs[0].text(i, v + 3, str(v), ha="center", va="bottom")
    axs[0].set_title("Ventas por categoría")

    axs[1].plot(meses, acumuladas, marker="o", linestyle="-")
    axs[1].set_title("Ventas acumuladas")
    axs[1].grid(True, alpha=0.3)

    sc = axs[2].scatter(precios, unidades, s=ingresos, alpha=0.6, edgecolors="k")
    axs[2].set_title("Precio vs Unidades")

    fig.tight_layout(); plt.show()


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    # Ejecuta y completa cada ejercicio a tu ritmo:
    e1_barras_colores_por_barra()
    e2_barras_colormap_segun_valor()
    e3_lineas_basicas()
    e4_dispersion_tamano_color()
    e5_histograma_estadisticos()
    e6_pie_buenas_practicas()
    e7_boxplot_multigrupo()
    e8_heatmap()
    e9_reto_integrador()
