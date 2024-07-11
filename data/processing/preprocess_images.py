import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Paths to the dataset
data_dir = 'path/to/food-101/images'
labels_file = 'path/to/food-101/meta/train.txt'

# Load image paths and labels
with open(labels_file, 'r') as f:
    lines = f.readlines()

image_paths = []
labels = []

for line in lines:
    image_path, label = line.strip().split('/')
    image_paths.append(os.path.join(data_dir, image_path + '.jpg'))
    labels.append(label)

# Convert labels to numerical format
label_to_index = {label: index for index, label in enumerate(sorted(set(labels)))}
labels = [label_to_index[label] for label in labels]

# Split the data into training and validation sets
train_paths, val_paths, train_labels, val_labels = train_test_split(image_paths, labels, test_size=0.2, random_state=42)

# Image data generator with augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

# Save the preprocessed data
np.save('data/train_paths.npy', train_paths)
np.save('data/val_paths.npy', val_paths)
np.save('data/train_labels.npy', train_labels)
np.save('data/val_labels.npy', val_labels)

# Save the label to index mapping
with open('data/label_to_index.json', 'w') as f:
    json.dump(label_to_index, f)
