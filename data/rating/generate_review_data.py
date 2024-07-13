import json
import random
from datetime import datetime, timedelta

restaurants = [f"restaurant_{i}" for i in range(1, 51)]
users = [f"user_{i}" for i in range(1, 101)]
ratings = [1, 2, 3, 4, 5]

def generate_review():
    restaurant = random.choice(restaurants)
    user = random.choice(users)
    rating = random.choice(ratings)
    review_date = datetime.now() - timedelta(days=random.randint(0, 30))
    review = {
        "restaurant": restaurant,
        "user": user,
        "rating": rating,
        "review_date": review_date.strftime('%Y-%m-%d %H:%M:%S')
    }
    return review

# Generate sample review data
reviews = [generate_review() for _ in range(1000)]

# Save to a file
with open('data/reviews.json', 'w') as file:
    json.dump(reviews, file)
