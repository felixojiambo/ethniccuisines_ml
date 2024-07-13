import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")

# Save the model
import pickle
with open('models/predictive_model.pkl', 'wb') as file:
    pickle.dump(model, file)
