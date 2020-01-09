"""
 * Python script count objects in an image
 *
 * usage: python CCA.py <filename> <sigma> <threshold>
"""
import sys

import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.measure
import skimage.viewer

# get filename, sigma, and threshold value from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])
t = float(sys.argv[3])

# read and display the original image
image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# blur and grayscale before thresholding
blur = skimage.filters.gaussian(image, sigma=sigma)

# perform inverse binary thresholding
mask = blur < t

# display the result
viewer = skimage.viewer.ImageViewer(mask)
viewer.show()

# Perform CCA on the mask
labeled_image = skimage.measure.label(mask, connectivity=2)

viewer = skimage.viewer.ImageViewer(skimage.color.label2rbg(labeled_image, bg_label=0))
viewer.show()
