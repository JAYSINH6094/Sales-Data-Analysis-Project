import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_data.csv")

# Snapshot date for RFM
snapshot_date = pd.to_datetime(df['InvoiceDate']).max() + pd.Timedelta(days=1)

# RFM Calculation
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - pd.to_datetime(x).max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
}).rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
})

# Scale values
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print("\nCustomer Segmentation Clusters:\n", rfm.groupby('Cluster').mean())
rfm.to_csv("data/processed/customer_segments.csv")
