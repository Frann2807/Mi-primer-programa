"""
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""
def mayor(lista):
    numero_mayor = 0
    for dato in lista:
        if dato > numero_mayor:
            numero_mayor = dato
    return numero_mayor

largo_lista = 0

numeros = []

while largo_lista < 3:
    user_number = input("Dime un numero: ")
    if user_number.isdigit():
        numeros.append(int(user_number))
        print("¡Numero añadido!")
        largo_lista += 1

print("Tu lista es: {}.".format(numeros))

mayor_lista = mayor(numeros)
print("El mayor de tu lista es: {}".format(mayor_lista))

