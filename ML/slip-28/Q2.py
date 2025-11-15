# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a list of kernels to try
kernels = ['linear', 'poly', 'rbf', 'sigmoid']

# Dictionary to store accuracy of each kernel
accuracies = {}

# Loop through each kernel and evaluate the model
for kernel in kernels:
    # Create an SVM model with the current kernel
    svm_model = SVC(kernel=kernel)
    
    # Train the model on the training data
    svm_model.fit(X_train, y_train)
    
    # Make predictions on the test data
    y_pred = svm_model.predict(X_test)
    
    # Calculate the accuracy and store it
    accuracy = accuracy_score(y_test, y_pred)
    accuracies[kernel] = accuracy
    print(f"Accuracy of SVM with {kernel} kernel: {accuracy:.4f}")

# Display the accuracies of all kernels
print("\nAccuracies of different SVM kernels:")
for kernel, acc in accuracies.items():
    print(f"{kernel}: {acc:.4f}")

# Function to predict the type of Iris flower based on input features
def predict_flower_type(sepal_length, sepal_width, petal_length, petal_width, kernel='rbf'):
    # Create an SVM model with the specified kernel
    svm_model = SVC(kernel=kernel)
    
    # Train the model on the entire dataset
    svm_model.fit(X, y)
    
    # Create an input data array from the given features
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Predict the flower type
    prediction = svm_model.predict(input_data)
    
    # Map the prediction to the corresponding flower species
    species = iris.target_names[prediction][0]
    
    return species

# Example usage of the function to predict flower type
print("\nPredicting flower type for input data:")
sepal_length = 5.1
sepal_width = 3.5
petal_length = 1.4
petal_width = 0.2

predicted_species = predict_flower_type(sepal_length, sepal_width, petal_length, petal_width, kernel='rbf')
print(f"Predicted flower species: {predicted_species}")
