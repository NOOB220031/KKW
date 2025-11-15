import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("./CSV/Employee.csv")

# Drop missing values
data = data.dropna()

# Choose relevant features (Age & Income)
X = data[['Income', 'Age']]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans (k=3 example)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=data['Cluster'], cmap='rainbow')
plt.xlabel("Income (scaled)")
plt.ylabel("Age (scaled)")
plt.title("Employee Clustering")
plt.show()

print(data.head())
