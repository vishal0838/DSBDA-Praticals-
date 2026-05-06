import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (inbuilt)
df = sns.load_dataset('iris')

# Display first rows
print(df.head())

# Feature names
print("\nFeatures:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)