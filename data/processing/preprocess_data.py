import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load tweets from file
with open('data/tweets.json', 'r') as file:
    tweets = json.load(file)

# Load Instagram posts from file
with open('data/instagram_posts.json', 'r') as file:
    instagram_posts = json.load(file)

# Load Facebook posts from file
with open('data/facebook_posts.json', 'r') as file:
    facebook_posts = json.load(file)

# Combine all posts
all_posts = tweets + instagram_posts + facebook_posts

# Preprocess tweets
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
    
    return tokens

# Apply preprocessing
processed_posts = [preprocess_text(post) for post in all_posts]

# Save preprocessed posts to a file
with open('data/processed_posts.json', 'w') as file:
    json.dump(processed_posts, file)
