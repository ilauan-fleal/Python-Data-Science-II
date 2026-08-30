#Mais códigos utilizando pandas!

import pandas as pd
import numpy as np

dados = pd.date_range('1/01/2000', periods=9)

n = pd.Series(np.arange(9), index=dados)

n.to_csv('exemplo.csv')

