import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("./CSV/Wholesale customers data.csv")
data = data.dropna()

# Select only annual spending columns for clustering
X = data.drop(columns=['Channel', 'Region']).values

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dendrogram
plt.figure(figsize=(8, 5))
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix)
plt.title("Dendrogram")
plt.xlabel("Clients")
plt.ylabel("Distance")
plt.show()

# Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=5, linkage='ward')
data['Cluster'] = agg.fit_predict(X_scaled)

# Show clients grouped by Region and Cluster
print("\nClients grouped by Region and Cluster:")
grouped = data.groupby(['Region', 'Cluster']).size().reset_index(name='NumClients')
print(grouped)

# Show average annual spending per cluster **within each region**
print("\nAverage annual spending per cluster per region:")
spending_cols = data.columns[2:-1]  # All spending columns
region_cluster_avg = data.groupby(['Region','Cluster'])[spending_cols].mean().round(2)
print(region_cluster_avg)
