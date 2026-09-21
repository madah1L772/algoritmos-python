# Definir la tarifa por minuto especificada ($3.00 MXN)
COSTO_POR_MINUTO = 3.0

# Solicitar los minutos que duró la llamada
minutos = float(input("Ingrese la duracion de la llamada en minutos: "))

# Calcular el costo total multiplicando la duración por el costo fijo
total_llamada = minutos * COSTO_POR_MINUTO

# Mostrar el total a pagar
print(f"El costo de la llamada es: ${total_llamada:.2f} MXN")

