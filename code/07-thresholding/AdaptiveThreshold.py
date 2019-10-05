'''
 * Python script to demonstrate adaptive thresholding using Otsu's method.
 *
 * usage: python AdaptiveThreshold.py <filename> <kernel-size>
'''
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.filters
import skimage.viewer

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display the original image
image = skimage.io.imread(fname=filename)
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# grayscale and blur before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(image, sigma=k)

# perform adaptive thresholding
t = skimage.filters.thresh_otsu(blur)
mask = blur > t

viewer = skimage.viewer.ImageViewer(mask)
viewer.show()

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
viewer = skimage.viewer.ImageViewer(sel)
viewer.show()
