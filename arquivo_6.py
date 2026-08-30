#Alinhamento de dados!

import pandas as pd

import numpy as np

d1 = pd.DataFrame(np.arange(9).reshape(3,3),
                  index=['Alpha', 'Gama', 'Beta'],
                  columns=list('AbC'))


d2 = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('abcd'),
                  index=['A','B','C','D'])

print('\n\n')

print(d1)

print('\n\n')

print(d2)

