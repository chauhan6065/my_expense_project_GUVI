import pandas as pd
from config import engine

# Fetch data from MySQL
query = "SELECT * FROM expenses"
df = pd.read_sql(query, engine)

# Show first 5 rows
print(df.head())

# Analyze total spending per category
category_spending = df.groupby("category")["amount_paid"].sum()
print("Total spending per category:\n", category_spending)
