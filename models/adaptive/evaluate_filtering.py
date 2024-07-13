import json
import pandas as pd

# Load user preferences
with open('data/user_preferences.json', 'r') as file:
    user_preferences = json.load(file)

# Simulate user engagement data
user_engagement = []
for user in user_preferences.keys():
    engagement = {
        "user": user,
        "satisfaction_score": random.uniform(1, 5),  # Simulate user satisfaction score between 1 and 5
        "engagement_score": random.uniform(1, 10)  # Simulate user engagement score between 1 and 10
    }
    user_engagement.append(engagement)

# Save engagement data to a file
with open('data/user_engagement.json', 'w') as file:
    json.dump(user_engagement, file)

# Load engagement data
with open('data/user_engagement.json', 'r') as file:
    engagement_data = json.load(file)

# Convert to pandas DataFrame
df_engagement = pd.DataFrame(engagement_data)

# Calculate average satisfaction and engagement scores
average_satisfaction = df_engagement['satisfaction_score'].mean()
average_engagement = df_engagement['engagement_score'].mean()

print(f"Average User Satisfaction Score: {average_satisfaction}")
print(f"Average User Engagement Score: {average_engagement}")
