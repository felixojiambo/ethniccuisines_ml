import json
import pandas as pd
from sklearn.model_selection import train_test_split

# Load user interaction data
with open('data/user_interactions.json', 'r') as file:
    interactions = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(interactions)

# Normalize and structure the data
df['user'] = df['user'].astype('category').cat.codes
df['item'] = df['item'].astype('category').cat.codes

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Save preprocessed data
train_data.to_csv('data/train_data.csv', index=False)
test_data.to_csv('data/test_data.csv', index=False)
