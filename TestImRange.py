import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
from skimage import exposure

def viewImage(image):
    plt.imshow(image)
    plt.show()
   # cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    #cv2.imshow('Display', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    ## getting green HSV color representation
#green = np.uint8([[[0, 255, 0 ]]])
#green_hsv = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

#print( green_hsv)

#/home/lahiru/Downloads/good.jpg
image = cv2.imread('/home/lahiru/Pictures/Input.jpg')
#image = cv2.imread('/home/lahiru/Pictures/Pictures/Architecture/small foci of tumour with background normal.jpg')
r= cv2.imread('/home/lahiru/Pictures/Input.jpg')
viewImage(image)
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
viewImage(hsv_img) ## 1

# Purple_low = np.array([160,169,149] )
# Purple_high = np.array([164,187,147])
# curr_mask = cv2.inRange(hsv_img, Purple_low, Purple_high)
# hsv_img[curr_mask > 0] = ([0,0,0]) #puple color 3rd normalie
# viewImage(hsv_img) ## 2
# viewImage(curr_mask)



## converting the HSV image to Gray inorder to be able to apply
## contouring
#RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_RGB2GRAY)
viewImage(gray) ## 3

#r = cv2.imread('/home/lahiru/Pictures/small foci of tumour with background normal.jpg')
r = cv2.imread('/home/lahiru/Pictures/Input.jpg')
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
val = filters.threshold_otsu(gray)

#hist, bins_center = exposure.histogram(gray)


#img =(gray < val)


# ret, threshold = cv2.threshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# ret, threshold = cv2.threshold((gray<val),250,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


viewImage(gray-val) ## 4

contours, hierarcurr_maskchy =  cv2.findContours((gray-val),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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


largest_area, largest_contour_index = findGreatesContour(contours)

print(largest_area)
print(largest_contour_index)

print(len(contours))

if(M["m00"] != 0 and M["m00"] != 0):
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(cX)
    print(cY)

