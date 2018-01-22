lista_numeros = []

user_numbers = ""
resultado = 1

print("Te ire pidiendo numeros y luego te dare el resultado de todos los numeros multiplicados.")
print("Para finalizar la lista escribe Fin")

while not user_numbers == "Fin":
    user_numbers = input("Dime un numero: ")
    if user_numbers != "Fin":
        lista_numeros.append(int(user_numbers))


for numero in lista_numeros:
    resultado = (numero * resultado)

print("Resultado final es: {}.".format(resultado))