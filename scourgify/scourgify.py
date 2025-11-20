import csv
import sys
if len(sys.argv) > 3:
    sys.exit('Too many arguments')
if len(sys.argv) < 3:
    sys.exit('Too few arguments')
x,y = sys.argv[1].split('.')

if not y  == 'csv':
    sys.exit('Not a csv file')


a,b = sys.argv[2].split('.')
if not b == 'csv':
    sys.exit('Not a csv file')

with open(sys.argv[1],'r') as file:
    content = csv.DictReader(file)
    with open(sys.argv[2],'w') as book:
        writer = csv.DictWriter(book,fieldnames = ['first','last','house'])
        writer.writeheader()
        for line in content:
            person = line['name']
            home = line['house']
            lastname,firstname = person.split(',')
            writer.writerow({'first':firstname.strip(),'last':lastname.strip(),'house':home.strip()})




