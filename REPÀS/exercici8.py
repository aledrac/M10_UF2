num_palabras = int(input("Introduce el número de palabras (entre 1 y 3): "))

if 1 <= num_palabras <= 3:
    palabras = []

    for i in range(num_palabras):
        palabra = input(f"Introduce la palabra #{i + 1}: ")
        palabras.append(palabra)

    print("\nInformación sobre las palabras:")
    for palabra in palabras:
        print(f"Palabra: {palabra}")
        print(f"Número de caracteres: {len(palabra)}")
        print(f"Primer carácter: {palabra[0]}")
        print(f"Último carácter: {palabra[-1]}")
        print()
else:
    print("Número de palabras no válido. Debes introducir entre 1 y 3 palabras.")
