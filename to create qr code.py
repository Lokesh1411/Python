import pyqrcode #to create qr code
import png #to save them as png
from pyqrcode import QRCode

s='https://www.google.com/' #link for which qr code to be created

url=pyqrcode.create(s) #creates a qr code for s
url.svg('myqr.svg',scale=8) #saves as myqr.svg with scale/size=8
url.png('myqrcode.png',scale=6) #saves as myqrcode.png with scale/size=6
