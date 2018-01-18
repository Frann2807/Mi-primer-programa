numero_tabla = int(input("De que numero quieres la tabla de multiplicar? :"))

lista_multiplos_dos = []

for multiplo in range(1,11):
    if numero_tabla * multiplo % 2 == 0:
        print("{} x {} = {} ".format(numero_tabla, multiplo, numero_tabla * multiplo))