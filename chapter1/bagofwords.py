# Chapter 1 

# Tokenizing Sentences

# Create Sentences 
s1 = "That is a cute dog"
s2 = "My cat is cute"
# Normalize
s1 = s1.lower()
s2 = s2.lower()
# Tokenize
tokens = s1.split() + s2.split()
# Vocabulary 
vocab = {}
for t in tokens:
    if t not in vocab:
        vocab[t] = 1
    else:
        vocab[t] += 1

# Create the model of this unique set of vocab 
vector_model = []
for k in vocab.keys():
    vector_model.append(k)

# Initialize bag of words
bagofwords = {}
for w in vector_model:
    bagofwords[w] = 0
# All keys are unique words created across both sentences

# Test an input against the current vocab against the representation model or vector representation

input = "My cat is cute"
input = input.lower().split()

# Count the words
for w in input:
    if w in bagofwords:
        bagofwords[w] += 1

print(bagofwords)

