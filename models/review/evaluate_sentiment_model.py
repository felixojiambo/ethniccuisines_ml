import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load true sentiments (assuming you have a file with true labels)
with open('data/true_sentiments.json', 'r') as file:
    true_sentiments = json.load(file)

# Load predicted sentiments
with open('data/sentiments.json', 'r') as file:
    predicted_sentiments = json.load(file)

# Calculate evaluation metrics
accuracy = accuracy_score(true_sentiments, predicted_sentiments)
precision = precision_score(true_sentiments, predicted_sentiments, average='weighted')
recall = recall_score(true_sentiments, predicted_sentiments, average='weighted')
f1 = f1_score(true_sentiments, predicted_sentiments, average='weighted')

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
