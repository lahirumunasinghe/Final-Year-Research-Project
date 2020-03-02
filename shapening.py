import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

def viewImage(image):
    plt.imshow(image,cmap='gray')
    plt.show()

img = cv2.imread('/home/lahiru/Pictures/capsule.png')
viewImage(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
viewImage(img_gray)
kernel_sharp = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
kernel_sharp2 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
kernel_sharp3 = np.array([[-1,0,-1],[0,5,0],[-1,0,-1]])

sharpend = cv2.filter2D(img_gray,-1,kernel_sharp)
sharpend2 = cv2.filter2D(img_gray,-1,kernel_sharp2)
sharpend3 = cv2.filter2D(img_gray,-1,kernel_sharp3)
viewImage(sharpend3)
