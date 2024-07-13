import json
import random
import datetime

# Simulate historical user data
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
preferences = ['sushi', 'pizza', 'tacos', 'pasta', 'burgers']

user_data = []
start_date = datetime.date(2023, 1, 1)
for user in users:
    date = start_date
    for _ in range(random.randint(10, 100)):
        interaction = {
            "user": user,
            "date": date.isoformat(),
            "preference": random.choice(preferences)
        }
        user_data.append(interaction)
        date += datetime.timedelta(days=random.randint(1, 10))

# Save user data to a file
with open('data/historical_user_data.json', 'w') as file:
    json.dump(user_data, file)
