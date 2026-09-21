# Menú interactivo de selección de productos
print("--- MENU DE PRODUCTOS ---")
print("1. Laptop ($15,000.00)")
print("2. Smartphone ($8,000.00)")
opcion = int(input("Seleccione un producto (1 o 2): "))

# Asignar nombre y precio base según la opción elegida
if opcion == 1:
    producto = "Laptop"
    precio = 15000.0
elif opcion == 2:
    producto = "Smartphone"
    precio = 8000.0
else:
    producto = "Generico"
    precio = 1000.0

# Calcular el descuento del 20% y el precio ajustado
descuento = precio * 0.20
precio_con_descuento = precio - descuento

# Calcular el IVA del 15% sobre el precio con descuento
iva = precio_con_descuento * 0.15
precio_final = precio_con_descuento + iva

# Desplegar la información completa
print(f"\n--- RESUMEN DE COMPRA ---")
print(f"Producto: {producto}")
print(f"Precio original: ${precio:.2f}")
print(f"Precio con descuento (20%): ${precio_con_descuento:.2f}")
print(f"Precio final (con IVA 15%): ${precio_final:.2f}")

