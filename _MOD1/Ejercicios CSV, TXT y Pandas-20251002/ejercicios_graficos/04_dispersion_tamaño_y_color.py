import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize


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

e4_dispersion_tamano_color()