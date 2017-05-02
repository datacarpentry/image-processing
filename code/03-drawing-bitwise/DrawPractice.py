'''
 * Program to practice with OpenCV drawing methods.
'''
import cv2, numpy as np

# create the black canvas
img = np.zeros((600, 800, 3), dtype = "uint8")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE

# display the results
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)