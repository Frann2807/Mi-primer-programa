apetece_helado_input = input("¿Quieres un helado? (Si / No): ").upper()
tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ").upper()
señor_helados_input = input("¿Esta el señor de los helados? (Si / No): ").upper()
esta_tu_tia_input = input("¿Esta tu tia?  (Si / No): ").upper()

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = (tiene_dinero_input == "SI" or esta_tu_tia_input == "SI")
esta_el_señor_helado = señor_helados_input == "SI"


if apetece_helado and puede_permitirselo and esta_el_señor_helado:
    print("Pues compralo")

else:
    print("Pues mala suerte")