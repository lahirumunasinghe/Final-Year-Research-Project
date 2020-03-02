
# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread("/home/lahiru/Downloads/good.jpg")
img2 = cv2.imread("/home/lahiru/Downloads/Input.jpg")
img3 = cv2.imread("/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg")
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# find frequency of pixels in range 0-255

r = cv2.imread("/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg")
r[:,:,0] = 0
r[:,:,2] = 0
red = img[:,:,2]
range = cv2.inRange(red,185,200)
ret,thresh = cv2.threshold(red,180,255,cv2.THRESH_BINARY)
ret2,thresh2 = cv2.threshold(thresh,200,0,cv2.THRESH_BINARY)

histr = cv2.calcHist([image],[0],None,[256],[0,256])
histr2 = cv2.calcHist([image2],[0],None,[256],[0,256])

plt.imshow(red)
plt.show()

plt.imshow(range)
plt.show()

# show the plotting graph of an image
