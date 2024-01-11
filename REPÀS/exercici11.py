numero_usuario = int(input("Introduce un número entre 10 y 100: "))

if 10 <= numero_usuario <= 100:
    numeros_tupla = tuple(range(1, numero_usuario + 1))
    print(numeros_tupla)
else:
    print("Número no válido. Debes introducir un número entre 10 y 100.")
