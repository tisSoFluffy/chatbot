from words import words, documents, classes
from libraries import lemmatizer, random, np
from sklearn.model_selection import train_test_split

# initializing training data
training = []

output_empty = [0] * len(classes)
for doc in documents:
    
    # initializing bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    #print(len(words))
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
#train_x = list(training[:,0])
#train_y = list(training[:,1])

X = list(training[:,0])
y = list(training[:,1])
train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.33, random_state=42)


print("Training data created")

#encoder = tf.keras.layers.experimental.preprocessing.TextVectorization()
#encoder.adapt()

vocab = []
for doc in documents:
    for word in doc[0]:
        root_word = lemmatizer.lemmatize(word.lower())
        if root_word not in vocab: vocab.append(root_word)

len(vocab)
