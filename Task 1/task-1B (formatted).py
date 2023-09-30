# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2 as cv


# load the image, 
image = cv2.imread('led.jpg', 1)

# convert it to grayscale, and blur it
imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgray=cv2.GaussianBlur(imgray,(1,1),0)

# threshold the image to reveal light regions in the blurred image
_,thresh=cv2.threshold(imgray,211,255,cv2.THRESH_BINARY)


# perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)

# perform a connected component analysis on the thresholded image, then initialize a mask to store only the "large" components
labels=measure.label(thresh, connectivity=2,  background=0)
mask = np.zeros(thresh.shape, dtype="uint8")

# loop over the unique components
for label in np.unique(labels):
    # If this is the background label, ignore it
    if label == 0:
        continue

    # otherwise, construct the label mask and count the number of pixels
    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)

    # if the number of pixels in the component is sufficiently large, then add it to our mask of "large blobs"
    if numPixels > 10:
        mask = cv2.add(mask, labelMask)


# find the contours in the mask, then sort them from left to right
cnts,_=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts=contours.sort_contours(cnts)[0]

# loop over the contours

# Initialize lists to store centroid coordinates and area
cntrd=[]
areas=[]

# Loop over the contours
for c in cnts:


    # Calculate the area of the contour
    area=cv2.contourArea(c)

    #Calculate the centroid coordinates (check again)
    M = cv2.moments(c)
    if M["m00"] != 0:
        cx = float(M["m10"] / M["m00"])
        cy = float(M["m01"] / M["m00"])

    

    # Draw the bright spot on the image


    # Append centroid coordinates and area to the respective lists
    areas.append(area)
    cntrd.append((cx,cy))

# Save the output image as a PNG file
cv2.imwrite("led_detection_results.png", image)

# Open a text file for writing
with open("led_detection_results.txt", "w") as file:
    # Write the number of LEDs detected to the file
    file.write(f"No. of LEDs detected: {a}\n")
    # Loop over the contours
    
        # Write centroid coordinates and area for each LED to the file
        file.write(f"Centroid #{i + 1}: {centroid}\nArea #{i + 1}: {area}\n")
# Close the text file
file.close()
