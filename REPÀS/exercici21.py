entrada_usuario = input("Introduce 10 números separados por espacios: ")
numeros = [float(x) for x in entrada_usuario.split()]
suma_total = sum(numeros)
media = suma_total / len(numeros)
numeros.extend([f"suma total: {suma_total}", f"media: {media}"])
print("Números del usuario:")
print(numeros)
