import pytesseract
import cv2
img=cv2.imread(r'c:\tmp\cc.png',cv2.IMREAD_GRAYSCALE)
text=pytesseract.image_to_string(img)
print(text)
