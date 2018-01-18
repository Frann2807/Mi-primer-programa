numero_tabla = int(input("Esta tabla muestra los numeros multiplicados de 5 a 15.De que numero quieres la tabla de multiplicar? :"))

for multiplo in range(5,16):
    print("{} x {} = {} ".format(numero_tabla, multiplo, numero_tabla * multiplo))