'''
 * Generate a grayscale histogram for an image. 
'''
import cv2, sys, numpy as np
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

# display the image
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)
cv2.imshow("Grayscale Image", img)
cv2.waitKey(0)

# create mask here, using np.zeros() and cv2.rectangle()


# create the histogram, using mask instead of None in the
# cv2.calcHist() function call
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 256])

plt.plot(histogram)
plt.show()
