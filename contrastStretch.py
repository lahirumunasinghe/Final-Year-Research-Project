import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/lahiru/Pictures/capsule.png')
#img = Image.open('check.jpg').convert('L')
arr = np.asarray(img)
kernel_sharp2 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
plt.gray()
plt.title("1")
plt.imshow(arr)
img_gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
sharpend = cv2.filter2D(img_gray,-1,kernel_sharp2)

plt.imshow(img)

plt.figure(figsize=(10,10))
plt.subplot(1,2,1),plt.title('Original Image'),plt.imshow(img)#,'red')
plt.subplot(1,2,2),plt.title('OpenCV.findContours'),plt.imshow(sharpend,'gray')#,'red')
#plt.subplot(1,2,2),plt.title('shapning'),plt.imshow(sharpend,'sharpned')
result = Image.fromarray(arr)

result.save("nn.jpg")
plt.show()

image  = cv2.imread('res.jpg', 0)

n  = cv2.imread('check.jpg', 0)

cv2.imshow("sadsdas", image)

cv2.imshow("ori",n)
