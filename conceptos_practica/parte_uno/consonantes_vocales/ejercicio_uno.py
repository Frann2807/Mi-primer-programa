
texto_usuario = input("Dime una frase: ")


puntos = 0
espacios = 0
comas = 0

punto = ["."]
espacio = [" "]
coma = [","]

for letra in texto_usuario:
    if letra in punto:
        puntos += 1
    elif letra in espacio:
        espacios += 1
    elif letra in coma:
        comas += 1

print("Cantidad de espacios: {}".format(espacios))
print("Cantidad de puntos: {}".format(puntos))
print("Cantidad de comas: {}".format(comas))



