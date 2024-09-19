import nltk

languages = nltk.SnowballStemmer.languages

text = 'O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.'


# Encontrar a origem/raiz/prefixo, o que é de comum na expressão (a partir dele é possivel criar diversas variações)
snowballStemmer = nltk.SnowballStemmer('portuguese')

stopwords = nltk.corpus.stopwords.words('portuguese')
words = nltk.word_tokenize(text.lower())

responses = []

for word in words:
    if not (word in stopwords):
        # responses.append(word)
        responses.append(snowballStemmer.stem(word))

# radicais = []

# for res in responses:
#    radicais.append(snowballStemmer.stem(res))

print(responses)