import pandas as pd
from sklearn.metrics import mean_squared_error

# Load updated restaurant ratings
updated_ratings = pd.read_csv('data/updated_restaurant_ratings.csv')

# Simulate ground truth ratings for evaluation
# For demonstration purposes, let's simulate ground truth ratings
ground_truth_ratings = updated_ratings.copy()
ground_truth_ratings['rating'] = ground_truth_ratings['rating'] + (0.1 * (0.5 - pd.np.random.rand(len(ground_truth_ratings))))

# Calculate evaluation metrics
mse = mean_squared_error(ground_truth_ratings['rating'], updated_ratings['rating'])
print(f"Mean Squared Error: {mse}")

# Consistency check
consistency_check = ground_truth_ratings['rating'].corr(updated_ratings['rating'])
print(f"Consistency Check (Correlation): {consistency_check}")
