'''
 * Python script to extract a sub-image containing only the plant and
 * roots in an existing image.
'''
import cv2

# load and display original image
image = cv2.imread(filename = "roots.jpg")
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# extract, display, and save sub-image
# WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:


cv2.namedWindow(winname = "clip", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "clip", mat = clip)
cv2.waitKey(delay = 0)

# WRITE YOUR CODE TO SAVE clip HERE

