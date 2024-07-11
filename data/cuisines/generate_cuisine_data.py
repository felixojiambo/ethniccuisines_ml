import json
import random

# Simulate user history data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
cuisines = [f"cuisine_{i}" for i in range(1, 21)]  # 20 cuisines

user_history = []
for user in users:
    for cuisine in random.sample(cuisines, random.randint(1, 10)):
        interaction = {
            "user": user,
            "cuisine": cuisine,
            "rating": random.randint(1, 5)  # Random rating between 1 and 5
        }
        user_history.append(interaction)

# Simulate social media trends data
social_media_trends = {cuisine: random.randint(50, 500) for cuisine in cuisines}

# Save user history and social media trends to files
with open('data/user_history.json', 'w') as file:
    json.dump(user_history, file)

with open('data/social_media_trends.json', 'w') as file:
    json.dump(social_media_trends, file)
