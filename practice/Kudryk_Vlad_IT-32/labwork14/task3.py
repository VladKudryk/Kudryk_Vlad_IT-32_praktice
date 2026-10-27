import qrcode
from qrcode.image.pure import PyPNGImage

print("Vlad Kudryk, IT-32")

text = "Vlad Kudryk, IT-32, vlad.kudryk@example.com"
image = qrcode.make(text, image_factory=PyPNGImage)
image.save("contact.png")
print("saved: contact.png")