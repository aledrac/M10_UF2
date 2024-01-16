palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

tupla_palabras = (palabra1, palabra2)

frecuencia_letras = {}
for palabra in tupla_palabras:
    for letra in palabra:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1

print("Frecuencia de cada letra:")
for letra, frecuencia in frecuencia_letras.items():
    print(f"{letra}: {frecuencia} veces")
