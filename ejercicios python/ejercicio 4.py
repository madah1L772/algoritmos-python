# Definir la tarifa fija por kilómetro indicada en el problema ($80.00 MXN)
COSTO_POR_KM = 80.0

# Solicitar los kilómetros a recorrer
km_recorrer = float(input("Ingrese los kilometros a recorrer: "))

# Calcular el costo total multiplicando los km por el costo unitario
costo_boleto = km_recorrer * COSTO_POR_KM

# Mostrar el precio final del viaje
print(f"El costo del boleto sencillo es: ${costo_boleto:.2f} MXN")

