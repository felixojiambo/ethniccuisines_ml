import json
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Load user preferences
with open('data/user_preferences.json', 'r') as file:
    preferences = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(preferences)

# One-hot encode preferred cuisines
mlb = MultiLabelBinarizer()
df = df.join(pd.DataFrame(mlb.fit_transform(df.pop('preferred_cuisines')),
                          columns=mlb.classes_,
                          index=df.index))

# Save preprocessed data
df.to_csv('data/preprocessed_user_preferences.csv', index=False)
