import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from skimage import exposure
import cv2

#camera = data.camera()
r = cv2.imread('/home/lahiru/Pictures/small foci of tumour with background normal.jpg')
r[:,:,0] = 0
r[:,:,1] = 0
hsv_img = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
val = filters.threshold_otsu(gray)

hist, bins_center = exposure.histogram(gray)
val2 = gray-val
plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(gray, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(val2, cmap='gray', interpolation='nearest')
plt.axis('off')

plt.subplot(133)
plt.plot(bins_center, hist, lw=3)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()


