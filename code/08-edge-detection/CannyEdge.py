'''
 * Python script to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename> <lo> <hi>
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]
lo = int(sys.argv[2])
hi = int(sys.argv[3])

# load and display original image as grayscale
image = cv2.imread(filename = filename, flags = cv2.IMREAD_GRAYSCALE)
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# perform Canny edge detection
edges = cv2.Canny(image = image, 
    threshold1 = lo,
    threshold2 = hi)

# display edges
cv2.namedWindow(winname = "edges", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "edges", mat = edges)
cv2.waitKey(delay = 0)
