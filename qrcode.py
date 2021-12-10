import qrcode
import image

qr = qrcode.QRCode(
    version=15, #mean the version of the qr code highier the number the more complicated the qr code
    box_size=10,#size of he box where the qrucode will be displayed
    border=5#it is the white part of the image
)
data='https://www.youtube.com/watch?v=tdn9_MZ0lN4'
#as i defined the target url as the video that i want to watch later on python
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill='black',back_color="white")
img.save("qr.png")