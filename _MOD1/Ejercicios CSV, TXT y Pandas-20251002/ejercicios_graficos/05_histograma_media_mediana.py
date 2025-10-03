import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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
    
e5_histograma_estadisticos()