import json
import random

# Simulate user interaction data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
items = [f"restaurant_{i}" for i in range(1, 51)]  # 50 restaurants

interactions = []
for user in users:
    for item in items:
        if random.random() > 0.8:  # 20% chance of interaction
            interaction = {
                "user": user,
                "item": item,
                "rating": random.randint(1, 5)  # Random rating between 1 and 5
            }
            interactions.append(interaction)

# Save interactions to a file
with open('data/user_interactions.json', 'w') as file:
    json.dump(interactions, file)
