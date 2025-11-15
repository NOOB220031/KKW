import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('./CSV/BostonHousingData.csv')

# Use only RM and MEDV (Price)
X = df[['RM']].values  # Feature: Number of rooms
y = df['MEDV'].values  # Target: Price

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Ridge and Lasso regression models
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

# Fit Ridge Regression
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)

# Fit Lasso Regression
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)

# Predict price for a house with 5 rooms
rooms = np.array([[5]])
price_ridge = ridge.predict(rooms)[0]
price_lasso = lasso.predict(rooms)[0]

# Evaluate models
print("Ridge Regression:")
print(f"  MSE: {mean_squared_error(y_test, y_pred_ridge):.2f}")
print(f"  R2 Score: {r2_score(y_test, y_pred_ridge):.2f}")
print(f"  Predicted Price for 5 rooms: ${price_ridge:.2f}\n")

print("Lasso Regression:")
print(f"  MSE: {mean_squared_error(y_test, y_pred_lasso):.2f}")
print(f"  R2 Score: {r2_score(y_test, y_pred_lasso):.2f}")
print(f"  Predicted Price for 5 rooms: ${price_lasso:.2f}\n")

# Plot the regression lines
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, ridge.predict(X), color='red', label='Ridge Regression')
plt.plot(X, lasso.predict(X), color='green', label='Lasso Regression')
plt.xlabel('Number of Rooms (RM)')
plt.ylabel('House Price (MEDV)')
plt.title('Ridge vs Lasso Regression')
plt.legend()
plt.grid(True)
plt.show()
