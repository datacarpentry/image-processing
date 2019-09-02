'''
 * Python script demonstrating image modification and creation via
 * NumPy array slicing.
'''
import skimage.io
import skimage.viewer

# load and display original image
image = skimage.io.imread(fname="board.jpg")
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# extract, display, and save sub-image
clip = image[60:151, 135:481, :]
viewer = skimage.viewer.ImageViewer(clip)
viewer.show()
skimage.io.imsave(fname="clip.tif", arr=clip)

# replace clipped area with sampled color
color = image[330, 90]
image[60:151, 135:481] = color
viewer = skimage.viewer.ImageViewer(image)
viewer.show()
