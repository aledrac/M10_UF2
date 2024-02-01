# delete.py
from connection import connection

def delete_data(cursor, record_id):
    sql_delete = "DELETE FROM your_table_name WHERE id = %s"
    cursor.execute(sql_delete, (record_id,))
