import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Load user content
with open('data/user_content.json', 'r') as file:
    content = json.load(file)

# Separate text and image content
text_content = [c for c in content if c['type'] == 'text']
image_content = [c for c in content if c['type'] == 'image']

# Text Preprocessing
text_data = [c['data'] for c in text_content]
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
text_features = tfidf_vectorizer.fit_transform(text_data)

# Image Preprocessing (assuming images are saved in a directory)
image_dir = 'data/images/'
image_features = []
for c in image_content:
    image_path = os.path.join(image_dir, f"{c['user']}_{c['data']}.jpg")  # Simulated image path
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image_features.append(image)

image_features = np.array(image_features)

# Save preprocessed data
np.save('data/text_features.npy', text_features.toarray())
np.save('data/image_features.npy', image_features)
