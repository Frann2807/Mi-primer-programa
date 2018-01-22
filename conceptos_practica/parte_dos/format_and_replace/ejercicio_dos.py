"""
Crear un programa que le repita al usuario todo lo que dice pero con todas las vocales cambiadas por i.
"""
frase_usuario = input("Dime una frase: ").upper()
vocales = ["A", "E", "I", "O", "U"]
vocal = "I"

for letra in vocales:
    if letra in frase_usuario:
        frase_usuario = frase_usuario.replace(letra, vocal)

print(frase_usuario)