# Función para determinar la mayoría de edad
def es_mayor_de_edad(edad):
    # Verifica si la edad es mayor o igual a 18
    if edad >= 18:
        return "Mayor"
    else:
        return "Menor"

# Pruebas requeridas
print(es_mayor_de_edad(17)) # "Menor"
print(es_mayor_de_edad(18)) # "Mayor"
print(es_mayor_de_edad(45)) # "Mayor"

