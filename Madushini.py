import cv2
from MadushiniFile import writetoFile
from TestFeatureExtraction import extractFeatureNew
import numpy as np
from	matplotlib  import pyplot  as	plt
import glob

def auto_canny(image,sigma=033):
    v= np.median(image)

    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(255,(1.0+sigma)*v))
    edge = cv2.Canny(image,lower,upper)

    return edge


def extractFeatures(img,label):

    hist_lbp,hist_harlick,feat_glcm,gaborArr = extractFeatureNew(img)
    writetoFile(hist_lbp,hist_harlick,gaborArr,feat_glcm,label)


def ExtractFetureForSVM(path,val):
    filenames =path
    filenames.sort()
    images = [cv2.imread(img) for img in filenames]

    for sample in images:
        width, height,ch = sample.shape
        print (str(width)+" "+str(height))
        # Setting the points for cropped image
        left = width/5
        top = height / 5
        right = 4*width/5
        bottom = 4 * height / 5
        # Cropped image of above dimension
        # (It will not change orginal image)
        im1 = sample[ top:bottom,left:right]
        new = np.zeros_like(im1)

        edge = auto_canny(im1)
        new[edge==255] = [255,255,255]
        extractFeatures(new,val)

path1 = glob.glob("/home/lahiru/Pictures/Madushini project/Benign/*.jpg")
path2 = glob.glob("/home/lahiru/Pictures/Madushini project/Malignant/*.jpg")

ExtractFetureForSVM(path1,0)
ExtractFetureForSVM(path2,1)
