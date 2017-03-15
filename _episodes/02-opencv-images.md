---
title: "OpenCV Images"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

Now that we know a bit about computer images in general, let us turn to more
details about how images are represented in the Python implementation of the
OpenCV open-source computer vision library.

## OpenCV images are NumPy arrays

In the [Image Basics]({{page.root}}/01-image-basics) episode, we learned that
images are represented as rectangular arrays of individually-colored pixels,
and that the color of each pixel can be represented as an RGB triplet of 
numbers. One of the advantages of using the OpenCV computer vision library
is that OpenCV images are stored in a manner very consistent with the 
representation from that episode. In particular, OpenCV images are stored as 
three-dimensional NumPy arrays. 

The rectangular shape of the array corresponds to the shape of the image, 
although the order of the coordinates are reversed. The "depth" of the array
for an OpenCV image is three, with one layer for each of the three channels.
The differences in the order of coordinates and the order of the channel 
layers can cause some confusion, so we should spend a bit more time looking
at that.

When we think of a pixel in an image, we think of its (x, y) coordinates (in a
left-hand coordinate system) like (113, 45) and its color, specified as a RGB 
triple like (245, 134, 29). In an OpenCV image, the same pixel would be 
specified with *(y, x)* coordinates (45, 113) and *BGR* color (29, 134, 245). 

Let us take a look at this idea visually. Consider this image of a chair:

![Chair image](../fig/02-chair-orig.jpg)

A visual representation of how this image is stored as a NumPy array in OpenCV
is:

![Chair layers](../fig/02-chair-layers.png)

So, when we are working with OpenCV images, we specify the *y* coordinate 
first, then the *x* coordinate. And, the colors are stored as *BGR* 
values -- blue in layer 0, green in layer 1, red in layer 2 -- instead
of RGB triples.

## Reading, displaying, and saving images

OpenCV provides easy-to-use functions for reading, displaying, and saving 
images. All of the popular image formats, such as BMP, PNG, JPEG, and TIFF
are supported, along with several more esoteric formats. See the 
[OpenCV documentation](http://opencv.org/documentation.html)
for more information.

Here is a simple Python program to load, display, and save an image to a 
different format.

~~~
'''
 * Python program to open, display, and save an image.
 *
'''
import cv2

# read image 
img = cv2.imread("chair.jpg")

# display image and wait for keypress, using a resizable window
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)

# save a new version in .tif format
cv2.imwrite("chair.tif", img)
~~~
{: .python}

At the beginning of the program, we import the OpenCV library (`cv2`) so 
we can work with images. Then, we use the `cv2.imread()` function to read
a JPEG image entitled **chair.jpg**. OpenCV reads the image, converts it from
JPEG into a NumPy array, and returns the array; we save the array in a variable
named `img`.

Once we have the image in the program, we next display it using the 
`cv2.namedWindow()` and `cv2.imshow()` functions. The first parameter to 
`namedWindow()`, `"image"`, is the title that will show on the window 
displaying our image. The second parameter, `cv2.WINDOW_NORMAL`, means that
our window will be resizable, and that the displayed image will be 
automatically scaled to fit in the window. 

The first parameter in the `imshow()` function is the name of the window the 
image will be shown in. It should be the same as the name given to the window 
in the `namedWindow()` call. The second parameter is the variable containing 
the image to display.

The `cv2.waitKey(0)` function call instructs our program to wait -- potentially
forever -- until the user presses a key before moving on to the next line.
If we specify a number other than 0 in the `waitKey()` call, the program will
pause for that many milliseconds, and then continue automatically. 

> ## Experimenting with windows
> 
> Creating a named window before calling the `imshow()` function is optional.
> Navigate to the Desktop/workshops/image-processing/02-opencv-images directory, 
> and edit the **Open.py** program. Comment out the line with the 
> `namedWindow()` call, save the file, and then run the program by executing 
> the following command in the terminal:
> 
> ~~~
> python Open.py
> ~~~
> {: .bash}
> 
> What behavior changes when we do not use `namedWindow()` before `imshow()`?
{: .challenge}

## Manipulating pixels

If we desire or need to, we can individually manipulate the colors of pixels
by changing the numbers stored in the images' NumPy array. 
