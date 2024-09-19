import nltk

text = 'O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.'

stopwords = nltk.corpus.stopwords.words('portuguese')
words = nltk.word_tokenize(text.lower())

responses = []

for word in words:
    if not (word in stopwords):
        responses.append(word)

print(responses)