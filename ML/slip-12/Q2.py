import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

df = pd.read_csv('./CSV/Salary_positions.csv')

# Features and target
X = df[['Level']]
y = df['Salary']

# Simple Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred_lin = lin_reg.predict(X)

# Polynomial Regression (degree 4)
poly_features = PolynomialFeatures(degree=4)
X_poly = poly_features.fit_transform(X)
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)
y_pred_poly = poly_reg.predict(X_poly)

# Visualization
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, y_pred_lin, color='blue', label='Linear Regression')
plt.plot(X, y_pred_poly, color='green', label='Polynomial Regression (deg=4)')
plt.title('Salary vs Position Level')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()

# Evaluate accuracy
print("Linear Regression R² Score:", r2_score(y, y_pred_lin))
print("Polynomial Regression R² Score:", r2_score(y, y_pred_poly))

# Predictions for Level 11 and 12 (corrected version)
level_11 = pd.DataFrame({'Level': [11]})
level_12 = pd.DataFrame({'Level': [12]})

# Linear predictions
lin_pred_11 = lin_reg.predict(level_11)[0]
lin_pred_12 = lin_reg.predict(level_12)[0]

# Polynomial predictions
poly_pred_11 = poly_reg.predict(poly_features.transform(level_11))[0]
poly_pred_12 = poly_reg.predict(poly_features.transform(level_12))[0]


print(f"\nPredicted Salary (Level 11):")
print(f"  Linear:     ${lin_pred_11:.2f}")
print(f"  Polynomial: ${poly_pred_11:.2f}")

print(f"\nPredicted Salary (Level 12):")
print(f"  Linear:     ${lin_pred_12:.2f}")
print(f"  Polynomial: ${poly_pred_12:.2f}")
