import pandas as pd
import pickle
from surprise import Dataset, Reader
from surprise.accuracy import rmse

# Load the test data
test_data = pd.read_csv('data/test_data.csv')

# Load the trained model
with open('models/svd_model.pkl', 'rb') as file:
    algo = pickle.load(file)

# Convert the test data into a format suitable for the surprise library
reader = Reader(rating_scale=(1, 5))
testset = Dataset.load_from_df(test_data[['user', 'item', 'rating']], reader).construct_testset(test_data.values)

# Predict ratings for the test set
predictions = algo.test(testset)

# Evaluate the model
rmse(predictions)
