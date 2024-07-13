import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load user notification data
with open('data/user_notification_data.json', 'r') as file:
    notification_data = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(notification_data)

# Convert dates to datetime
df['date'] = pd.to_datetime(df['date'])

# Encode notifications as numeric values
label_encoder = LabelEncoder()
df['notification_encoded'] = label_encoder.fit_transform(df['notification'])

# Save preprocessed data
df.to_csv('data/preprocessed_notification_data.csv', index=False)
