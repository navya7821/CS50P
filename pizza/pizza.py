import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few arguments')

if len(sys.argv) >2 :
    sys.exit('Too many arguemnts')

x,y = sys.argv[1].split('.')
if not y == 'csv':
    sys.exit('Not a csv file')
if not x in ['sicilian','regular']:
    sys.exit('File doesnot exist')

table = []
with open(sys.argv[1],'r') as file:
    content = csv.reader(file)
    for line in content:
        table.append(line)


print(tabulate(table,headers='firstrow',tablefmt='grid'))






