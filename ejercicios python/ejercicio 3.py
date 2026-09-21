import math # Importar la librería math para la función ceil

# Solicitar las horas trabajadas/usadas (puede incluir decimales)
horas_uso = float(input("Ingrese la cantidad de horas estacionado: "))
precio_por_hora = float(input("Ingrese la tarifa por hora ($): "))

# Redondear hacia arriba cualquier fracción de hora usando math.ceil()
horas_a_cobrar = math.ceil(horas_uso)

# Calcular el costo total
total_pago = horas_a_cobrar * precio_por_hora

# Mostrar el cobro a realizar
print(f"Horas cobradas: {horas_a_cobrar} hrs. Total a pagar: ${total_pago:.2f} MXN")

