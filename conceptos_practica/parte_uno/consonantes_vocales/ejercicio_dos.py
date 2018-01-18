texto_usuario = input("Dime una frase: ")

mayusculas = 0
minusculas = 0


minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for letra in texto_usuario:
    if letra in minuscula:
        minusculas += 1
    elif letra in mayuscula:
        mayusculas += 1

print("Numero de mayusculas: {}".format(mayusculas))
print("Numero de minusculas: {}".format(minusculas))
