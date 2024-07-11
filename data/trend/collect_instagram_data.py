import instaloader
import json

# Initialize Instaloader
L = instaloader.Instaloader()

# Define hashtags to search
hashtags = ["ethnicfood", "ethniccuisine", "ethnicrestaurant"]
max_posts = 1000

# Collect posts
posts = []
for hashtag in hashtags:
    for post in instaloader.Hashtag.from_name(L.context, hashtag).get_posts():
        if len(posts) >= max_posts:
            break
        posts.append(post.caption)

# Save posts to a file
with open('data/instagram_posts.json', 'w') as file:
    json.dump(posts, file)
