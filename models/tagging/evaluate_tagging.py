import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.models import load_model
import pickle

# Load models
with open('models/text_model.pkl', 'rb') as file:
    text_model = pickle.load(file)

image_model = load_model('models/image_model.h5')

# Load preprocessed data and labels
text_features = np.load('data/text_features.npy')
image_features = np.load('data/image_features.npy')

# Load labels for evaluation
with open('data/user_content.json', 'r') as file:
    content = json.load(file)

tags = ['food', 'restaurant', 'cuisine', 'location', 'experience']
text_labels = []
image_labels = []
for c in content:
    label_vector = [1 if tag in c['tags'] else 0 for tag in tags]
    if c['type'] == 'text':
        text_labels.append(label_vector)
    else:
        image_labels.append(label_vector)

text_labels = np.array(text_labels)
image_labels = np.array(image_labels)

# Evaluate NLP model
text_predictions = text_model.predict(text_features)
text_accuracy = accuracy_score(text_labels, text_predictions)
text_precision = precision_score(text_labels, text_predictions, average='micro')
text_recall = recall_score(text_labels, text_predictions, average='micro')
text_f1 = f1_score(text_labels, text_predictions, average='micro')

print(f"Text Model - Accuracy: {text_accuracy}, Precision: {text_precision}, Recall: {text_recall}, F1-Score: {text_f1}")

# Evaluate image recognition model
image_predictions = image_model.predict(image_features)
image_predictions = np.round(image_predictions)
image_accuracy = accuracy_score(image_labels, image_predictions)
image_precision = precision_score(image_labels, image_predictions, average='micro')
image_recall = recall_score(image_labels, image_predictions, average='micro')
image_f1 = f1_score(image_labels, image_predictions, average='micro')

print(f"Image Model - Accuracy: {image_accuracy}, Precision: {image_precision}, Recall: {image_recall}, F1-Score: {image_f1}")
