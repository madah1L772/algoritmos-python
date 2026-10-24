# ejercicio 12: Realizar un algoritmo que pida N números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
n = int(input("¿Cuántos números va a ingresar? "))
mayores, menores, ceros = 0, 0, 0
for i in range(n):
    num = int(input("Ingrese un número: "))
    if num > 0: mayores += 1
    elif num < 0: menores += 1
    else: ceros += 1
print("Mayores a 0:", mayores, "| Menores a 0:", menores, "| Ceros:", ceros)

