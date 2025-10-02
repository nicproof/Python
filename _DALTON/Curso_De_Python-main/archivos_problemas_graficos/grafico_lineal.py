import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"_DALTON\Curso_De_Python-main\archivos_problemas_graficos\pedos.csv")

#creando el grafico
#sns.lineplot(x="fecha",y="pedos",data=df)
sns.lineplot(x="fecha",
    y="pedos",
    data=df,
    color="white",
    linewidth=0.5,
    ci=None)

#creando un punto en el momento de mas pedos
mayor=df.loc[df['pedos'].idxmax()]
menor=df.loc[df['pedos'].idxmin()]
#plt.plot("01-09",17,"o")
plt.plot(mayor['fecha'],mayor['pedos'],"s", color="green")
plt.plot(menor['fecha'],menor['pedos'],"d", color="red") 
                              

ax = plt.gca() # Obtiene los ejes actuales
ax.set_facecolor("#333333") # Establece un gris muy claro para el fondo

plt.xticks(rotation=45)
plt.tight_layout()
#mostrando el grafico
plt.show()