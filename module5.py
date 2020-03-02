import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("Input.jpg")

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret,th1 = cv2.threshold(image,60,140,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
ret4,th4 = cv2.threshold(image,105,125,cv2.THRESH_BINARY) #70 130
ret5,th5 = cv2.threshold(image,60,140,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

guas = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
guas2 = cv2.adaptiveThreshold(th5,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

ret,th3 = cv2.threshold(image,60,140,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(th2,kernel,iterations = 0)

proj = np.sum(dilation,1)

# Create output image same height as text, 500 px wide
m = np.max(proj)
w = 500
result = np.zeros((proj.shape[0],500))

# Draw a line for each row
for row in range(dilation.shape[0]):
   cv2.line(result, (0,row), (int(proj[row]*w/m),row), (255,255,255), 1)

plt.subplot(131),plt.imshow(th5),plt.title('original')
plt.xticks([]), plt.yticks([])

#plt.subplot(132),plt.imshow(th1,  cmap="gray"),plt.title('binary')
#plt.xticks([]), plt.yticks([])

#plt.subplot(133),plt.imshow(result,  cmap="gray"),plt.title('horizontal projection')
#plt.xticks([]), plt.yticks([])
#plt.show()


#plt.imshow(th3)
#plt.show()
plt.imshow(th5)
plt.show()

_, contours, _ =cv2.findContours(th5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('no of shapes {0}'.format(len(contours)))
idx = 0
for cnt in contours:
    idx+=1
    rect = cv2.boundingRect(cnt)
  #  rect = cv2.minAreaRect(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x-10,y-10),(x+w+20,y+h+20),(0,255,0),2)
    #new_img=image[y-10:y+h+20,x-10:x+w+20]
    #cv2.imwrite(str(idx) + '.png', new_img)
   
    #box = cv2.boxPcoints(rect)
    #box = np.int0(box)
    #img = cv2.drawContours(img, [box], 0, (0, 255, 0), 3)
    

plt.figure('Example 1')
plt.imshow(img)
plt.title('Binary Contours of an image')
plt.show()

