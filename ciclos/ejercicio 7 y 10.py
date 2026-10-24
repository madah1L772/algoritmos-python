# ejercicio 7: Un sensor en la puerta de una discotecaregistra la edad de 8 personas que intentanentrar. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
# ejercicio 10: Una discoteca tiene 8 personas registradas. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
menores = 0
# Iteramos para registrar la edad de 8 personas
for i in range(1, 9):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    if edad < 18:
        menores += 1
print("Total de menores de edad:", menores)

