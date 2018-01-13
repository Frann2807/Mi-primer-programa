print("Este es un juego simple. Se necesitan dos personas para jugarlo; Uno pone un numero y el tiene que intentar adivinarlo.")

jugador_numero_uno = input("Dime tu nombre: ")
jugador_numero_dos = input("Dime tu nombre: ")

print("{} Tu seras el que indique el numero a adivinar.".format(jugador_numero_uno))
print("{} Tu seras el que intente adivinar el numero.".format(jugador_numero_dos))

print("Turno de {}".format(jugador_numero_uno))
number_to_guess = int(input("{} Dime un numero del 1 al 10: ".format(jugador_numero_uno)))

print("Turno de {}".format(jugador_numero_dos))
user_number = int(input("{} Dime un numero del 1 al 10: ".format(jugador_numero_dos)))

while user_number != number_to_guess:
    user_number = int(input("Mala suerte {}! Te has equivocado. Vuelve a intentarlo: ".format(jugador_numero_dos)))

if number_to_guess == user_number:
    print("¡Felicitaciones {} Lo has adivinado!".format(jugador_numero_dos))


