"""
Crea un programa que te diga cuanto falta para tu cumpleaños y que día de la semana será.
"""
import datetime

def dia_semana(fecha):
    dias_semana = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Vienes", 5: "Sabado", 6: "Domingo"}
    dia = fecha.weekday()
    return dias_semana[dia]

hoy = datetime.datetime.now()

print("Dime la fecha del dia de tu cumpleaños.(A Futuro)")
day = int(input("Dia: "))
month = int(input("Mes: "))
year = int(input("Año: "))
user_birthday = datetime.datetime(year=year, month= month, day= day)

faltante_cumpleaños = user_birthday - hoy

print("Quedan {} dias para que sea tu cumpleaños.".format(faltante_cumpleaños.days))
print("Tu cumpleaños cae un {}.".format(dia_semana(user_birthday)))

