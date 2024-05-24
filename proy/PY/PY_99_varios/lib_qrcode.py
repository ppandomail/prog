import qrcode
import io

qrcode.make("Hola mundo!!!").save("qr.png")

# Otra forma, mostrando qr en consola
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data('Oi mundo!!!')
qr.make(fit=True)
img = qr.make_image()
img.save('qr2.png')
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())