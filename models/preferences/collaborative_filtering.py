import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Load the training data
train_data = pd.read_csv('data/train_data.csv')

# Convert the data into a format suitable for the surprise library
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(train_data[['user', 'item', 'rating']], reader)

# Use the SVD algorithm
algo = SVD()

# Perform cross-validation
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Train the algorithm on the train set
trainset = data.build_full_trainset()
algo.fit(trainset)

# Save the trained model
import pickle
with open('models/svd_model.pkl', 'wb') as file:
    pickle.dump(algo, file)
