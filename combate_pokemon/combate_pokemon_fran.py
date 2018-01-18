pokemon_elegido = input("¿Contra que pokemon quieres luchar?(Squirtle / Charmander / Bulbasaur): ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0
nombre_enemigo = False

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    ataque_enemigo = 8
    nombre_enemigo = "Squirtle"

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    ataque_enemigo = 7
    nombre_enemigo = "Charmander"

elif pokemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    ataque_enemigo = 10
    nombre_enemigo = "Bulbasaur"

else:
    print("No se que elegiste asi que no se puede combatir")

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque deseas utilizar? (Chispazo / Bola voltio) :").upper()
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
        print("Le haces 10 de daño a {}".format(nombre_enemigo))
    elif ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
        print("Le haces 12 de daño a {}".format(nombre_enemigo))

    print("La vida de {} es {}".format(nombre_enemigo, vida_enemigo))
    if vida_enemigo <= 0:
        print("Gana Pikachu")


    elif vida_enemigo > 0:
        vida_pikachu -= ataque_enemigo
        print("{} te hace {} de daño".format(nombre_enemigo, ataque_enemigo))

        print("La vida de pikachu es {}".format(vida_pikachu))
    if vida_pikachu <= 0:
        print("Gana {}".format(nombre_enemigo))



print("El combate ha terminado")