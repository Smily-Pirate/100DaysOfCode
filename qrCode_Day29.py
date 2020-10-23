import pyqrcode
from pyqrcode import QRCode
import png
s = "www.geeksforgeeks.org"

url = pyqrcode.create(s)
url.svg("mysr.svg", scale = 8)
url.png('myqr.png', scale = 6)