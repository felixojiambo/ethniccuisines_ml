import json
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

# Load user reviews
with open('data/user_reviews.json', 'r') as file:
    reviews = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(reviews)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\b\w{1,2}\b', '', text)  # Remove short words
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

# Apply text cleaning
df['cleaned_review'] = df['review'].apply(clean_text)

# Tokenization and stop word removal
stop_words = set(stopwords.words('english'))
df['tokenized_review'] = df['cleaned_review'].apply(lambda x: [word for word in x.split() if word not in stop_words])

# TF-IDF feature extraction
tfidf = TfidfVectorizer(max_features=1000)
tfidf_matrix = tfidf.fit_transform(df['cleaned_review'])

# Save preprocessed data and TF-IDF model
df.to_csv('data/preprocessed_reviews.csv', index=False)
with open('data/tfidf_model.json', 'w') as file:
    json.dump(tfidf.vocabulary_, file)
