# Solicitar el número total de alumnos participantes
num_alumnos = int(input("Ingrese el numero de alumnos que iran al viaje: "))

# Evaluar rangos de alumnos para aplicar las reglas de cobro
if num_alumnos >= 100:
    costo_alumno = 65.0
    costo_autobus = num_alumnos * costo_alumno
elif 50 <= num_alumnos <= 99:
    costo_alumno = 70.0
    costo_autobus = num_alumnos * costo_alumno
elif 30 <= num_alumnos <= 49:
    costo_alumno = 95.0
    costo_autobus = num_alumnos * costo_alumno
else:  # Menos de 30 alumnos
    costo_autobus = 4000.0  # Renta fija
    costo_alumno = costo_autobus / num_alumnos  # Se divide el costo fijo entre los alumnos

# Mostrar el pago por alumno y el pago total a la compañía
print(f"Costo por alumno: ${costo_alumno:.2f}")
print(f"Pago total a la compañia de viajes: ${costo_autobus:.2f}")

