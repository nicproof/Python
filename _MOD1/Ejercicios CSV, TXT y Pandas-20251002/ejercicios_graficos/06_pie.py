import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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
    
e6_pie_buenas_practicas()