import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.svm import SVC


iris = load_iris()
X, y = iris.data, iris.target


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)


clf = SVC(kernel='linear')
clf.fit(X_pca, y)

new_data = [[5.1, 3.5, 1.4, 0.2]]
new_data_pca = pca.transform(new_data)  # Reduce new data

prediction = clf.predict(new_data_pca)
flower_type = iris.target_names[prediction][0]
print(f"Predicted flower type: {flower_type}")


plt.figure(figsize=(8,6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.scatter(new_data_pca[0,0], new_data_pca[0,1], color='red', s=100, label='New Data')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Dataset PCA (4D → 2D)")
plt.legend()
plt.colorbar(scatter, label="Species")
plt.show()
