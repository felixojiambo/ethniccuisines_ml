import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Load preprocessed data
df = pd.read_csv('data/preprocessed_historical_user_data.csv')

# Prepare data for regression
X = df[['date', 'user']]
X['date'] = pd.to_datetime(X['date']).astype(int) / 10**9  # Convert date to numerical value
X = pd.get_dummies(X, columns=['user'])

y = df['preference_encoded']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the model
with open('models/predictive_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Make predictions
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
