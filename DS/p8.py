# Import required libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
data = {
    'Fresh': [12669, 7057, 6353, 13265, 22615],
    'Milk': [9656, 9810, 8808, 1196, 5410],
    'Grocery': [7561, 9568, 7684, 4221, 7198],
    'Frozen': [214, 1762, 2405, 6404, 3915],
    'Detergents_Paper': [2674, 3293, 3516, 507, 1777],
    'Delicassen': [1338, 1776, 7844, 1788, 5185]
}
df = pd.DataFrame(data)

# Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Elbow method
sse = []
K = range(1, len(df) + 1)  # Avoid k > number of samples

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(scaled_data)
    sse.append(km.inertia_)

# Plot
plt.plot(K, sse, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Sum of Squared Errors')
plt.title('Elbow Method')
plt.grid(True)
plt.show()
