import numpy as np
from scipy import stats

# Generate two sample groups
sample1 = np.random.normal(loc=10, scale=2, size=30)
sample2 = np.random.normal(loc=12, scale=2, size=30)

# Perform t-test
t_stat, p_val = stats.ttest_ind(sample1, sample2)
print("T-statistic:", t_stat)
print("P-value:", p_val)

# Conclusion
if p_val < 0.05:
    print("Reject null hypothesis – significant difference.")
else:
    print("Fail to reject null – no significant difference.")
