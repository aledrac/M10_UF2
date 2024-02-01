# update.py
from connection import connection

def update_data(cursor, record_id, new_value):
    sql_update = f"UPDATE your_table_name SET field1 = %s WHERE id = %s"
    cursor.execute(sql_update, (new_value, record_id))
