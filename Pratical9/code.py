# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# Create boxplot
sns.boxplot(x='sex', y='age', hue='survived', data=df)

# Title and labels
plt.title("Age Distribution by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")

# Show plot
plt.show()