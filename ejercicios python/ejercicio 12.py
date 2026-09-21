# Solicitar la cantidad de asistentes al evento
personas = int(input("Ingrese la cantidad de personas para el banquete: "))

# Determinar el costo por platillo de acuerdo al volumen de asistentes
if personas > 300:
    costo_platillo = 75.0
elif personas > 200:
    costo_platillo = 85.0
else:
    costo_platillo = 95.0

# Calcular el presupuesto total
presupuesto = personas * costo_platillo

# Mostrar el costo por platillo y el total estimado
print(f"Costo por platillo: ${costo_platillo:.2f}")
print(f"Presupuesto total para el evento: ${presupuesto:.2f}")

