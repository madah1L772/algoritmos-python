# Función para realizar operaciones aritméticas básicas por nombre
def operacion_basica(a, b, operacion):
    # Evalúa la cadena recibida para aplicar la operación correspondiente
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplica":
        return a * b
    else:
        # Retorna mensaje de error si la operación no coincide
        return "Operación no válida"

# Pruebas requeridas
print(operacion_basica(6, 4, "resta"))       # 2
print(operacion_basica(5, 3, "multiplica"))  # 15
print(operacion_basica(10, 2, "raiz"))       # "Operación no válida"

