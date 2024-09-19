import nltk

# Conjunto de textos que passarão pelo processo de tokenização por palavras
texts = ['O rato roeu a roupa do rei de Roma. O rei de Roma matou o rato.', 'A situação faz o sapo pular.', 'Se fosse na minha empresa...', 'Já dizia o Datena, é brinCADEIRA!']

responses = []

for text in texts:
    responses.append(nltk.word_tokenize(text))

print(responses)