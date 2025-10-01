
#abriendo el archivo con with open
with open("_DALTON\\Curso_De_Python-main\\archivos\\texto_de_dalto.txt",encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerrarlo al usar with open