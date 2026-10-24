# ejercicio 18: Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.
total_horas = 0
for i in range(1, 7):
    horas = float(input(f"Horas trabajadas el día {i}: "))
    total_horas += horas
pago_hora = float(input("Ingrese el pago por hora: "))
sueldo_total = total_horas * pago_hora
print("Total de horas:", total_horas, "| Sueldo total: $", sueldo_total)

