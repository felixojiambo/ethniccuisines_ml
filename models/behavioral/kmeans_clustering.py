import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load preprocessed user data
df = pd.read_csv('data/preprocessed_user_data.csv')

# Select features for clustering
X = df[['interaction', 'value', 'cuisine']]

# Apply K-means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(X)

# Add cluster labels to the DataFrame
df['cluster'] = labels

# Evaluate clustering using silhouette score
score = silhouette_score(X, labels)
print(f"Silhouette Score: {score}")

# Save clustered data
df.to_csv('data/clustered_user_data.csv', index=False)
