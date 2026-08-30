#Manipulando base de dados com SqlAlchemy
import pandas as pd
import sqlalchemy as sqla

d = sqla.create_engine('sqlite:///meusdados.sqlite')

r = pd.read_sql('select * from test', d)

print(r)


