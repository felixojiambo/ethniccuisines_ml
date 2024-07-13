import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares

# Load preprocessed user preference data
df = pd.read_csv('data/preprocessed_user_preferences.csv')

# Convert data to user-item matrix
user_item_matrix = df.set_index('user').astype(float)

# Convert to sparse matrix
sparse_matrix = csr_matrix(user_item_matrix.values)

# Split data into training and test sets
train_matrix, test_matrix = train_test_split(sparse_matrix, test_size=0.2, random_state=42)

# Train the ALS model
model = AlternatingLeastSquares(factors=20, regularization=0.1, iterations=50)
model.fit(train_matrix.T)

# Evaluate the model
def evaluate_model(model, test_matrix, top_k=10):
    test_users = test_matrix.nonzero()[0]
    precision_at_k = []

    for user in test_users:
        user_items = test_matrix[user].indices
        user_recommendations = model.recommend(user, train_matrix, N=top_k, filter_already_liked_items=True)
        recommended_items = [item[0] for item in user_recommendations]
        true_positives = len(set(user_items).intersection(set(recommended_items)))
        precision_at_k.append(true_positives / top_k)

    mean_precision_at_k = np.mean(precision_at_k)
    return mean_precision_at_k

precision = evaluate_model(model, test_matrix)
print(f"Precision at {10}: {precision}")

# Save the model
import pickle
with open('models/als_model.pkl', 'wb') as file:
    pickle.dump(model, file)
