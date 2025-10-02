import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"_DALTON\Curso_De_Python-main\archivos_problemas_graficos\cofla_ingresos.csv")

max_ingresos = df['ingresos'].max()
min_ingresos = df['ingresos'].min()
fuente_min = df.loc[df['ingresos'] == min_ingresos, 'fuente'].iloc[0]
fuente_max = df.loc[df['ingresos'] == max_ingresos, 'fuente'].iloc[0]
colores = ['green' if fuente == fuente_max 
            else 
            'red' if fuente == fuente_min
            else 
            'black' for fuente in df['fuente']]



#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df, palette=colores)


#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

ax = plt.gca() # Obtiene los ejes actuales
ax.set_facecolor("#4A66E4") # Establece un gris muy claro para el fondo

#mostrando el grafico
plt.show()

