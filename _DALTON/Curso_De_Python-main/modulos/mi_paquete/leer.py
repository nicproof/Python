archivo_sin_leer = open("_DALTON\\Curso_De_Python-main\\modulos\\mi_paquete\\Texto.txt", encoding="UTF-8")

print("\nLeemos archivo completo de una sola vez")
print("-----------------------------------------")
archivo_leido = archivo_sin_leer.read()
print(archivo_leido)
archivo_sin_leer.close()
print("-----------------------------------------\n")


archivo_linea_a_linea = open("_DALTON\\Curso_De_Python-main\\modulos\\mi_paquete\\Texto.txt", encoding="UTF-8")
print("Leemos archivo linea a linea usando un bucle")
print("--------------------------------------------")
lineas = archivo_linea_a_linea.readlines()
for linea in lineas:
    print("->",linea)
archivo_linea_a_linea.close()
print("--------------------------------------------\n")

archivo_por_caracteres = open("_DALTON\\Curso_De_Python-main\\modulos\\mi_paquete\\Texto.txt", encoding="UTF-8")
print("Leemos archivo linea a linea usando read(n)")
print("--------------------------------------------")
linea = archivo_por_caracteres.readline(50)
archivo_por_caracteres.close()
print (linea)
print("--------------------------------------------\n")

    










    