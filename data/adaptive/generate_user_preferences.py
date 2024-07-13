import json
import random

# Simulate user preference data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
cuisines = [f"cuisine_{i}" for i in range(1, 21)]  # 20 cuisines

user_preferences = []
for user in users:
    preferences = {
        "user": user,
        "preferred_cuisines": random.sample(cuisines, random.randint(1, 10))
    }
    user_preferences.append(preferences)

# Save preferences to a file
with open('data/user_preferences.json', 'w') as file:
    json.dump(user_preferences, file)
