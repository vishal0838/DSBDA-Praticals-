import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load dataset
df = pd.read_csv("Social_Network_Ads.csv")

# Select features and target
X = df[["Age", "EstimatedSalary"]]   # inputs
y = df["Purchased"]                  # output (0 or 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Extract values
TN, FP, FN, TP = cm.ravel()

print("Confusion Matrix:\n", cm)

# Metrics
accuracy = (TP + TN) / (TP + TN + FP + FN)
error = 1 - accuracy
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("\nAccuracy:", round(accuracy, 2))
print("Error Rate:", round(error, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))