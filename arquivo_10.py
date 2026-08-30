#Criando DataFrame Dinâmico

import pandas as pd

dados = pd.DataFrame({'ALPHA':[1,2,3,4,5,6,7],
                      'GAMA':[0,7,8,9,10,11,12],
                      'BETA':[0,0,0,0,0,0,0]},index=[1,2,3,4,5,6,7])

print(dados)

