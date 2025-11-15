import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("./CSV/HousingData.csv")

print("First few rows of dataset:")
print(df.head())

# Features and Target
X = df[['RM']]   # Average number of rooms per dwelling (as feature for polynomial regression)
y = df['MEDV']   # Median value of owner-occupied homes in $1000s (target)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Polynomial Features (degree=2 for quadratic regression)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predictions
y_pred = model.predict(X_test_poly)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.4f}")

# --- Visualization ---
plt.scatter(X, y, color='blue', alpha=0.5, label="Actual data")

# Generate smooth curve for prediction line
X_curve = np.linspace(X.min(), X.max(), 300).reshape(-1,1)
X_curve = pd.DataFrame(X_curve, columns=['RM']) # Ensure it's a DataFrame
X_curve_poly = poly.transform(X_curve)
y_curve = model.predict(X_curve_poly)

plt.plot(X_curve, y_curve, color='red', linewidth=2, label="Polynomial Regression (degree=2)")
plt.xlabel("Average number of rooms (RM)")
plt.ylabel("Median house value (MEDV)")
plt.title("Polynomial Regression - Boston Housing Dataset")
plt.legend()
plt.show()
