#2 listas, una con nombres otra con apellidos
nombres = ["Lucas","Matías","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","tarado"]

#Registrar esta información en un TXT de forma óptima

with open("_DALTON\\Curso_De_Python-main\\archivos_problemas\\nombres_y_apellidos.txt","w",encoding="UTF-8") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    
    
    
    