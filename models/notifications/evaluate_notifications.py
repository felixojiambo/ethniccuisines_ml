import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Load preprocessed data
df = pd.read_csv('data/preprocessed_notification_data.csv')

# Load the bandit models
with open('models/user_bandits.pkl', 'rb') as file:
    user_bandits = pickle.load(file)

# Prepare data for evaluation
users = df['user'].unique()
notifications = df['notification_encoded'].unique()

# Evaluate the bandit algorithm
total_interactions = 0
successful_interactions = 0

for user in users:
    user_data = df[df['user'] == user]
    bandit = user_bandits[user]
    
    for index, row in user_data.iterrows():
        notification = row['notification_encoded']
        response = row['response']
        
        chosen_arm = bandit.select_arm()
        if notification == chosen_arm and response == 1:
            successful_interactions += 1
        total_interactions += 1

# Calculate engagement rate
engagement_rate = successful_interactions / total_interactions
print(f"Engagement Rate: {engagement_rate}")

# Calculate other metrics
# For reinforcement learning, these metrics might be less relevant, but let's use them for comparison
y_true = df['response']
y_pred = [user_bandits[row['user']].select_arm() == row['notification_encoded'] for _, row in df.iterrows()]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
