'''
 * Python script to demonstrate Sobel edge detection.
 *
 * usage: python SobelEdge.py <filename> <kernel-size> <threshold>
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

# perform Sobel edge detection in x and y dimensions
edgeX = cv2.Sobel(binary, cv2.CV_16S, 1, 0)
edgeY = cv2.Sobel(binary, cv2.CV_16S, 0, 1)

# convert back to 8-bit, unsigned numbers and combine edge images
edgeX = np.uint8(np.absolute(edgeX))
edgeY = np.uint8(np.absolute(edgeY))
edge = cv2.bitwise_or(edgeX, edgeY)

# display edges
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.imshow("edges", edge)
cv2.waitKey(0)