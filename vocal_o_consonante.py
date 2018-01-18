"""
Crea un programa que te enseñe el numero de vocales y consonantes dentro de una frase introducida por el usuario.
"""

frase_usuario = input("Introduce una frase: ").upper()

vocales = ["A", "E", "I", "O", "U"]

n_vocales = 0
n_consonantes = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("El numero de vocales en tu frase es de {}.".format(n_vocales))
print("El numero de consonantes en tu frase es de {}.".format(n_consonantes))

