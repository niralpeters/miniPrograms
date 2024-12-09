import pyqrcode

website = "www.youtube.com/@niralpeters"
qrCodeGen = pyqrcode.create(website)
qrCodeGen.png("qrcode.png", scale=6)