# ANOVA (Analysis of Variance)
# Import required libraries
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Step 1: Define sample data for four groups
 
group1 = [23, 25, 29, 34, 30]
group2 = [19, 20, 22, 24, 25]
group3 = [15, 18, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]
 
# Step 2: Create a single DataFrame
 
data = pd.DataFrame({
    'value': group1 + group2 + group3 + group4,
    'group': ['Group1'] * len(group1) +
             ['Group2'] * len(group2) +
             ['Group3'] * len(group3) +
             ['Group4'] * len(group4)
})

 
# Step 3: Perform one-way ANOVA

f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

print("One-Way ANOVA Results:")
print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Conclusion: Reject null hypothesis – Significant differences exist among groups.")
else:
    print("Conclusion: Fail to reject null hypothesis – No significant differences found.")

 
# Step 4: Perform Tukey's Post-Hoc Test
 
tukey = pairwise_tukeyhsd(endog=data['value'], groups=data['group'], alpha=0.05)

print("\nTukey-Kramer Post-Hoc Test:")
print(tukey)
