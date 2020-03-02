import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = Image.open('check.jpg').convert('L')
arr = np.asarray(img)

plt.gray()
plt.title("1")
plt.imshow(arr)


plt.imshow(img)

plt.figure(figsize=(10,10))
plt.subplot(1,2,1),plt.title('Original Image'),plt.imshow(img)#,'red')
plt.subplot(1,2,2),plt.title('OpenCV.findContours'),plt.imshow(arr,'gray')#,'red')
result = Image.fromarray(arr)

result.save("nn.jpg")
plt.show()

image  = cv2.imread('res.jpg', 0)

n  = cv2.imread('check.jpg', 0)

cv2.imshow("sadsdas", image)

cv2.imshow("ori",n)