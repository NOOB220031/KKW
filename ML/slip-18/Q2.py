import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("./CSV/Salary_positions.csv")

# Features and target
X = df[['Level']]
y = df['Salary']

# Polynomial transformation (degree 4)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)

# Fit Polynomial Regression
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# Predictions for the dataset
y_pred_poly = poly_reg.predict(X_poly)

# Evaluate model
r2 = r2_score(y, y_pred_poly)
print(f"Polynomial Regression R² Score: {r2:.4f}")

# Use same column name as training data
level_11 = pd.DataFrame({'Level': [11]})
level_12 = pd.DataFrame({'Level': [12]})

pred_11 = poly_reg.predict(poly_features.transform(level_11))[0]
pred_12 = poly_reg.predict(poly_features.transform(level_12))[0]

print(f"Predicted Salary (Level 11): ${pred_11:.2f}")
print(f"Predicted Salary (Level 12): ${pred_12:.2f}")

# Visualization
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Regression (deg=4)')
plt.title("Salary vs Position Level (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()
