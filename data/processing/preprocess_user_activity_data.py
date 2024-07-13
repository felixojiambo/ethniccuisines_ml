import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load user activity data
with open('data/user_activities.json', 'r') as file:
    user_activities = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(user_activities)

# Feature extraction: Convert categorical features to numerical
df['action'] = df['action'].astype('category').cat.codes
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute
df['second'] = df['timestamp'].dt.second

# Normalize features
scaler = StandardScaler()
df[['action', 'hour', 'minute', 'second']] = scaler.fit_transform(df[['action', 'hour', 'minute', 'second']])

# Save preprocessed data
df.to_csv('data/preprocessed_user_activities.csv', index=False)
