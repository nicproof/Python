import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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

    # Aquí se generan datos simulados para los gráficos.

    # Datos para graficos de barra.
    categorias = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
    ventas_cat = np.array([120, 80, 45, 150, 95])
    colores = ["#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2"]

    # Datos para gráfico de línea.
    meses = np.arange(1, 12 + 1)
    ventas_mensuales = np.array([20, 25, 18, 22, 24, 28, 26, 30, 27, 29, 31, 35])
    acumuladas = np.cumsum(ventas_mensuales)

    # Datos para gráfico de dispersión.
    rng = np.random.default_rng(33)
    precios = rng.uniform(10, 40, 60)
    unidades = rng.integers(1, 30, 60)
    ingresos = precios * unidades



    # Con esto dibujamos el area que ocupa cada subplot
    fig, axs = plt.subplots(1, 3, figsize=(14, 4))   # Con fig lo que hacemos es definir la figura que contendrá los subplots
                                                     # Con axs definimos los ejes, como un array... en este caso 1 fila y 3 columnas
                                                     # Nos referimos a cada subplot como axs[0], axs[1], axs[2]
    fig.suptitle("Mini Dashboard (para hacer)")      # Titulo de la ventana prindipal



    axs[0].bar(categorias, ventas_cat, color=colores)            # Aquí dibujamos un grafico de barras, eje x categorias, eje y ventas_cat y colores
    for i, v in enumerate(ventas_cat):                           # Bucle para recorrer las barras generadas
        axs[0].text(i, v + 3, str(v), ha="center", va="bottom")  # Añadimos los valores encima de cada barra y nombre debajo de cada barra  
    axs[0].set_title("Ventas por categoría")                     # Titulo del primer subplot 



    axs[1].plot(meses, acumuladas, marker="o", linestyle="-")    # Aquí dibujamos un grafico de lineas, eje x meses, eje y acumuladas
    axs[1].set_title("Ventas acumuladas")                        # Titulo del segundo subplot    
    axs[1].grid(True, alpha=0.3)                                 # Añadimos una rejilla al grafico   



    sc = axs[2].scatter(precios, unidades, 
                        s=ingresos, alpha=0.6, edgecolors="k")  # Aquí dibujamos un grafico de dispersion, eje x precios, eje y unidades, tamaño de los puntos ingresos
    axs[2].set_title("Precio vs Unidades")                      # Titulo del tercer subplot



    fig.tight_layout();   # Por lo visto evita que se solapen los subplots al modificar el tamaño de la ventana
    plt.show()            # Mostramos la ventana con los subplots

e9_reto_integrador()