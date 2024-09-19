import nltk

text = 'O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.'

# Diivide o texto em palavras através da localização de espaços
words = nltk.word_tokenize(text)

print(words)