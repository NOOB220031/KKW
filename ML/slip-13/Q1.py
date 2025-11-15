import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import accuracy_score

# 1. Load Google stock data
data = yf.download("GOOGL", start="2015-01-01", end="2023-01-01")[['Close']]

# 2. Scale data
scaler = MinMaxScaler(feature_range=(0,1))
scaled = scaler.fit_transform(data)

# 3. Create dataset (60 days → 1 next day)
def create_dataset(dataset, step=60):
    X, y = [], []
    for i in range(len(dataset)-step-1):
        X.append(dataset[i:i+step, 0])
        y.append(dataset[i+step, 0])
    return np.array(X), np.array(y)

X, y = create_dataset(scaled, 60)
X = X.reshape(X.shape[0], X.shape[1], 1)

# 4. Train/Test split
train_size = int(len(X)*0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 5. Build simple RNN with LSTM
model = Sequential([
    LSTM(50, input_shape=(X_train.shape[1], 1)),
    Dense(1)
])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# 6. Predictions
pred = model.predict(X_test)
pred = scaler.inverse_transform(pred)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1,1))

# 7. Trend accuracy (up/down)
pred_trend = np.where(pred[1:] > pred[:-1], 1, 0)
actual_trend = np.where(y_test_actual[1:] > y_test_actual[:-1], 1, 0)
acc = accuracy_score(actual_trend, pred_trend)*100
print(f"Trend Prediction Accuracy: {acc:.2f}%")

# 8. Plot results
plt.figure(figsize=(12,6))
plt.plot(y_test_actual, label="Actual")
plt.plot(pred, label="Predicted")
plt.legend()
plt.title("Google Stock Price Prediction")
plt.show()
