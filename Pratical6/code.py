import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 1. Load the dataset
# Assuming iris.csv is in your directory. If not, sklearn has it built-in:
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target

# 2. Split data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize and train the Naïve Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# 4. Make predictions
y_pred = model.predict(X_test)

# 5. Compute Metrics
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Confusion Matrix:\n", cm)
print(f"\nAccuracy: {accuracy:.2f}")
print(f"Error Rate: {1 - accuracy:.2f}")
print("\nDetailed Performance Metrics:")
print(classification_report(y_test, y_pred, target_names=data.target_names))