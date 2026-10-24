# ejercicio 9: Revisa la entrada de peso de 10 maletas en un ciclo y cuenta cuántas superan el límite de 23 kg.
# ejercicio 11: Revisa en un ciclo el peso registrado de 10 maletas y cuenta cuántas superan el límite de 23 kg.
contador_pesadas = 0
# Recorremos el peso de las 10 maletas en un ciclo
for i in range(1, 11):
    peso = float(input(f"Ingrese el peso de la maleta {i} (kg): "))
    if peso > 23:
        contador_pesadas += 1
print("Maletas que superan 23 kg:", contador_pesadas)

