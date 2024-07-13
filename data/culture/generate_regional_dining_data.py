import json
import random

# Simulate regional dining data
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
cuisines = ['sushi', 'pizza', 'tacos', 'pasta', 'burgers', 'curry', 'dumplings', 'paella']

regional_dining_data = []
for region in regions:
    for cuisine in cuisines:
        popularity = random.uniform(0, 1)  # Popularity score between 0 and 1
        dining_entry = {
            "region": region,
            "cuisine": cuisine,
            "popularity": popularity
        }
        regional_dining_data.append(dining_entry)

# Save regional dining data to a file
with open('data/regional_dining_data.json', 'w') as file:
    json.dump(regional_dining_data, file)
