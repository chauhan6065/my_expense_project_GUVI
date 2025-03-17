import streamlit as st
import pandas as pd
from config import engine

# Streamlit UI
st.title("📊 Personal Expense Tracker")

# Fetch data from MySQL
query = "SELECT * FROM expenses"
df = pd.read_sql(query, engine)

# Show data
st.dataframe(df)

# Show total spending per category
st.subheader("💰 Total Spending per Category")
category_spending = df.groupby("category")["amount_paid"].sum()
st.bar_chart(category_spending)

# Show spending per month
st.subheader("📆 Monthly Spending")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.strftime('%Y-%m')
monthly_spending = df.groupby("month")["amount_paid"].sum()
st.line_chart(monthly_spending)
