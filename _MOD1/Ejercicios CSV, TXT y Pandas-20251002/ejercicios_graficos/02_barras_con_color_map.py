import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

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
    fig, ax = plt.gcf(), plt.gca()
    plt.colorbar(sm, ax=ax, label="Valor") 
    # plt.colorbar(sm, label="Valor")
    plt.title("E2: Barras con colormap")
    plt.tight_layout(); plt.show()

e2_barras_colormap_segun_valor()