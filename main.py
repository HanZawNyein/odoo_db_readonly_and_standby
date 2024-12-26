import psycopg2

# Connection details
pgbouncer_host = "innovixacademy.com"  # The hostname or IP address of the PgBouncer service
pgbouncer_port = "6432"  # The port PgBouncer is listening on (default is 6432)
dbname = "standby"  # Database name defined in the PgBouncer configuration
user = "odoo"  # Your PostgreSQL user
password = "odoo"  # Your PostgreSQL password

# Create a connection to the standby database through PgBouncer
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=pgbouncer_host,
    port=pgbouncer_port
)

# Create a cursor to perform database operations
cursor = conn.cursor()

# Example: Perform a read-only query
cursor.execute("SELECT * FROM your_table LIMIT 10;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
