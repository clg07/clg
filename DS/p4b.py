#chi-test
import pandas as pd
import numpy as np  
import matplotlib as plt
import seaborn as sb 
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

# Load sample dataset
df = sb.load_dataset('mpg')

# Display the dataset
print(df)

# Describe horsepower and model_year
print(df['horsepower'].describe())
print(df['model_year'].describe())

# Binning horsepower into categories: low, medium, high
bins = [0, 75, 150, 240]
df['horsepower_new'] = pd.cut(df['horsepower'], bins=bins, labels=['l', 'm', 'h'])
print(df['horsepower_new'])

# Binning model_year into three time intervals
ybins = [69, 72, 74, 84]
labels = ['t1', 't2', 't3']
df['modelyear_new'] = pd.cut(df['model_year'], bins=ybins, labels=labels)
print(df['modelyear_new'])

# Create contingency table
df_chi = pd.crosstab(df['horsepower_new'], df['modelyear_new'])
print(df_chi)

# Perform Chi-square test
chi2, p, dof, expected = chi2_contingency(df_chi)
print("Chi-Square Value:", chi2)
print("p-value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:\n", expected)
