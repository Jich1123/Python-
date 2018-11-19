import pytesseract as pt
from PIL import Image
image = Image.open('')
text = pt.image_to_string(image)
print(text)