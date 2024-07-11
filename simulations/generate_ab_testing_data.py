import json
import random

# Simulate user interaction data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
cuisines = [f"cuisine_{i}" for i in range(1, 21)]  # 20 cuisines

user_interactions = []
for user in users:
    for cuisine in random.sample(cuisines, random.randint(1, 10)):
        interaction = {
            "user": user,
            "cuisine": cuisine,
            "interaction_type": random.choice(["click", "like", "booking"]),
            "interaction_value": random.randint(1, 5)  # Random interaction value between 1 and 5
        }
        user_interactions.append(interaction)

# Save interactions to a file
with open('data/user_interactions_ab_testing.json', 'w') as file:
    json.dump(user_interactions, file)
