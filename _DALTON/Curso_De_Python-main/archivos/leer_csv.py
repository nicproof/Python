import csv

with open("_DALTON\\Curso_De_Python-main\\archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)