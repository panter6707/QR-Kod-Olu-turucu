import pyqrcode

url = input("QR Kodun URL'sini verin: ")

qr_code = pyqrcode.create(url)

qr_code.svg('qrkode.svg',scale=5)