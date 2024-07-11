import pandas as pd
import numpy as np
from surprise import Dataset, Reader, SVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split

# Load the training data
train_data = pd.read_csv('data/train_data.csv')

# Collaborative Filtering using SVD
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(train_data[['user', 'cuisine', 'rating']], reader)
algo = SVD()
trainset = data.build_full_trainset()
algo.fit(trainset)

# Content-Based Filtering using TF-IDF
cuisine_names = [f"cuisine_{i}" for i in range(1, 21)]
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(cuisine_names)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Hybrid Recommendation Function
def hybrid_recommend(user_id, n_recommendations=5):
    # Collaborative Filtering
    user_ratings = train_data[train_data['user'] == user_id]
    known_cuisines = user_ratings['cuisine'].tolist()
    predictions = []
    
    for cuisine in range(len(cuisine_names)):
        if cuisine not in known_cuisines:
            predictions.append((cuisine, algo.predict(user_id, cuisine).est))
    
    predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
    top_collab = [x[0] for x in predictions[:n_recommendations]]
    
    # Content-Based Filtering
    sim_scores = list(enumerate(cosine_sim[top_collab[0]]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_content = [x[0] for x in sim_scores[:n_recommendations]]
    
    # Combine recommendations
    hybrid_recommendations = list(set(top_collab + top_content))[:n_recommendations]
    return [cuisine_names[i] for i in hybrid_recommendations]

# Example recommendation
user_id = 0  # Example user ID
recommendations = hybrid_recommend(user_id)
print("Recommended Cuisines:", recommendations)
