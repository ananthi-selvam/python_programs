# install qrcode lib from python documentation
# recommended to use this script in Virtual environment
# generating QR code using data given by user
import qr_code_generator

url = input("Enter URL: ").strip()
filename = input("Enter file name: ").strip()

qr = qrcode.QRCode(box_size=12, border=4 )
qr.add_data(url)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code is saved as {filename}')
