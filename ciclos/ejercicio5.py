# ejercicio 5: Crea un programa que recorra los númerosdel 1 al 20 e imprima únicamente aquellosque sean pares, indicando al final cuántos números pares se encontraron en total.
pares = []
# Recorremos los números enteros del 1 al 20
for i in range(1, 21):
    if i % 2 == 0:
        pares.append(i)
print("Números pares:", pares)
print("Total de pares:", len(pares))

