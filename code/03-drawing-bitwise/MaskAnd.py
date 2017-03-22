'''
 * Python program to apply a mask to an image.
 *
'''
import cv2, numpy as np

# Load the original image
img = cv2.imread("maize-roots.tif")

# Create the basic black image 
mask = np.zeros(img.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(mask, (44, 357), (720, 740), (255, 255, 255), -1)

# Apply the mask and display the result
maskedImg = cv2.bitwise_and(img, mask)
cv2.namedWindow("Masked Image", cv2.WINDOW_NORMAL)
cv2.imshow("Masked Image", maskedImg)
cv2.waitKey(0)
