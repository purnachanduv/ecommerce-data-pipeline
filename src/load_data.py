import csv
import psycopg
from pathlib import Path
from decimal import Decimal

project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "cleaned_orders.csv"

with psycopg.connect(
host="localhost",
dbname="ecommerce_db",
user="postgres",
password=input("Enter PostgreSQL password: ")
) as connection:
    print("Database connection successful!")


    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            order_id = int(row["order_id"])
            customer_name = row["customer_name"]
            product = row["product"]
            quantity = int(row["quantity"])
            price = Decimal(row["price"])
            total_amount = Decimal(row["total_amount"])

            with connection.cursor() as cursor:
                cursor.execute(
                """
                INSERT INTO orders (
                    order_id,
                    customer_name,
                    product,
                    quantity,
                    price,
                    total_amount
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id)
                DO UPDATE SET
                    customer_name = EXCLUDED.customer_name,
                    product = EXCLUDED.product,
                    quantity = EXCLUDED.quantity,
                    price = EXCLUDED.price,
                    total_amount = EXCLUDED.total_amount;
                """,
                (
                    order_id,
                    customer_name,
                    product,
                    quantity,
                    price,
                    total_amount
                )
            )

            print(f"Loaded order: {order_id}")

    print("All orders loaded successfully!")

