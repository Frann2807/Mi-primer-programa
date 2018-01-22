"""
Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 70]
numero_mayor = 0

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero > numero_mayor:
        numero_mayor = numero

print(numero_mayor)