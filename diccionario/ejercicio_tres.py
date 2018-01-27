"""
Crea un programa que cuente el número de veces que aparece una palabra en una string
"""

string = dict()

user_string = input("Dime una frase: ")
palabra = ""

for indice in range(len(user_string)):
    letra = user_string[indice]
    if letra != " " and letra != "." and letra != ",":
        palabra += letra


    else:
        if palabra in string:
            cantidad_repeat = string[palabra]
            cantidad_repeat += 1
            string[palabra] = cantidad_repeat
        else:
            cantidad_repeat = 1
            string[palabra] = cantidad_repeat
        palabra = ""

if palabra in string:
    cantidad_repeat = string[palabra]
    cantidad_repeat += 1
    string[palabra] = cantidad_repeat
elif palabra != "":
    cantidad_repeat = 1
    string[palabra] = cantidad_repeat
    palabra = ""

print(string)
