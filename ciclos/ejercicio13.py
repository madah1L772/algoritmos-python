# ejercicio 13: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.
ahorros = []
# Registramos el depósito de cada uno de los 12 meses del año
for i in range(1, 13):
    monto = float(input(f"Ingrese el ahorro del mes {i}: "))
    ahorros.append(monto)
    print(f"Lleva ahorrado hasta el mes {i}: ${sum(ahorros)}")
print("Ahorro total en el año:", sum(ahorros))

