'''
 * Python program to open, display, and save an image.
 *
'''
import skimage.io
import skimage.viewer

# read image
image = skimage.io.imread(fname="chair.jpg")

# display image and wait for keypress, using a resizable window
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# save a new version in .tif format
skimage.io.imsave(fname="chair.tif", arr=image)
