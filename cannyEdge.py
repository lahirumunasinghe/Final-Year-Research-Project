import numpy as np
import argparse
import glob
import cv2

def auto_canny(image,sigma=033):
    v= np.median(image)

    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(255,(1.0+sigma)*v))
    edge = cv2.Canny(image,lower,upper)

    return edge

# ap= argparse.ArgumentParser()
# ap.add_argument("--i","--images",required=True,help="path to input dataset of images")
# args = vars(ap.parse_args())

#for imagePath in glob.glob(args["images"]+"/*.jpg"):

image = cv2.imread('/home/lahiru/Pictures/Ultra.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
blurred = cv2.GaussianBlur(gray,(3,3),0)

wide = cv2.Canny(blurred,10,200)
tight = cv2.Canny(blurred,255,250)
auto = auto_canny(blurred)
cv2.imshow("Original",image)
cv2.imshow("Edge",np.hstack([wide,tight,auto]))
cv2.waitKey()
