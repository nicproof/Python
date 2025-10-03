import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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

e3_lineas_basicas()