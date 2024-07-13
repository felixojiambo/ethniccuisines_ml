import json
import numpy as np
from sklearn.neural_network import MLPClassifier
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

# Load preprocessed data
text_features = np.load('data/text_features.npy')
image_features = np.load('data/image_features.npy')

# Load tags for training
with open('data/user_content.json', 'r') as file:
    content = json.load(file)

tags = ['food', 'restaurant', 'cuisine', 'location', 'experience']

# Create tag label arrays
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

# Train NLP model
text_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
text_model.fit(text_features, text_labels)

# Train CNN model for image recognition
image_model = Sequential()
image_model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
image_model.add(MaxPooling2D((2, 2)))
image_model.add(Conv2D(64, (3, 3), activation='relu'))
image_model.add(MaxPooling2D((2, 2)))
image_model.add(Flatten())
image_model.add(Dense(128, activation='relu'))
image_model.add(Dense(len(tags), activation='sigmoid'))

image_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
image_model.fit(image_features, image_labels, epochs=10, batch_size=32)

# Save models
import pickle
with open('models/text_model.pkl', 'wb') as file:
    pickle.dump(text_model, file)

image_model.save('models/image_model.h5')
