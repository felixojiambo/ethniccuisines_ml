import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load regional dining data
with open('data/regional_dining_data.json', 'r') as file:
    regional_dining_data = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(regional_dining_data)

# Normalize popularity scores
scaler = StandardScaler()
df['popularity_normalized'] = scaler.fit_transform(df[['popularity']])

# Save preprocessed data
df.to_csv('data/preprocessed_regional_dining_data.csv', index=False)
