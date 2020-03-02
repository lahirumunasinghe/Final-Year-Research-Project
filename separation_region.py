import numpy as np
import cv2

img = cv2.imread('/home/lahiru/Pictures/Test.png')

## Step 1-3: drawContours in empty image
mask = np.zeros((100,200), np.uint8)
pts = np.array([[0,0],[0,50],[199,75],[199,0]])
_=cv2.drawContours(mask, np.int32([pts]),0, 255, -1)

## Step 4: do mask-op
img1 = img.copy()
img2 = img.copy()
img1[mask==0] = 0
img2[mask>0] = 0

## Write
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Separate/mask.png", mask)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Separate/img1.png", img1)
cv2.imwrite("/home/lahiru/PycharmProjects/untitled/Separate/img2.png", img2)
