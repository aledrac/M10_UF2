# create_table.py
def create_table(cursor):
    sql = '''
    CREATE TABLE IF NOT EXISTS buenastardes (
        id SERIAL PRIMARY KEY,
        field1 VARCHAR(255) NOT NULL,
        field2 VARCHAR(255) NOT NULL,
        field3 INT NOT NULL,
        field4 VARCHAR(255) NOT NULL,
        field5 INT NOT NULL,
        field6 VARCHAR(255) NOT NULL
    )
    '''
    cursor.execute(sql)
