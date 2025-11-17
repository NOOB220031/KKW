import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


data = pd.read_csv("./CSV/Employee.csv")

data = data.dropna()

X = data[['Income', 'Age']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

plt.scatter(X_scaled[:,0], X_scaled[:,1], c=data['Cluster'], cmap='rainbow')
plt.xlabel("Income (scaled)")
plt.ylabel("Age (scaled)")
plt.title("Employee Clustering")
plt.show()

print(data.head())
