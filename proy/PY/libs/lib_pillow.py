'''

Pillow

. URL: https://pillow.readthedocs.io/en/stable/

'''

from PIL import Image

im  = Image.open('qr.png')
print(im.format, im.size, im.mode)
im.show()

