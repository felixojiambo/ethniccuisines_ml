import pandas as pd
from prefixspan import PrefixSpan

# Load clustered user data
df = pd.read_csv('data/clustered_user_data.csv')

# Group interactions by user to create sequences
user_sequences = df.groupby('user').apply(lambda x: x.sort_values('cuisine')['cuisine'].tolist()).tolist()

# Apply PrefixSpan algorithm
ps = PrefixSpan(user_sequences)
patterns = ps.frequent(5)  # Minimum support threshold of 5

# Print frequent patterns
for pattern in patterns:
    print(pattern)
