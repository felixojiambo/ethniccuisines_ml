import json
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load preprocessed reviews
with open('data/processed_reviews.json', 'r') as file:
    reviews = json.load(file)

# Load pre-trained BERT model and tokenizer for sentiment analysis
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment
def predict_sentiment(review):
    inputs = tokenizer.encode_plus(review, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment = torch.argmax(probs).item()
    return sentiment

# Predict sentiments for all reviews
sentiments = [predict_sentiment(review) for review in reviews]

# Save sentiments to a file
with open('data/sentiments.json', 'w') as file:
    json.dump(sentiments, file)
