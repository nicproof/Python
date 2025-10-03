import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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
    
    
e1_barras_colores_por_barra()