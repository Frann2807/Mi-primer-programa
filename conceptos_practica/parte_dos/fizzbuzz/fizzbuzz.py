"""
Dada una listaa de enteros:
Vamos a sustituir los multiplos de 3 por un fizz
y los multiplos de 5 por un buzz.
Multiplos de 3 y de 5 sustituir por Fizzbuzz.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 70]

for indice in range(len(numeros)):
    numero = numeros[indice]
    valor = ""

    if numero % 3 == 0 or numero % 5 == 0:

        numero[indice] = ""

        if numero % 3 == 0:
            numero[indice] += "Fizz"

        if numero % 5 == 0:
            numero[indice] += "Buzz"


print(numeros)
