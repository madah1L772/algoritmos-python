# ejercicio 20: Una compañía fabrica focos de colores (verdes, blancos y rojos). Se desea contabilizar, de un lote de N focos, el número de focos de cada color que hay en existencia.
n = int(input("Total de focos en el lote: "))
verdes, blancos, rojos = 0, 0, 0
for i in range(n):
    color = input(f"Color del foco {i+1} (verde/blanco/rojo): ").strip().lower()
    if color == "verde": verdes += 1
    elif color == "blanco": blancos += 1
    elif color == "rojo": rojos += 1
print("Verdes:", verdes, "| Blancos:", blancos, "| Rojos:", rojos)

