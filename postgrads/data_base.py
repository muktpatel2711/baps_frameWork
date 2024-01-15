import psycopg2

db_name = 'your_database'
user = 'your_username'
password = 'your_password'
host = 'localhost'
port = '5432'

# Connect to the default 'postgres' database to create a new database
connection_params = {
    'dbname': 'postgres',
    'user': user,
    'password': password,
    'host': host,
    'port': port,
}

with psycopg2.connect(**connection_params) as connection:
    # Create a cursor
    cursor = connection.cursor()

    # Create a new database
    cursor.execute(f"CREATE DATABASE {db_name}")

    # Commit the changes
    connection.commit()

# Connect to the newly created database
connection_params['dbname'] = db_name
with psycopg2.connect(**connection_params) as connection:
    # Create a cursor
    cursor = connection.cursor()

    # Create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS my_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER
    )
    '''

    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()
