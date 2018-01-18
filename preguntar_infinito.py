
confirmacion_borrado = ""
respuestas_posbiles = ["Si", "No"]

while confirmacion_borrado not in respuestas_posbiles:
    confirmacion_borrado = input("Quieres borrar el archivo? ({})".format("/".join(respuestas_posbiles)))