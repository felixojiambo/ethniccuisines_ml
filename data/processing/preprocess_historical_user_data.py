import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load user data
with open('data/historical_user_data.json', 'r') as file:
    user_data = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(user_data)

# Convert dates to datetime
df['date'] = pd.to_datetime(df['date'])

# Encode preferences as numeric values
label_encoder = LabelEncoder()
df['preference_encoded'] = label_encoder.fit_transform(df['preference'])

# Save preprocessed data
df.to_csv('data/preprocessed_historical_user_data.csv', index=False)
