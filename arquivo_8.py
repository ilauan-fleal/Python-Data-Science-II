import pandas as pd

import numpy as np

x = pd.DataFrame(np.random.randn(7, 4), columns=list('abcd'), index=['A','B','C','D','E','F','G'])

print(x)

k = lambda x: x.max() - x.min()

d = x.apply(k, axis='columns')

print('\n\n')

print(d)

r = x['a'].map(format)

print("\n\n")

print(r)

print('\n\n')

print(x.sort_index(axis=1, ascending=True))