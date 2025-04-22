# Hypothesis Testing
from tracemalloc import Statistic
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generate two sample groups
sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)

# Perform t-test
t_stat, p_val = stats.ttest_ind(sample1, sample2)
print("T-statistic:", t_stat)
print("P-value:", p_val)
print(f"Degrees of Freedom: {len(sample1) + len(sample2) - 2}")
plt.figure(figsize=(10, 6))
plt.hist(sample1, alpha=0.5, label='Sample 1', color='blue')
plt.hist(sample2, alpha=0.5, label='Sample 2', color='orange')
plt.axvline(np.mean(sample1), color='blue', linestyle='dashed',linewidth=2) 
plt.axvline(np.mean(sample2), color='orange',linestyle='dashed', linewidth=2)
plt.title('Distributions of Sample 1and Sample 2')
plt.xlabel('Values')
plt.ylabel("Frequency")
plt.legend()

alpha = 0.05
# Conclusion
if p_val < alpha:
    critical_region = np.linspace(min(sample1.min(), sample2.min()),max(sample1.max(),sample2.max()), 1000)
    plt.fill_between(critical_region, 0, 5, color='red', alpha=0.3,label='Critical Region')
    plt.text(11, 5, f'T-statistic: {t_stat:2f}',ha='center', va='center', color='black',backgroundcolor='white')
    plt.show()
    if np.mean(sample1) > np.mean(sample2):
        print("Conclusion: There is significant evidence to reject the null hypothesis.")
        print("Interpretation: The mean of Sample 1 is significantly higher than that ofSample 2.")
    else:
        print("Conclusion: There is significant evidence to reject the null hypothesis.")
        print("Interpretation: The mean of Sample 2 is significantly higher than that of Sample1.")
else:
    print("Conclusion: Fail to reject the null hypothesis.")
    print("Interpretation: There is not enough evidence to claim a significant differencebetween the means.")
