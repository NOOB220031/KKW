import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("./CSV/house_price.csv")

print("First few rows of dataset:")
print(df.head())

df = df.dropna(axis=1, how='all')

print("\nNull values in dataset:")
print(df.isnull().sum())

df = df.dropna(subset=['sqft_living', 'price'])
df = df[df['price'] > 0]

X = df[['sqft_living']]   
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MSE:", mse)
print("R2 Score:", round(r2, 4))

comparison_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred})
print("\nActual vs Predicted Prices:")
print(comparison_df.head())
