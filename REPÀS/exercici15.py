numeros = []

while True:
    entrada_usuario = input("Introduce un número (o 0 para terminar): ")
    numero = int(entrada_usuario)

    if numero == 0:
        break

    numeros.append(numero)

tupla_ordenada = tuple(sorted(numeros))

print(f"Tupla ordenada de menor a mayor: {tupla_ordenada}")
