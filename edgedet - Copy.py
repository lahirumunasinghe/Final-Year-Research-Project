import cv2
import numpy as np
from PIL import Image
import matplotlib.image as mpimg

from matplotlib import pyplot as plt

img = cv2.imread('/home/lahiru/Pictures/small foci of tumour with background normal.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
imgh=mpimg.imread('/home/lahiru/Pictures/small foci of tumour with background normal.jpg')
lum_img = imgh[:,:,0]
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 0)

# Calculate horizontal projection
proj = np.sum(dilation,1)

# Create output image same height as text, 500 px wide
m = np.max(proj)
w = 500
result = np.zeros((proj.shape[0],500))

# Draw a line for each row
for row in range(dilation.shape[0]):
   cv2.line(result, (0,row), (int(proj[row]*w/m),row), (255,255,255), 1)

#ret5,th5 = cv2.threshold(image,60,140,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img1 = Image.open('sample_1.png').convert('L')

arr = np.asarray(img)
high_thresh, thresh_im = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

lowThresh = 0.5*high_thresh
blur = cv2.GaussianBlur(img,(5,5),0)

print lowThresh
print high_thresh
edges = cv2.Canny(blur,180,180)
#edge2 = cv2.Canny(edges,100,180)
#edge3 = cv2.Canny(edge2,100,180)
#edge4 = cv2.Canny(edge3,100,180)


plt.subplot(121),plt.imshow(blur,cmap = 'gray')
plt.title('blur Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.subplot(211),plt.imshow(result),plt.title("hwbshwj"), plt.xticks([]), plt.yticks([])

plt.show()
