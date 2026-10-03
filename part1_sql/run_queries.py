import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "meesho_reseller.db"
)

QUERY_DIR = os.path.join(
    BASE_DIR,
    "part1_sql",
    "queries"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "part1_sql",
    "output"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

queries = [
    (
        "01_monthly_category_revenue.sql",
        "monthly_category_revenue.csv"
    ),
    (
        "02_region_revenue.sql",
        "region_revenue.csv"
    ),
    (
        "03_top_resellers.sql",
        "top_resellers.csv"
    ),
    (
        "04_zero_order_resellers.sql",
        "zero_order_resellers.csv"
    ),
    (
        "05_zero_order_count_demo.sql",
        "zero_order_count_demo.csv"
    ),
    (
        "06_june_aov.sql",
        "june_aov.csv"
    )
]

conn = sqlite3.connect(DB_PATH)

for query_file, output_file in queries:

    query_path = os.path.join(
        QUERY_DIR,
        query_file
    )

    output_path = os.path.join(
        OUTPUT_DIR,
        output_file
    )

    with open(query_path, "r", encoding="utf-8") as f:
        query = f.read()

    cursor = conn.execute(query)

    columns = [
        description[0]
        for description in cursor.description
    ]

    rows = cursor.fetchall()

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

    print(f"Created: {output_file}")

conn.close()

print("All Part 1 SQL queries completed successfully.")