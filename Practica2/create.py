# create.py
from connection import connection

def insert_data(cursor, field1, field2, field3, field4, field5, field6):
    sql_insert = '''
    INSERT INTO your_table_name(field1, field2, field3, field4, field5, field6) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(sql_insert, (field1, field2, field3, field4, field5, field6))
