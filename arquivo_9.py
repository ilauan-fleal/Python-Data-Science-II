#Obtendo um array de índices!

import pandas as pd

x = pd.Series(['A','B','C','D','E','F'])

y = pd.Series(['A','B','C'])

z = pd.Index(x).get_indexer(y)

print(z)

