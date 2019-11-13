"""
 * Python script to extract a sub-image containing only the plant and
 * roots in an existing image.
"""
import skimage.io
import skimage.viewer

# load and display original image
image = skimage.io.imread(fname="roots.jpg")
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# extract, display, and save sub-image
# WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:

viewer = skimage.viewer.ImageViewer(clip)
viewer.show()


# WRITE YOUR CODE TO SAVE clip HERE
