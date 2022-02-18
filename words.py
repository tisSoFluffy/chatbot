import init
import nltk

from init import intents, kaggle_intents, c_intents

words = []
documents = []
classes = []
#print(f'words.py {len(words)}')
# for intent in intents['intents']:
#     for pattern in intent['patterns']:

#         w = nltk.word_tokenize(pattern)
#         words.extend(w)
#         documents.append((w, intent['tag']))

#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

#This is where the kaggle_dataset is implemented. Remove this if we do not want to train with it.
for intent in c_intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
