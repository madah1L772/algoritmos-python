# ejercicio 2: Mostrar la tabla de multiplicar de un n numero ingresado por teclado.
# Solicitamos al usuario que ingrese un número entero por teclado
n = int(input("Ingrese un número: "))
# Recorremos del 1 al 10 para generar la tabla
for i in range(1, 11):
    resultado = n * i
    print(n, "x", i, "=", resultado)

