# import the necessary packages
from scipy.spatial import distance as dist
from scipy import stats
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
from matplotlib import pyplot as plt
import statistics
from scipy.ndimage import label
from skimage import filters
from skimage import exposure
import copy

def segment_on_dt(a, img):
    border = cv2.dilate(img, None, iterations=3)
    border = border - cv2.erode(border, None)
    #cv2.imwrite("border.png", border)

    dt = cv2.distanceTransform(img,cv2.DIST_L1,5)
    #cv2.imwrite("distance.png", border)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(np.uint8)
    #cv2.imwrite("dt.png", dt)
    dt_a = cv2.adaptiveThreshold(dt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    #cv2.imwrite("dt_a.png", dt_a)
    #closing = cv2.dilate(dt,None,iterations=2)
    closing = cv2.erode(dt,None,iterations=3)
    #cv2.imwrite("closing.png", closing)
    _, dt = cv2.threshold(dt, 108, 255, cv2.THRESH_BINARY)
    dt_a = cv2.adaptiveThreshold(closing,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    #cv2.imwrite("adap.png", dt_a-border)
    er = cv2.dilate(dt_a-border,None,iterations=1)
    dl = cv2.erode(er,None,iterations=1)

    #cv2.imwrite("closing2.png", dl)
    #cv2.imwrite("dt_thres.png", dt)

    lbl, ncc = label(dt)
    lbl = lbl * (255/ncc)
    # Completing the markers now.
    lbl[border == 255] = 255
    lbl = lbl.astype(np.int32)
    #cv2.imwrite("label.png", lbl)
    cv2.watershed(a, lbl)
    lbl[lbl == -1] = 0
    lbl = lbl.astype(np.uint8)
    return  dl

def viewImage(image):
    plt.imshow(image)
    plt.show()

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# ap.add_argument("-w", "--width", type=float, required=True,
# 	help="width of the left-most object in the image (in inches)")
# args = vars(ap.parse_args())
#####################################################################################


# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
def measureDistance(imageIn):
    # image = imageIn.copy()

	distanceArray=[]
	countNumDistance = 1  # type: int
	width = 0.55
        image = copy.copy(imageIn)
	image2 = copy.copy(imageIn)
	#image = cv2.imread("/home/lahiru/PycharmProjects/untitled/SliceImage/slice_01_01.png")
	#image2 = cv2.imread("/home/lahiru/PycharmProjects/untitled/SliceImage/slice_01_01.png")

	#r = cv2.imread('/home/lahiru/Pictures/2.jpg')
	#r1 = cv2.imread('/home/lahiru/Pictures/2.jpg')
	image[:,:,0] = 0
	image[:,:,1] = 0
	hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)
	val = filters.threshold_otsu(gray)

	hist, bins_center = exposure.histogram(gray)
	val2 = gray-val
	cv2.imwrite('img_bin.png', val2)

	# img = cv2.imread('/home/lahiru/Pictures/img.jpg'k)
	# if img == None:
	#     print("!!! Failed to open input image")
	#     sys.exit(0)

	# Pre-processing.
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	_, img_bin = cv2.threshold(val-gray, 250, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
	#cv2.imwrite('img_bin.png',img_bin )

	img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, np.ones((5, 5), dtype=int))
	#cv2.imwrite('img_bin_morphoEx.png', img_bin)

	# img_bin2 = cv2.adaptiveThreshold(img_bin,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
	# cv2.imwrite('adaptive.png', img_bin2)

	result = segment_on_dt(image, img_bin)

	# find contours in the edge map
	cnts = cv2.findContours(result.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	cnts = imutils.grab_contours(cnts)

	# sort the contours from left-to-right and, then initialize the
	# distance colors and reference object
	(cnts, _) = contours.sort_contours(cnts)
	colors = ((0, 0, 255), (240, 0, 159), (0, 165, 255), (255, 255, 0),
		(255, 0, 255))
	refObj = None
##################################################################################################
	# loop over the contours individually
	imgnum = 0
	for c in cnts:
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < 150 or cv2.contourArea(c) > 1000 :
			continue

		# compute the rotated bounding box of the contour
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")

		# order the points in the contour such that they appear
		# in top-left, top-right, bottom-right, and bottom-left
		# order, then draw the outline of the rotated bounding
		# box
		box = perspective.order_points(box)

		# compute the center of the bounding box
		cX = np.average(box[:, 0])
		cY = np.average(box[:, 1])
##########################################################################
		# if this is the first contour we are examining (i.e.,
		# the left-most contour), we presume this is the
		# reference object
		if refObj is None:
			# unpack the ordered bounding box, then compute the
			# midpoint between the top-left and top-right points,
			# followed by the midpoint between the top-right and
			# bottom-right
			(tl, tr, br, bl) = box
			(tlblX, tlblY) = midpoint(tl, bl)
			(trbrX, trbrY) = midpoint(tr, br)

			# compute the Euclidean distance between the midpoints,
			# then construct the reference object
			D = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
			refObj = (box, (cX, cY), D / width)
			continue
################################################################################
		# draw the contours on the image
		orig = image2.copy()
		cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
		cv2.drawContours(orig, [refObj[0].astype("int")], -1, (0, 255, 0), 2)

		# stack the reference coordinates and the object coordinates
		# to include the object center
		refCoords = np.vstack([refObj[0], refObj[1]])
		objCoords = np.vstack([box, (cX, cY)])
##################################################################################
		count =0
		countdis= 0
		# loop over the original points
		for ((xA, yA), (xB, yB), color) in zip(refCoords, objCoords, colors):
			# draw circles corresponding to the current points and
			# connect them with a line
			if(countdis == 4):
				cv2.circle(orig, (int(xA), int(yA)), 5, color, -1)
				cv2.circle(orig, (int(xB), int(yB)), 5, color, -1)
				cv2.line(orig, (int(xA), int(yA)), (int(xB), int(yB)),
					color, 2)

				# compute the Euclidean distance between the coordinates,
				# and then convert the distance in pixels to distance in
				# units
				D = dist.euclidean((xA, yA), (xB, yB)) / refObj[2]
				(mX, mY) = midpoint((xA, yA), (xB, yB))
				cv2.putText(orig, "{:.1f}in".format(D), (int(mX), int(mY - 10)),
					cv2.FONT_HERSHEY_SIMPLEX, 0.55,    color, 2)

				distanceArray.append(D)
				# show the output image
				# cv2.imshow('image', orig)
				# cv2.waitKey(0)
				#viewImage(orig)

			#for the write images that getting path ############################################
			# path = '/home/lahiru/PycharmProjects/untitled/distance/'+str(imgnum)+'img_bin'+str(count)+'.png'
			# if(count == 4):
			# 	cv2.imwrite(path,orig)
			countdis = countdis+1
			count = count+1
		imgnum = imgnum+1
		countNumDistance=countNumDistance+1
		if(countNumDistance==61):
			break
	#i=0
	# while i < len(distanceArray):
	# 	print(distanceArray[i])
	# 	i+=1;

	median =np.median(distanceArray)
	stdev= statistics.stdev(distanceArray)
	mean = np.mean(distanceArray)

	print(median,statistics.stdev(distanceArray),mean)
	return median,stdev,mean



#/home/lahiru/Pictures/Input.jpg
# image = cv2.imread("/home/lahiru/PycharmProjects/untitled/SliceImage/slice_03_03.png")
# image = cv2.imread("/home/lahiru/Pictures/Input.jpg")
# measureDistance(image)
