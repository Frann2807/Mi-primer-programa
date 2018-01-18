numeros_usuario = []
numero_usuario = ""

while len(numeros_usuario) < 5:
    while not numero_usuario.isdigit():
        numero_usuario = input("Dime un numero:")
    numeros_usuario.append(int(numero_usuario))
    numero_usuario = ""
    print("¡Numero añadido!")

print(numeros_usuario)

numero_pequeño = numeros_usuario [0]

for numero in numeros_usuario:
    if numero_pequeño > numero:
        numero_pequeño = numero


print("El numero mas pequeño es {}.".format(numero_pequeño))