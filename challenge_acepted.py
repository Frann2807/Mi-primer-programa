
number_to_guess = 7

user_number = int(input("Tienes 5 intentos para adivianar el numero entre el 1 y el 10.Adivina el numero: "))

if user_number == number_to_guess:
    print("Has ganado")

else:
    print("Has perdido.")
    user_number = int(input("Intentalo de nuevo: "))
    if user_number == number_to_guess:
        print("Lo has logrado!")
    else:
        print("Mala suerte")
        user_number = int(input("Puedes hacerlo, Intentalo de nuevo!: "))
        if user_number == number_to_guess:
            print("Te dije que podias hacerlo, Felicidades!")
        else:
            print("Vamos,Se que puedes hacerlo!")
            user_number = int(input("Intentalo de nuevo:"))
            if user_number == number_to_guess:
                print("Felicitaciones! Lo has conseguido")
            else:
                print("Mantente determinado, Tu pudes!")
                user_number = int(input("Ultimo intento:"))
                if user_number == number_to_guess:
                    print("Felicitaciones! Tu determinacion dio fruto!")
                else:
                    print("Tranquilo! No te sientas mal, Es solo un juego!")
