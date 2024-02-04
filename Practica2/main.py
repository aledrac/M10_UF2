# main.py
from create_table import create_table_fun
from delete import delete_table_fun , delete_register
from conn import connection , conn
from create import insert_datos
from read import mostrar_datos
from update import actualizar_datos

def main():


    conn.cursor()
    
    option = input("¿Desea crear la tabla? (s/n): ").lower()

    if option == 's':
        # Crear la tabla si el usuario lo desea
        create_table_fun()
        print("Tabla creada correctamente.")

    while True:
        print("\n*** Menú ***")
        print("1. Insertar datos")
        print("2. Mostrar datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Eliminar tabla")
        print("6. Salir")

        choice = input("Seleccione una opción (1-6): ")


        if choice == '1':
            print("Opcion Insertar datos.")
           # Insertar datos en la tabla si el usuario lo desea
            insert_datos()

        elif choice == '2':
            print("Opcion Mostrar datos.")
           # muestra datosde la tabla si el usuario lo desea
            mostrar_datos()

        elif choice == '3':
            print("Opcion Actualizar datos.")
           # actualiza datos de la tabla si el usuario lo desea
            actualizar_datos()

        elif choice == '4':
            print("Opcion Eliminar datos.")
           # elimina datos de la tabla si el usuario lo desea
            delete_register()

        elif choice == '5':
            print("Opcion borrado Tabla.")
           # Eliminar la tabla si el usuario lo desea
            delete_table_fun()

        elif choice == '6':
           # Cerrar conexion
            conn.close()
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
