user_number = int(input("Dime un numero: "))

paridad = False

for numero in range(2,user_number):
    if user_number % numero == 0:
        paridad = True


if paridad == False:
    print("El numero es primo.")

elif paridad == True:
    print("El numero No es primo.")