import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load clustered data
df = pd.read_csv('data/clustered_regional_dining_data.csv')

# Load the region-specific models
with open('models/region_specific_models.pkl', 'rb') as file:
    models = pickle.load(file)

# Evaluate the models
regions = df['region'].unique()

for region in regions:
    region_data = df[df['region'] == region]
    X = pd.get_dummies(region_data['cuisine'])
    y = region_data['popularity_normalized']
    
    model = models[region]
    y_pred = model.predict(X)
    
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    
    print(f"Region: {region} - MSE: {mse}, R2: {r2}")
