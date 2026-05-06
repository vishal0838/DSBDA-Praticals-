# Import libraries
import pandas as pd

# Load dataset (download iris.csv)
df = pd.read_csv("iris.csv")

# Display first rows
print(df.head())

# Group by categorical variable (species)
grouped = df.groupby('species')

# Calculate summary statistics
summary = grouped.agg({
    'sepal_length': ['mean', 'median', 'min', 'max', 'std'],
    'sepal_width': ['mean', 'median', 'min', 'max', 'std']
})

print("\nSummary Statistics:")
print(summary)