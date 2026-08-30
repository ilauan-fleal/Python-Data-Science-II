import pandas as pd


#Aplicando pandas diretamente, sobre um dicionário!


dados = {'Alpha': 8000, 'Gama':9500, 'Beta': 12000, 'Delta': 15000}

p = pd.Series(dados)

print(p)