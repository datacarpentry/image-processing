"""
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
 *
 * usage: python RootMass.py <filename> <sigma>
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
img = cv2.imread(fname=filename, as_gray=True)

# blur before thresholding
blur = skimage.filters.gaussian(img, sigma=sigma)

# perform adaptive thresholding to produce a binary image
t = skimage.filters.thresh_otsu(blur)
binary = blur > t

# save binary image; first find beginning of file extension
dot = filename.index(".")
binaryFileName = filename[:dot] + "-binary" + filename[dot:]
skimage.io.imsave(fname=binaryFileName, arr=binary)

# determine root mass ratio
rootPixels = np.nonzero(binary)
w = binary.shape[1]
h = binary.shape[0]
density = float(rootPixels) / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
