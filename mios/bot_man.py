user_name = input("Hola! Soy Bot_Man. ¿Cual es tu nombre?: ")

estado_usuario = []

estado_usuario.append(input("¿Como estas {}?".format(user_name)).upper())


if "BIEN" in estado_usuario:
    print("¡Que buena suerte! ¡Hay que festejar")

elif "MAL" in estado_usuario:
    print("Mala suerte... Pero no te preocupes! Vamos por esas birras")

elif "RE LOCO" in estado_usuario:
    print("SLK ameo, No te encanute ese finoli!")