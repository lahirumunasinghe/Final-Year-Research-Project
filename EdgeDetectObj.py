import cv2
import numpy as np
from matplotlib import pyplot as plt

def viewImage(image):
    plt.imshow(image)
    plt.show()
   # cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    #cv2.imshow('Display', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    ## getting green HSV color representation
    #red = np.uint8([[[255, 0, 0 ]]])
    #green = image.np.uint8([[[0, 255, 0 ]]])
    red_pixel_rgb = np.array([[[255, 0, 0]]], dtype=np.uint8)
    #green_hsv = cv2.cvtColor().imshow(green)
    #plt.show()
    #print( green_hsv)

image = cv2.imread('/home/lahiru/Downloads/Down/leaf.jpeg')


r = image.copy()
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
viewImage(hsv_img) ## 1

green_low = np.array([45 , 100, 50] )
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([75,255,200])
viewImage(hsv_img) ## 2

## converting the HSV image to Gray inorder to be able to apply
## contouring
RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
viewImage(gray) ## 3

ret, threshold = cv2.plt.imshow(red)
plt.show()
threshold(gray, 90, 255, 0)
viewImage(threshold) ## 4

contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
viewImage(image) ## 5

def findGreatesContour(contours):
    largest_area = 0
    largest_contour_index = -1
    i = 0
    total_contours = len(contours)
    while (i < total_contours ):
        area = cv2.contourArea(contours[i])
        if(area > largest_area):
            largest_area = area
            largest_contour_index = i
        i+=1

    return largest_area, largest_contour_index

# to get the center of the contour
cnt = contours[13]
M = cv2.moments(cnt)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

largest_area, largest_contour_index = findGreatesContour(contours)

print(largest_area)
print(largest_contour_index)

print(len(contours))

print(cX)
print(cY)
