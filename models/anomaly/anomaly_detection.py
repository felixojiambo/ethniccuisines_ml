import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Load preprocessed data
df = pd.read_csv('data/preprocessed_user_activities.csv')

# Prepare data for anomaly detection
X = df[['action', 'hour', 'minute', 'second']]

# Fit Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(X)

# Evaluate the model (assuming we have ground truth labels for anomalies)
# For demonstration purposes, let's simulate ground truth labels
import random
df['true_anomaly'] = [random.choice([1, -1]) for _ in range(len(df))]

# Calculate evaluation metrics
print(classification_report(df['true_anomaly'], df['anomaly']))
