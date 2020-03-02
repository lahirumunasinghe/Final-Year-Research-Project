import numpy as np
import matplotlib.pyplot as plt
import cv2

FILE = "/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg"
image3 = cv2.imread("/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg")
i = cv2.imread(FILE)
i2 = cv2.imread("/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg")
i3 = cv2.imread("/home/lahiru/Downloads/normal and abnomal with thick collid and nuclear clearing.jpg") #use one

red = i[:,:,2]
red2 = i2[:,:,2]
red3 = i3[:,:,2]

img = cv2.imread(FILE,0)
invert = cv2.bitwise_not(red)
redblur = cv2.GaussianBlur(red,(5,5),0)#Input.jpgclear.jpg
redblur2 = cv2.GaussianBlur(red2,(5,5),0) #otsu
redblur3 = cv2.GaussianBlur(red3,(15,15),0)


#histr = cv2.calcHist(red, [0], None, [256], [0, 256])
#plt.plot(histr, color = 'r')
#plt.xlim([0,256])

histr2 = cv2.calcHist(redblur, [0], None, [256], [0, 256])
histr3 = cv2.calcHist(redblur2, [0], None, [256], [0, 256])
histr4 = cv2.calcHist(redblur3, [0], None, [256], [0, 256])

plt.plot(histr2, color = 'r')
plt.xlim([0,256])

plt.plot(histr3, color = 'b')
plt.xlim([0,256])

plt.plot(histr4, color = 'g')
plt.xlim([0,256])
# Otsu's thresholding after Gaussian filtering
#blurring
blur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)

mask = cv2.inRange(redblur3, 80, 140)
#redthresh = cv2.adaptiveThreshold(redblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

retthresh, otsuThresh = cv2.threshold(redblur3, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

erosion = cv2.erode(otsuThresh,np.ones((2,2), np.uint8),iterations = 5)
dilate = cv2.dilate(erosion,np.ones((2,2), np.uint8),iterations = 5)

dilate2 = cv2.dilate(otsuThresh,np.ones((3,3), np.uint8),iterations = 10)
erosion2 = cv2.erode(dilate2,np.ones((2,2), np.uint8),iterations = 10)



#ret3,th3 = cv2.threshold(blur,170,180,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret3,th3 = cv2.threshold(img,230,255,cv2.THRESH_TRUNC) #70 130
blur2 = cv2.GaussianBlur(th3,(5,5),0)
adaptiveThresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,101,2)

#rtf,thf = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
#range = cv2.inRange(img, 100, 140)
#rtf,thf = cv2.threshold(blur, 114, 255, cv2.THRESH_BINARY)

#Canny
med = np.median(redblur)
sigma = 0.33
lower = int(max(0, (1.0-sigma)*med))
upper = int(min(255, (1.0+sigma)*med))
edges = cv2.Canny(redblur,lower,upper)

#Main Window
#plt.figure(figsize=(15,5))
#images = [blur, histr3, dilate]
#titles = ['Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
#plt.subplot(1,3,1),plt.imshow(images[0],'gray')
#plt.title(titles[0]), plt.xticks([]), plt.yticks([])
#plt.subplot(1,3,2),plt.hist(images[2].ravel(),256)
#plt.title(titles[1]), plt.xticks([]), plt.yticks([])
#plt.subplot(1,3,3),plt.imshow(images[2],'gray')
#plt.title(titles[2]), plt.xticks([]), plt.yticks([])

im = cv2.imread(FILE)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,130,179,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(thresh)
plt.show()
