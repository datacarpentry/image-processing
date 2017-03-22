'''
 * Python program to use OpenCV drawing tools to create a mask.
 *
'''
import cv2, numpy as np

# Load and display the original image
img = cv2.imread("maize-roots.tif")
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(0)

# Create the basic black image 
mask = np.zeros(img.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(mask, (44, 357), (720, 740), (255, 255, 255), -1)

# Display constructed mask
cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

