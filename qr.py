import qrcode
import requests

# Define the text to be encoded in the QR code
text = "Hello, this is a QR code!"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img_path = "qr_code.png"
img.save(img_path)

# Upload the image to GitHub repository
github_repo_url = "import qrcode"
import requests

# Define the text to be encoded in the QR code
text = "Hello, this is a QR code!"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img_path = "qr_code.png"
img.save(img_path)

# Upload the image to GitHub repository
github_repo_url = "https://github.com/hrsh-1294/build-releasetut.git"
upload_url = f"{github_repo_url}/blob/main/{img_path}"

with open(img_path, "rb") as file:
    files = {"file": (img_path, file)}
    response = requests.put(upload_url, files=files)

if response.status_code == 200:
    print("QR code image uploaded successfully to GitHub repository!")
else:
    print("Failed to upload QR code image to GitHub repository.")
"
upload_url = f"{github_repo_url}/blob/main/{img_path}"

with open(img_path, "rb") as file:
    files = {"file": (img_path, file)}
    response = requests.put(upload_url, files=files)

if response.status_code == 200:
    print("QR code image uploaded successfully to GitHub repository!")
else:
    print("Failed to upload QR code image to GitHub repository.")
