import random
import pandas as pd
from faker import Faker

fake = Faker()

# Expense Categories and Payment Modes
categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Groceries', 'Rent']
payment_modes = ['Cash', 'Credit Card', 'Debit Card', 'UPI', 'Net Banking']

# Generate Expense Data
def generate_expense_data(n=100):
    data = []
    for _ in range(n):
        data.append([
            fake.date_between(start_date='-1y', end_date='today'),
            random.choice(categories),
            random.choice(payment_modes),
            fake.sentence(nb_words=4),
            round(random.uniform(50, 500), 2),  # Expense amount
            round(random.uniform(0, 50), 2) if random.random() > 0.7 else 0  # Cashback
        ])
    return pd.DataFrame(data, columns=['date', 'category', 'payment_mode', 'description', 'amount_paid', 'cashback'])

df = generate_expense_data(1000)
df.to_csv("expenses.csv", index=False)
print("✅ Fake expense data generated and saved as expenses.csv!")
