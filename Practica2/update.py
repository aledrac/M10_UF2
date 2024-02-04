# update.py
import psycopg2
from conn import connection, conn

def actualizar_datos():
    try:

        # Solicitar al usuario los valores
        id_val = input("Ingrese el ID: ")
        nombre_val = input("Ingrese el nuevo nombre: ")

        sql_update = f"""UPDATE public.direcciones SET nombre='{nombre_val}' WHERE id= {id_val} """

        connection.execute(sql_update)
        conn.commit()
        
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)

