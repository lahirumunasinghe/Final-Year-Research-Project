import cv2
import numpy
from scipy.ndimage import label
import numpy as np
from matplotlib import pyplot as plt

def viewImage(image):
    plt.imshow(image)
    plt.show()

r = cv2.imread('/home/lahiru/Pictures/50Xnormal vs lesion 22.jpg')
r1 = cv2.imread('/home/lahiru/Pictures/50Xnormal vs lesion 22.jpg')
gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/gray.png", gray)
_, img_bin = cv2.threshold(gray, 180, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/thresh.png", img_bin)
dilate = cv2.dilate(img_bin,None,iterations=18)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/dilate.png", dilate)
erode = cv2.erode(dilate,None,iterations=18)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/erode.png", erode)
dt_a = cv2.adaptiveThreshold(erode,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
viewImage(dt_a)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/adaptive.png", dt_a)
dt_a[dt_a != 255] = 0
result = cv2.dilate(dt_a,None)
r1[result == 255] = (0, 255, 0)
viewImage(r1)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Capsule/endResult.png", r1)
