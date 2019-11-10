"""
 * Python script to practice simple thresholding.
 *
 * usage: python ThresholdPractice.py <filename> <kernel-size> <threshold>
"""
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.filters
import skimage.viewer

# get filename, kernel size, and threshold value from command line
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# read and display the original image
image = skimage.io.imread(fname=filename)
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(image, sigma=k)

# perform inverse binary thresholding
# MODIFY CODE HERE!
t = skimage.filters.thresh_otsu(blur)
mask = blur < t

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
viewer = skimage.viewer.ImageViewer(sel)
viewer.show()
