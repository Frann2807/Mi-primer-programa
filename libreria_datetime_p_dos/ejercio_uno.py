"""
Añadir la opcion de "Quizas" Al programa
"""

import datetime
import random

def dia_semana(fecha):
    dias_semana = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Vienes", 5: "Sabado", 6: "Domingo"}
    dia = fecha.weekday()
    return dias_semana[dia]

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not_or_someting(message):
    response = None
    while response != "Si" and response != "No" and response != "A veces":
        response = input(message + " (Si/No/A veces)")
    return response

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 5
DRINKER_PENALIZATION = 5
SEDENTARY_PENALIZATION = 8
EAT_BAD = 8

print_with_underscores("¡Averigua cuanto te queda de vida!")

print("Completa esta encuesta para saber cuanto tiempo te queda.")

birth_date = input("¿Cual fue tu dia de nacimiento? (formato: dd/mm/yyyy): ")
datetime.datetime.now()
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

years_lost = 0

eat = ask_yes_or_not_or_someting("¿Comes saludable?")

if eat == "No":
    years_lost += EAT_BAD
elif eat == "A veces":
    years_lost += EAT_BAD/2

smoker = ask_yes_or_not_or_someting("¿Fumas?")

if smoker == "Si":
    years_lost += SMOKER_PENALIZATION
elif smoker == "A veces":
    years_lost += SMOKER_PENALIZATION/2

drinker = ask_yes_or_not_or_someting("¿Bebes?")

if drinker == "Si":
    years_lost += DRINKER_PENALIZATION
elif drinker == "A veces":
    years_lost += DRINKER_PENALIZATION/2

sedentary = ask_yes_or_not_or_someting("¿Haces deportes?")

if sedentary == "No":
    years_lost += SEDENTARY_PENALIZATION
elif sedentary == "A veces":
    years_lost += SEDENTARY_PENALIZATION/2

base_lifespan = random.randint(AVERAGE_LIFESPAN/2, AVERAGE_LIFESPAN)

lifespan = base_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan*365)
days_to_death = death_day - datetime.datetime.now()
print("Fecha de tu muerte: {}".format(death_day.strftime("%d/%m/%Y")))
print("Te quedan {} dias para morir.".format(days_to_death.days))