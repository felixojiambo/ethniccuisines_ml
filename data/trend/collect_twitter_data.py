import tweepy
import json

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Set up tweepy authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define search criteria
search_query = "#ethnicfood OR #ethniccuisine OR #ethnicrestaurant"
max_tweets = 1000  # Define the number of tweets to collect

# Collect tweets
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q=search_query, lang="en", tweet_mode='extended').items(max_tweets):
    tweets.append(tweet.full_text)

# Save tweets to a file
with open('data/tweets.json', 'w') as file:
    json.dump(tweets, file)
