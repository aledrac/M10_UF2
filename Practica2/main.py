from connection import connection
from create_table import create_table
from create import insert_data
from read import select_data
from update import update_data
from delete import delete_data

def main():
    create_table_option = input("¿Desea crear la tabla? (s/n): ").lower()

    if create_table_option == 's':
        # Crear la tabla si el usuario lo desea
        cursor = connection.cursor()
        create_table(cursor)
        connection.commit()
        cursor.close() 
        print("Tabla creada correctamente.")

    while True:
        print("\n*** Menú ***")
        print("1. Insertar datos")
        print("2. Mostrar datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            # Insertar datos
            field1 = input("Ingrese el valor para field1: ")
            field2 = input("Ingrese el valor para field2: ")
            field3 = input("Ingrese el valor para field3: ")
            field4 = input("Ingrese el valor para field4: ")
            field5 = input("Ingrese el valor para field5: ")
            field6 = input("Ingrese el valor para field6: ")
            insert_data(connection.cursor(), field1, field2, field3, field4, field5, field6)
            connection.commit()
            print("Datos insertados correctamente.")

        elif choice == '2':
            # Mostrar datos
            print("\nDatos en la tabla:")
            select_data(connection.cursor())

        elif choice == '3':
            # Actualizar datos
            record_id = input("Ingrese el ID del registro que desea actualizar: ")
            new_value = input("Ingrese el nuevo valor para field1: ")
            update_data(connection.cursor(), record_id, new_value)
            connection.commit()
            print("Datos actualizados correctamente.")

        elif choice == '4':
            # Eliminar datos
            record_id = input("Ingrese el ID del registro que desea eliminar: ")
            delete_data(connection.cursor(), record_id)
            connection.commit()
            print("Datos eliminados correctamente.")

        elif choice == '5':
            # Salir del programa
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
