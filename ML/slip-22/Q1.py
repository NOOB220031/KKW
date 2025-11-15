import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("./CSV/house_price.csv")

# Show first few rows
print("First few rows of dataset:")
print(df.head())

# Drop completely empty columns
df = df.dropna(axis=1, how='all')

# Find null values
print("\nNull values in dataset:")
print(df.isnull().sum())

# Keep only rows where our important columns are not null
df = df.dropna(subset=['sqft_living', 'price'])
df = df[df['price'] > 0]
# Simple Linear Regression: predict price using sqft_living
X = df[['sqft_living']]   # Feature
y = df['price']           # Target


# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MSE:", mse)
print("R2 Score:", round(r2, 4))

# Compare actual vs predicted prices
comparison_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred})
print("\nActual vs Predicted Prices:")
print(comparison_df.head())
