numero_tabla = int(input("De que numero quieres la tabla de multiplicar? :"))

lista_multiplos = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplo in lista_multiplos:
    print("{} x {} = {} ".format(numero_tabla, multiplo, numero_tabla * multiplo))