import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import exposure
import cv2

from matplotlib import pyplot as plt
def viewImage(image):
    plt.imshow(image,cmap='gray')
    plt.show()
# img = cv2.imread('coins.png')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

r = cv2.imread('/home/lahiru/Pictures/50Xnormal vs lesion 2.jpg')
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
viewImage(gray)
val = filters.threshold_otsu(gray)

hist, bins_center = exposure.histogram(gray)
val2 = val-gray

viewImage(val2)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(val2,cv2.MORPH_OPEN,kernel, iterations = 3)
viewImage(opening)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
viewImage(sure_bg)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L1,3)
viewImage(dist_transform)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
viewImage(sure_fg)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
viewImage(ret)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(r,markers)
r[markers == -1] = [255,0,0]
