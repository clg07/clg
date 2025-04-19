import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the training dataset
df = pd.read_csv("Dataset.csv")  # Make sure this is in the same folder
data = df["covid"] + " " + df["fever"]
X = data.astype(str)
y = df['flu']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to vectors
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train classifier
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

# Load test dataset
data1 = pd.read_csv("Test.csv")  # Make sure this is in the same folder
new_data = data1["covid"] + " " + data1["fever"]
new_data_counts = vectorizer.transform(new_data.astype(str))

# Predict on new data
predictions = classifier.predict(new_data_counts)
print("Predictions on Test.csv:")
print(predictions)

# Evaluate on training split
accuracy = accuracy_score(y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, classifier.predict(X_test_counts)))

# Save predictions
data1["flu_prediction"] = predictions
data1.to_csv("Test1.csv", index=False)
print("\nPredictions saved to Test1.csv")
