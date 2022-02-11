import init
import nltk

from init import intents

words = []
documents = []
classes = []
print(f'words.py {len(words)}')
for intent in intents['intents']:
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])
