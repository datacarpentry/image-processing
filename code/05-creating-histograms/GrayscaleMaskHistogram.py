'''
 * Generate a grayscale histogram for an image. 
 * Usage: python GrayscaleMaskHistogram.py <filename> 
'''
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = cv2.imread(filename = sys.argv[1], flags = cv2.IMREAD_GRAYSCALE)

# display the image
cv2.namedWindow(winname = "Grayscale Image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "Grayscale Image", mat = image)
cv2.waitKey(delay = 0)

# create mask here, using np.zeros() and cv2.rectangle()
# WRITE YOUR CODE HERE

# create the histogram, using mask instead of None in the
# cv2.calcHist() function call
# MODIFY CODE HERE
histogram = cv2.calcHist(
    images = [img], 
    channels = [0], 
    mask = None, 
    histSize = [256], 
    ranges = [0, 256])

# configure and draw the histogram figure
plt.figure()
plt.title(label = "Grayscale Histogram")
plt.xlabel(xlabel = "grayscale value")
plt.ylabel(ylabel = "pixels")
plt.xlim([0, 256])

plt.plot(histogram)
plt.show()
