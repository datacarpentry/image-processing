'''
 * Python program to create a color histogram on a masked image.
 *
 * Usage: python ColorHistogramMask.py <filename>
'''
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = cv2.imread(filename = sys.argv[1])

# display the original image 
cv2.namedWindow(winname = "Original Image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "Original Image", mat = image)
cv2.waitKey(delay = 0)

# create a circular mask to select the 7th well in the first row
# WRITE YOUR CODE HERE

# use cv2.bitwise_and() to apply the mask to img, and save the 
# results in a new image named maskedImg
# WRITE YOUR CODE HERE

# create a new window and display maskedImg, to verify the 
# validity of your mask
# WRITE YOUR CODE HERE


# right now, the mask is black and white, but it has three
# color channels. We need it to have only one channel.
# Convert the mask to a grayscale image, using slicing to
# pull off just the first channel
# WRITE YOUR CODE HERE

# split into channels
channels = cv2.split(image)

# list to select colors of each channel line
colors = ("b", "g", "r") 

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for(channel, c) in zip(channels, colors):
    # change this to use your circular mask to apply the histogram
    # operation to the 7th well of the first row
    # MODIFY CODE HERE
    histogram = cv2.calcHist(
        images = [channel], 
        channels = [0], 
        mask = None, 
        histSize = [256], 
        ranges = [0, 256])

    plt.plot(histogram, color = c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()
