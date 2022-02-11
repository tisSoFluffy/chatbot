import words as wo
from libraries import lemmatizer, pickle
from init import words, documents, classes, ignore_words

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), 'unique lemmatized words',words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes,open('classes.pkl', 'wb'))