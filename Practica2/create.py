import psycopg2
from conn import connection,conn

def insert_datos():
    try:

        # Solicitar al usuario los valores
        id_val = input("Ingrese el ID: ")
        direccion_val = input("Ingrese la dirección: ")
        nombre_val = input("Ingrese el nombre: ")
        cod_postal_val = input("Ingrese el código postal: ")
        num_tel_val = input("Ingrese el número de teléfono: ")
        poblacion_val = input("Ingrese la población: ")
        pais_val = input("Ingrese el país: ")

        # Construir la consulta SQL con los valores ingresados
        sql_insert = f'''
            INSERT INTO public.direcciones(id, dirección, nombre, cod_postal, num_tel, poblacion, pais)
            VALUES({id_val}, '{direccion_val}', '{nombre_val}', {cod_postal_val}, {num_tel_val}, '{poblacion_val}', '{pais_val}')
        '''

        # Ejecutar la consulta SQL
        connection.execute(sql_insert)
        conn.commit()
        print("Datos insertados correctamente.")
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)