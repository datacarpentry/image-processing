'''
 * Python program to create a color histogram.
 *
 * Usage: python ColorHistogram.py <filename>
'''
import cv2
import sys
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = cv2.imread(filename = sys.argv[1])

# display the image 
cv2.namedWindow(winname = "Original Image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "Original Image", mat = image)
cv2.waitKey(delay = 0)

# split into channels
channels = cv2.split(image)

# tuple to select colors of each channel line
colors = ("b", "g", "r") 

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for(channel, c) in zip(channels, colors):
    histogram = cv2.calcHist(
        images = [channel], 
        channels = [0], 
        mask = None, 
        histSize = [256], 
        ranges = [0, 256])

    plt.plot(histogram, color = c)

plt.xlabel(xlabel = "Color value")
plt.ylabel(ylabel = "Pixels")

plt.show()
