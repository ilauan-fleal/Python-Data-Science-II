import pandas as pd
import sys
#Utilizando pandas, para fazer leitura de arquivo


resultado = pd.read_table('arquivo.txt',sep=f'\\s+')

print(resultado)

#Escrita de arquivo csv:


resultado.to_csv(sys.stdout, sep='|')

