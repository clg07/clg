import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load training CSV
df = pd.read_csv(r"C:\Users\Administrator\Documents\Sem 6\IR\Dataset.csv")
data = df["covid"] + "" + df["fever"]
X = data.astype(str)
y = df['flu']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train classifier
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

# Load test data
data1 = pd.read_csv(r"C:\Users\Administrator\Documents\Sem 6\IR\Test.csv")
new_data = data1["covid"] + "" + data1["fever"]
new_data_counts = vectorizer.transform(new_data.astype(str))

# Predict and evaluate
predictions = classifier.predict(new_data_counts)
print(predictions)

accuracy = accuracy_score(y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy: {accuracy:.2f}")
print("Classification Report: ")
print(classification_report(y_test, classifier.predict(X_test_counts)))

# Save predictions to CSV
predictions_df = pd.DataFrame(predictions, columns=['flu_prediction'])
data1 = pd.concat([data1, predictions_df], axis=1)
data1.to_csv(r"C:\Users\Administrator\Documents\Sem 6\IR\Test1.csv", index=False)
