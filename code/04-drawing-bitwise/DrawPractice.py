'''
 * Program to practice with OpenCV drawing methods.
'''
import cv2
import numpy as np

# create the black canvas
image = np.zeros(shape = (600, 800, 3), dtype = "uint8")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE

# display the results
cv2.namedWindow(winname = "image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "image", image)
cv2.waitKey(delay = 0)
