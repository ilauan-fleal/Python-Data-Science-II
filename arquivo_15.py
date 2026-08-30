import pandas as pd
from lxml import objectify



#Fazendo leitura de arquivo json

dados = pd.read_json('db.json')

print(dados)

print('\n\n')

#Processamento de arquivo.xml

arquivo = 'Performance_MNR.xml'

parse = objectify.parse(open(arquivo))

rota = parse.getroot()


listagem = []

campos = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']


for x in rota.INDICATOR:
    todos_os_dados = {}
    for y in x.getchildren():
        if y.tag in campos:
            continue
        todos_os_dados[y.tag] = y.pyval
    listagem.append(todos_os_dados)


p = pd.DataFrame(listagem)

print(p)

