"""
IFCD104 - Visualización con Matplotlib (GUIADO)
------------------------------------------------
Archivo pensado para aprender y practicar en VS Code.
Incluye teoría breve, ejemplos y ejercicios guiados con solución.


Consejo: cierra cada ventana de gráfico para continuar con el siguiente.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
# import random

# def generar_color_hex_aleatorio():
#     """Genera un código de color hexadecimal aleatorio (ej. #a3b1c2)."""
#     # Genera 6 dígitos hexadecimales al azar
#     return '#{:06x}'.format(random.randint(0, 0xFFFFFF))

# colores_originales = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

# # Creamos una nueva lista con colores aleatorios, manteniendo la misma longitud
# colores_aleatorios = [generar_color_hex_aleatorio() for _ in colores_originales]

# print(f"Colores originales: {colores_originales}")
# print(f"Colores aleatorios: {colores_aleatorios}")


# ======================================================
# 0) INTRO RÁPIDA
# ======================================================
def intro_rapida():
    """
    Matplotlib: API de bajo nivel para dibujar gráficos en Python.
    Idea clave: primero "dibujas" (plot, bar, scatter...), y luego "muestras" con plt.show().
    - plt.figure() opcional para crear una figura con tamaño y título de ventana.
    - plt.plot / plt.bar / plt.scatter / plt.hist / plt.pie / plt.boxplot / plt.imshow ...
    - plt.xlabel, plt.ylabel, plt.title, plt.legend, plt.grid, plt.tight_layout ...
    """
    print("Intro lista. Ejecuta el resto de funciones para ver ejemplos visuales.")


# ======================================================
# 1) BARRAS: un color por barra
# ======================================================
def barras_colores_por_barra():
    """
    Objetivo: que cada barra tenga un color distinto.
    Puntos clave:
      - Usa `color=[lista_de_colores]` con el mismo largo que los datos.
      - Colores pueden ser nombres ("red") o hex ("#1f77b4").
    """
    x = ["A", "B", "C", "D", "E"]
    y = [5, 7, 3, 8, 4]
    colores = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

    plt.figure("IFCD104 - Barras: un color por barra", figsize=(7, 4))
    plt.bar(x, y, color=colores)
    plt.title("Barras: cada barra con un color")
    plt.xlabel("Categoría")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()


# ======================================================
# 1.b) BARRAS con colormap según el valor
# ======================================================
def barras_colormap_segun_valor():
    """
    Objetivo: colorear automáticamente según el valor de cada barra.
    Técnicas:
      - Normalizar valores con Normalize(vmin, vmax)
      - Elegir colormap (viridis, plasma, inferno, magma, cool, etc.)
      - Crear ScalarMappable y añadir colorbar como referencia.
    """
    x = ["A", "B", "C", "D", "E", "F", "G"]
    y = [5, 12, 3, 9, 7, 14, 2]

    norm = Normalize(vmin=min(y), vmax=max(y))
    colormap = cm.plasma
    colores = colormap(norm(y))

    plt.figure("IFCD104 - Barras: colormap por valor", figsize=(7, 4))
    plt.bar(x, y, color=colores)
    plt.title("Barras con colormap según valor (plasma)")
    plt.xlabel("Categoría")
    plt.ylabel("Valor")
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array([])
    fig, ax = plt.gcf(), plt.gca() # porque no funcionaba el original
    # plt.colorbar(sm, label="Valor")
    plt.colorbar(sm, ax=ax, label="Valor")
    plt.tight_layout()
    plt.show()
    

# ======================================================
# 2) LÍNEAS: estilos, marcadores y leyenda
# ======================================================
def lineas_basicas():
    x = np.linspace(0, 10, 200)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure("IFCD104 - Líneas", figsize=(7, 4))
    plt.plot(x, y1, marker="o", linestyle="-", label="sin(x)")
    plt.plot(x, y2, marker="s", linestyle="--", label="cos(x)")
    plt.title("Gráfico de líneas")
    plt.xlabel("x"); plt.ylabel("y")
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# ======================================================
# 3) DISPERSIÓN: tamaño y color
# ======================================================
def dispersion_con_tamano_y_color():
    """
    Objetivo: usar tamaño de punto (s) y color (c) para codificar variables.
    - s controla el área del marcador
    - alpha controla la transparencia
    - edgecolors añade contorno
    """
    rng = np.random.default_rng(42)
    x = rng.normal(50, 10, 120)
    y = rng.normal(30, 5, 120)
    tamanos = rng.integers(30, 200, size=120)  # codifica magnitud
    colores = rng.normal(0, 1, 120)            # codifica otra variable

    plt.figure("IFCD104 - Dispersión", figsize=(7, 4))
    sc = plt.scatter(x, y, s=tamanos, c=colores, alpha=0.75, edgecolors="k", cmap="viridis")
    plt.title("Dispersión con tamaño y color")
    plt.xlabel("X"); plt.ylabel("Y")
    cb = plt.colorbar(sc, label="Variable (color)")
    plt.tight_layout()
    plt.show()


# ======================================================
# 4) HISTOGRAMA con líneas de media y mediana
# ======================================================
def histograma_con_estadisticos():
    rng = np.random.default_rng(0)
    datos = rng.normal(loc=10, scale=2.5, size=1000)
    media = np.mean(datos)
    mediana = np.median(datos)

    plt.figure("IFCD104 - Histograma", figsize=(7, 4))
    plt.hist(datos, bins=25, edgecolor="black", alpha=0.7)
    plt.axvline(media, linestyle="--", label=f"Media = {media:.2f}")
    plt.axvline(mediana, linestyle=":", label=f"Mediana = {mediana:.2f}")
    plt.title("Histograma con media y mediana")
    plt.xlabel("Valor"); plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.show()


# ======================================================
# 5) PIE (gráfico de sectores) con buenas prácticas
# ======================================================
def pie_buenas_practicas():
    """
    Buenas prácticas:
      - No uses demasiadas categorías (4-6 máx).
      - Ordena o agrupa categorías pequeñas en 'Otros'.
      - Muestra porcentajes con autopct y separa ligeramente con explode.
    """
    valores = [45, 25, 18, 12]
    etiquetas = ["Producto A", "Producto B", "Producto C", "Producto D"]

    plt.figure("IFCD104 - Pie", figsize=(5.5, 5.5))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90,
            explode=[0.03, 0.03, 0, 0])
    plt.title("Participación por producto")
    plt.tight_layout()
    plt.show()


# ======================================================
# 6) BOXPLOT multi-grupo
# ======================================================
def boxplot_multigrupo():
    rng = np.random.default_rng(123)
    g1 = rng.normal(50, 8, 200)
    g2 = rng.normal(55, 10, 200)
    g3 = rng.normal(48, 6, 200)

    plt.figure("IFCD104 - Boxplot", figsize=(7, 4))
    plt.boxplot([g1, g2, g3], labels=["G1", "G2", "G3"])
    plt.title("Distribución por grupo (boxplot)")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()


# ======================================================
# 7) HEATMAP simple
# ======================================================
def heatmap_simple():
    rng = np.random.default_rng(7)
    matriz = rng.random((8, 10))

    plt.figure("IFCD104 - Heatmap", figsize=(7, 4))
    im = plt.imshow(matriz, aspect="auto", cmap="magma")
    plt.title("Mapa de calor")
    plt.xlabel("Columna"); plt.ylabel("Fila")
    plt.colorbar(im, label="Intensidad")
    plt.tight_layout()
    plt.show()


# ======================================================
# 8) RETO INTEGRADOR (GUIADO + SOLUCIÓN)
# ======================================================
def reto_integrador_guiado():
    """
    Enunciado:
      Dado un conjunto de ventas mensuales por categoría,
      crea un "mini dashboard" con:
        - Barras por categoría (cada barra de un color, y etiqueta encima)
        - Línea de ventas acumuladas mensuales
        - Dispersión precio vs unidades con tamaño=ingresos
    Datos simulados. Sigue los pasos en el código.
    """
    # 1) Datos
    categorias = ["A", "B", "C", "D", "E"]
    ventas_cat = np.array([120, 80, 45, 150, 95])  # por categoría
    colores = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

    meses = np.arange(1, 13)
    ventas_mensuales = np.array([20, 25, 18, 22, 24, 28, 26, 30, 27, 29, 31, 35])
    acumuladas = np.cumsum(ventas_mensuales)

    rng = np.random.default_rng(33)
    precios = rng.uniform(10, 40, 60)
    unidades = rng.integers(1, 30, 60)
    ingresos = precios * unidades  # para tamaño

    # 2) Subplots
    fig, axs = plt.subplots(1, 3, figsize=(14, 4))
    fig.suptitle("Mini Dashboard de Ventas (IFCD104)")

    # 2.a) Barras
    axs[0].bar(categorias, ventas_cat, color=colores)
    axs[0].set_title("Ventas por categoría")
    axs[0].set_xlabel("Categoría"); axs[0].set_ylabel("€")
    # Etiquetas sobre cada barra
    for i, v in enumerate(ventas_cat):
        axs[0].text(i, v + 3, str(v), ha="center", va="bottom")

    # 2.b) Línea acumulada
    axs[1].plot(meses, acumuladas, marker="o", linestyle="-")
    axs[1].set_title("Ventas acumuladas")
    axs[1].set_xlabel("Mes"); axs[1].set_ylabel("€")
    axs[1].grid(True, alpha=0.3)

    # 2.c) Dispersión precio vs unidades (tamaño=ingresos)
    sc = axs[2].scatter(precios, unidades, s=ingresos, alpha=0.6, edgecolors="k")
    axs[2].set_title("Precio vs Unidades (tam=Ingresos)")
    axs[2].set_xlabel("Precio (€)"); axs[2].set_ylabel("Unidades")
    # Nota: podemos normalizar 'ingresos' si los círculos salen demasiado grandes
    fig.tight_layout()
    plt.show()


# ======================================================
# 9) EJERCICIOS PROPUESTOS (con solución)
# ======================================================
def ejercicio_1_solucion():
    """
    E1: Crea un gráfico de barras con colores basados en el valor.
        Añade una colorbar.
    """
    x = list("ABCDEFG")
    y = [14, 9, 22, 7, 12, 15, 18]

    norm = Normalize(vmin=min(y), vmax=max(y))
    cmap = cm.inferno
    colores = cmap(norm(y))

    plt.figure("Ejercicio 1 - Solución", figsize=(7, 4))
    plt.bar(x, y, color=colores)
    sm = cm.ScalarMappable(cmap=cmap, norm=norm); sm.set_array([])
    plt.colorbar(sm, label="Valor")
    plt.title("E1: Barras con colormap (inferno)")
    plt.tight_layout(); plt.show()


def ejercicio_2_solucion():
    """
    E2: Haz un histograma de 1000 datos N(0,1) con 30 bins.
        Dibuja líneas de media y ±1 desviación típica.
    """
    rng = np.random.default_rng(1)
    datos = rng.normal(0, 1, 1000)
    media = np.mean(datos); std = np.std(datos)

    plt.figure("Ejercicio 2 - Solución", figsize=(7, 4))
    plt.hist(datos, bins=30, edgecolor="black", alpha=0.7)
    for x in [media, media-std, media+std]:
        plt.axvline(x, linestyle="--")
    plt.title("E2: Histograma con media y ±1σ")
    plt.tight_layout(); plt.show()


def ejercicio_3_solucion():
    """
    E3: Dispersión con colormap por 'y' y tamaño por 'x'.
    """
    rng = np.random.default_rng(2)
    x = rng.uniform(10, 100, 120)
    y = rng.normal(50, 15, 120)
    tamanos = x  # tamaño proporcional a x (simple)

    plt.figure("Ejercicio 3 - Solución", figsize=(7, 4))
    sc = plt.scatter(x, y, s=tamanos, c=y, alpha=0.7, edgecolors="k", cmap="plasma")
    plt.colorbar(sc, label="y")
    plt.title("E3: Dispersión (tam=x, color=y)")
    plt.xlabel("x"); plt.ylabel("y")
    plt.tight_layout(); plt.show()


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    #Descomenta lo que quieras ejecutar:

    intro_rapida()

    # barras_colores_por_barra()
    barras_colormap_segun_valor()
    # barras_colormap_segun_valor()

    # lineas_basicas()
    # dispersion_con_tamano_y_color()
    # histograma_con_estadisticos()
    # pie_buenas_practicas()
    # boxplot_multigrupo()
    # heatmap_simple()

    # reto_integrador_guiado()

    # ejercicio_1_solucion()
    # ejercicio_2_solucion()
    # ejercicio_3_solucion()
