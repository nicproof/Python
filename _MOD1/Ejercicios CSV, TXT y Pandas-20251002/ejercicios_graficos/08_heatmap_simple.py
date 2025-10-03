import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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
    
e8_heatmap()