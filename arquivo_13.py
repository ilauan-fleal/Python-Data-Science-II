#Realizando leitura de arquivo .csv
import csv




with open("exemplo.csv") as file:
    linhas = list(csv.reader(file))


for x in linhas:
    print(x)

cabecalho = linhas[0]
valores = linhas[1:]

dicionario = {x: y for x, y in zip(cabecalho,zip(*valores))}

print('\n\n')

for k, v in dicionario.items():
    print(f"{k} : {v}\n")