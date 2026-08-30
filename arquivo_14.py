
import csv

#Escrita de arquivo CSV

with open('arquivo.csv', 'w') as file:
    escrita = csv.writer(file)
    escrita.writerow(('Um', 'Dois', 'Três', 'Quatro'))
    escrita.writerow(('1', '2', '3', '4'))
    escrita.writerow(('5', '6', '7', '8'))
    escrita.writerow(('9', '10', '11', '12'))
    escrita.writerow(('13', '14', '15', '16'))

