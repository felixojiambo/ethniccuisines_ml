import json
import gensim
from gensim.models.coherencemodel import CoherenceModel

# Load preprocessed posts
with open('data/processed_posts.json', 'r') as file:
    processed_posts = json.load(file)

# Load dictionary and corpus
dictionary = gensim.corpora.Dictionary.load('models/lda_model.id2word')
corpus = [dictionary.doc2bow(post) for post in processed_posts]

# Load LDA model
lda_model = gensim.models.ldamodel.LdaModel.load('models/lda_model')

# Compute coherence score
coherence_model_lda = CoherenceModel(model=lda_model, texts=processed_posts, dictionary=dictionary, coherence='c_v')
coherence_score = coherence_model_lda.get_coherence()

print(f'Coherence Score: {coherence_score}')
