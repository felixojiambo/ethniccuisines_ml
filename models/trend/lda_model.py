import json
import gensim
from gensim import corpora

# Load preprocessed posts
with open('data/processed_posts.json', 'r') as file:
    processed_posts = json.load(file)

# Create dictionary and corpus for LDA
dictionary = corpora.Dictionary(processed_posts)
corpus = [dictionary.doc2bow(post) for post in processed_posts]

# Train LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

# Print topics
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)

# Save the model
lda_model.save('models/lda_model')
