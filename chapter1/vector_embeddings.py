import numpy as np
from gensim.models import Word2Vec


sentences = [
    "That is a cute dog",
    "My cat is cute",
    "The dog is playing with the cat",
    "A cute puppy is running in the park",
    "My cat and dog are friends",
    "The park is a great place for a walk",
    "I love my cute pets"
]

# Normalize and tokenize sentences into words
sentences = [s.lower().split() for s in sentences]

# Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Word Vector
word_vector = model.wv['cute']
print(f"Cute vector:{word_vector}")

# Similar words
similar_words = model.wv.most_similar('cute')
print(f"Words most similar to cute {similar_words}")



