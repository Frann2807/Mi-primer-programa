"""
Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.
"""
import datetime

def dia_semana(fecha):
    dias_semana = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Vienes", 5: "Sabado", 6: "Domingo"}
    dia = fecha.weekday()
    return dias_semana[dia]

hoy = datetime.datetime.now()

back_five_days = hoy - datetime.timedelta(days=5)

print("Hace cinco dias fue: {}.".format(back_five_days.strftime("%d de %m del %Y")))
print("Fue un {}.".format(dia_semana(back_five_days)))