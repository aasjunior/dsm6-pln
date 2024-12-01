import pandas as pd
import numpy as np

# Criação da coleção de dados (corpus)
text = [
    "É amplamente elogiado por sua rapidez, ótima câmera e bateria durável, além de não travar durante o uso. O aparelho também é apreciado por suas funções adicionais como NFC e Smart View, e pelo excelente custo-benefício.",
    "Gostei bastante, a tela tem um ótimo tamanho... achei bem satisfatório para o preço do celular, não tenho com o que reclamar por enquanto, estou bem satisfeito!",
    "Celular muito bonito, veio tudo certinho!! só não gostei pq nã embalaram o cell em um saco bolha, e a caixa veio sem nenhuma proteção! mas o telefone não tem nenhum arranhão. Tirando isso, tudo certo.",
    "Dei de presente pra minha esposa... Por enquanto tudo certo.",
    "Por enquanto estou achando muito bom, fotos boas, respostas rápidas da biometria, além disso tem o smart view... fora isso ele é muito bom. Obs o carregador é fraco demorar para carregar o telefone um pouco.",
    "Produto muito bom bateria dura bastante só não gostei do tamanho, estou acostumado com celular maior,mas pra quem gosta recomendo podem comprar sem medo.",
    "O produto tem um design lindo, porém tem pouca durabilidade em relação à bateria... Só não faço a devolução devido a necessidade que eu tenho em relação ao aparelho.",
    "Eu não tive muito sorte com essa compra, esse celular está com um mês de uso e tá travando... ele não obedece.",
    "A qualidade das câmeras deixa muito a desejar, mas para um básico, dá pro gasto... precisa adquirir um separadamente.",
    "Celular mediano, esperava mais por ser samsung... travando o app usado no momento fazendo com que você desigualdade tela para reiniciar o app.",
    "Produto infelizmente após poucos meses de uso, apresenta defeitos de travamento e acessos remotos a apps e ligações.",
    "Produto muito bom bateria dura bastante só não gostei do tamanho...mas pra quem gosta recomendo podem comprar sem medo.",
    "O produto tem um design lindo, porém tem pouca durabilidade em relação à bateria... Só não faço a devolução devido a necessidade que eu tenho em relação ao aparelho.",
    "Ou configuração pois não me adaptei com o a15... mas faz parte, não é ruim mas a configuração tem que sofrer pois já fui em 2 técnico samsung.",
    "Produto veio errado e me foi negado o reembolso de forma descarada e ilegal com total desprezo ao consumidor.",
    "O meu só prestou 3 dias aí não carregou mais e eles não aceitaram a devolução fiquei no prejuízo.",
    "Péssima qualidade. Comprei com 1 mes de uso deu problema não tá carregando mais. Péssimo não comprem.",
    "É um celular bem lento. Bem devagar para abrir apps e executar tarefas simples como copiar e colar texto entre dois apps.",
    "O celular com 1 mês de uso apresentou problemas... Vou ter q mandar pra assistência técnica.",
    "O celular é bom, por onde sai o áudio que parece que não tem uma proteção é como se fosse outro celular que encaixaram em cima dele só tem metade da proteção do audio na parte de cima.",
    "Nem cinco dia de uso já começou a dar defeito... Mas o celular não 📵 👎. Minha primeira experiência, foi a desejar."
]


# Rótuloa atribuídos a cada texto armazenado dentro do corpus
classes = [
    "Positivo",  # É amplamente elogiado por sua rapidez, ótima câmera e bateria durável, além de não travar durante o uso. O aparelho também é apreciado por suas funções adicionais como NFC e Smart View, e pelo excelente custo-benefício.
    "Positivo",  # Gostei bastante, a tela tem um ótimo tamanho... achei bem satisfatório para o preço do celular, não tenho com o que reclamar por enquanto, estou bem satisfeito!
    "Neutro",    # Celular muito bonito, veio tudo certinho!! só não gostei pq nã embalaram o cell em um saco bolha, e a caixa veio sem nenhuma proteção! mas o telefone não tem nenhum arranhão. Tirando isso, tudo certo.
    "Neutro",    # Dei de presente pra minha esposa... Por enquanto tudo certo.
    "Positivo",  # Por enquanto estou achando muito bom, fotos boas, respostas rápidas da biometria, além disso tem o smart view... fora isso ele é muito bom. Obs o carregador é fraco demorar para carregar o telefone um pouco.
    "Positivo",  # Produto muito bom bateria dura bastante só não gostei do tamanho, estou acostumado com celular maior,mas pra quem gosta recomendo podem comprar sem medo.
    "Neutro",    # O produto tem um design lindo, porém tem pouca durabilidade em relação à bateria... Só não faço a devolução devido a necessidade que eu tenho em relação ao aparelho.
    "Negativo",  # Eu não tive muito sorte com essa compra, esse celular está com um mês de uso e tá travando... ele não obedece.
    "Neutro",    # A qualidade das câmeras deixa muito a desejar, mas para um básico, dá pro gasto... precisa adquirir um separadamente.
    "Negativo",  # Celular mediano, esperava mais por ser samsung... travando o app usado no momento fazendo com que você desigualdade tela para reiniciar o app.
    "Negativo",  # Produto infelizmente após poucos meses de uso, apresenta defeitos de travamento e acessos remotos a apps e ligações.
    "Positivo",  # Produto muito bom bateria dura bastante só não gostei do tamanho...mas pra quem gosta recomendo podem comprar sem medo.
    "Neutro",    # O produto tem um design lindo, porém tem pouca durabilidade em relação à bateria... Só não faço a devolução devido a necessidade que eu tenho em relação ao aparelho.
    "Neutro",    # Ou configuração pois não me adaptei com o a15... mas faz parte, não é ruim mas a configuração tem que sofrer pois já fui em 2 técnico samsung.
    "Negativo",  # Produto veio errado e me foi negado o reembolso de forma descarada e ilegal com total desprezo ao consumidor.
    "Negativo",  # O meu só prestou 3 dias aí não carregou mais e eles não aceitaram a devolução fiquei no prejuízo.
    "Negativo",  # Péssima qualidade. Comprei com 1 mes de uso deu problema não tá carregando mais. Péssimo não comprem.
    "Negativo",  # É um celular bem lento. Bem devagar para abrir apps e executar tarefas simples como copiar e colar texto entre dois apps.
    "Negativo",  # O celular com 1 mês de uso apresentou problemas... Vou ter q mandar pra assistência técnica.
    "Neutro",    # O celular é bom, por onde sai o áudio que parece que não tem uma proteção é como se fosse outro celular que encaixaram em cima dele só tem metade da proteção do audio na parte de cima.
    "Negativo"   # Nem cinco dia de uso já começou a dar defeito... Mas o celular não 📵 👎. Minha primeira experiência, foi a desejar.
]

# Cria a estrutura para armazenamento dos textos e classes (DataFrame)
df = pd.DataFrame({'texto': text, 'classe': classes})

df.to_csv('dataset.csv', index=False)

# Imprime o formato em que os dados são armazenados dentro do DataFrame
print(df)