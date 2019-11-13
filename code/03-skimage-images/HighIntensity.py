"""
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
"""
import sys
import skimage.io
import skimage.viewer

# read input image, based on filename parameter
image = skimage.io.imread(fname=sys.argv[1])

# display original image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# keep only high-intensity pixels
image[image < 128] = 0

# display modified image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()
