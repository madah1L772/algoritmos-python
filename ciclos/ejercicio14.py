# ejercicio 14: Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero
n = int(input("Ingrese la cantidad de números: "))
mayores = 0
menores_iguales = 0
for i in range(n):
    val = float(input("Ingrese un valor: "))
    if val > 0: mayores += 1
    else: menores_iguales += 1
print("Mayores a 0:", mayores)
print("Menores o iguales a 0:", menores_iguales)

