"""
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
"""

def par(lista):

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

print("Los numeros pares son: {}".format(par(numeros)))