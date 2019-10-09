'''
 * Generate a grayscale histogram for an image.
 *
 * Usage: python GrayscaleHistogram.py <fiilename>
'''
import sys
import skimage.io
import skimage.viewer
import numpy as np
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = skimage.io.imread(fname=sys.argv[1], as_gray=True)
print(image.min(), image.max())

# display the image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# create the histogram
histogram = np.histogram(image, bins=256, range=(0., 1.))[0]

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255]) # <- named arguments do not work here

plt.plot(histogram) # <- or here
plt.show()

