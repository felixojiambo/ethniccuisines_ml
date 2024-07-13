import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load preprocessed data
df = pd.read_csv('data/preprocessed_regional_dining_data.csv')

# Prepare data for clustering
X = df[['popularity_normalized']]

# Determine the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Assuming the optimal number of clusters is 3 based on the elbow method
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Save the clustered data
df.to_csv('data/clustered_regional_dining_data.csv', index=False)
