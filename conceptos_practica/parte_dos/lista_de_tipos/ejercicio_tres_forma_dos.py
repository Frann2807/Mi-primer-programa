"""
Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.
"""

lista_datos = ["asd", 1, "abc", 3, 7, "Fran"]
lista_num = []
lista_str = []

for dato in lista_datos:

    if type(dato) == str:
        lista_str.append(dato)

    elif type(dato) == int:
        lista_num.append(dato)

print("Lista de numeros: {}".format(lista_num))
print("Lista de palabras: {}".format(lista_str))

