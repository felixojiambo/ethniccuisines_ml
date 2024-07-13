import pandas as pd
import numpy as np
import random

class MultiArmedBandit:
    def __init__(self, n_arms):
        self.n_arms = n_arms
        self.counts = np.zeros(n_arms)
        self.values = np.zeros(n_arms)

    def select_arm(self):
        epsilon = 0.1
        if random.random() > epsilon:
            return np.argmax(self.values)
        else:
            return random.randrange(self.n_arms)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value

# Load preprocessed data
df = pd.read_csv('data/preprocessed_notification_data.csv')

# Prepare data
users = df['user'].unique()
notifications = df['notification_encoded'].unique()
n_arms = len(notifications)

# Initialize the bandit algorithm for each user
user_bandits = {user: MultiArmedBandit(n_arms) for user in users}

# Simulate the reinforcement learning process
for index, row in df.iterrows():
    user = row['user']
    notification = row['notification_encoded']
    response = row['response']
    
    bandit = user_bandits[user]
    chosen_arm = bandit.select_arm()
    
    # Simulate sending a notification
    reward = response if notification == chosen_arm else 0
    bandit.update(chosen_arm, reward)

# Save the bandit models
import pickle
with open('models/user_bandits.pkl', 'wb') as file:
    pickle.dump(user_bandits, file)
