
#? .csv file

import csv

# crea un archivo csv que es una hoja de excel
csv_file = open('datos.csv', 'w',)

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'country', 'lenguage'])
csv_writer.writerow(['Juan', 'Gonzalez', 25, 'Spain', 'Spanish'])
csv_writer.writerow(['Maria', 'Gonzalez', 30, 'Spain', 'Spanish'])
csv_writer.writerow(['Pedro', 'Gonzalez', 35, 'Spain', 'Spanish'])

csv_file.close()

with open('datos.csv', 'r') as csv_file:
    for line in csv_file:
        print(line)