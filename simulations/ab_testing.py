import pandas as pd
import random

# Load preprocessed A/B testing data
df = pd.read_csv('data/ab_testing_data.csv')

# Define a simple random recommender
def random_recommender(user_id, n_recommendations=5):
    cuisines = [f"cuisine_{i}" for i in range(1, 21)]
    return random.sample(cuisines, n_recommendations)

# Define a function to simulate user interaction with the recommendation system
def simulate_interaction(user_id, recommendations):
    interactions = df[df['user'] == user_id]
    engagement = 0
    for rec in recommendations:
        if rec in interactions['cuisine'].values:
            engagement += interactions[interactions['cuisine'] == rec]['interaction_value'].sum()
    return engagement

# Split users into groups
group_a_users = df[df['group'] == 'A']['user'].unique()
group_b_users = df[df['group'] == 'B']['user'].unique()

# Evaluate hybrid recommender for Group A
hybrid_engagement = 0
for user in group_a_users:
    recommendations = hybrid_recommend(user)
    hybrid_engagement += simulate_interaction(user, recommendations)

# Evaluate random recommender for Group B
random_engagement = 0
for user in group_b_users:
    recommendations = random_recommender(user)
    random_engagement += simulate_interaction(user, recommendations)

print(f"Average engagement for hybrid recommender: {hybrid_engagement / len(group_a_users)}")
print(f"Average engagement for random recommender: {random_engagement / len(group_b_users)}")
