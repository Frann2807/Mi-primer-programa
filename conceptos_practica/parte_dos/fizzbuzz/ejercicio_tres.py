"""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro
de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 70]

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos_cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print("Multiplos de dos: {}".format(multiplos_dos))
print("Multiplos de tres: {}".format(multiplos_tres))
print("Multiplos de cinco: {}".format(multiplos_cinco))
print("Multiplos de siete: {}".format(multiplos_siete))