import nltk

# Transformação da palavra para sua versão original/natural (infinitivo/singular)
# Funciona para latin e inglês, mas não português :/
wordNetLemmatizer = nltk.stem.WordNetLemmatizer()

word1 = wordNetLemmatizer.lemmatize('alunos')
word2 = wordNetLemmatizer.lemmatize('corpora')
word3 = wordNetLemmatizer.lemmatize('girls')

# pos -> cria uma classificação para determinada palavra (a -> adjetivo)
word4 = wordNetLemmatizer.lemmatize('better', pos='a')

# qual verbo originou a palavra clustering
word5 = wordNetLemmatizer.lemmatize('clustering', pos='v')

print(word1) # alunos
print(word2) # corpus
print(word3) # girl
print(word4) # good
print(word5) # cluster