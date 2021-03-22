import pyqrcode #pip install pyqrcode

import sys

print("--- Command Line:", sys.argv)
if len(sys.argv) < 2:
    # expect 2 arguments
    print(f"Usage: {sys.argv[0]} my-msg")
    exit(1)

msg = sys.argv[1]

qrcode = pyqrcode.create(msg)

qrcode.png("QRmsg.png", scale=8)

print("--- QR Code is created in QRmsg.png")

