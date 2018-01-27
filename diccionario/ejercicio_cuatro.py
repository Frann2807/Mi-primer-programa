"""
Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string.
"""

def subrayar(frase):
    cant_line = dict()
    palabra = ""
    lineas = ""
    for letra in frase:
        palabra += letra
        lineas += "-"
    cant_line[palabra]: lineas
    print(palabra)
    return lineas

user_frase = input("Dime una frase: ")

print(subrayar(user_frase))