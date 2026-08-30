#Interagindo, diretamente, com banco de dados

import sqlite3
import pandas as pd


query = """
CREATE TABLE test
(A VARCHAR(30),
 B VARCHAR(20),
 C REAL,
 D INTEGER);

"""

c = sqlite3.connect('meusdados.sqlite')

c.execute(query)

c.commit()


dados = [('ALPHA', 'GAMA', 1.76, 7),
         ('BETA', 'DELTA', 2.7, 9),
         ('SIGMA', 'ETA', 9.8, 10)]


s = "INSERT INTO test VALUES(?, ?, ?, ?)"

c.executemany(s,dados)

c.commit()


#Fazendo consultas de SQL


d = c.execute("SELECT * FROM test")

linhas = d.fetchall()

print(linhas)


print(d.description)

#Construindo DataFrame

q = pd.DataFrame(linhas, columns=[y[0] for y in d.description])

print(q)