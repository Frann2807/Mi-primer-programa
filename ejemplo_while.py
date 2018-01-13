numero_inicial = 10

print(numero_inicial)

if numero_inicial % 2 == 0:
    print("Este numero es el incial y par")
else:
    print("Este es el numero inicial y es impar")

while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)
    if numero_inicial % 2 == 0:
        print("Este numero es par")
    else:
        print("Este numero es impar")

print("He terminado")