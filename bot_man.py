user_name = input("Hola! Soy Bot_Man. ¿Cual es tu nombre?: ")

estado_usuario = input("¿Como estas {}?: ".format(user_name)).upper()

if estado_usuario == "BIEN":
    print("Me alegro {}!".format(user_name))

else:
    estado_usuario == "MAL"
    print("No te preocupes! Todo mejora con el tiempo!")
