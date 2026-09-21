# Solicitar la cantidad de lápices requeridos
cantidad = int(input("Ingrese la cantidad de lapices a comprar: "))

# Determinar precio unitario en función del volumen
if cantidad >= 1000:
    precio_unitario = 0.85
else:
    precio_unitario = 0.90

# Calcular el precio total
total = cantidad * precio_unitario

# Desplegar el importe total a pagar
print(f"Precio por lapiz: ${precio_unitario:.2f}")
print(f"Total a pagar por {cantidad} lapices: ${total:.2f}")

