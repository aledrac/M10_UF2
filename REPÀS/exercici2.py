valor_euros = float(input("Introduce el valor en euros: "))
porcentaje_iva = float(input("Introduce el porcentaje de IVA (4%, 10% o 21%): "))
valor_final = valor_euros * (1 + porcentaje_iva / 100)


print(f"\nValor final con IVA: {valor_final:.2f} euros")
