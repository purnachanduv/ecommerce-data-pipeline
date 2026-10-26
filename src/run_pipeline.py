import subprocess
import sys

print("\nSTEP 1: Cleaning the order data...")
subprocess.run(
    [sys.executable, "src/read_data.py"],
    check=True
)

print("\nSTEP 2: Loading data into PostgreSQL...")
subprocess.run(
    [sys.executable, "src/load_data.py"],
    check=True
)

print("\nSTEP 3: Verifying the database...")
subprocess.run(
    [sys.executable, "src/connect_db.py"],
    check=True
)

print("\nPipeline completed successfully!")