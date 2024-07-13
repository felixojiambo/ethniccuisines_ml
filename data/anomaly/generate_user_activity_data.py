import json
import random
from datetime import datetime, timedelta

users = [f"user_{i}" for i in range(1, 101)]
actions = ["click", "like", "search", "add_to_cart", "purchase"]

def generate_user_activity():
    user = random.choice(users)
    action = random.choice(actions)
    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))
    activity = {
        "user": user,
        "action": action,
        "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S')
    }
    return activity

# Generate sample user activity data
user_activities = [generate_user_activity() for _ in range(1000)]

# Save to a file
with open('data/user_activities.json', 'w') as file:
    json.dump(user_activities, file)
