import datetime

def dia_semana(fecha):
    dias_semana = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Vienes", 5: "Sabado", 6: "Domingo"}
    dia = fecha.weekday()
    return dias_semana[dia]

day = int(input("Dia: "))
month = int(input("Mes: "))
year = int(input("Año: "))

fecha_usuario = datetime.datetime(year=year, month=month, day=day)

print("La fecha {} cae un dia {}.".format(fecha_usuario.strftime("%d de %m del %Y"), dia_semana(fecha_usuario)))
