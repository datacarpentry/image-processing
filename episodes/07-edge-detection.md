---
title: "Edge Detection"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to apply *edge 
detection* to an image. In edge detection, we find the boundaries or edges of
objects in an image, by determining where the brightness of the image changes
dramtically. Once we have found the edges of the objects in the image, we can 
use that information to find the image *contours*, which we will learn about in
the following [Contours]({{ page.root }}./08-contours.md) episode. With the 
contours, we can do things like counting the number of objects in the image,
measure the size of the objects, and so on. 

As was the case for blurring and thresholding, there are several different 
methods in OpenCV that can be used for edge detection, so we will examine only
a few. 

## Introduction to edge detection

To begin our introduction to edge detection, let us look at an image with a
very simple edge -- this grayscale image of two overlapped pieces of paper, one
black and and one white:

![Black and white image](../fig/07-bw.jpg)

The obvious edge in the image is the vertical line between the black paper and
the white paper. To our eyes, there is a quite sudden change between the black
pixels and the white pixels. But, at a pixel-by-pixel level, is the transition
really that sudden? 

We can tell by examining some of the pixels; imagine a short line segment, 
halfway down the image and straddling the edge between the black and white
paper. This plot shows the pixel values (between 0 and 255, since this is a 
grayscale image) for forty pixels spanning the transition from black to white.

![Gradient near transition](../fig/07-bw-gradient.png)

It is obvious that the "edge" here is not so sudden! So, any OpenCV method to
detect edges in an image must be able to decide where the edge is, and place 
appropriately-colored pixels in that location. 

## Sobel edge detection

*Sobel edge detection* uses numerical approximations of derivatives to detect
edges in an image. Here is an example of how the process might work. If we look
at the gradient plot above, we shall see that its shape reoughly corresponds to
the sigmoid function, as shown by the purple line in this plot:

![Sigmoid function and derivative](../fig/07-sigmoid.png)

Now, look at the first derivative of the sigmoid function, shown by the hatched
green line. The peak of the first derivative curve corresponds to half way 
along the gradient line, and so the peak value can be used to determine where
the edge should be.

This is how the Sobel edge detection algorithm works. It computes the 
derivative of a curve fitting the gradient between light and dark areas in an
image, and then finds the peak of the derivative, which is interpreted as the
location of an edge pixel. The technique is implemented via the `cv2.Sobel()`
method.

The following program illustrates how the `cv2.Sobel()` method can be used to 
detect the edges in an image. We will execute the program on this image, which
we used before in the [Thresholding]({{ page.root }}./06-thresholding.md) 
episode:

![Colored shapes](../fig/06-junk-before.jpg)

We are interested in finding the edges of the shapes in the image, and so the
colors are not important. Our strategy will be to read the image as grayscale,
convert it to a binary image using the techniques from the 
[Thresholding]({{ page.root }}./06-thresholding.md) episode, and then apply 
Sobel edge detection. We will actually have to do the edge detection twice, 
once to examine gradient differentials in the x dimension, and then again to 
look at the differentials in the y dimension. After that, we will combine the
two results into one image, which will show the edges detected. 

~~~
'''
 * Python script to demonstrate Sobel edge detection.
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# load and display original image
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# blur image and use simple inverse binary thresholding to create
# a binary image
blur = cv2.GaussianBlur(img, (k, k), 0)
(t, mask) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# perform Sobel edge detection in x and y dimensions
edgeX = cv2.Sobel(mask, cv2.CV_64F, 1, 0)
edgeY = cv2.Sobel(mask, cv2.CV_64F, 0, 1)

# convert back to 8-bit, unsigned numbers and combine edge images
edgeX = np.uint8(np.absolute(edgeX))
edgeY = np.uint8(np.absolute(edgeY))
edge = cv2.bitwise_or(edgeX, edgeY)

# display edges
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.imshow("edges", edge)
cv2.waitKey(0)
~~~
{: .python}

This program takes three command-line arguments: the filename of the image to
process, and two arguments related to thresholding, the blur kernel size, k, 
and the threshold value, t. After the required libraries are imported, the 
program reads the command-line arguments and saves them in their respective
variables. 

Next, the original images is read, in grayscale, and displayed. Then, the
image is blurred and thresholded, using simple inverse binary thresholding.

Now we apply edge detection, with these two lines of code:

~~~
edgeX = cv2.Sobel(mask, cv2.CV_64F, 1, 0)
edgeY = cv2.Sobel(mask, cv2.CV_64F, 0, 1)
~~~
{: .python}

![Sobel edge detection subimages](../fig/07-junk-edge-x-y.jpg)
