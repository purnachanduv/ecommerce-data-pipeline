import csv

with open("data/orders.csv", "r") as input_file:
    reader = csv.DictReader(input_file)

    with open("data/cleaned_orders.csv", "w", newline="") as output_file:
        fieldnames = [
            "order_id",
            "customer_name",
            "product",
            "quantity",
            "price",
            "total_amount"
        ]

        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            quantity = int(row["quantity"])
            price = float(row["price"])

            total_amount = quantity * price

            writer.writerow({
                "order_id": row["order_id"],
                "customer_name": row["customer_name"],
                "product": row["product"],
                "quantity": quantity,
                "price": price,
                "total_amount": total_amount
            })