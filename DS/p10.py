# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)  # For reproducibility

data = pd.DataFrame({
    'variable1': np.random.normal(0, 1, 1000),
    'variable2': np.random.normal(2, 2, 1000) + 0.5 * np.random.normal(0, 1, 1000),
    'variable3': np.random.normal(-1, 1.5, 1000),
    'category': pd.Series(np.random.choice(['A', 'B', 'C', 'D'], size=1000, p=[0.4, 0.3, 0.2, 0.1]), dtype='category')
})

# Step 2: Scatter Plot (Variable Relationship)
 
plt.figure(figsize=(10, 6))
plt.scatter(data['variable1'], data['variable2'], alpha=0.5)
plt.title('Relationship between Variable 1 and Variable 2', fontsize=16)
plt.xlabel('Variable 1', fontsize=14)
plt.ylabel('Variable 2', fontsize=14)
plt.grid(True)
plt.show()

# Step 3: Bar Chart (Category Distribution)
 
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=data)
plt.title('Distribution of Categories', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()

# Step 4: Heatmap (Correlation)
 
plt.figure(figsize=(10, 8))
numerical_cols = ['variable1', 'variable2', 'variable3']
sns.heatmap(data[numerical_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap', fontsize=16)
plt.show()

 
print("Data Storytelling")
print("--------------------------------------------------")
print("1 Title: Exploring the Relationship between Variable 1 and Variable 2")
print("2️ nThe scatter plot (Figure 1) shows the relationship between Variable 1 and Variable 2.")
print("\nThe scatter plot (Figure 1) shows the relationship between Variable 1 and Variable 2.")
print("\nScatter Plot")
print("Figure 1: Scatter Plot of Variable 1 and Variable 2")

print("\nTo better understand the distribution of the categorical variable 'category', we created a bar chart.")
print("\nBar Chart")
print("Figure 2: Distribution of Categories")

print("\nAdditionally, we explored the correlation between numerical variables using a heatmap.")
print("\nHeatmap")
print("Figure 3: Correlation Heatmap")

