# ejercicio 3: Pide al usuario que ingrese 5 númerosenteros uno por uno. Al finalizar la lectura,muestra la suma total de todos los números ingresados.
suma_total = 0
# Creamos un ciclo que se repita exactamente 5 veces
for i in range(1, 6):
    num = int(input(f"Ingrese el número {i}: "))
    suma_total += num
print("La suma total es:", suma_total)


