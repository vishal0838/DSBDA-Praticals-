import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Creating the Dataset
data = {
    'Student_ID': range(1, 11),
    'Math_Score': [85, 90, np.nan, 70, 88, 150, 65, 80, 75, np.nan], 
    'Science_Score': [80, 82, 78, 95, 2, 88, 84, np.nan, 90, 85],   
    'Reading_Score': [70, 72, 75, 68, 74, 80, 77, 82, 79, 81],
    'Age': [20, 21, 19, 20, 22, -5, 20, 21, 22, 20]                
}

df = pd.DataFrame(data)

print("Step 1: Original Data with Issues")
display(df)

# --- Task 1: Handling Missing Values & Inconsistencies ---
# Fix logical inconsistency: Age cannot be negative
df.loc[df['Age'] <= 0, 'Age'] = np.nan

# Fill missing values using the Median (standard practice for skewed data)
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())
df['Age'] = df['Age'].fillna(df['Age'].median())

# --- Task 2: Handling Outliers (IQR Method) ---
# We calculate the bounds for Math_Score
Q1 = df['Math_Score'].quantile(0.25)
Q3 = df['Math_Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Capping: Replace outliers with the upper/lower boundary values
df['Math_Score'] = np.clip(df['Math_Score'], lower_bound, upper_bound)

# --- Task 3: Data Transformation ---
# Purpose: Reducing skewness using Log Transformation
# We use log1p (log(1+x)) to handle potential zeros gracefully
df['Log_Science'] = np.log1p(df['Science_Score'])

print("\nStep 2: Cleaned and Transformed Data")
display(df)

# Visualizing the distribution change (Optional but great for Jupyter)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(df['Science_Score'], kde=True, ax=ax1).set_title('Original Science Score')
sns.histplot(df['Log_Science'], kde=True, ax=ax2).set_title('Log Transformed Science Score')
plt.show()