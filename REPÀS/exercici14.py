entrada_usuario = input("Introduce 10 números separados por espacio: ")

numeros = [int(x) for x in entrada_usuario.split()]

tupla_ordenada = tuple(sorted(numeros))

print(f"Tupla ordenada de menor a mayor: {tupla_ordenada}")
