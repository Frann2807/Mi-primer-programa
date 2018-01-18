numeros_usuario = []
user_number = ""
cantidad_numeros = 0
finalizar = ""

print("Este programa resulve la Media de una cantidad de numeros.")
print("Te pedire una serie de numero a continuacion. Recuerda escribir Fin para finalizar")

while user_number != "Fin":
    user_number = (input("Dime un numero: "))
    if user_number.isdigit():
        numeros_usuario.append(int(user_number))
        cantidad_numeros += 1
        print("¡Numero añadido!")

print("Tus numeros son: {}".format(numeros_usuario))
print("La cantidad de numeros agregados es: {}.".format(cantidad_numeros))

suma_numeros_usuario = 0

for numero in numeros_usuario:
    suma_numeros_usuario += numero

print("La media de numeros que me diste es: {} ".format(suma_numeros_usuario / cantidad_numeros))