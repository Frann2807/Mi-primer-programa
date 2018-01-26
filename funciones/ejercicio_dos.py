"""
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).
"""

def rango (primero, minimo, maximo):
    if primero >= minimo and primero <= maximo:
        valor_rango = True
    else:
        valor_rango = False
    return valor_rango

print(rango(101, 1, 100))

