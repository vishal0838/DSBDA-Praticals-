# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("housing.csv")

# Separate input (X) and output (y)
X = df.drop("MEDV", axis=1)   # Features
y = df["MEDV"]                # Target (house price)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict prices
predictions = model.predict(X_test)

# Show results in proper format
result = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": predictions
})

print("First 10 Results:\n")
print(result.head(10))

# Show accuracy
print("\nR2 Score:", round(r2_score(y_test, predictions), 2))