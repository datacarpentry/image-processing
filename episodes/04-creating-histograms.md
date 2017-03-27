---
title: "Creating Histograms"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to create and 
display histograms for images.

## Introduction to Histograms

As it pertains to images, a *histogram* is a graphical representation showing
how frequently various color values occur in the image. We saw in the 
[Image Basics]({{ page.root }}/01-image-basics) episode that we could use a
histogram to visualize the differences in uncompressed and compressed image 
formats. If your project involves detecting color changes between images, 
histograms will prove to be very useful.

## Grayscale Histograms

We will start with grayscale images and histograms first, and then move on to 
color images. Here is a Python script to load an image in grayscale instead 
of full color, and then create and display the corresponding histogram. 

~~~
'''
 * Generate a grayscale histogram for an image. 
'''
import cv2, sys
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

# display the image
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)
cv2.imshow("Grayscale Image", img)
cv2.waitKey(0)

# create the histogram
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 256])

plt.plot(histogram)
plt.show()
~~~
{: .python}

In the program, we have a new import from `matplotlib`, to gain access to the
tools we will use to draw the histogram. The statement

`from matplotlib import pyplot as plt`

loads up the `pyplot` library, and gives it a shorter name, `plt`. 

Next, we use the `cv2.imread()` function to load our image. We use the first 
command line parameter as the filename of the image, as we did in the 
[OpenCV Images]({{ page.root }}/02-opencv-images) lesson. The second parameter
to `cv2.imread()` instructs the function to transform the image into 
grayscale as it is loaded in to the program. Note that this does not change
the original image. There are OpenCV functions to convert a color image to 
grayscale, but in cases where the program does not need the color image, we can
save ourselves some typing by loading the image as grayscale from the outset.

The next salient piece of code is where we ask OpenCV to create the histogram,
with the 

`histogram = cv2.calcHist([img], [0], None, [256], [0, 256])`

function call. The `cv2.calcHist()` function can operate on more than one image
if we so desire, and so the first parameter to the function is the list of 
images to process. In our case, we are only using one image, so we add it to
a list by enclosing it in square brackets: `[img]`.

The next parameter is a list specifying the channels to examine for the 
histogram. Since this is a grayscale image, there is only one channel, and so
we pass in `[0]`. 

The third parameter is the mask to use to select the portion of the image to
examine for the histogram. Here we are looking at the whole image, so we pass
in `None` for the mask.

The next parameter is the histogram size, or the number of "bins" to use for
the histogram. We pass in `[256]` because we want to see the pixel count for
each of the 256 possible values in the grayscale image.

The final parameter is the range of values each of the pixels in the image can
have. Assuming 24-bit color, each channel has values in the range `[0, 256]`,
which is what we pass in. 

The output of the `cv2.calcHist()` function is a one-dimensional NumPy array,
with 256 rows and one column, representing the number of pixels with the color
value corresponding to the index. I.e., the first number in the array is the
number of pixels found with color value 00000000, and the final number in the
array is the number of pixels found with color value 11111111. 

Next, we turn our attention to displaying the histogram, by taking advantage
of the plotting facilities of the `matplotlib` library. We create the plot with
`plt.figure()`, then label the figure and the coordinate axes with 
`plt.title()`, `plt.xlabel()`, and `plt.ylabel()` functions. The last step in
the preparation of the figure is to set the limits on the values on the 
x-axis with the `plt.xlim([0, 256])` function call. 

Finally, we create the histogram plot itself with `plt.plot(histogram)`, and 
then make it appear with `plt.show()`. When we run the program on this image
of a plant seedling,

![Plant seedling](../fig/04-plant-seedling.jpg)

the program produces this histogram:

![Plant seedling histogram](../fig/04-plant-seedling-gs-histogram.png)
