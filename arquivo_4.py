#Novo exemplo de construção de DataFrame com Pandas!
import pandas as pd

dados = {'Letras':['A', 'B', 'C', 'D', 'E', 'F'],
         'ano':[2000,2001,2002,2003,2004,2005],
         'número':[1.1, 1.2, 1.3, 1.4, 1.5, 1.6]}



novo_frame = pd.DataFrame(dados, columns=['ano', 'Letras', 'número'], index=['um', 'dois', 'três', 'quatro', 'cinco', 'seis'])

outro_novo_frame = pd.DataFrame(dados, index=['um', 'dois', 'três', 'quatro','cinco','seis'], columns=['A','B','C'])
print('\n\n')
print(novo_frame)
print('\n\n')
print(outro_novo_frame)
