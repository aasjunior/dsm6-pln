import nltk

# Técnica para entender a mnatureza das palavras presentes no corpus
# Classificação das palavreas por meio da classe gramatical

text = 'O rato roeu a roupa do rei de Roma.'

words = nltk.word_tokenize(text.lower())

stopwords = nltk.corpus.stopwords.words('portuguese')

responses = []

for word in words:
    if not (word in stopwords):
        responses.append(word)

print(responses)

# Entender o significado das palavras - Analise semantica
categories = nltk.pos_tag(responses)

pos_tagging = nltk.ne_chunk(categories)

print(pos_tagging)