import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load data with predicted anomalies and true labels
df = pd.read_csv('data/preprocessed_user_activities.csv')

# Assuming the 'anomaly' column contains the model's predictions and 'true_anomaly' contains the ground truth
precision = precision_score(df['true_anomaly'], df['anomaly'])
recall = recall_score(df['true_anomaly'], df['anomaly'])
f1 = f1_score(df['true_anomaly'], df['anomaly'])

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")
