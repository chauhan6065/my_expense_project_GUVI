import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

# Connect to MySQL and create database
conn = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
cursor.execute(f"USE {DATABASE}")

# Create table for expenses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        category VARCHAR(50),
        payment_mode VARCHAR(50),
        description TEXT,
        amount_paid DECIMAL(10,2),
        cashback DECIMAL(10,2)
    )
""")

conn.commit()
conn.close()
print("✅ Database and table created successfully!")
