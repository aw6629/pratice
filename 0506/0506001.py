import cv2
img=cv2.imread(r'c:\tmp\michaeljordan.jpg',cv2.IMREAD_GRAYSCALE)
img.fill(0)
print(type(img))
print(img.dtype)
print(img.ndim)
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()