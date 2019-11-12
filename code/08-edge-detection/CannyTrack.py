"""
 * Python script to demonstrate Canny edge detection
 * with trackbars to adjust the thresholds. 
 *
 * usage: python CannyTrack.py <filename>
"""
import skimage
import skimage.feature
import skimage.viewer
import sys


filename = sys.argv[1]
image = skimage.io.imread(fname=filename, as_gray=True)
viewer = skimage.viewer.ImageViewer(image)


def canny(image, sigma, low_threshold, high_threshold):
    return skimage.feature.canny(
        image=image,
        sigma=sigma,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
    )


# Create the plugin and add sliders for the parameters
canny_plugin = skimage.viewer.plugins.Plugin(image_filter=canny)
canny_plugin.name = "Canny Filter Plugin"
canny_plugin += skimage.viewer.widgets.Slider(
    "sigma", low=0.0, high=7.0, value=2.0
)
canny_plugin += skimage.viewer.widgets.Slider(
    "low_threshold", low=0.0, high=1.0, value=0.1
)
canny_plugin += skimage.viewer.widgets.Slider(
    "high_threshold", low=0.0, high=1.0, value=0.2
)

# add the plugin to the viewer and show the window
viewer += canny_plugin
viewer.show()
