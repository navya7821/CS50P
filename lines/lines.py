import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
file_name = sys.argv[1]
x,y = file_name.split('.')
if not y == 'py':
    sys.exit("Not a python File")


try:
    with open(sys.argv[1],"r") as file:
        content = file.readlines()
        count = len(content)
        for line in content :
            stripped = line.strip()
            if stripped == '':
                count -=1
            elif stripped.startswith('#'):
                count-=1





except FileNotFoundError:
    sys.exit('File does not exist')
except IndexError:
    pass
print(count)
