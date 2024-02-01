# read.py
def select_data(cursor):
    sql_select = "SELECT * FROM your_table_name"
    cursor.execute(sql_select)
    result = cursor.fetchall()

    if not result:
        print("No hay datos en la tabla.")
    else:
        for row in result:
            print(row)
