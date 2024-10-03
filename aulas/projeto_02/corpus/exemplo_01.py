import pandas as pd
import numpy as np

# Criação da coleção de dados (corpus)
text = [
    'O rato roeu a roupa do rei de Roma', 
    'Vagabundo tem em todo lugar!', 
    'A situação faz o sapo pular', 
    'Não gostou, processa!', 
    'Você é um moleque', 
    'O rato reou o processo do vagabundo. Se fosse na minha empresa, você já estava fora!'
]

# Rótuloa atribuídos a cada texto armazenado dentro do corpus
classes = ['S1MP50N', 'LANCHES', 'LANCHES', 'S1MP50N', 'S1MP50N', 'LANCHES']

# Cria a estrutura para armazenamento dos textos e classes (DataFrame)
df = pd.DataFrame({'texto': text, 'classe': classes})

# Imprime o formato em que os dados são armazenados dentro do DataFrame
print(df)