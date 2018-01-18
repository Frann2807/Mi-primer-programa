"""
Pregunta al usuario una serie de 10 numeros, determina cual es el mas grande de los 10.
"""

numeros_usuario = []
numero_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_usuario.isdigit():
        numero_usuario = input("Dime un numero:")
    numeros_usuario.append(int(numero_usuario))
    numero_usuario = ""
    print("¡Numero añadido!")

print(numeros_usuario)

numero_grande = numeros_usuario [0]

for numero in numeros_usuario:
    if numero_grande < numero:
        numero_grande = numero


print("El numero mas grande es {}".format(numero_grande))