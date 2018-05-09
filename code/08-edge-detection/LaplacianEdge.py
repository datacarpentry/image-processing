'''
 * Python script to demonstrate Laplacian edge detection.
 *
 * usage: python LaplacianEdge.py <filename> <kernel-size> <threshold>
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# load and display original image
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# blur image and use simple inverse binary thresholding to create
# a binary image
blur = cv2.GaussianBlur(img, (k, k), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# WRITE YOUR CODE HERE
# perform Laplacian edge detection
# cv2.Laplacian() takes two parameters, the input image, and the data
# type used for the output image. Use the cv2.Laplacian() method to 
# detect the edges in the binary image, storing the result in an image 
# named edge.

# WRITE YOUR CODE HERE
# Convert the edge image back to 8 bit unsigned integer data type.

# display edges
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.imshow("edges", edge)
cv2.waitKey(0)
