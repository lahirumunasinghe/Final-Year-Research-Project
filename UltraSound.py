import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure
from PIL import Image
import glob

def auto_canny(image,sigma=033):
    v= np.median(image)

    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(255,(1.0+sigma)*v))
    edge = cv2.Canny(image,lower,upper)

    return edge

def viewImage(image):
    plt.imshow(image,cmap='gray')
    plt.show()

# kernel_sharp = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
#kernel_median = np.array([0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111],[0.1111,0.1111,0.1111])
count=0
for filename in glob.glob('/home/lahiru/Pictures/Ultra/*.jpg'): #assuming gif
    #im=Image.open(filename)
    # r = cv2.imread('/home/lahiru/Pictures/Ultra.jpg')

    im =cv2.imread(filename)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    adaptive= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    hist, bins_center = exposure.histogram(gray)

    gasian = cv2.GaussianBlur(gray,(5,5),0)
    # sharpend = cv2.filter2D(gasian,-1,kernel_sharp)

    wide = cv2.Canny(gasian,10,200)
    tight = cv2.Canny(gasian,255,250)
    auto = auto_canny(gasian)
    print("run")
    path1 = '/home/lahiru/PycharmProjects/untitled/newUltra/img_bin_auto'+str(count)+'.png'
    path2 = '/home/lahiru/PycharmProjects/untitled/newUltra/img_bin_wide'+str(count)+'.png'
    path3 = '/home/lahiru/PycharmProjects/untitled/newUltra/img_bin_tight'+str(count)+'.png'
    #viewImage(auto)
    # plt.plot( bins_center,hist, lw=3)
    # plt.show()
    cv2.imwrite(path1,auto)
    cv2.imwrite(path2,wide)
    cv2.imwrite(path3,tight)
    count = count+1
