"""
Dada una lista de strings, devolver una lista con el largo de cada string.
"""
lista_datos = []
lista_largo_str = []
str_user = ""

print("Dime una serie de palabras y yo te dire el largo de cada una de ellas.Escribe Fin para finalizar.")

while not str_user == "Fin":
    str_user = input("Dime una palabra: ")
    if str_user.isalpha() and str_user != "Fin":
        print("¡Palabra añadida!")
        lista_datos.append(str_user)

for palabra in lista_datos:
    lista_largo_str.append(len(palabra))

print("La lista de palabras que me diste es la siguiente: {}.".format(lista_datos))
print("La cantidad de de letras que posee cada palabra es: {} .".format(lista_largo_str))
