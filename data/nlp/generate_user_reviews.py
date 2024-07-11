import json
import random

# Simulate user reviews
users = [f"user_{i}" for i in range(1, 101)]  # 100 users
cuisines = [f"cuisine_{i}" for i in range(1, 21)]  # 20 cuisines
reviews = [
    "Amazing food and great service.",
    "The ambiance was perfect, but the food was just okay.",
    "I loved the variety of dishes. Will visit again!",
    "Not worth the price. Overrated.",
    "A delightful experience overall. Highly recommended!",
    "The food was too spicy for my taste.",
    "Friendly staff and delicious meals.",
    "The dessert was the highlight of the meal.",
    "Not impressed with the hygiene standards.",
    "Authentic flavors and generous portions."
]

user_reviews = []
for user in users:
    for cuisine in random.sample(cuisines, random.randint(1, 5)):
        review = {
            "user": user,
            "cuisine": cuisine,
            "review": random.choice(reviews)
        }
        user_reviews.append(review)

# Save reviews to a file
with open('data/user_reviews.json', 'w') as file:
    json.dump(user_reviews, file)
