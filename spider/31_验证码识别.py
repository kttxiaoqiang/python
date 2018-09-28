import pytesseract as pt
from PIL import Image
text=pt.image_to_string(image='./11_wendang/1.jpeg')
print(text)