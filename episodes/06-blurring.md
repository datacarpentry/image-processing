---
title: "Blurring images"
teaching: 10
exercises: 40
questions:
- "How can we apply a low-pass blurring filter to an image?"
objectives:
- "Explain why applying a low-pass blurring filter to an image is beneficial."
- "Apply a Gaussian blur filter to an image using skimage."
- "Identify other methods of blurring images"
- "Explain what often happens if we pass unexpected values to a Python 
function."
keypoints:
- "Applying a low-pass blurring filter smooths edges and removes noise from
an image."
- "Blurring is often used as a first step before we perform 
[Thresholding]({{ page.root }}./07-thresholding.md),
[Edge Detection]({{ page.root }}./08-edge-detection), or before we find the
[Contours]({{ page.root }}./08-contours) of an image."
- "The Gaussian blur can be applied to an image with the `cv2.GaussianBlur()`
function."
- "The blur kernel for the Gaussian blur function should be odd."
- "Larger blur kernels may remove more noise, but they will also remove detail
from and image."
- "The `int()` function can be used to parse a string into an integer."
---

In this episode, we will learn how to use skimage functions to blur images.
When we blur an image, we make the color transition from one side of an 
edge in the image to another smooth rather than sudden. The effect is to 
average out rapid changes in pixel intensity. The blur, or smoothing,
of an image removes "outlier" pixels that may be noise in the image. Blurring
is an example of applying a *low-pass filter* to an image. In computer vision,
the term "low-pass filter" applies to removing noise from an image while 
leaving the majority of the image intact. A blur is a very common operation 
we need to perform before other tasks such as edge detection. There are 
several different blurring functions in skimage, so we will focus on just one 
here, the Gaussian blur. 

## Gaussian blur

Consider this image of a cat, in particular the area of the image outlined by 
the white square. 

![Cat image](../fig/05-cat-snap.jpg)

Now, zoom in on the area of the cat's eye, as shown in the left-hand image 
below. When we apply a blur filter, we consider each pixel in the 
image, one at a time. In this example, the pixel we are applying the filter to 
is highlighted in red, as shown in the right-hand image. 

![Cat eye pixels](../fig/05-cat-eye-pixels.jpg)

In a blur, we consider a rectangular group of pixels surrounding
the pixel to filter. This group of pixels, called the *kernel*, moves along
with the pixel that is being filtered. So that the filter pixel is always
in the center of the kernel, the width and height of the kernel must be odd. 
In the example shown above, the kernel is square, with a dimension of seven 
pixels. 

To apply this filter to the current pixel, a weighted average of the the 
color values of the pixels in the kernel is calculated. In a Gaussian blur,
the pixels nearest the center of the kernel are given more weight than those
far away from the center. This averaging is done on a channel-by-channel basis, 
and the average channel values become the new value for the filtered pixel. 
Larger kernels have more values factored into the average, and this implies 
that a larger kernel will blur the image more than a smaller kernel. 

To get an idea of how this works, consider this plot of the two-dimensional 
Gaussian function: 

![2D Gaussian function](../fig/05-gaussian-plot.png)

Imagine that plot overlaid over the kernel for the Gaussian blur filter. The
height of the plot corresponds to the weight given to the underlying pixel in
the kernel. I.e., the pixels close to the center become more important to the 
filtered pixel color than the pixels close to the edge of the kernel. The 
mathematics involved in the Gaussian blur filter are not quite that simple, but
this explanation gives you the basic idea. 

To illustrate the blur process, consider the blue channel color values from the
seven-by-seven kernel illustrated above: 

~~~
68  82 71 62 100  98  61 
90  67 74 78  91  85  77 
50  53 78 82  72  95 100 
87  89 83 86 100 116 128 
89 108 86 78  92  75 100 
90  83 89 73  68  29  18 
77 102 70 57  30  30  50
~~~
{: .output}

The filter is going to determine the new blue channel value for the center
pixel -- the one that currently has the value 86. The filter calculates a 
weighted average of all the blue channel values in the kernel, {76, 83, 81,
..., 39, 53, 68}, giving higher weight to the pixels near the center of the 
kernel. This weighted average would be the new value for the center pixel. 
The same process would be used to determine the green and red channel
values, and then the kernel would be moved over to apply the filter to the next
pixel in the image. 

Something different needs to happen for pixels near the edge of the image, 
since the kernel for the filter may be partially off the image. For example, 
what happens when the filter is applied to the upper-left pixel of the image? 
Here are the blue channel pixel values for the upper-left pixel of the cat 
image, again assuming a seven-by-seven kernel:

~~~
  x   x   x   x   x   x   x
  x   x   x   x   x   x   x
  x   x   x   x   x   x   x
  x   x   x   4   5   9   2 
  x   x   x   5   3   6   7 
  x   x   x   6   5   7   8 
  x   x   x   5   4   5   3 
~~~
{: .output}

The upper-left pixel is the one with value 4. Since the pixel is at the 
upper-left corner. there are no pixels underneath much of the kernel;
here, this is represented by x's. So, what does the filter do in that 
situation?

The default behavior is to *reflect* the pixels that are in the image to fill
in for the pixels that are missing from the kernel. If we fill in a few of the
missing pixels, you will see how this works:

~~~
  x   x   x   5   x   x   x
  x   x   x   6   x   x   x
  x   x   x   5   x   x   x
  2   9   5   4   5   9   2 
  x   x   x   5   3   6   7 
  x   x   x   6   5   7   8 
  x   x   x   5   4   5   3 
~~~
{: .output}

A similar process would be used to fill in all of the other missing pixels from
the kernel. Other *border options* are available; you can learn more about them
in the [skimage documentation](https://scikit-image.org/docs/dev/user_guide). 

This animation shows how the blur kernel moves along in the original image in 
order to calculate the color channel values for the blurred image.

![Blur demo animation](../fig/05-blur-demo.gif)

skimage has built-in functions to perform blurring for us, so we do not have to 
perform all of these mathematical operations ourselves. The following Python 
program shows how to use the skimage Gaussian blur function. 

~~~
'''
 * Python script to demonstrate Gaussian blur.
 *
 * usage: python GaussBlur.py <filename> <kernel-size> 
'''
import cv2, sys

# get filename and kernel size from command line
filename = sys.argv[1]
k = int(sys.argv[2])
~~~
{: .python}

In this case, the 
program takes two command-line parameters. The first is the filename of the 
image to filter, and the second is the kernel size, which as we learned above, 
must be odd. The program uses a square kernel for the filter. 

In the program, we first import the `cv2` and `sys` libraries, as we
have done before. Then, we read the two command-line arguments. The first, the 
filename, should be familiar code by now. For the kernel size argument, we have
to convert the second argument from a string, which is how all arguments are 
read into the program, into an integer, which is what we will use for our 
kernel size. This is done with the 

`k = int(sys.argv[2])` 

line of code. The `int()` function takes a string as its parameter, and returns 
the integer equivalent. 

> ## What happens if the `int()` parameter does not look like a number? (10 min)
> 
> In the program fragment, we are using the `int()` function to *parse* the
> second command-line argument, which comes in to the program as a string, 
> and convert it into an integer. What happens if the second command-line
> argument does not look like an integer? Let us perform an experiment to find
> out. 
> 
> Write a simple Python program to read one command-line argument, convert the
> argument to an integer, and then print out the result. Then, run your program
> with an integer argument, and then again with some non-integer arguments. For
> example, if your program is named **IntArg.py**, you might perform these 
> runs:
> 
> ~~~
> python IntArg.py 13
> python IntArg.py puppy
> python IntArg.py 3.14159
> ~~~
> {: .bash}
> 
> What does `int()` do if it receives a string that cannot be parsed into an 
> integer? 
> 
> > ## Solution
> > 
> > Here is a simple program to read in one command-line argument, parse it as
> > and integer, and print out the result:
> > 
> > ~~~
> > '''
> >  * Read a command-line argument, parse it as an integer, and 
> >  * print out the result.
> >  *
> >  * usage: python IntArg.py <argument>
> > '''
> > import sys
> > 
> > v = int(sys.argv[1])
> > print("Your command-line argument is:", v)
> > ~~~
> > {: .python}
> > 
> > Executing this program with the three command-line arguments suggested 
> > above produces this output:
> > 
> > ~~~
> > Your command-line argument is: 13
> > 
> > Traceback (most recent call last):
> >   File "IntArg.py", line 9, in <module>
> >     v = int(sys.argv[1])
> > ValueError: invalid literal for int() with base 10: 'puppy'
> > 
> > Traceback (most recent call last):
> >  File "IntArg.py", line 9, in <module>
> >    v = int(sys.argv[1])
> > ValueError: invalid literal for int() with base 10: '3.14159'
> > ~~~
> > {: .output}
> > 
> > You can see that if we pass in an invalid value to the `int()` function, 
> > the Python interpreter halts the program and prints out an error message,
> > describing what the problem was. 
> {: .solution}
{: .challenge}

Next, the program reads and displays the original, unblurred image. This should
also be very familiar to you at this point. 

~~~
# read and display original image
image = cv2.imread(filename = filename)
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)
~~~
{: .python}

Now we apply the average blur:

~~~
# apply Gaussian blur, creating a new image
blurred = cv2.GaussianBlur(src = image, 
    ksize = (k, k), sigmaX = 0)
~~~
{: .python}

The first two parameters to `cv2.GaussianBlur()` are the image to blur, 
`image`, and a tuple describing the shape of the kernel, `(k, k)`. The third 
parameter is the standard deviation for the two-dimensional Gaussian 
distribution in the x dimension. If we pass in `0`, as we have done here, 
skimage automatically determines default standard deviations for both the x and 
y dimensions, based on the kernel size. This is how we will normally invoke the
`cv2.GaussianBlur()` function. The `cv2.GaussianBlur()` function returns a new 
image after the filter has been applied.

After the blur filter has been executed, the program wraps things up by 
displaying the blurred image in a new window. 

~~~
# display blurred image
cv2.namedWindow(winname = "blurred", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "blurred", mat = blurred)
cv2.waitKey(delay = 0)
~~~
{: .python}

Here is a constructed image to use as the input for the preceding program.

![Original image](../fig/05-gaussian-original.png)

When the program runs, it displays the original image, applies the filter, 
and then shows the blurred result. The following image is the result after
applying a filter with a kernel size of seven. 

![Gaussian blurred image](../fig/05-gaussian-blurred.png)

> ## Experimenting with kernel size (5 min)
> 
> Navigate to the **Desktop/workshops/image-processing/06-blurring** directory
> and execute the **GaussBlur.py** script, which contains the program shown
> above. Execute it with two command-line parameters, like this:
> 
> ~~~
> python GaussBlur.py GaussianTarget.png 7
> ~~~
> {: .bash}
> 
> Remember that the first command-line argument is the name of the file to 
> filter, and the second is the kernel size. Now, experiment with the kernel 
> size, running the program with smaller and larger values (keeping them all 
> odd, of course). Generally speaking, what effect does kernel size have on the
> blurred image?
> 
> > ## Solution
> > 
> > Generally speaking, the larger the kernel size, the more blurry the result.
> > A larger kernel will tend to get rid of more noise in the image, which will
> > help for other operations we will cover soon, such as edge detection. 
> > However, a larger kernel also tends to eliminate some of the detail from
> > the image. So, we must strike a balance with the kernel size used for
> > blur filters. 
> {: .solution}
{: .challenge}

> ## Experimenting with kernel shape (10 min)
> 
> Now, modify the **GaussBlur.py** program so that it takes *three*
> command-line parameters instead of two. The first parameter should still be
> the name of the file to filter. The second and third parameters should be the
> width and height of the kernel to use, so that the kernel is rectangular 
> instead of square. The new version of the program should be invoked like 
> this:
> 
> ~~~
> python GaussBlur.py GaussianTarget.png 5 7
> ~~~
> {: .bash}
> 
> Using the program like this utilizes a kernel that is five pixels wide by 
> seven pixels tall for the blurring. 
> 
> > ## Solution
> > 
> > ~~~
> > '''
> >  * Python script to demonstrate Gaussian blur.
> >  *
> >  * usage: python GaussBlur.py <filename> <kernel-width> <kernel-height> 
> > '''
> > import cv2, sys
> > 
> > # get filename and kernel size from command line
> > filename = sys.argv[1]
> > w = int(sys.argv[2])
> > h = int(sys.argv[3])
> > 
> > # read and display original image
> > image = cv2.imread(filename = filename)
> > cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "original", mat = image)
> > cv2.waitKey(delay = 0)
> > 
> > # apply Gaussian blur, creating a new image
> > blurred = cv2.GaussianBlur(src = image, 
> >     ksize = (w, h), sigmaX = 0)
> > 
> > # display blurred image
> > cv2.namedWindow(winname = "blurred", flags = cv2.WINDOW_NORMAL)
> > cv2.imshow(winname = "blurred", mat = blurred)
> > cv2.waitKey(delay = 0)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

## Other methods of blurring

The Gaussian blur is not the only way to apply low-pass filters in skimage. 
In particular, we could use the `cv2.blur()`, `cv2.boxFilter()`, 
`cv2.medianBlur()`, or `cv2.bilateralFilter()` functions. The 
[skimage documentation](https://scikit-image.org/docs/dev/user_guide)
recommends Gaussian blurring for images with Gaussian (i.e., random) noise,
median blurring for removing "salt and pepper" or "static" noise, and bilateral
blurring when we want to preserve sharp edges. 

> ## Blurring the bacteria colony images (15 min)
> 
> As we move further into the workshop, we will see that in order to complete
> the colony-counting morphometric challenge at the end, we will need to read
> the bacteria colony images as grayscale, and blur them, before moving on to
> the tasks of actually counting the colonies. Create a Python program to read
> one of the colony images (with the filename provided as a command-line 
> parameter) as grayscale, and then apply a Gaussian blur to the image. You
> should also provide the kernel size for the blur as a second command-line 
> parameter. Do not alter the original image. As a reminder, the images are 
> located in the **Desktop/workshops/image-processing/10-challenges/morphometrics**
> directory. 
{: .challenge}
