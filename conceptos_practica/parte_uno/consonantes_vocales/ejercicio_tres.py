texto_usuario = input("Dime una frase: ").upper()

lista_vocales = []
vocales = ["A", "E", "I", "O", "U"]

for letra in texto_usuario:
    if letra in vocales:
        lista_vocales.append(letra)

print("Vocales: {}".format(lista_vocales))