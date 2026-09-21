# Función para calcular el área de un triángulo con validación
def area_triangulo(base, altura):
    # Valida que ambos parámetros sean estrictamente mayores a cero
    if base > 0 and altura > 0:
        # Aplica la fórmula (base * altura) / 2
        return (base * altura) / 2.0
    else:
        # Retorna 0 si algún valor no es válido
        return 0

# Pruebas requeridas
print(area_triangulo(10, 5)) # 25.0
print(area_triangulo(7, 4))  # 14.0
print(area_triangulo(-2, 5)) # 0

