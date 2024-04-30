import qrcode
from PIL import Image

# Replace 'Your text here' with the text you want to encode
text = "Your text here"

# Create the QR code object
qr = qrcode.QRCode(
    version=1,  # Adjust version for larger data (optional)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Adjust error correction (optional)
)
qr.add_data(text)
qr.make(fit=True)

# Convert QR code to PIL image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
filename = "qr_code.png"  # You can change the filename
img.save(filename)

print(f"QR code saved as: {filename}")
