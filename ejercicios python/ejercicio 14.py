# Solicitar tiempo de llamada, día y turno
minutos = float(input("Ingrese la duracion de la llamada en minutos: "))
dia = input("Ingrese el dia de la semana (ej. Domingo, Lunes, etc.): ").strip().lower()

# Calcular la base imponible por la duración de la llamada (mismo esquema del problema 13)
c1 = min(minutos, 5.0) * 1.00 if minutos > 0 else 0.0
c2 = min(max(minutos - 5.0, 0.0), 3.0) * 0.80
c3 = min(max(minutos - 8.0, 0.0), 2.0) * 0.70
c4 = max(minutos - 10.0, 0.0) * 0.50

subtotal_llamada = c1 + c2 + c3 + c4

# Determinar la tasa de impuesto aplicable según el día y turno
if dia == "domingo":
    porcentaje_impuesto = 0.03  # Impuesto de 3% si es domingo
    turno = "N/A"
else:  # Día hábil
    turno = input("Ingrese el turno (matutino / vespertino): ").strip().lower()
    if turno == "matutino":
        porcentaje_impuesto = 0.15  # Impuesto del 15%
    elif turno == "vespertino":
        porcentaje_impuesto = 0.10  # Impuesto del 10%
    else:
        porcentaje_impuesto = 0.0

# Calcular el impuesto y el total final
monto_impuesto = subtotal_llamada * porcentaje_impuesto
total_pago = subtotal_llamada + monto_impuesto

# Desplegar los valores de cada concepto de cobro
print("\n<<< DESGLOSE FINAL DE COBRO >>>")
print(f"Subtotal de llamada: ${subtotal_llamada:.2f}")
print(f"Impuesto aplicado ({int(porcentaje_impuesto*100)}%): ${monto_impuesto:.2f}")
print(f"Total final a pagar: ${total_pago:.2f} MXN")

