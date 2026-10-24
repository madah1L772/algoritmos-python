# ejercicio 19: Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo
salario = 1500.0
# Ciclo para calcular el salario durante los 6 años siguientes
for anio in range(1, 7):
    # Aplicamos un incremento del 10% anual al salario actual
    salario = salario + (salario * 0.10)
    print(f"Salario al año {anio}: ${salario:.2f}")

