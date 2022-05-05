import qrcode

qr_img = qrcode.make('https://thomasmorethelen.com')

qr_img.save('my_qrcode.png')
