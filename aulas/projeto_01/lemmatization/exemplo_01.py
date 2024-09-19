import nltk
from nltk.corpus import wordnet

# Função para mapear o POS tag do nltk para o formato do WordNet
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default para substantivos

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

wordNetLemmatizer = nltk.stem.WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')

text = 'Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold with those who favor fire.'

words = nltk.word_tokenize(text.lower())

# Obtenção das tags POS
pos_tags = nltk.pos_tag(words)

responses = []

for word, tag in pos_tags:
    if not (word in stopwords):
        responses.append(wordNetLemmatizer.lemmatize(word, get_wordnet_pos(tag)))

print(responses)