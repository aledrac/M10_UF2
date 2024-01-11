palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if len(palabra1) >= 2 and len(palabra2) >= 2:
    nueva_palabra1 = palabra2[:2] + palabra1[2:]
    nueva_palabra2 = palabra1[:2] + palabra2[2:]
    print(f"{nueva_palabra1} {nueva_palabra2}")
else:
    print("Las palabras deben tener al menos dos caracteres cada una.")
