import pandas as pd
from scipy.stats import chi2_contingency

# Sample data
data = {'Preference': ['Tea', 'Tea', 'Coffee', 'Coffee', 'Tea', 'Coffee'],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']}

df = pd.DataFrame(data)

# Create cross-tab
ct = pd.crosstab(df['Preference'], df['Gender'])

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(ct)
print("Chi-Square:", chi2)
print("P-value:", p)

# Conclusion
if p < 0.05:
    print("Reject null – variables are related.")
else:
    print("Fail to reject null – variables are independent.")
