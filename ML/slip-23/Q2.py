import pandas as pd

# Load dataset (replace with your file)
file_path = "./CSV/BostonHousingData.csv"
data = pd.read_csv(file_path)

# Display first few rows
print("Original Dataset:")
print(data.head())

# Find null values in each column
print("\nNull values in each column:")
print(data.isnull().sum())

# Remove rows with null values
cleaned_data = data.dropna()

print("\nDataset after removing null values:")
print(cleaned_data.head())

# Save cleaned dataset if needed
cleaned_data.to_csv("./cleaned_dataset.csv", index=False)
