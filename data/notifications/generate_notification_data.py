import json
import random
import datetime

# Simulate user interaction data with notifications
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
notifications = ['new_restaurant', 'trending_cuisine', 'discount_offer', 'event_reminder']

user_notification_data = []
start_date = datetime.date(2023, 1, 1)
for user in users:
    date = start_date
    for _ in range(random.randint(10, 100)):
        interaction = {
            "user": user,
            "date": date.isoformat(),
            "notification": random.choice(notifications),
            "response": random.choice([0, 1])  # 0: ignored, 1: engaged
        }
        user_notification_data.append(interaction)
        date += datetime.timedelta(days=random.randint(1, 10))

# Save user notification data to a file
with open('data/user_notification_data.json', 'w') as file:
    json.dump(user_notification_data, file)
