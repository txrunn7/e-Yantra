import cv2
import numpy as np
from skimage import measure
import imutils
from imutils import contours

img=cv2.imread(r"C:\Users\shyam\Computer Vision and Image Processing\Sample Images\whitespots.jpg")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY)
#contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

labels=measure.label(thresh, connectivity=2,  background=0)
mask = np.zeros(thresh.shape, dtype="uint8")

for label in np.unique(labels):
	# if this is the background label, ignore it
	if label == 0:
		continue
	# otherwise, construct the label mask and count the
	# number of pixels 
	labelMask = np.zeros(thresh.shape, dtype="uint8")
	labelMask[labels == label] = 255
	numPixels = cv2.countNonZero(labelMask)
	# if the number of pixels in the component is sufficiently
	# large, then add it to our mask of "large blobs"
	if numPixels > 10:
		mask = cv2.add(mask, labelMask)
		
cnts,_=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts=contours.sort_contours(cnts)[0]

print("Number of LEDs detected: "+str(len(cnts)))

for (i, c) in enumerate(cnts):
    M = cv2.moments(c)
    if M["m00"] != 0:
        cx = float(M["m10"] / M["m00"])
        cy = float(M["m01"] / M["m00"])
        cv2.circle(img, (int(cx),int(cy)), 4, (0, 255, 0), -1)
        # cv2.putText(img, str(cx) + "," + str(cy), (cx + 10, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 1)
        cv2.putText(img, str(i + 1), (int(cx) + 10, int(cy) + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 1)
        print("Centroid #" + str(i + 1) + ": " + "(" + str(cx) + "," + str(cy) + ")")
        print("Area #" + str(i + 1) + ": " + str(cv2.contourArea(c)))

cv2.imshow('Centroids',img)

cv2.waitKey(0)
