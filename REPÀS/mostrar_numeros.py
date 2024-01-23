
def mostrar_numeros_enteros(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1  # Intercambiar los números si están en orden inverso

    numeros_enteros = list(range(int(num1) + 1, int(num2)))
    suma_numeros = sum(numeros_enteros)

    print(f"Números enteros entre {num1} y {num2}: {numeros_enteros}")
    print(f"Suma de los números enteros: {suma_numeros}")
