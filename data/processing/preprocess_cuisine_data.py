import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load user history and social media trends data
with open('data/user_history.json', 'r') as file:
    user_history = json.load(file)

with open('data/social_media_trends.json', 'r') as file:
    social_media_trends = json.load(file)

# Convert user history to DataFrame
df = pd.DataFrame(user_history)

# Normalize social media trends
trend_values = list(social_media_trends.values())
scaler = MinMaxScaler()
normalized_trends = scaler.fit_transform(pd.DataFrame(trend_values))

# Add social media trends as features to the DataFrame
df['social_media_trend'] = df['cuisine'].apply(lambda x: normalized_trends[cuisines.index(x)][0])

# Convert categorical data to numerical data
df['user'] = df['user'].astype('category').cat.codes
df['cuisine'] = df['cuisine'].astype('category').cat.codes

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Save preprocessed data
train_data.to_csv('data/train_data.csv', index=False)
test_data.to_csv('data/test_data.csv', index=False)
