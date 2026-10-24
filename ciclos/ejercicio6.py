# ejercicio 6: Diseñe una aplicación que permita ingresar nnúmeros y muestre y sume los números pares.
n = int(input("Cantidad de números: "))
pares = []
for i in range(n):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares.append(num)
print("Pares ingresados:", pares)
print("Suma de los pares:", sum(pares))

