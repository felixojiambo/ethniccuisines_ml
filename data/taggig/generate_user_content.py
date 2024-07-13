import json
import random

# Simulate user-generated content
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
tags = ['food', 'restaurant', 'cuisine', 'location', 'experience']
content_types = ['text', 'image']

user_content = []
for user in users:
    for _ in range(random.randint(1, 5)):
        content = {
            "user": user,
            "type": random.choice(content_types),
            "data": f"Sample content data {_} from {user}",
            "tags": random.sample(tags, random.randint(1, 3))
        }
        user_content.append(content)

# Save user content to a file
with open('data/user_content.json', 'w') as file:
    json.dump(user_content, file)
