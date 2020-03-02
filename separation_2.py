import sys
import cv2
import numpy
from scipy.ndimage import label
import numpy as np
from skimage import filters
from skimage import exposure
from matplotlib import pyplot as plt
# import opencv.core.Core;
# import org.opencv.core.Mat;
# import opencv.imgcodecs.Imgcodecs;
# import opencv.imgproc.Imgproc;
#import org


def viewImage(image):
    plt.imshow(image)
    plt.show()

def segment_on_dt(a, img):
    border = cv2.dilate(img, None, iterations=3)
    border = border - cv2.erode(border, None)
    cv2.imwrite("border.png", border)

    dt = cv2.distanceTransform(img,cv2.DIST_L1,5)
    cv2.imwrite("distance.png", border)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(numpy.uint8)
    cv2.imwrite("dt.png", dt)
    dt_a = cv2.adaptiveThreshold(dt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    cv2.imwrite("dt_a.png", dt_a)
    closing = cv2.dilate(dt,None,iterations=2)
    closing = cv2.erode(dt,None,iterations=3)
    cv2.imwrite("closing.png", closing)
    _, dt = cv2.threshold(dt, 108, 255, cv2.THRESH_BINARY)
    dt_a = cv2.adaptiveThreshold(closing,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    cv2.imwrite("adap.png", dt_a-border)
    er = cv2.dilate(dt_a-border,None,iterations=1)
    dl = cv2.erode(er,None,iterations=1)

    cv2.imwrite("closing2.png", dl)
    cv2.imwrite("dt_thres.png", dt)

    lbl, ncc = label(dt)
    lbl = lbl * (255/ncc)
    # Completing the markers now.
    lbl[border == 255] = 255
    lbl = lbl.astype(numpy.int32)
    cv2.imwrite("label.png", lbl)
    cv2.watershed(a, lbl)
    lbl[lbl == -1] = 0
    lbl = lbl.astype(numpy.uint8)
    return  dl


# Application entry point
r = cv2.imread('/home/lahiru/Pictures/2.jpg')
r1 = cv2.imread('/home/lahiru/Pictures/2.jpg')
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
val = filters.threshold_otsu(gray)

hist, bins_center = exposure.histogram(gray)
val2 = gray-val
cv2.imwrite('img_bin.png', val2)

# img = cv2.imread('/home/lahiru/Pictures/img.jpg'k)
# if img == None:
#     print("!!! Failed to open input image")
#     sys.exit(0)

# Pre-processing.
img_gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(val-gray, 250, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imwrite('img_bin.png',img_bin )

img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, numpy.ones((5, 5), dtype=int))
cv2.imwrite('img_bin_morphoEx.png', img_bin)

# img_bin2 = cv2.adaptiveThreshold(img_bin,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
# cv2.imwrite('adaptive.png', img_bin2)

result = segment_on_dt(r, img_bin)
cv2.imwrite('result.png', result)
result[result != 255] = 0

result = cv2.dilate(result,None)
r1[result == 255] = (0, 255, 0)
cv2.imwrite('output.png', r1)


