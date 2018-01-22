lista_datos = ["asd", 1, "abc", 3, 7, "Fran"]
lista_num = []
lista_str = []

for dato in lista_datos:
    if dato.isalpha():
        lista_str.append(dato)
    elif dato.isdigit():
        lista_num.append(dato)

print("Lista de numeros: {}".format(lista_num))
print("Lista de palabras: {}".format(lista_str))

