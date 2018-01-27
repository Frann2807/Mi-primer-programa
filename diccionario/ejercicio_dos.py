"""
Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés
"""
salida = False
diccionario = {"Rojo": "Red",
               "Amarillo": "Yellow",
               "Azul": "Blue"}

while not salida:
    accion = input("¿Que quieres hacer? [Añadir un Color [A]] / Consultar un color [C] / Salir [S]: ")

    #Accion Añadir
    if accion == "A":
        print("Vamos a añadir una traduccion de un color:")
        print("---------------------------------------")
        nombre = input("Nombre del Color: ")
        traduccion = input("Traduccion: ")
        diccionario[nombre] = traduccion

    #Accion Consultar
    elif accion == "C":
        print("Vamos a traduccir tu color:")
        print("---------------------------------------")
        nombre = input("¿Que color deseas traducir?: ")
        print(diccionario[nombre])




    #Accion Salir
    elif accion == "S":
        salida = True