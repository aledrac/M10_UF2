import random

numero_sec = random.randint(1, 100)
intentos = 0

with open("adivina_numero.txt", "w") as archivo:
    archivo.write(str(numero_sec))

while True:
    intento_user = int(input("Introduce un número entre 1 y 100: "))
    intentos += 1

    if intento_user == numero_sec:
        print(f"¡Has acertado! El número secreto era {numero_sec}. Necesitaste {intentos} intentos.")
        break
    elif intento_user < numero_sec:
        print("Demasiado pequeño. Inténtalo otra vez.")
    else:
        print("Demasiado grande. Un poco menos.")
