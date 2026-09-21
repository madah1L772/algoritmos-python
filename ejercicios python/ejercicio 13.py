# Solicitar la duración en minutos de la llamada
minutos = float(input("Ingrese el tiempo de la llamada en minutos: "))

# Variables para desglosar el costo según cada tramo tarifario
costo_primeros_5 = 0.0
costo_siguientes_3 = 0.0
costo_siguientes_2 = 0.0
costo_resto = 0.0

# Tramo 1: Primeros 5 minutos ($1.00 c/u)
if minutos > 0:
    m1 = min(minutos, 5.0)
    costo_primeros_5 = m1 * 1.00

# Tramo 2: Del minuto 6 al 8 ($0.80 c/u)
if minutos > 5:
    m2 = min(minutos - 5.0, 3.0)
    costo_siguientes_3 = m2 * 0.80

# Tramo 3: Del minuto 9 al 10 ($0.70 c/u)
if minutos > 8:
    m3 = min(minutos - 8.0, 2.0)
    costo_siguientes_2 = m3 * 0.70

# Tramo 4: A partir del minuto 10 en adelante ($0.50 c/u)
if minutos > 10:
    m4 = minutos - 10.0
    costo_resto = m4 * 0.50

# Sumar los subtotales para obtener el costo total
subtotal = costo_primeros_5 + costo_siguientes_3 + costo_siguientes_2 + costo_resto

# Mostrar desglose por cada concepto exigido
print("\n<<< DESGLOSE DE COBRO >>>")
print(f"Primeros 5 min ($1.00 c/u): ${costo_primeros_5:.2f}")
print(f"Siguientes 3 min ($0.80 c/u): ${costo_siguientes_3:.2f}")
print(f"Siguientes 2 min ($0.70 c/u): ${costo_siguientes_2:.2f}")
print(f"Minutos restantes ($0.50 c/u): ${costo_resto:.2f}")
print(f"Total a pagar: ${subtotal:.2f} MXN")

