#Construindo dataframes com o pandas!

import pandas as pd

dados = {'Letras':['Alpha', 'Gama', 'Beta', 'Delta'],
         'ano':[2000,2001,2002,2003],
         'número':[1.1, 1.2, 1.3, 1.4]}



estrutura = pd.DataFrame(dados)
print(estrutura)