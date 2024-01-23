from generador_aleatorio import numero_aleatorio_entre

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        numero_aleatorio = numero_aleatorio_entre(num1, num2)
        print(f"Número aleatorio entre {num1} y {num2}: {numero_aleatorio}")

    except ValueError:
        print("Error: Introduce números válidos.")

if __name__ == "__main__":
    main()
