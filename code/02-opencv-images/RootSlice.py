'''
 * Python script to extract a sub-image containing only the plant and
 * roots in an existing image.
'''
import cv2

# load and display original image
img = cv2.imread("roots.jpg")
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# extract, display, and save sub-image
# WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:


cv2.namedWindow("clip", cv2.WINDOW_NORMAL)
cv2.imshow("clip", clip)
cv2.waitKey(0)

# WRITE YOUR CODE TO SAVE clip HERE

