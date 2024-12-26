import psycopg2

# Database connection parameters
DB_HOST = "54.169.254.130"  # Assuming HAProxy is routing to the read-only DB
DB_PORT = 5433       # PostgreSQL port
DB_NAME = "postgres" # Database name
DB_USER = "odoo"     # Username
DB_PASSWORD = "odoo"  # Password


def get_connection(host, port, db_name, user, password):
    """Establish connection to the database."""
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=db_name,
            user=user,
            password=password
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def set_readonly_mode(connection):
    """Set the database session to read-only mode."""
    try:
        cursor = connection.cursor()
        cursor.execute("SET default_transaction_read_only = true;")
        cursor.close()
    except psycopg2.Error as e:
        print("Error setting session to read-only:", e)


def fetch_data(connection):
    """Fetch data from a table."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM some_table LIMIT 10;")
        rows = cursor.fetchall()
        return rows
    except psycopg2.Error as e:
        print("Error fetching data:", e)
        return []


if __name__ == "__main__":
    """Main function to handle database connection and data retrieval."""
    # Establish connection
    connection = get_connection(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)

    if connection:
        # Set the session to read-only mode
        set_readonly_mode(connection)

        # Fetch data
        rows = fetch_data(connection)

        # Print the fetched rows
        if rows:
            for row in rows:
                print(row)

        # Close the connection
        connection.close()
