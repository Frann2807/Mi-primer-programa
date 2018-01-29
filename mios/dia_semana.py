def dia_semana(fecha):
    dias_semana = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Vienes", 5: "Sabado", 6: "Domingo"}
    dia = fecha.weekday()
    return dias_semana[dia]
