#Extraindo dados de uma API


import requests
import pandas as pd

link = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resposta = requests.get(link)

dados = resposta.json()

infos = pd.DataFrame(dados, columns=['number','title','labels','state'])

print(infos)