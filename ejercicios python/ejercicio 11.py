# Definición de la función para encontrar el número mayor entre tres valores
def mayor_de_tres(a, b, c):
    # Comparar los tres números mediante condicionales
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Solicitar las tres cantidades al usuario
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

# Llamar a la función pasando las variables ingresadas como argumentos
resultado_mayor = mayor_de_tres(n1, n2, n3)

# Imprimir el resultado obtenido
print(f"El numero mayor de los tres es: {resultado_mayor}")

