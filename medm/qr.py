import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def generate_qr(data: str, file: str = None):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    output_file = file if file else "qrcode.png"
    img.save(output_file)
    print(f"QR Code saved to {output_file}")


def decode_qr(file: str):
    img = Image.open(file)
    decoded_data = decode(img)
    if decoded_data:
        print(f"Decoded data: {decoded_data[0].data.decode()}")
    else:
        print("No QR code found in the image.")
