# you have to install library qrcode with command: pip install qrcode
import qrcode

data = 'Don\'r forget to subcribe'

img = qrcode.make(data)

img.save('C:/Users/......./myqrcode1.png') #need to change the backslash to front slash





qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/......./myqrcode2.png') #need to change the backslash to front slash




#pip install pyzbar
#pip install PIL
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open(('C:/Users/......./myqrcode1.png')

result = decode(img)

print(result)
