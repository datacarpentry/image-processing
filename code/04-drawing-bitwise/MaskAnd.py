'''
 * Python program to apply a mask to an image.
 *
'''
import cv2
import numpy as np

# Load the original image
image = cv2.imread(filename = "maize-roots.tif")

# Create the basic black image 
mask = np.zeros(shape = image.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(img = mask, 
	pt1 = (44, 357), pt2 = (720, 740), 
	color = (255, 255, 255), 
	thickness = -1)

# Apply the mask and display the result
maskedImg = cv2.bitwise_and(src1 = image, src2 = mask)
cv2.namedWindow(winname = "masked image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "masked image", mat = maskedImg)
cv2.waitKey(delay = 0)

