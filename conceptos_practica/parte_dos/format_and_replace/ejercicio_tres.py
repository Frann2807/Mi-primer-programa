"""
Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”
"""

frase_usuario = input("Dime una frase: ").upper()
vocales = ["A", "E", "I", "O", "U"]
numero = 1

for letra in frase_usuario:
    if letra in vocales:
        frase_usuario = frase_usuario.replace(letra, str(numero), 1)
        numero += 1

print(frase_usuario)