diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()
print(claves)

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)
valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")
print(valor_de_kasdks)

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
