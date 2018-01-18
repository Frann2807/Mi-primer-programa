mi_lista = ["Lechuga", "Tomate", "Helado", "Pan", "Olivas", "Atun", "Fanta"]

largo_lista = len(mi_lista)

indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de mi compra.")