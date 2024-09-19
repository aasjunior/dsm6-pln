import nltk

text = 'Paulo Freire disse quando a educação não é libertadora, o sonho do oprimido é ser o opressor. ;( #FelizDiaDosProfessores #EducacaoLibertadora @PauloFreireOficial XD)'

# Objeto responsável pela identificação das características (emojis, tags e menções) durante o processo de tokenização
twiiterTokenizer = nltk.TweetTokenizer()

words = twiiterTokenizer.tokenize(text)

print(words)