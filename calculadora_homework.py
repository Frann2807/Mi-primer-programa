operacion_user = input("¿Que operacion deseas realizar? (Multiplicacion / Division / Resta / Suma): ").upper()

primer_numero = int(input("Dime el primer numero:"))
segundo_numero = int(input("Dime el segundo numero:"))
resultado = 0
if operacion_user == "MULTIPLICACION":
    resultado = (primer_numero * segundo_numero)
    print("El resultado es: {}".format(resultado))

elif operacion_user == "DIVISION":
    resultado = (primer_numero / segundo_numero)
    print("El resultado es: {}".format(resultado))

elif operacion_user == "RESTA":
    resultado = (primer_numero - segundo_numero)
    print("El resultado es: {}".format(resultado))

elif operacion_user == "SUMA":
    resultado = (primer_numero + segundo_numero)
    print("El resultado es: {}".format(resultado))

else:
    print("No entiendo la operacion que me pides. Lo siento.")
