import json
import random
import numpy as np

# Simulate user interaction data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
cuisines = [f"cuisine_{i}" for i in range(1, 21)]  # 20 cuisines
interactions = ['click', 'like', 'booking']

user_interactions = []
for user in users:
    for cuisine in random.sample(cuisines, random.randint(1, 10)):
        interaction = {
            "user": user,
            "cuisine": cuisine,
            "interaction": random.choice(interactions),
            "value": random.randint(1, 5)  # Random interaction value between 1 and 5
        }
        user_interactions.append(interaction)

# Save interactions to a file
with open('data/user_interactions.json', 'w') as file:
    json.dump(user_interactions, file)
