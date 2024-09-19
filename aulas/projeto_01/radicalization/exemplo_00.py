import nltk

languages = nltk.SnowballStemmer.languages

# Encontrar a origem/raiz/prefixo, o que é de comum na expressão (a partir dele é possivel criar diversas variações)
snowballStemmer = nltk.SnowballStemmer('portuguese')

word1 = 'computador'
word2 = 'computação'
word3 = 'computando'
word4 = 'menino'
word5 = 'meninos'
word6 = 'menina'
word7 = 'menin'

print(snowballStemmer.stem(word1))
print(snowballStemmer.stem(word2))
print(snowballStemmer.stem(word3))
print(snowballStemmer.stem(word4))
print(snowballStemmer.stem(word5))
print(snowballStemmer.stem(word6))
print(snowballStemmer.stem(word7))

# print(languages)
