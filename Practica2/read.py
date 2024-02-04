# read.py
import psycopg2
from conn import connection,conn

def mostrar_datos():
    try:

        # Solicitar id al usuario 
        id_val = input("Ingrese el ID a buscar: ")

        sql_select = f'''SELECT * FROM public.direcciones where id = {id_val}'''

        connection.execute(sql_select)
        # conn.commit()
        result = connection.fetchall()

        for i in result:
            print("id: " , i[0],)
            print("nombre:", i[1],)
            print("direccion: ", i[2], "\n")

    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)

