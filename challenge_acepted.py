
number_to_guess = 8
name_player = input("Escribe tu nombre :")

user_number = int(input("Tienes 5 intentos para adivianar el numero entre el 1 y el 10.Adivina el numero: "))

if user_number == number_to_guess:
    print("WOW! Has ganado{}!".format(name_player))

else:
    print("Mala suerte! Pero no te preocupes {} , Solo es el primer intento.".format(name_player))
    user_number = int(input("Intentalo de nuevo: "))
    if user_number == number_to_guess:
        print("Lo has logrado{}!".format(name_player))
    else:
        print("Mala suerte!")
        user_number = int(input("Puedes hacerlo {}, Intentalo de nuevo!: ".format(name_player)))
        if user_number == number_to_guess:
            print("Te dije que podias hacerlo {}, Felicidades!".format(name_player))
        else:
            print("Vamos,Se que puedes hacerlo {}!".format(name_player))
            user_number = int(input("Intentalo de nuevo:"))
            if user_number == number_to_guess:
                print("Felicitaciones! Lo has conseguido")
            else:
                print("Mantente determinado, Tu pudes {}!".format(name_player))
                user_number = int(input("Ultimo intento:"))
                if user_number == number_to_guess:
                    print("Felicitaciones {}! Tu determinacion dio fruto!".format(name_player))
                else:
                    print("Tranquilo! No te sientas mal, Es solo un juego {}!".format(name_player))
