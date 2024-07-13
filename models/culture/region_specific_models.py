import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load clustered data
df = pd.read_csv('data/clustered_regional_dining_data.csv')

# Create region-specific models
regions = df['region'].unique()
models = {}

for region in regions:
    region_data = df[df['region'] == region]
    X = pd.get_dummies(region_data['cuisine'])
    y = region_data['popularity_normalized']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Region: {region} - MSE: {mse}, R2: {r2}")
    
    models[region] = model

# Save the region-specific models
import pickle
with open('models/region_specific_models.pkl', 'wb') as file:
    pickle.dump(models, file)
