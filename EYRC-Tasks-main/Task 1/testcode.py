from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('sample.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray=cv2.GaussianBlur(imgray,(9,9),0)
_,thresh=cv2.threshold(imgray,133,255,cv2.THRESH_BINARY)
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)


labels=measure.label(thresh,connectivity=2, background=0)

mask=np.zeros(thresh.shape,dtype='uint8')
mask1=mask.copy()

for label in np.unique(labels):
    if label ==0:
        continue
    
    labelmask=np.zeros(thresh.shape,dtype='uint8')
    labelmask[labels==label]=255
    numpix=cv2.countNonZero(labelmask)
    mask1=cv2.add(mask1,labelmask)
    
cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts=contours.sort_contours(cnts,method="left-to-right")[0]
cv2.drawContours(img,cnts,-1,(0,255,0),2)

cv2.imshow('led',img)
cv2.destroyAllWindows()