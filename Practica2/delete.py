# delete.py
import psycopg2
from conn import connection, conn

def delete_table_fun():
    try:
        # Eliminar la tabla direcciones
        sql_delete_table = """DROP TABLE IF EXISTS public.direcciones"""
        connection.execute(sql_delete_table)
        conn.commit()
        print("Tabla 'direcciones' eliminada correctamente.")
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)

def delete_register():
    try:
         # Solicitar al usuario los valores
        id_val = input("Ingrese el ID: ")

        sql_delete = f"""DELETE FROM public.direcciones WHERE id = {id_val}"""

        connection.execute(sql_delete)
        conn.commit()

    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
