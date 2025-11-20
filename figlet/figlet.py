from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts_list = figlet.getFonts()
if not len(sys.argv) in [1,3]:
    sys.exit('Invalid usage')
if not sys.argv[2] in fonts_list:
    sys.exit("Invalid usage")


if len(sys.argv)==1:
    s = input('Input: ')
    ge = random.choice(fonts_list)
    figlet.setFont(font=ge)
    print(figlet.renderText(s))

elif len(sys.argv)==3:
    if sys.argv[1] in ['-f','--font']:
        s = input('Input: ')
        figlet.setFont(font=sys.argv[2])
        print("Output:")
        print(figlet.renderText(s))
    else:
        sys.exit('Invalid usage')

else:
    sys.exit('Invalid usage')


