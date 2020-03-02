import numpy as np
import matplotlib.pyplot as plt
import cv2
 
FILE = "/home/lahiru/Pictures/small foci of tumour with background normal.jpg"

img = cv2.imread(FILE,0)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
#ret3,th3 = cv2.threshold(blur,170,180,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret3,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC) #70 130
blur2 = cv2.GaussianBlur(th3,(5,5),0)
rtf,thf = cv2.threshold(th3, 114, 255, cv2.THRESH_BINARY)
range = cv2.inRange(img, 100, 140)
edges = cv2.Canny(blur2,0,0)

# Plot Here
plt.figure(figsize=(15,5))
images = [blur, 0, th3]
titles = ['Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
plt.subplot(1,3,1),plt.imshow(images[0],'gray')
plt.title(titles[0]), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.hist(images[0].ravel(),256)
plt.title(titles[1]), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(images[2],'gray')
plt.title(titles[2]), plt.xticks([]), plt.yticks([])

im = cv2.imread(FILE)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,130,179,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#image, contours, hierarchy = cv2.findContours(thf,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thf,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (255,255,255), 3)



#_, contours, _ =cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('no of shapes {0}'.format(len(contours)))
idx = 0
for cnt in contours:
    idx+=1
    rect = cv2.boundingRect(cnt)
  #  rect = cv2.minAreaRect(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    if(w*h >= 1000 and w*h <= 10000): 
        cv2.rectangle(img,(x-10,y-10),(x+w+20,y+h+20),(0,255,0),2)
        #print((w*h))
        #new_img=im[y-10:y+h+20,x-10:x+w+20]
        #cv2.imwrite('C:/Users/Kasun/source/repos/PythonApplication3/Images/'+str(idx) + '.png', new_img)
   
    #box = cv2.boxPcoints(rect)
    #box = np.int0(box)
    #img = cv2.drawContours(img, [box], 0, (0, 255, 0), 3)


plt.figure(figsize=(10,10))
plt.subplot(1,2,1),plt.title('Original Image'),plt.imshow(im)#,'red')
plt.subplot(1,2,2),plt.title('OpenCV.findContours'),plt.imshow(img,'gray')#,'red')
plt.figure('Example 1')
plt.imshow(img)
plt.title('Binary Contours of an image')
plt.figure('blur')
plt.imshow(blur2)
plt.title('blur2')
plt.figure('thf')
plt.imshow(thf)
plt.title('thf')
plt.figure('edge')
plt.imshow(edges)
plt.title('edge')
plt.show()

print('number of detected contours: ',len(contours))
