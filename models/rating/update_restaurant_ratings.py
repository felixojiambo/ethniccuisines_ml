import pandas as pd

# Load preprocessed review data
df = pd.read_csv('data/preprocessed_reviews.csv')

# Calculate average rating for each restaurant
restaurant_ratings = df.groupby('restaurant')['rating'].mean().reset_index()

# Save updated restaurant ratings
restaurant_ratings.to_csv('data/updated_restaurant_ratings.csv', index=False)
