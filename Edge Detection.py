import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread("/home/lahiru/Pictures/Input.jpg")

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h = image.shape[0]
w = image.shape[1]


ret,th1 = cv2.threshold(image,70,130,cv2.THRESH_BINARY)
edges = cv2.Canny(th1,60,120)



plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edeg Image'), plt.xticks([]), plt.yticks([])

plt.show()
