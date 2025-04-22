# Principal Component Analysis (PCA)
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])

X = iris_df.drop('target', axis=1)
y = iris_df['target']
 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA
 
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Explained variance ratio
explained_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

# -------------------------
# Step 4: Plot cumulative variance
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(cumulative_var, marker='o', linestyle='--')
plt.title('Explained Variance Ratio by PCA Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.show()

n_components = np.argmax(cumulative_var >= 0.95) + 1
print(f"Number of principal components to explain 95% variance: {n_components}")

# Re-apply PCA with reduced dimensions
pca_final = PCA(n_components=n_components)
X_reduced = pca_final.fit_transform(X_scaled)
 
plt.figure(figsize=(8, 6))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis', s=50, alpha=0.7)
plt.title('Data in Reduced PCA Space')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Target Classes')
plt.show()
