import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("./CSV/Salary_positions.csv")

# Features and target
X = df[['Level']]
y = df['Salary']

# Simple Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Predictions
level_11 = pd.DataFrame({'Level': [11]})
level_12 = pd.DataFrame({'Level': [12]})

lin_pred_11 = lin_reg.predict(level_11)[0]
lin_pred_12 = lin_reg.predict(level_12)[0]

print(f"Predicted Salary (Level 11): ${lin_pred_11:.2f}")
print(f"Predicted Salary (Level 12): ${lin_pred_12:.2f}")

# Visualization
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X, lin_reg.predict(X), color='blue', label='Linear Regression')
plt.title("Salary vs Position Level (Simple Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()
