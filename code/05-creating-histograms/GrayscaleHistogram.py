'''
 * Generate a grayscale histogram for an image.
 *
 * Usage: python GrayscaleHistogram.py <fiilename> 
'''
import cv2
import sys
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = cv2.imread(filename = sys.argv[1], flags = cv2.IMREAD_GRAYSCALE)

# display the image
cv2.namedWindow(winname = "Grayscale Image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "Grayscale Image", mat = image)
cv2.waitKey(delay = 0)

# create the histogram
histogram = cv2.calcHist(images = [image], 
    channels = [0], 
    mask = None, 
    histSize = [256], 
    ranges = [0, 256])

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 256]) # <- named arguments do not work here

plt.plot(histogram) # <- or here
plt.show()

