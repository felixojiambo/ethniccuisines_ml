import json
import pandas as pd

# Load review data
with open('data/reviews.json', 'r') as file:
    reviews = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(reviews)

# Convert review_date to datetime
df['review_date'] = pd.to_datetime(df['review_date'])

# Normalize ratings
df['rating'] = df['rating'] / df['rating'].max()

# Save preprocessed data
df.to_csv('data/preprocessed_reviews.csv', index=False)
