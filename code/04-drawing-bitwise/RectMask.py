'''
 * Python program to use OpenCV drawing tools to create a mask.
 *
'''
import cv2
import numpy as np

# Load and display the original image
image = cv2.imread(filename = "maize-roots.tif")
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# Create the basic black image 
mask = np.zeros(shape = image.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(img = mask, pt1 = (44, 357), pt2 = (720, 740), 
	color = (255, 255, 255), thickness = -1)

# Display constructed mask
cv2.namedWindow(winname = "mask", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "mask", mat = mask)
cv2.waitKey(delay = 0)

