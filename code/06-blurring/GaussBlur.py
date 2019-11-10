"""
 * Python script to demonstrate Gaussian blur.
 *
 * usage: python GaussBlur.py <filename> <sigma>
"""
import skimage
from skimage.viewer import ImageViewer
import sys

# get filename and kernel size from command line
filename = sys.argv[1]
sigma = float(sys.argv[2])

# read and display original image
image = skimage.io.imread(fname=filename)
viewer = ImageViewer(image)
viewer.show()

# apply Gaussian blur, creating a new image
blurred = skimage.filters.gaussian(
    image, sigma=(sigma, sigma), truncate=3.5, multichannel=True
)

# display blurred image
viewer = ImageViewer(blurred)
viewer.show()
