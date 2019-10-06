'''
 * Python program to use a slider to control fixed-level 
 * thresholding value.
 *
 * usage: python interactive_thresholding.py <filename>
'''

import skimage
import skimage.viewer
import sys

filename = sys.argv[1]


def filter_function(image, sigma, threshold):
    masked = image.copy()
    masked[skimage.filters.gaussian(image, sigma=sigma) <= threshold] = 0
    return masked

smooth_threshold_plugin = skimage.viewer.plugins.Plugin(
    image_filter=filter_function
    )

smooth_threshold_plugin.name = "Smooth and Threshold Plugin"

smooth_threshold_plugin += skimage.viewer.widgets.Slider(
    "sigma", low=0.0, high=7.0, value=1.0)
smooth_threshold_plugin += skimage.viewer.widgets.Slider(
    "threshold", low=0.0, high=1.0, value=0.5)

image = skimage.io.imread(fname=filename, as_gray=True)

viewer = skimage.viewer.ImageViewer(image=image)
viewer += smooth_threshold_plugin
viewer.show()
