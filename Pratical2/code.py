import pandas as pd
import numpy as np
from scipy import stats

# 0. Create a dummy "Academic Performance" dataset
data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Math_Score': [85, 90, np.nan, 88, 92, 300, 85, 89], # 300 is an outlier
    'Reading_Score': [70, 72, 75, 68, 71, 69, 70, 500],   # 500 is an outlier
    'Attendance': [95, 80, 85, np.nan, 90, 88, 92, 85]   # Missing value
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# --- 1. Handle Missing Values & Inconsistencies ---
# We'll fill missing Math scores with the mean and Attendance with the median.
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())

# --- 2. Handle Outliers ---
# We use the Interquartile Range (IQR) method to detect and cap outliers.
def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Cap values instead of deleting to keep data size consistent
    df[column] = np.where(df[column] > upper_bound, upper_bound, 
                 np.where(df[column] < lower_bound, lower_bound, df[column]))
    return df

df = handle_outliers(df, 'Math_Score')
df = handle_outliers(df, 'Reading_Score')

# --- 3. Data Transformation ---
# We apply a Log Transformation to Reading_Score to reduce skewness.
df['Log_Reading_Score'] = np.log1p(df['Reading_Score']) 

print("Processed Dataset:\n", df)