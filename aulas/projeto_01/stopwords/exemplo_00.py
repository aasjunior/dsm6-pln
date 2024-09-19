import nltk

text = 'O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.'

# stopwords -> palavras não ligadas diretamente ao contexto (artigos, preposições, pronomes...)
stopwords = ['o', 'O', 'a', 'do', 'de']

words = nltk.word_tokenize(text)

responses = []

for word in words:
    if not (word in stopwords):
        responses.append(word)

print(responses)