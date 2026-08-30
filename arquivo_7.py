import pandas as pd

import numpy as np

d1 = pd.DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'),
                  index=['Alpha', 'Gama', 'Beta'])


d2 = pd.DataFrame(np.arange(16).reshape(4,4), columns=list('abcd'),
                  index=['A','B','C','D'])


t = lambda y: y.max() - y.min()

n = d1.apply(t, axis='columns')

print(n)
