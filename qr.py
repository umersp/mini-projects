#dependencies
# first insatll --  pip install qrcode 
#                   pip install pillow

import qrcode

img = qrcode.make("https://www.instagram.com/umer_sp_009/")
# img = qrcode.make("hello ji!")

img.save("QR_for_insta.jpg")