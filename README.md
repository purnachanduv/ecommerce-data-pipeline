# E-commerce Data Pipeline

## Project Overview

This project demonstrates a simple data engineering pipeline using Python and PostgreSQL.

The pipeline reads e-commerce order data from a CSV file, transforms the data by calculating the total amount for each order, loads the processed data into a PostgreSQL database, and uses SQL queries to analyse sales and customer spending.

## Technologies Used

* Python
* PostgreSQL
* SQL
* CSV

## Project Structure

```text
ecommerce-data-pipeline/
├── data/
│   ├── orders.csv
│   └── cleaned_orders.csv
├── sql/
│   └── analysis.sql
├── src/
│   ├── read_data.py
│   ├── connect_db.py
│   └── load_data.py
└── README.md
```

## Pipeline Steps

1. **Extract:** Read order data from `orders.csv`.
2. **Transform:** Use Python to calculate `total_amount` from quantity multiplied by price.
3. **Load:** Load the cleaned order data into PostgreSQL.
4. **Analyse:** Use SQL queries to calculate revenue by product, customer spending, and order counts.

## SQL Analysis

The project includes SQL queries to:

* Count the total number of orders.
* Calculate revenue by product.
* Calculate total spending by customer.
* Count orders placed by each customer.

## Key Results

* Total orders processed: 10
* Highest-revenue product: Laptop
* Highest-spending customer: Priya

## Learning Outcomes

* Reading and processing CSV files with Python.
* Connecting Python to PostgreSQL.
* Inserting and updating records in a database.
* Writing SQL queries using `GROUP BY`, `SUM`, `COUNT`, and `ORDER BY`.
* Building a basic end-to-end data pipeline.
