# create_table.py
from conn import connection,conn

def create_table_fun():
    sql = '''
        CREATE TABLE DIRECCIONES (
            id SERIAL PRIMARY KEY,
            dirección VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            cod_postal INT NOT NULL,
            num_tel INT NOT NULL,
            poblacion VARCHAR(255) NOT NULL,
            pais VARCHAR(255) NOT NULL
        )
        '''
    print(sql)
    connection.execute(sql)
    print(connection)
    conn.commit()
    
