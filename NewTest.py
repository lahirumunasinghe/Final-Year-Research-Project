import cv2
import numpy as np
from matplotlib import pyplot as plt

def viewImage(image):
    plt.imshow(image)
    plt.show()

image = cv2.imread('/home/lahiru/Pictures/small foci of tumour with background normal.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
viewImage(image)
viewImage(edged)

# ret, threshold = cv2.threshold(image, 90, 255, 0)
