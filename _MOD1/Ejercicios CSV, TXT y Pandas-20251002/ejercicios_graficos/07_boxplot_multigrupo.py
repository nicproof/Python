import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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

e7_boxplot_multigrupo()