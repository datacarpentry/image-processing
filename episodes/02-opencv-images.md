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
> 
> > ## Solution
> > 
> > Not using `namedWindow()` causes the image to be shown at full size, in a
> > non-resizable window.
> {: .solution}
{: .challenge}

## Manipulating pixels

If we desire or need to, we can individually manipulate the colors of pixels
by changing the numbers stored in the images' NumPy array. 

For example, suppose we are interested in this maize root cluster image. We 
want to be able to focus our program's attention on the roots themselves,
while ignoring the black background. 

![Root cluster image](../fig/02-roots.jpg)

Since the image is stored as an array of numbers, we can simply look through
the array for pixel color values that are less than some threshold value. 
NumPy has a very elegant method for doing just that. Consider this program,
which keeps only the pixel color values in an image that have value greater
than or equal to 128.

~~~
'''
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
'''
import cv2, sys

# read input image, based on filename parameter
img = cv2.imread(sys.argv[1])
	
# display original image
cv2.namedWindow("original img", cv2.WINDOW_NORMAL)
cv2.imshow("original img", img)
cv2.waitKey(0)

# keep only high-intensity pixels
img[img < 128] = 0
		
# display modified image
cv2.namedWindow("modified img", cv2.WINDOW_NORMAL)
cv2.imshow("modified img", img)
cv2.waitKey(0)
~~~
{: .python}

Our program imports `sys` in additon to `cv2`, so that we can use *command-line 
arguments* when we execute the program. In particular, in this program we use
a command-line argument to specify the filename of the image to process. If the
name of the file we are interested in is **roots.jpg**, and the name of the 
program is **HighIntensity.py**, then we run our Python program form the 
command line like this:

~~~
python HighIntensity.py roots.jpg
~~~
{: .bash}

The place where this happens in the code is the `cv2.imread(sys.argv[1])`
function call. When we invoke our program with command line arguments, 
they are passed in to the program as a list; `sys.argv[1]` is the first one
we are interested in; it contains the image filename we want to process. 
(`sys.argv[0]` is simply the name of our program, **HighIntensity.py** in 
this case). 

> ## Benefits of command-line arguments
> 
> Passing parameters such as filenames into our programs as parameters makes 
> our code more flexible. We can now run **HighIntensity.py** on *any* image 
> we wish, without having to go in and edit the code. 
{: .callout}

The NumPy command to ignore all low-intensity pixels is `img[img < 128] = 0`.
Every pixel color value in the whole 3-dimensional array with a value less
that 128 is set to zero. In this case, the result is an image in which the 
extraneous background detail has been removed. 

![Thresholded root image](../fig/02-roots-threshold.jpg)

## Access via slicing

Since OpenCV images are stored as NumPy arrays, we can use array slicing to 
select rectangular areas of an image. Then, we could save the selection as a 
new image, change the pixels in the image, and so on. 
