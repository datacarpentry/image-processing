'''
 * Python program to create a color histogram on a masked image.
 *
 * Usage: python ColorHistogramMask.py <filename>
'''
import sys
import skimage.draw
import skimage.io
import skimage.viewer
import numpy as np
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname=sys.argv[1])

# display the original image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# create a circular mask to select the 7th well in the first row
# WRITE YOUR CODE HERE

# use np.logical_and() to apply the mask to img, and save the
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

# list to select colors of each channel line
colors = ("r", "g", "b")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    # change this to use your circular mask to apply the histogram
    # operation to the 7th well of the first row
    # MODIFY CODE HERE
    histogram = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))

    plt.plot(histogram, color=c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()
