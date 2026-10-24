# ejercicio 16: Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere saber cuántas de ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a $1000, y cuántas fueron menores o iguales a $500. Además, se requiere saber el monto de lo vendido en cada categoría y de forma global. Realice un algoritmo que permita determinar lo anterior
n = int(input("Total de ventas del día: "))
v_bajas, v_medias, v_altas = [], [], []
for i in range(n):
    venta = float(input("Monto de la venta: "))
    if venta <= 500: v_bajas.append(venta)
    elif venta <= 1000: v_medias.append(venta)
    else: v_altas.append(venta)
print("<=500:", len(v_bajas), "ventas, Monto:", sum(v_bajas))
print("501-1000:", len(v_medias), "ventas, Monto:", sum(v_medias))
print(">1000:", len(v_altas), "ventas, Monto:", sum(v_altas))
print("Monto global:", sum(v_bajas) + sum(v_medias) + sum(v_altas))

