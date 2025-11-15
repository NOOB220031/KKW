import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('./CSV/weather_forecast_data.csv')

print("First 5 rows of dataset:")
print(df.head())

X = df[['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'Pressure']]
y = df['Rain']  # Target column

# Convert target to numeric codes (rain=1, no rain=0)
y = y.map({'rain': 1, 'no rain': 0})

# Split dataset (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['no rain', 'rain']))

# Example: predict new data
sample = pd.DataFrame({
    'Temperature': [26],
    'Humidity': [70],
    'Wind_Speed': [5],
    'Cloud_Cover': [40],
    'Pressure': [1005]
})

prediction = model.predict(sample)
prediction_label = 'rain' if prediction[0] == 1 else 'no rain'
print("\nPrediction for sample data:", prediction_label)
