import psycopg2

# Database connection parameters
DB_HOST = "haproxy"  # Assuming HAProxy is routing to the read-only DB
DB_PORT = 5432       # PostgreSQL port
DB_NAME = "postgres" # Database name
DB_USER = "odoo"     # Username
DB_PASSWORD = "odoo"  # Password

try:
    # Establish connection
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    connection.set_session(readonly=True)  # Force read-only mode

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SELECT query
    cursor.execute("SELECT * FROM some_table LIMIT 10;")
    rows = cursor.fetchall()

    # Print the fetched rows
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
