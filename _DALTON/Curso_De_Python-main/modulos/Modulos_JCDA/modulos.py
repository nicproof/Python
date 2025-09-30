import modulo_saludar                               # importamos el modulo completo
import modulo_saludar as ms                         # importamos el modulo completo y le asignamos un alias
from modulo_saludar import saludar                  # importamos solo la funcion saludar del modulo
from modulos_externos import modulo_despedida       # importamos un modulo que esta dentro de una carpeta
import modulos_externos.modulo_despedida


saludo1 = modulo_saludar.saludar("Juan")   # accedemos a la funcion saludar del modulo, para ello usamos el nombre del modulo
print(saludo1)

saludo2 = ms.saludar("Ana")   # accedemos a la funcion saludar del modulo usando el alias, para ello usamos as
print(saludo2)

saludo3 = saludar("Luis")   # accedemos a la funcion saludar directamente, para ello usamos from ... import ...
print(saludo3)

# print(__main__)  # __main__ es el nombre del modulo principal, es decir, el modulo que se esta ejecutando
# print(modulo_saludar.__name__)  # __name__ es el nombre del modulo, en este caso modulo_saludar

despedida1 = modulo_despedida.despedirse("Maria")  # accedemos a la funcion despedirse del modulo que esta dentro de una carpeta
print(despedida1)

despedida2 = modulos_externos.modulo_despedida.despedirse("Pedro")  # accedemos a la funcion despedirse del modulo que esta dentro de una carpeta
print(despedida2)

