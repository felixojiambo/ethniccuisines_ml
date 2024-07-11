import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load reviews from file
with open('data/all_reviews.json', 'r') as file:
    reviews = json.load(file)

# Preprocess reviews
def preprocess_text(text):
    # Remove URLs, mentions, hashtags, and special characters
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords and short tokens
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    
    return " ".join(tokens)

# Apply preprocessing
processed_reviews = [preprocess_text(review) for review in reviews]

# Save preprocessed reviews to a file
with open('data/processed_reviews.json', 'w') as file:
    json.dump(processed_reviews, file)
