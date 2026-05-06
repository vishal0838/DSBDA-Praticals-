# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load inbuilt Titanic dataset
df = sns.load_dataset('titanic')

# Display first rows
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Find patterns using countplot
sns.countplot(x='survived', data=df)
plt.title("Survival Count")
plt.show()

# Survival based on gender
sns.countplot(x='survived', hue='sex', data=df)
plt.title("Survival based on Gender")
plt.show()

# Survival based on passenger class
sns.countplot(x='survived', hue='class', data=df)
plt.title("Survival based on Class")
plt.show()