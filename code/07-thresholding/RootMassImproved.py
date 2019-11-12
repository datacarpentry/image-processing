"""
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
 *
 * This version applies thresholding twice, to get rid of the white
 * circle and label from the image before performing the root mass
 * ratio calculations.
 *
 * usage: python RootMassImproved.py <filename> <sigma>
"""
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.filters

# get filename and kernel size values from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])

# read the original image, converting to grayscale
image = skimage.io.imread(fname=filename, as_gray=True)

# blur before thresholding
blur = skimage.filters.gaussian(image, sigma=sigma)

# WRITE CODE HERE
# perform inverse binary thresholding to create a mask that will remove
# the white circle and label.


# WRITE CODE HERE
# use the mask you just created to remove the circle and label from the
# blur image


# perform adaptive thresholding to produce a binary image
t = skimage.filters.thresh_otsu(blur)
binary = blur > t

# save binary image; first find extension beginning
dot = filename.index(".")
binaryFileName = filename[:dot] + "-binary" + filename[dot:]
skimage.io.imwsave(filename=binaryFileName, img=binary)

# determine root mass ratio
rootPixels = np.nonzero(binary)
w = binary.shape[1]
h = binary.shape[0]
density = float(rootPixels) / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
