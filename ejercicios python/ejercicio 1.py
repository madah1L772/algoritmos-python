# Solicitar al usuario la cantidad en pesos mexicanos y el tipo de cambio actual
pesos = float(input("Ingrese la cantidad de pesos mexicanos (MXN): "))
tipo_cambio = float(input("Ingrese el tipo de cambio del dolar en MXN: "))

# Calcular la cantidad equivalente en dolares
dolares = pesos / tipo_cambio

# Mostrar el resultado final
print(f"Con ${pesos:.2f} MXN puedes comprar ${dolares:.2f} USD.")

