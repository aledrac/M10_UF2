meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    numero_mes = int(input("Introduce un número entre 0 y 12 (pon 0 para finalizar): "))

    if numero_mes == 0:
        break

    if 1 <= numero_mes <= 12:
        print(f"El mes es: {meses[numero_mes - 1]}")
    else:
        print("Número no válido. Debes poner un número entre 1 y 12 o 0 para finalizar.")
