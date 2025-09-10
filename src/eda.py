import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_excel('data/Online_Retail.xlsx')

# Data Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/cleaned_data.csv", index=False)

# Top 10 Products by Revenue
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:\n", top_products)

plt.figure(figsize=(10,6))
top_products.plot(kind='barh')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Products")
plt.tight_layout()
plt.savefig("data/processed/top_products.png")
plt.show()

# Monthly Revenue Trend
monthly_revenue = df.groupby('InvoiceMonth')['TotalPrice'].sum()
print("\nMonthly Revenue Trend:\n", monthly_revenue)

plt.figure(figsize=(10,6))
monthly_revenue.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("data/processed/monthly_revenue.png")
plt.show()
