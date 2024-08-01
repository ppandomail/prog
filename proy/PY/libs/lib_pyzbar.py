import cv2  # pip install opencv-python
import qrcode
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import io

qrcode.make("Hola mundo!!!").save("qr.png")

result = decode(cv2.imread("qr.png"), symbols=[ZBarSymbol.QRCODE])
print(result[0].data.decode('ascii'))
