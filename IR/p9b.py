import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Synthetic ranking dataset
X = np.array([[1, 2], [2, 3], [3, 3], [4, 5], [5, 5], [6, 7]])  # Features
y = np.array([0, 0, 1, 1, 2, 2])  # Relevance scores (higher is better)

# Increase the test size to make sure we have enough samples to stratify
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y, random_state=42)

# Using SVM classifier
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Display predictions for understanding
print("True labels: ", y_test)
print("Predicted labels: ", y_pred)
