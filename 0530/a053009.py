from PIL import Image
import pytesseract
text=pytesseract.image_to_string(Image.open(r'c:\tmp\aa.png'))
print(text)