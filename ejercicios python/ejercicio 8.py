# Solicitar el precio original del traje
precio_traje = float(input("Ingrese el precio del traje ($): "))

# Evaluar la condición del precio para determinar el porcentaje de descuento
if precio_traje > 2500.0:
    porcentaje_descuento = 0.15  # 15% para precios mayores a $2500
else:
    porcentaje_descuento = 0.08  # 8% para los demás casos

# Calcular el valor monetario del descuento y el precio neto
monto_descuento = precio_traje * porcentaje_descuento
precio_final = precio_traje - monto_descuento

# Desplegar los resultados requeridos
print(f"Descuento obtenido: ${monto_descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")

