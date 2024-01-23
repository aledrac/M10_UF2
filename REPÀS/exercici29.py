
from mostrar_numeros import mostrar_numeros_enteros

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        mostrar_numeros_enteros(num1, num2)

    except ValueError:
        print("Error: Introduce números válidos.")

if __name__ == "__main__":
    main()
