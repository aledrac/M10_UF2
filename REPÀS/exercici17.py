frase_usuario = input("Introduce una frase: ")

frase_sin_espacios = tuple(frase_usuario.replace(" ", ""))
frase_sin_repetidos = tuple(set(frase_sin_espacios))

print(f"Tupla sin espacios y sin caracteres repetidos: {frase_sin_repetidos}")
