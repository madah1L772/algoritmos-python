from datetime import datetime

# Solicitar el año de nacimiento del aspirante
anio_nacimiento = int(input("Ingrese el ano de nacimiento: "))

# Obtener el año actual del sistema automáticamente
anio_actual = datetime.now().year

# Calcular la edad restando los años
edad = anio_actual - anio_nacimiento

# Mostrar la edad calculada
print(f"La persona tiene {edad} anos.")

