import os
import psycopg2

def get_connection():
    db_host = os.environ.get("PGHOST")
    db_name = os.environ.get("PGDATABASE")
    db_user = os.environ.get("PGUSER")
    db_password = os.environ.get("PGPASSWORD")


    connection = psycopg2.connect(
        host = db_host,
        database = db_name,
        user = db_user,
        password = db_password)
    return connection

def execute_query(query, params=None, returning_columns=None):
    connection = get_connection()
    cursor = connection.cursor()
    
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    if returning_columns:
        result = cursor.fetchone() if cursor.rowcount > 0 else None
        if result:
            data = {column: result[i]
                    for i, column in enumerate(returning_columns)}
        else:
            data = None
    else:
        data = None
    
    connection.commit()
    connection.close()

    return data


def fetch_data(query, params=None):
    connection = get_connection()
    cursor = connection.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    data = cursor.fetchall()

    connection.close()

    return data