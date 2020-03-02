import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('/home/lahiru/Downloads/small focus of tumour with background normal.jpg')
#red2 = image[:,:,2]
plt.imshow(image)
plt.show()
