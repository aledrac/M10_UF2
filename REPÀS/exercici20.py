diccionario_contactos = {}

while True:
    nombre = input("Introduce un nombre (o escribe 'no' para dejar de agregar contactos): ")

    if nombre.lower() == 'no':
        break

    if nombre in diccionario_contactos:
        print("¡Error! Este nombre ya está en el diccionario. No se añadirá de nuevo.")
    else:
        edad = input("Introduce la edad: ")
        diccionario_contactos[nombre] = int(edad)

print("Diccionario de contactos:")
print(diccionario_contactos)
