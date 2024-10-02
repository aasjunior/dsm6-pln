import nltk

wordNetLemmatizer = nltk.stem.WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')

text = 'Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold with those who favor fire.'

words = nltk.word_tokenize(text.lower())

responses = []

for word in words:
    if not (word in stopwords):
        responses.append(wordNetLemmatizer.lemmatize(word))

print(responses)