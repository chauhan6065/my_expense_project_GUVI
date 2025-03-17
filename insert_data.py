import pandas as pd
from config import engine

# Read data from CSV
df = pd.read_csv("expenses.csv")

# Insert into MySQL
df.to_sql('expenses', con=engine, if_exists='append', index=False)
print("✅ Data successfully inserted into MySQL!")
