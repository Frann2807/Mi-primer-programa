"""
Obtener los tipos de datos que hay en una lista.
"""

lista_datos = [1, 2, 3, "asd", False, [], True, 23, 2.1]
lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(dato)
    print("El {} de la lista es de tipo: {}".format(dato, type(dato)))

"La lista ha finalizado."
