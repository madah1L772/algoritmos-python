# Función para comparar dos valores sin usar max()
def mayor_de_dos(a, b):
    # Evalúa si a es mayor que b; de lo contrario, b es el mayor o igual
    if a > b:
        return a
    else:
        return b

# Pruebas requeridas
print(mayor_de_dos(15, 27))  # 27
print(mayor_de_dos(40, -10)) # 40
print(mayor_de_dos(8, 8))    # 8

