"""
Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.
"""

frase_usuario = input("Dime una frase: ")

for letra in frase_usuario:
    if letra == "A" or "a":
        new_frase_usuario = frase_usuario.replace(letra, "Vaca")

print(new_frase_usuario)