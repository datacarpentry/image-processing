---
title: "OpenCV Images"
teaching: 30
exercises: 70
questions:
- "How are digital images stored in Python with the OpenCV computer vision library?"
objectives:
- "Explain how OpenCV images are stored in NumPy arrays."
- "Explain the order of the three color values in OpenCV images."
- "Read, display, and save images using OpenCV."
- "Resize images with OpenCV."
- "Perform simple image thresholding with NumPy array operations."
- "Explain why command-line parameters are useful."
- "Extract sub-images using array slicing."
- "Explain what happens to image metadata when an image is loaded into a Python 
program."
keypoints:
- "OpenCV images are stored as three-dimensional NumPy arrays."
- "In OpenCV images, the blue channel is specified first, then the green, then
the red, i.e., BGR instead of RGB."
- "Images are read from disk with the `cv2.imread()` function."
- "We create a sizable window that automatically scales the displayed image 
with the `cv2.namedWindow()` function."
- "We cause an image to be displayed in a window with the `cv2.imshow()` 
function."
- "We cause our program to pause until we press a key with the `cv2.waitKey(0)`
function call."
- "We can resize images with the `cv2.resize()` function."
- "NumPy array commands, like `img[img < 128] = 0`, and be used to manipulate
the pixels of an OpenCV image."
- "Command-line arguments are accessed via the `sys.argv` list; `sys.argv[1]`
is the first parameter passed to the program, `sys.argv[2]` is the second, 
and so on."
- "Array slicing can be used to extract sub-images or modify areas of OpenCV
images, e.g., `clip = img[60:150, 135:480, :]`."
- "Metadata is not retained when images are loaded as OpenCV images."
---

Now that we know a bit about computer images in general, let us turn to more
details about how images are represented in the Python implementation of the
OpenCV open-source computer vision library.

## OpenCV images are NumPy arrays

In the [Image Basics]({{page.root}}/02-image-basics) episode, we learned that
images are represented as rectangular arrays of individually-colored square 
pixels, and that the color of each pixel can be represented as an RGB triplet 
of numbers. One of the advantages of using the OpenCV computer vision library
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
[OpenCV documentation](http://docs.opencv.org/)
for more information.

Let us examine a simple Python program to load, display, and save an image to a 
different format. Here are the first few lines:

~~~
'''
 * Python program to open, display, and save an image.
 *
'''
import cv2

# read image 
image = cv2.imread(filename = "chair.jpg")
~~~
{: .python}

First, we import the OpenCV library (`cv2`) so 
we can work with images. Then, we use the `cv2.imread()` function to read
a JPEG image entitled **chair.jpg**. OpenCV reads the image, converts it from
JPEG into a NumPy array, and returns the array; we save the array in a variable
named `image`.

Next, we will do something with the image:

~~~
# display image and wait for keypress, using a resizable window
cv2.namedWindow(winname = "image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "image", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

Once we have the image in the program, we next display it using the 
`cv2.namedWindow()` and `cv2.imshow()` functions. The first parameter to 
`namedWindow()`, `"image"`, is the title that will show on the window 
displaying our image. The second parameter, `cv2.WINDOW_NORMAL`, means that
our window will be resizable, and that the displayed image will be 
automatically scaled to fit in the window. 

> ## `cv2.namedWindow()` on Mac OS X
> 
> Using the `cv2.namedWindow()` to create the display window before showing an
> image creates a resizable window with content that automatically scales on 
> Windows and Linux systems, but not on Mac OS X systems. As of this writing
> (spring 2017) with Anaconda and OpenCV running on OS 10.12 Sierra, 
> `cv2.namedWindow()` creates a resizable window, *but* the image displayed in
> the window *does not* automatically scale to fit the window. If you are using
> the virtual machine designed for these lessons, the behavior should be
> just as described in this episode. 
{: .callout}

The first parameter in the `imshow()` function is the name of the window the 
image will be shown in. It should be the same as the name given to the window 
in the `namedWindow()` call. The second parameter is the variable containing 
the image to display.

The `cv2.waitKey(delay = 0)` function call instructs our program to wait -- 
potentially forever -- until the user presses a key before moving on to the 
next line. If we specify a number other than 0 in the `waitKey()` call, the 
program will pause for that many milliseconds, and then continue automatically.

Next, we will save the image in another format:

~~~
# save a new version in .tif format
cv2.imwrite(filename = "chair.tif", img = image)
~~~
{: .python}

The final statement in the program, `cv2.imwrite(filename = "chair.tif", img = image)`,
writes the image to a file named `chair.tif`. The `imwrite()` function automatically
determines the type of the file, based on the file extension we provide. In 
this case, the `.tif` extension causes the image to be saved as a TIFF.

> ## Extensions do not always dictate file type
> 
> The OpenCV `imwrite()` function automatically uses the file type we specify in
> the file name parameter's extension. Note that this is not always the case.
> For example, if we are editing a document in Microsoft Word, and we save the
> document as `paper.pdf` instead of `paper.docx`, the file *is not* saved as
> a PDF document. 
{: .callout}

> ## Named versus positional arguments
> 
> When we call functions in Python, there are two ways we can specify the 
> necessary arguments. We can specify the arguments *positionally*, i.e., in
> the order the parameters appear in the function definition, or we can 
> use *named arguments*. 
> 
> For example, the `cv2.imread()` function definition specifies two parameters,
> the file name to read and an optional flag value. So, we could load in the 
> chair image in the sample code above using positional parameters like this:
> 
> `image = cv2.imread('chair.jpg')`
> 
> Since the function expects the first argument to be the file name, there is
> no confusion about what `'char.jpg'` means.
> 
> The style we will use in this workshop is to name each parameters, like this:
> 
> `image = cv2.imread(filename = 'chair.jpg')`
> 
> This style will make it easier for you to learn how to use the variety of 
> functions we will cover in this workshop. 
{: .callout}

> ## Experimenting with windows (3 min)
> 
> Creating a named window before calling the `imshow()` function is optional.
> Navigate to the **Desktop/workshops/image-processing/03-opencv-images**
> directory, and edit the **Open.py** program. Comment out the line with the
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

> ## Resizing an image (20 min)
> 
> Using your mobile phone, tablet, web cam, or digital camera, take an image.
> Copy the image to the **Desktop/workshops/image-processing/03-opencv-images**
> directory. Write a Python program to read your image into a variable named
> `image`. Then, resize the image by a factor of 50 percent, using this line of
> code:
> 
> ~~~
> small = cv2.resize(src = image, dsize = None, fx = 0.5, fy = 0.5)
> ~~~
> {: .python}
> 
> As it is used here, the parameters to the `cv2.resize()` function are the 
> image to transform, `image`, the dimensions we want the new image to have --
> here we send `None`, indicating that OpenCV should figure out the dimensions
> -- and the new size in the x and y dimensions, in this case 50% each. 
> 
> Finally, write the resized image out to a new file named **resized.jpg**. 
> Once you have executed your program, examine the image properties of the 
> output image and verify it has been resized properly.
> 
> > ## Solution
> > 
> > Here is what your Python program might look like.
> > 
> > ~~~
> > '''
> >  * Python program to read an image, resize it, and save it
> >  * under a different name.
> > '''
> > import cv2
> > 
> > # read in image
> > image = cv2.imread(filename = "chicago.jpg")
> > 
> > # resize the image
> > small = cv2.resize(src = image, dsize = None, fx = 0.5, fy = 0.5)
> > 
> > # write out image
> > cv2.imwrite(filename = "resized.jpg", img = small)
> > ~~~
> > {: .python}
> > 
> > From the command line, we would execute the program like this:
> > 
> > ~~~
> > python Resize.py
> > ~~~
> > {: .bash}
> > 
> > The program resizes the **chicago.jpg** image by 50% in both dimensions,
> > and saves the result in the **resized.jpg** file. 
> {: .solution}
{: .challenge}

## Manipulating pixels

If we desire or need to, we can individually manipulate the colors of pixels
by changing the numbers stored in the image's NumPy array. 

For example, suppose we are interested in this maize root cluster image. We 
want to be able to focus our program's attention on the roots themselves,
while ignoring the black background. 

![Root cluster image](../fig/02-roots.jpg)

Since the image is stored as an array of numbers, we can simply look through
the array for pixel color values that are less than some threshold value. This
process is called *thresholding*, and we will see more powerful methods to 
perform the thresholding task in the 
[Thresholding]({{ page.root }}/07-thresholding/) episode. Here, though, we
will look at a simple and elegant NumPy method for thresholding. Let us develop 
a program that keeps only the pixel color values in an image that have value 
greater than or equal to 128. We will start by reading the image and
displaying it.

~~~
'''
* Python script to ignore low intensity pixels in an image.
*
* usage: python HighIntensity.py <filename>
'''
import cv2, sys

# read input image, based on filename parameter
image = cv2.imread(filename = sys.argv[1])
	
# display original image
cv2.namedWindow(winname = "original image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original image", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

Our program imports `sys` in addition to `cv2`, so that we can use 
*command-line arguments* when we execute the program. In particular, in this 
program we use a command-line argument to specify the filename of the image to
process. If the name of the file we are interested in is **roots.jpg**, and 
the name of the program is **HighIntensity.py**, then we run our Python 
program form the command line like this:

~~~
python HighIntensity.py roots.jpg
~~~
{: .bash}

The place where this happens in the code is the 
`cv2.imread(filename = sys.argv[1])`
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

Now we can threshold the image and display the result.

~~~
# keep only high-intensity pixels
image[image < 128] = 0
		
# display modified image
cv2.namedWindow(winname = "modified image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "modified image", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

The NumPy command to ignore all low-intensity pixels is `img[img < 128] = 0`.
Every pixel color value in the whole 3-dimensional array with a value less
that 128 is set to zero. In this case, the result is an image in which the 
extraneous background detail has been removed. 

![Thresholded root image](../fig/02-roots-threshold.jpg)

> ## Keeping only low intensity pixels (20 min)
> 
> In the previous example, we showed how we could use Python and OpenCV to turn
> on only the high intensity pixels from an image, while turning all the low 
> intensity pixels off. Now, you can practice doing the opposite -- keeping all
> the low intensity pixels while changing the high intensity ones. Consider 
> this image of a Su-Do-Ku puzzle, named **sudoku.png**:
> 
> ![Su-Do-Ku puzzle](../fig/02-sudoku.png)
> 
> Navigate to the **Desktop/workshops/image-processing/03-opencv-images** 
> directory, and copy the **HighIntensity.py** program to another file named
> **LowIntensity.py**. Then, edit the **LowIntensity.py** program so that it 
> turns all of the white pixels in the image to a light gray color, say with 
> all three color channel values for each formerly white pixel set to 64. Your
> results should look like this: 
> 
> ![Modified Su-Do-Ku puzzle](../fig/02-sudoku-gray.png)
> 
> > ## Solution
> > 
> > After modification, your program should look like this:
> > 
> > ~~~
> > '''
> > * Python script to modify high intensity pixels in an image.
> > *
> > * usage: python LowIntensity.py <filename>
> > '''
> > import cv2, sys
> > 
> > # read input image, based on filename parameter
> > image = cv2.imread(filename = sys.argv[1])
> > 
> > # display original image
> > cv2.namedWindow(winname = "original image", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "original image", mat = image)
> > cv2.waitKey(delay = 0)
> > 
> > # change high intensity pixels to gray
> > img[img > 200] = 64
> > 
> > # display modified image
> > cv2.namedWindow(winname = "modified image", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "modified image", mat = image)
> > cv2.waitKey(delay = 0)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

## Access via slicing

Since OpenCV images are stored as NumPy arrays, we can use array slicing to 
select rectangular areas of an image. Then, we could save the selection as a 
new image, change the pixels in the image, and so on. It is important to 
remember that coordinates are specified in *(y, x)* order and that color values
are specified in *(b, g, r)* order when doing these manipulations.

Consider this image of a whiteboard, and suppose that we want to create a 
sub-image with just the portion that says "odd + even = odd," along with the
red box that is drawn around the words. 

![Whiteboard image](../fig/02-board.jpg)

We can use a tool such as ImageJ to determine the coordinates of the corners
of the area we wish to extract. If we do that, we might settle on a rectangular
area with an upper-left coordinate of *(135, 60)* and a lower-right coordinate
of *(480, 150)*, as shown in this version of the whiteboard picture:

![Whiteboard coordinates](../fig/02-board-coordinates.jpg)

Note that the coordinates in the preceding image are specified in *(x, y)*
order. Now if our entire whiteboard image is stored as an OpenCV image named 
`image`, we can create a new image of the selected region with a statement like
this:

`clip = image[60:150, 135:480, :]`

Our array slicing specifies the range of y-coordinates first, `60:150`, and
then the range of x-coordinates, `135:480`. The third part of the slice, `:`,
indicates that we want all three color channels in our new image. 

A program to create the subimage would start by loading the image:

~~~
'''
 * Python script demonstrating image modification and creation via 
 * NumPy array slicing.
'''
import cv2

# load and display original image
image = cv2.imread(filename = "board.jpg")
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

Then we use array slicing to
create a new image with our selected area and then display the new image. 

~~~
# extract, display, and save sub-image
clip = image[60:150, 135:480, :]
cv2.namedWindow(winname = "clip", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "clip", mat = clip)
cv2.imwrite(filename = "clip.tif", img = clip)
cv2.waitKey(delay = 0)
~~~
{: .python}

We can also change the values in an image, as shown next. 

~~~
# replace clipped area with sampled color
c = image[330, 90]
image[60:150, 135:480] = c
cv2.namedWindow(winname = "modified", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "modified", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

First, we sample the color at a particular location of the 
image, saving it in a NumPy array named `c`, a 1 × 1 × 3 array with the blue, 
green, and red color values for the pixel located at *(x = 90, y = 330)*. Then, 
with the `img[60:150, 135:480] = c` command, we modify the image in the 
specified area. In this case, the command "erases" that area of the whiteboard, 
replacing the words with a white color, as shown in the final image produced by 
the program:

!["Erased" whiteboard](../fig/02-board-final.jpg)

> ## Practicing with slices (10 min)
> 
> Navigate to the **Desktop/workshops/image-processing/03-opencv-images** 
> directory, and edit the **RootSlice.py** program. It contains a skeleton
> program that loads and displays the maize root image shown above. Modify
> the program to create, display, and save a sub-image containing only the
> plant and its roots. Use ImageJ to determine the bounds of the area you will
> extract using slicing.
> 
> > ## Solution
> > 
> > Here is the completed Python program to select only the plant and roots 
> > in the image.
> > 
> > ~~~
> > '''
> >  * Python script to extract a sub-image containing only the plant and
> >  * roots in an existing image.
> > '''
> > import cv2
> > 
> > # load and display original image
> > image = cv2.imread(filename = "roots.jpg")
> > cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "original", mat = image)
> > cv2.waitKey(delay = 0)
> > 
> > # extract, display, and save sub-image
> > # WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:
> > clip = image[0:1999, 1410:2765, :]
> > 
> > cv2.namedWindow(winname = "clip", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "clip", mat = clip)
> > cv2.waitKey(delay = 0)
> > 
> > # WRITE YOUR CODE TO SAVE clip HERE
> > cv2.imwrite(filename = "clip.jpg", img = clip)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Metadata, continued (10 min)
> Let us return to the concept of image metadata, introduced briefly in the
> [Image Basics]({{ page.root }}/02-image-basics/) episode. Specifically, what
> happens to the metadata of an image when it is read into, and written from,
> a Python program using OpenCV?
> 
> To answer this question, write a very short (three lines) Python script to 
> read in a file and save it under a different name. Navigate to the 
> **Desktop/workshops/image-processing/03-opencv-images** directory, and write
> your script there. You can use the **flowers-before.jpg** as input, and save
> the output as **flowers-after.jpg**. Then, examine the metadata from both
> images using commands like **identify -verbose flowers-after.jpg**. Is the metadata 
> the same? If not, what are some key differences?
> 
> > ## Solution
> > 
> > Here is a short Python script to open the image and save it in a different
> > filename:
> > 
> > ~~~
> > import cv2
> > 
> > img = cv2.imread(filename = "flowers-before.jpg")
> > cv2.imwrite(filename = "flowers-after.jpg", img = img)
> > ~~~
> > {: .python}
> > 
> > The newly-saved file is missing most of the original metadata. Comparing 
> > this to the original, as shown in the 
> > [Image Basics]({{ page.root }}/02-image-basics/) episode, it is easy to see
> > that virtually all of the useful metadata has been lost! 
> > 
> > The moral of this challenge is to remember that image metadata *will not* 
> > be preserved in images that your programs write via the `cv2.imwrite()` 
> > function. If metadata is important to you, take precautions to always 
> > preserve the original files. 
> {: .solution}
{: .challenge}

> ## Slicing and the colorimetric challenge (10 min)
> 
> In the [introductory]({{page.root}}/01-introduction/) episode, we were 
> introduced to a colorimetric challenge, namely, graphing the color values of
> a solution in a titration, to see when the color change takes place. Let's 
> start thinking about how to solve that problem. 
> 
> One part of our ultimate solution will be sampling the color channel values 
> from an image of the solution. To make our graph more reliable, we will want 
> to calculate a mean channel value over several pixels, rather than simply 
> focusing on one pixel from the image. 
> 
> Navigate to the **Desktop/workshops/image-processing/10-challenges/colorimetrics**
> directory, and open the **titration.tiff** image in ImageJ. 
> 
> ![Titration image](../fig/00-titration.jpg)
> 
> Find the *(x, y)* coordinates of an area of the image you think would be good 
> to sample in order to find the average channel values. Then, write a small
> Python program that computes the mean channel values for a 10 × 10 pixel 
> *kernel* centered around the coordinates you chose. Print the results to the 
> screen, in a format like this:
> 
> ~~~
> Avg. red value: 193.7778
> Avg. green value: 189.1481
> Avg. blue value: 178.6049
> ~~~
> {: .output}
{: .challenge}
