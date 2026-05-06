# 1. Import required libraries
import pandas as pd
import numpy as np

# 2. Load dataset (download from Kaggle and save as data.csv)
# Source: https://www.kaggle.com/c/titanic/data
df = pd.read_csv("data.csv")

# 3. Display first few rows
print("First 5 rows:")
print(df.head())

# 4. Data Preprocessing

# Check dataset dimensions
print("\nShape of dataset:", df.shape)

# Check column names
print("\nColumns:")
print(df.columns)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# 5. Data Formatting & Normalization

# Convert data types if needed
df['Age'] = df['Age'].astype(float)
df['Fare'] = df['Fare'].astype(float)

# Normalize numerical columns (Age, Fare)
df['Age_norm'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df['Fare_norm'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

# 6. Convert categorical variables into numerical

# Convert 'Sex' column (male=0, female=1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encoding for 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'])

# Final dataset preview
print("\nProcessed Data:")
print(df.head())