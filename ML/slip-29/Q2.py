import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load the dataset (replace with your correct dataset path)
data = pd.read_csv('D:\Msc - computer science\SEM-3\ML\practical\CSV-Files\Employee.csv')

# Print the first 5 rows and basic information
print(data.head())
print(data.info())

# Drop rows with missing values (if any)
data = data.dropna()

# Assume the relevant columns for clustering are 'Income' and 'Age' (replace with actual columns)
X = data[['Income', 'Age']]  # Adjust column names as needed

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method
inertia = []
k_range = range(1, 11)  # Testing k values from 1 to 10
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)  # Explicitly set n_init
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow method result
plt.figure(figsize=(10, 6))
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.grid(True)
plt.show()

# Determine the optimal number of clusters using Silhouette Score
silhouette_scores = []
for k in k_range[1:]:  # k=1 is not valid for silhouette score
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)  # Explicitly set n_init
    cluster_labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, cluster_labels)
    silhouette_scores.append(score)

# Plot the silhouette scores
plt.figure(figsize=(10, 6))
plt.plot(k_range[1:], silhouette_scores, marker='o')
plt.title('Silhouette Scores for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.xticks(k_range[1:])
plt.grid(True)
plt.show()

# Based on the plots, choose the optimal k (update this value based on your observations)
optimal_k = 3  # Replace with the value you find optimal based on the plots

# Apply K-means clustering with the optimal k
kmeans = KMeans(n_clusters=optimal_k, n_init=10, random_state=42)  # Explicitly set n_init
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Print the first few rows with cluster labels
print(data.head())

# Optionally: Plot the clustered data
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data['Cluster'], cmap='viridis', marker='o')
plt.title(f'K-Means Clustering of Employees (k={optimal_k})')
plt.xlabel('Income (scaled)')
plt.ylabel('Age (scaled)')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
