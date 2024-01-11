numero_usuario = int(input("Introduce un número del 1 al 10: "))

if 1 <= numero_usuario <= 10:
    print(f"Tabla de multiplicar del {numero_usuario}:")
    for i in range(1, 11):
        resultado = numero_usuario * i
        print(resultado, end=' ')
else:
    print("El número no vale. Tienes que ingresar un número entre 1 y 10.")
