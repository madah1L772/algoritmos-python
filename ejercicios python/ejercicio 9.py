# Solicitar la calificación de los tres exámenes
ex1 = float(input("Ingrese calificacion del examen 1: "))
ex2 = float(input("Ingrese calificacion del examen 2: "))
ex3 = float(input("Ingrese calificacion del examen 3: "))

# Aplicar las ponderaciones correspondientes (25%, 25% y 50%)
promedio = (ex1 * 0.25) + (ex2 * 0.25) + (ex3 * 0.50)

# Imprimir el promedio final ponderado
print(f"El promedio final del alumno es: {promedio:.2f}")

