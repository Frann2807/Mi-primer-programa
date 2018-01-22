lista_usuario_letras = []
lista_usuario_numeros = []
eleccion_usuario = " "

while eleccion_usuario != "FIN":

    eleccion_usuario = input("¿Que quieres añadir; Un numero o una Palabra?").upper()

    if eleccion_usuario == "NUMERO":
        numero_usuario = int(input("Dime un numero: "))
        lista_usuario_numeros.append(numero_usuario)
        print("Numero añadido!")

    elif eleccion_usuario == "PALABRA":
        palabra_usuario = input("Dime una palabra: ")
        lista_usuario_letras.append(palabra_usuario)
        print("Palabra añadida!")

    elif eleccion_usuario == "FIN":
        print("La lista ha terminado.")
    else:
        print("No se que has querido decirme, lo siento.")

print("Esta es tu lista de palabras: {}".format(lista_usuario_letras))
print("Esta es tu lista de numeros: {}".format(lista_usuario_numeros))


