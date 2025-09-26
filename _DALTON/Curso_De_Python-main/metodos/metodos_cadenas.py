cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()
print(mayusc)

#convierte a minusculas
minusc = cadena1.lower()
print(minusc)

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()
print("->", primer_letra_mayusc)

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")
print(busqueda_find)

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepciòn
busqueda_index = cadena1.index("H")
print(busqueda_index)

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#si es alfanumèrico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")
print(contar_coincidencias)

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asì devuelve True
empieza_con = cadena1.startswith("H")
print(empieza_con)

#verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")
print(termina_con)

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," <-> ")
print(cadena_nueva)

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(cadena_separada)
print(cadena_separada[0])
