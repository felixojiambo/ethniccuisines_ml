import json
import pandas as pd

# Load user interaction data
with open('data/user_interactions_ab_testing.json', 'r') as file:
    interactions = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(interactions)

# Split users into two groups: Group A (hybrid recommender) and Group B (random recommender)
df['group'] = df['user'].apply(lambda x: 'A' if int(x.split('_')[1]) % 2 == 0 else 'B')

# Save preprocessed data
df.to_csv('data/ab_testing_data.csv', index=False)
