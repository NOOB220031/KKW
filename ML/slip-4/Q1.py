import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("./CSV/Mall_Customers.csv")

print(data.head())
print(data.info())

# Select features (example: Annual Income & Spending Score)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans with k=5 (example)
kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot results
plt.figure(figsize=(8,6))
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=data['Cluster'], cmap='viridis')
plt.title("KMeans on Mall Customers")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.colorbar(label="Cluster")
plt.show()

print(data.head())
