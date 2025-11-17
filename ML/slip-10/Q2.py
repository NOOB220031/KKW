import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./CSV/iris.csv")


print("Before conversion:")
print(df.head())

df['Species_numeric'] = df['Species'].astype('category').cat.codes
species_names = df['Species'].astype('category').cat.categories


print("\nAfter conversion:")
print(df.head())

for i, species in enumerate(species_names):
    data = df[df['Species_numeric'] == i]
    plt.scatter(data['SepalLengthCm'], data['SepalWidthCm'], label=species)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.legend()
plt.show()


for i, species in enumerate(species_names):
    data = df[df['Species_numeric'] == i]
    plt.scatter(data['PetalLengthCm'], data['PetalWidthCm'], label=species)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.legend()
plt.show()