'''
 * Program to practice with OpenCV drawing methods.
'''
import skimage
import numpy as np
import random
from skimage.viewer import ImageViewer

# create the black canvas
image = np.zeros(shape = (600, 800, 3), dtype = "uint8")

# WRITE YOUR CODE TO DRAW ON THE IMAGE HERE

# display the results
viewer = ImageViewer(image)
viewer.show()
