# ejercicio 15: Realice un algoritmo para generar e imprimir los números pares que se encuentran entre 0 y 100.
pares = []
# Generamos los números con saltos de 2 en 2 desde 0 hasta 100
for i in range(0, 101, 2):
    pares.append(i)
print("Números pares del 0 al 100:")
print(pares)

