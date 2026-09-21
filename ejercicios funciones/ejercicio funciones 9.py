# Función para clasificar el signo de un número
def obtener_signo(numero):
    # Clasificación mediante ramas if, elif y else
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# Pruebas requeridas
print(obtener_signo(12)) # "Positivo"
print(obtener_signo(-8)) # "Negativo"
print(obtener_signo(0))  # "Cero"

