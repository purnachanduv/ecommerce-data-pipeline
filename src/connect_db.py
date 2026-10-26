import psycopg

try:
    with psycopg.connect(
        host="localhost",
        dbname="ecommerce_db",
        user="postgres",
        password=input("Enter PostgreSQL password: ")
    ) as connection:

        print("Database connection successful!")

        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM orders;")

            result = cursor.fetchone()

            print("Total orders:", result[0])

except Exception as error:
    print("Connection failed:", error)