# import the necessary packages
from skimage import feature
import numpy as np
 
class LocalBinaryPatterns:
	def __init__(self, numPoints, radius):
		# store the number of points and radius
		self.numPoints = numPoints
		self.radius = radius
 
	def describe(self, image, eps=1e-7):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		lbp = feature.local_binary_pattern(image, self.numPoints,
			self.radius, method="uniform")
		(hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, self.numPoints + 3),
			range=(0, self.numPoints + 2))

		# normalize the histogram
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)

		# return the histogram of Local Binary Patterns
		return hist

# import the necessary packages
#from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-t", "--training", required=True,
#	help="path to the training images")
#ap.add_argument("-e", "--testing", required=True, 
#	help="path to the tesitng images")
#args = vars(ap.parse_args())
 
# initialize the local binary patterns descriptor along with
# the data and label lists


desc = LocalBinaryPatterns(24, 8)
data = []
labels = []



#	# load the image, convert it to grayscale, and describe it
#image = cv2.imread('C:/Users/Kasun/source/repos/PythonApplication3/FinalImages1/1577419774.8.png')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#hist = desc.describe(gray) 
#	# extract the label from the image path, then update the
#	# label and data lists
##labels.append(imagePath.split(os.path.sep)[-2])
#data.append(hist)
 
#print(hist)
