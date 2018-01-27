"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.
"""

salida = False
agenda = dict()

while not salida:
    accion = input("¿Que quieres hacer? [Añadir una fecha [A]] / Consultar una fecha [C] / Salir [S]: ")

    #Accion Añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        print("---------------------------------------")
        nombre = input("Nombre: ")
        fecha = input("Fecha: ")
        agenda[nombre] = fecha

    #Accion Consultar
    elif accion == "C":
        print("Vamos a consultar una fecha de nacimiento:")
        print("---------------------------------------")
        nombre = input("¿De quien quieres saber la fecha?: ")
        print(agenda[nombre])




    #Accion Salir
    elif accion == "S":
        salida = True
