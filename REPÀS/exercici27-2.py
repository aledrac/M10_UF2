
from calculadora import suma_dos_numeros

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = suma_dos_numeros(num1, num2)
        print(f"El resultado de la suma es: {resultado}")

    except ValueError:
        print("Error: Introduce números válidos.")

if __name__ == "__main__":
    main()
