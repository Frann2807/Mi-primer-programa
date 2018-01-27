salida = False
agenda = []

while not salida:
    accion = input("¿Que quieres hacer? [Añadir un numero [A]] / Consultar un numero [C] / Salir [S]: ")

    #Accion Añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        print("---------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda.append([nombre, numero])

    #Accion Consultar
    elif accion == "C":
        print("Vamos a consultar un numero de telefono:")
        print("---------------------------------------")
        nombre = input("¿De quien quieres saber el numero?: ")

        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])




    #Accion Salir
    elif accion == "S":
        salida = True

