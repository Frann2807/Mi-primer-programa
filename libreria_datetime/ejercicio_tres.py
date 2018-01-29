"""
Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.
"""
import datetime

print("Dime una fecha y te dire cuantas horas han pasado desde ese dia.")
day = int(input("Dia: "))
month = int(input("Mes: "))
year = int(input("Año: "))
hour = int(input("Hora: "))
minute = int(input("Minutos: "))
fecha_usuario = datetime.datetime(year=year, month= month, day= day, hour=hour, minute=minute)

hoy = datetime.datetime.now()
diferencia_dias = fecha_usuario - hoy

print("Han pasado {} horas desde el dia {}.".format(int(diferencia_dias.total_seconds() / 3600), fecha_usuario.strftime("%d de %m del %Y")))

