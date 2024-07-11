import json

# Load tweets
with open('data/tweets.json', 'r') as file:
    tweets = json.load(file)

# Load Instagram posts
with open('data/instagram_posts.json', 'r') as file:
    instagram_posts = json.load(file)

# Load Facebook posts
with open('data/facebook_posts.json', 'r') as file:
    facebook_posts = json.load(file)

# Aggregate all reviews
all_reviews = tweets + instagram_posts + facebook_posts

# Save aggregated reviews to a file
with open('data/all_reviews.json', 'w') as file:
    json.dump(all_reviews, file)
