import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Data Analysis Dashboard")

DATA_PATH = "data/Online_Retail.xlsx"

# Step 1: Check dataset
if not os.path.exists(DATA_PATH):
    st.error(f"❌ Dataset not found at: {DATA_PATH}")
    st.stop()

# Step 2: Load dataset with proper parsing
try:
    df = pd.read_excel(DATA_PATH, parse_dates=['InvoiceDate'])
    # 🔑 Fix: convert all object columns to string
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)

    st.success(f"✅ Dataset loaded! Shape: {df.shape}")
except Exception as e:
    st.error(f"❌ Error reading dataset: {e}")
    st.stop()

# Step 3: Preview raw data
st.subheader("🔹 Dataset Preview (first 5 rows)")
st.dataframe(df.head())

# Step 4: Data Cleaning
df = df.dropna(subset=['CustomerID'])
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Ensure InvoiceDate is datetime
if not pd.api.types.is_datetime64_any_dtype(df['InvoiceDate']):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)

st.success("✅ Data cleaned successfully!")
st.write("Dataset size after cleaning:", df.shape)

# Step 5: Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Products by Revenue")
    top_products = df.groupby('Description')['TotalPrice'].sum().nlargest(10).reset_index()
    fig1 = px.bar(
        top_products,
        x='TotalPrice',
        y='Description',
        orientation='h',
        title="Top 10 Products by Revenue",
        labels={'TotalPrice': 'Revenue', 'Description': 'Product'}
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🌍 Top 10 Countries by Revenue")
    country_revenue = df.groupby('Country')['TotalPrice'].sum().nlargest(10).reset_index()
    fig2 = px.bar(
        country_revenue,
        x='TotalPrice',
        y='Country',
        orientation='h',
        title="Top 10 Countries by Revenue",
        labels={'TotalPrice': 'Revenue', 'Country': 'Country'}
    )
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Monthly Revenue Trend")
monthly_revenue = df.groupby('InvoiceMonth')['TotalPrice'].sum().reset_index()
fig3 = px.line(
    monthly_revenue,
    x='InvoiceMonth',
    y='TotalPrice',
    markers=True,
    title="Monthly Revenue Trend",
    labels={'InvoiceMonth': 'Month', 'TotalPrice': 'Revenue'}
)
st.plotly_chart(fig3, use_container_width=True)
