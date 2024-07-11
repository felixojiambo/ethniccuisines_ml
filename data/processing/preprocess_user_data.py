import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load user interaction data
with open('data/user_interactions.json', 'r') as file:
    interactions = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(interactions)

# Encode categorical variables
df['interaction'] = df['interaction'].astype('category').cat.codes
df['cuisine'] = df['cuisine'].astype('category').cat.codes

# Normalize the data
scaler = StandardScaler()
df[['interaction', 'value', 'cuisine']] = scaler.fit_transform(df[['interaction', 'value', 'cuisine']])

# Save the preprocessed data
df.to_csv('data/preprocessed_user_data.csv', index=False)
