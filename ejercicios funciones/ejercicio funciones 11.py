# Función para encontrar el mayor de tres números usando operadores lógicos y >=
def mayor_de_tres(a, b, c):
    # Evalúa si a es mayor o igual a b y c
    if a >= b and a >= c:
        return a
    # Evalúa si b es mayor o igual a a y c
    elif b >= a and b >= c:
        return b
    # Si las condiciones anteriores no se cumplen, c es el mayor
    else:
        return c

# Pruebas requeridas
print(mayor_de_tres(5, 12, 9)) # 12
print(mayor_de_tres(20, 3, 1)) # 20
print(mayor_de_tres(4, 4, 4))   # 4

