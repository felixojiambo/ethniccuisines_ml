import numpy as np
import json
import tensorflow as tf
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd

# Load preprocessed data
val_paths = np.load('data/val_paths.npy')
val_labels = np.load('data/val_labels.npy')

# Load label to index mapping
with open('data/label_to_index.json', 'r') as f:
    label_to_index = json.load(f)

# Image data generator
val_datagen = ImageDataGenerator(rescale=1./255)

# Create validation data generator
val_generator = val_datagen.flow_from_dataframe(
    dataframe=pd.DataFrame({'filename': val_paths, 'class': val_labels}),
    x_col='filename',
    y_col='class',
    target_size=(224, 224),
    batch_size=32,
    class_mode='raw',
    shuffle=False
)

# Load the trained model
model = tf.keras.models.load_model('models/food_cnn_model.h5')

# Predict on validation data
val_predictions = model.predict(val_generator)
val_pred_labels = np.argmax(val_predictions, axis=1)

# Classification report
report = classification_report(val_labels, val_pred_labels, target_names=list(label_to_index.keys()))
print(report)
