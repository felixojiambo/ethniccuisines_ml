import requests
import json

# Facebook API credentials
access_token = "YOUR_ACCESS_TOKEN"
search_query = "ethnicfood OR ethniccuisine OR ethnicrestaurant"
max_posts = 1000

# Define the API endpoint
url = f"https://graph.facebook.com/v12.0/search?q={search_query}&type=post&access_token={access_token}"

# Collect posts
posts = []
while len(posts) < max_posts:
    response = requests.get(url)
    data = response.json()
    posts.extend(data['data'])
    if 'paging' in data and 'next' in data['paging']:
        url = data['paging']['next']
    else:
        break

# Save posts to a file
with open('data/facebook_posts.json', 'w') as file:
    json.dump(posts, file)
