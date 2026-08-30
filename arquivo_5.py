#Explorando o método reindex com Pandas!

import pandas as pd
import numpy as np

Frame = pd.DataFrame(np.arange(16).reshape(4, 4), index=['A', 'B', 'C', 'D'], columns=['Alpha', 'Gama', 'Beta', 'Delta'])

novo_frame = Frame.reindex(['A','b','C','d'])

print(novo_frame)

print('\n\n')

print(novo_frame.iloc[0:2])

print('\n\n')

print(novo_frame.loc['A':'C'])