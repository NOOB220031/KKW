import pandas as pd

file_path = "./CSV/BostonHousingData.csv"
data = pd.read_csv(file_path)

print("Original Dataset:")
print(data.head())

print("\nNull values in each column:")
print(data.isnull().sum())

cleaned_data = data.dropna()

print("\nDataset after removing null values:")
print(cleaned_data.head())

cleaned_data.to_csv("./cleaned_dataset.csv", index=False)
