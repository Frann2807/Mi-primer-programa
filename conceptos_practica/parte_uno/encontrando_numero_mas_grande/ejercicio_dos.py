numeros_usuario = []
user_number = ""
cantidad_numeros = 0
finalizar = ""

print("Te pedire una serie de numeros y luego te dire la cantidad de numeros que me escribiste. Escribe Fin para finalizar la lista de numeros.")

while user_number != "Fin":
    user_number = (input("Dime un numero: "))
    if user_number.isdigit():
        numeros_usuario.append(int(user_number))
        cantidad_numeros += 1
        print("¡Numero añadido!")


print("Los numeros que me diste fueron: {} ".format(numeros_usuario))
print("La cantidad de numeros que me diste fue de: {} numeros.".format(cantidad_numeros))






