---
title: "Creating Histograms"
teaching: 25
exercises: 60
questions:
- "How can we create grayscale and color histograms to understand the 
distribution of color values in an image?"
objectives:
- "Explain what a histogram is."
- "Load an image in grayscale format."
- "Create and display grayscale and color histograms for entire images."
- "Create and display grayscale and color histograms for certain areas of images, via masks."
keypoints:
- "We can load images in grayscale by passing the `as_gray=True` 
parameter to the `skimage.io.imread()` function."
- "We can create histograms o images with the `np.histogram` function."
- "We can separate the RGB channels of an image using slicing operations."
- "We can display histograms using the `matplotlib pyplot` `figure()`, 
`title()`, `xlabel()`, `ylabel()`, `xlim()`, `plot()`, and `show()` functions."
---

In this episode, we will learn how to use skimage functions to create and 
display histograms for images.

## Introduction to Histograms

As it pertains to images, a *histogram* is a graphical representation showing
how frequently various color values occur in the image. We saw in the 
[Image Basics]({{ page.root }}/02-image-basics) episode that we could use a
histogram to visualize the differences in uncompressed and compressed image 
formats. If your project involves detecting color changes between images, 
histograms will prove to be very useful, and histograms are also quite handy
as a preparatory step before performing 
[Thresholding]({{ page.root }}/07-thresholding) or 
[Edge Detection]({{ page.root }}/08-edge-detection).

## Grayscale Histograms

We will start with grayscale images and histograms first, and then move on to 
color images. Here is a Python script to load an image in grayscale instead 
of full color, and then create and display the corresponding histogram. The first
few lines are:

~~~
'''
 * Generate a grayscale histogram for an image.
 *
 * Usage: python GrayscaleHistogram.py <fiilename> 
'''
import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt

# read image, based on command line filename argument;
# read the image as grayscale from the outset
image = skimage.io.imread(fname=sys.argv[1], as_gray=True)

# display the image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()
~~~
{: .python}

In the program, we have a new import from `matplotlib`, to gain access to the
tools we will use to draw the histogram. The statement

`from matplotlib import pyplot as plt`

loads up the `pyplot` library, and gives it a shorter name, `plt`. 

Next, we use the `skimage.io.imread()` function to load our image. We use the first 
command line parameter as the filename of the image, as we did in the 
[Skimage Images]({{ page.root }}/03-skimage-images) lesson. The second parameter
to `skimage.io.imread()` instructs the function to transform the image into 
grayscale as it is loaded in to the program. Note that this does not change
the original image. There are skimage functions to convert a color image to 
grayscale, but in cases where the program does not need the color image, we can
save ourselves some typing by loading the image as grayscale from the outset.

Skimage does not provide a special function to compute histograms, but we can use
the function `np.histogram` instead:

~~~
# create the histogram
histogram = np.histogram(image, bins=256, range=(0, 256))
~~~
{: .python}

The parameter `bins` determines the histogram size, or the number of "bins" to use for
the histogram. We pass in `256` because we want to see the pixel count for
each of the 256 possible values in the grayscale image.

The parameter `range` is the range of values each of the pixels in the image can
have. Assuming 24-bit color, each channel has values between 0 and 255. We 
communicate that to the `np.histogram()` function with the `(0, 256)` parameter,
which is somewhat confusing. The minimum value is inclusive, while the 
maximum value is *one more* than the actual maximum value of the range. 

The output of the `np.histogram` function is a one-dimensional NumPy array,
with 256 rows and one column, representing the number of pixels with the color
value corresponding to the index. I.e., the first number in the array is the
number of pixels found with color value 0, and the final 
number in the array is the number of pixels found with color value 255. 

Next, we turn our attention to displaying the histogram, by taking advantage
of the plotting facilities of the `matplotlib` library.

~~~
# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 256]) # <- named arguments do not work here

plt.plot(histogram) # <- or here
plt.show()
~~~
{: .python}


We create the plot with
`plt.figure()`, then label the figure and the coordinate axes with 
`plt.title()`, `plt.xlabel()`, and `plt.ylabel()` functions. The last step in
the preparation of the figure is to set the limits on the values on the 
x-axis with the `plt.xlim([0, 256])` function call. 

> ## Variable-length argument lists
> 
> Note that we cannot used named parameters for the `plt.xlim()` or 
> `plt.plot()` functions. This is because these functions are defined
> to take an arbitrary number of *unnamed* arguments. The designers wrote
> the functions this way because they are very versitile, and creating named
> parameters for all of the possible ways to use them would be complicated.
{: .callout}

Finally, we create the histogram plot itself with `plt.plot(histogram)`, and 
then make it appear with `plt.show()`. When we run the program on this image
of a plant seedling,

> ## Histograms in matplotlib
> 
> Matplotlib provides a dedicated function to compute and display histograms:
> `plt.hist()`. We will not use it in this lesson in order to understand how to calculate
> histograms in more detail. In practice, it is a good idea to use this function, because it
> visualizes histograms more appropriately than `plt.plot()`.
> Here, you could use it by calling `plt.hist(image, bins=256, range=(0, 256))` instead of
> `numpy.histogram()` and `plt.plot()`.
> 
> 
{: .callout}

![Plant seedling](../fig/04-plant-seedling.jpg)

the program produces this histogram:

![Plant seedling histogram](../fig/04-plant-seedling-gs-histogram.png)

> ## Using a mask for a histogram (25 min)
> 
> Looking at the histogram above, you will notice that there is a large number
> of very dark pixels, as indicated in the chart by the spike around the 
> grayscale value 30. That is not so surprising, since the original image is 
> mostly black background. What if we want to focus more closely on the leaf of
> the seedling? That is where a mask enters the picture!
> 
> Navigate to the **Desktop/workshops/image-processing/05-creating-histograms**
> directory, and edit the **GrayscaleMaskHistogram.py** program. The skeleton
> program is a copy of the mask program above, with comments showing where to
> make changes. 
> 
> First, use a tool like ImageJ to determine the *(x, y)* coordinates of a 
> bounding box around the leaf of the seedling. Then, using techniques from the
> [Drawing and Bitwise Operations]({{ page.root }}/04-drawing-bitwise/)
> episode, create a mask with a white rectangle covering that bounding box. 
> 
> After you have created the mask, apply it to the input image before passing
> it to the `np.histogram` function.
> Then, run the **GrayscaleMaskHistogram.py** program and observe the resulting
> histogram. 
> 
> > ## Solution
> > ~~~
> > '''
> >  * Generate a grayscale histogram for an image. 
> >  * 
> >  * Usage: python GrayscaleMaskHistogram.py <filename>
> > '''
> > import sys
> > import numpy as np
> > import skimage.draw
> > import skimage.io
> > import skimage.viewer
> > from matplotlib import pyplot as plt
> > 
> > # read image, based on command line filename argument;
> > # read the image as grayscale from the outset
> > img = skimage.io.imread(fname=sys.argv[1], as_gray=True)
> > 
> > # display the image
> > viewer = skimage.viewer.ImageViewer(img)
> > viewer.show()
> > 
> > # create mask here, using np.zeros() and skimage.draw.rectangle()
> > # WRITE YOUR CODE HERE
> > mask = np.zeros(shape=img.shape, dtype="bool")
> > bounding_box = skimage.draw.rectangle(start=(199, 410), end=(384, 485)) 
> > 
> > # mask the image and create the new histogram
> > histogram = np.histogram(img[mask], bins=256, range=(0, 256))
> > 
> > # configure and draw the histogram figure
> > plt.figure()
> > plt.title("Grayscale Histogram")
> > plt.xlabel("grayscale value")
> > plt.ylabel("pixels")
> > plt.xlim([0, 256])
> > 
> > plt.plot(histogram)
> > plt.show()
> > ~~~
> > {: .python}
> > 
> > Your histogram of the masked area should look something like this:
> > 
> > ![Grayscale histogram of masked area](../fig/04-plant-seedling-gs-histogram-mask.png)
> {: .solution}
> 
{: .challenge}

## Color Histograms

We can also create histograms for full color images, in addition to grayscale 
histograms. We have seen color histograms before, in the 
[Image Basics]({{ page.root }}/02-image-basics) episode. A program to create
color histograms starts in a familiar way:

~~~
'''
 * Python program to create a color histogram.
 *
 * Usage: python ColorHistogram.py <filename>
'''
import sys
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = skimage.io.imread(fname=sys.argv[1])

# display the image 
viewer = skimage.viewer.Viewer(image)
viewer.show()
~~~
{: .python}

We import the needed libraries, read 
the image based on the command-line parameter (in color this time), and then
display the image. 

~~~
# split into channels
channels = [image[:, :, i] for i in range(image.shape[2])]
~~~
{: .python}


Next, we make the histogram, by calling the `numpy.histogram` function three 
times, once for each of the channels. We obtain the individual channels, by
slicing the image along the last axis. For example, we can obtain the red color channel
by calling `r_chan = image[:, :, 0]`.

~~~
# tuple to select colors of each channel line
colors = ("r", "g", "b") 
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_id, c in zip(channel_ids, colors):
    histogram = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))
    plt.plot(histogram, color=c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()
~~~
{: .python}


We will draw the histogram line for 
each channel in a different color, and so we create a tuple of the colors to 
use for the three lines with the 

`colors = ("r", "g", "b")`

line of code. Then, we limit the range of the x-axis with the `plt.xlim()` 
function call. 

Next, we use the `for` control structure to iterate through the three
channels, plotting an appropriately-colored histogram line for each. This may
be new Python syntax for you, so we will take a moment to discuss what is 
happening in the `for` statement. 

The Python built-in `zip()` function takes a series of one or more lists and 
returns an *iterator* of *tuples*, where the first tuple contains the first
element of each of the lists, the second contains the second element of each
of the lists, and so on. 

> ## Iterators, tuples, and `zip()`
> 
> In Python, an *iterator*, or an *iterable object*, is, basically, something 
> that can be iterated over with the `for` control structure. A *tuple* is
> a sequence of objects, just like a list. However, a tuple cannot be changed,
> and a tuple is indicated by parentheses instead of square brackets. The 
> `zip()` function takes one or more iterable objects, and returns an iterator
> of tuples consisting of the corresponding ordinal objects from each 
> parameter.
> 
> For example, consider this small Python program:
> 
> ~~~
> list1 = (1, 2, 3, 4, 5)
> list2 = ('a', 'b', 'c', 'd', 'e')
> 
> for x in zip(list1, list2):
> 	print(x)
> ~~~
> {: .python}
> 
> Executing this program would produce the following output:
> 
> > (1, 'a')
> > 
> > (2, 'b')
> > 
> > (3, 'c')
> > 
> > (4, 'd')
> > 
> > (5, 'e')
> {: .output}
{: .callout}

In our color histogram program, we are using a tuple, `(channel_id, c)`, as the 
`for` variable. The first time through the loop, the `channel_id` variable takes the
value `0`, referring to the position of the red color channel,
and the `c` variable contains the string `"r"`. The second time 
through the loop the values are the green channels position and `"g"`, and the third 
time they are the blue channel position and `"b"`. 

Inside the `for` loop, our code looks much like it did for the grayscale 
example. We calculate the histogram for the current channel with the 

`histogram = np.histogram(image[:, :, channel_id], bins=256, range=(0, 256))`

function call, and then add a histogram line of the correct color to the 
plot with the 

`plt.plot(histogram, color=c)`

function call. Note the use of our loop variables, `channel_id` and `c`. 

Finally we label our axes and display the histogram, shown here:

![Color histogram](../fig/04-plant-seedling-histogram.png)

> ## Color histogram with a mask (25 min)
> 
> We can also apply a mask to the images we apply the color histogram process
> to, in the same way we did for grayscale histograms. Consider this image of a
> well plate, where various chemical sensors have been applied to water and 
> various concentrations of hydrochloric acid and sodium hydroxide:
> 
> ![Well plate image](../fig/09-well-plate.jpg)
> 
> Suppose we are interested in the color histogram of one of the sensors in the
> well plate image, specifically, the seventh well from the left in the topmost
> row, which shows Erythrosin B reacting with water. 
> 
> Use ImageJ to find the center of that well and the radius (in pixels) of the 
> well. Then, navigate to the 
> **Desktop/workshops/image-processing/05-creating-histograms** directory, and
> edit the **ColorHistogramMask.py** program. 
> 
> Guided by the comments in the **ColorHistogramMask.py** program, create a 
> circular mask to select only the desired well. Then, use that mask to apply
> the color histogram operation to that well. When you execute the program on 
> the **plate-01.tif** image, your program should display `maskedImg`, which 
> will look like this:
> 
> ![Masked well plate](../fig/04-masked-well-plate.jpg)
> 
> And, the program should produce a color histogram that looks like this: 
> 
> ![Well plate histogram](../fig/04-well-plate-histogram.png)
> 
> > ## Solution
> > 
> > Here is the modified version of **ColorHistogramMask.py** that produced the
> > preceding images.
> > 
> > ~~~
> > '''
> >  * Python program to create a color histogram on a masked image.
> >  *
> >  * Usage: python ColorHistogramMask.py <filename>
> > '''
> > import sys
> > import skiamge.io
> > import skimage.viewer
> > import skiamge.draw
> > import numpy as np
> > from matplotlib import pyplot as plt
> > 
> > # read original image, in full color, based on command
> > # line argument
> > image = skimage.io.imread(fname=sys.argv[1])
> > 
> > # display the original image 
> > viewer = skimage.viewer.ImageViewer(image)
> > viewer.show()
> > 
> > # create a circular mask to select the 7th well in the first row
> > # WRITE YOUR CODE HERE
> > mask = np.zeros(shape=image.shape, dtype="bool")
> > circle = skimage.draw.circle(240, 1053, radius=49, shape=image.shape[:2])
> > mask[circle] = 1
> > 
> > # use np.logical_and() to apply the mask to img, and save the 
> > # results in a new image named maskedImg
> > # WRITE YOUR CODE HERE
> > masked_img = np.logical_and(image, mask)
> > 
> > # create a new window and display maskedImg, to verify the 
> > # validity of your mask
> > # WRITE YOUR CODE HERE
> > viewer = skimage.viewer.ImageViewer(masked_img)
> > viewer.show()
> > 
> > # right now, the mask is black and white, but it has three
> > # color channels. We need it to have only one channel.
> > # Convert the mask to a grayscale image, using slicing to
> > # pull off just the first channel.
> > # WRITE YOUR CODE HERE
> > mask = mask[:, :, 0]
> > 
> > # list to select colors of each channel line
> > colors = ("r", "g", "b") 
> > channel_ids = (0, 1, 2)
> > 
> > # create the histogram plot, with three lines, one for
> > # each color
> > plt.xlim([0, 256])
> > for(channel_id, c) in zip(channel_ids, colors):
> >     # change this to use your circular mask to apply the histogram
> >     # operation to the 7th well of the first row
> >     # MODIFY CODE HERE
> >     histogram = np.histogram(image[:, :, channel_id][mask],)
> >         bins=256, 
> >         range=(0, 256))
> > 
> >     plt.plot(histogram, color = c)
> > 
> > plt.xlabel("Color value")
> > plt.ylabel("Pixels")
> > 
> > plt.show()
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Histograms for the morphometrics challenge (10 min)
> 
> Using the grayscale and color histogram programs we developed in this episode,
> create histograms for the bacteria colonies in the 
> **Desktop/workshops/image-processing/10-challenges** directory. Save the 
> histograms for later use.
{: .challenge}
