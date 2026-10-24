# ejercicio 4: Pide al usuario que ingrese N númerosenteros enteros uno por uno. Al finalizar lalectura, muestra la suma total de todos los números ingresados.
n = int(input("¿Cuántos números desea ingresar? "))
suma_total = 0
# Bucle que se ejecuta N veces según el valor ingresado
for i in range(n):
    num = int(input("Ingrese un número: "))
    suma_total += num
print("La suma total es:", suma_total)

