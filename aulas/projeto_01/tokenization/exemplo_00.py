import nltk

# Definição do texto que passará pelo processo de tokenização
text = 'O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.'

# Irá dividir o texto recebido em sentenças
sentences = nltk.sent_tokenize(text)

print(sentences)