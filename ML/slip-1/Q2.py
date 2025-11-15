# Write a Python program to prepare Scatter Plot for Iris Dataset. Convert Categorical 
# values in numeric format for a dataset

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("./CSV/iris.csv")

# Show first 5 rows (before conversion)
print("Before conversion:")
print(df.head())

# Convert categorical 'Species' to numeric
df['Species_numeric'] = df['Species'].astype('category').cat.codes
species_names = df['Species'].astype('category').cat.categories

# Show first 5 rows (after conversion)
print("\nAfter conversion:")
print(df.head())

# Scatter Plot 1: SepalLength vs SepalWidth (using converted numeric data)
for i, species in enumerate(species_names):
    data = df[df['Species_numeric'] == i]
    plt.scatter(data['SepalLengthCm'], data['SepalWidthCm'], label=species)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.legend()
plt.show()

# Scatter Plot 2: PetalLength vs PetalWidth (using converted numeric data)
for i, species in enumerate(species_names):
    data = df[df['Species_numeric'] == i]
    plt.scatter(data['PetalLengthCm'], data['PetalWidthCm'], label=species)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.legend()
plt.show()