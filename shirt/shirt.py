import PIL
import sys
import os
from PIL import Image
with Image.open('shirt.png') as img:
    size_image = img.size

if len(sys.argv) < 3:
    sys.exit('Too few arguments')
if len(sys.argv) > 3:
    sys.exit('Too many arguments')

onex, oney = os.path.splitext(sys.argv[1])
twox , twoy = os.path.splitext(sys.argv[2])
if not  oney.lower() or twoy.lower in ['jpg','jpeg','png']:
    sys.exit('Invalid output')
elif not oney == twoy:
    sys.exit('Input and output have different extensions')
try:
    with Image.open(sys.argv[1],'r') as file:
        sized = PIL.ImageOps.fit(file,size = size_image)
        with Image.open('shirt.png') as shirt:
            sized.paste(shirt,shirt)
            sized.save(sys.argv[2])

except FileNotFoundError:
    sys.exit('Input doesnot exist')





