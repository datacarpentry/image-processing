---
title: "Blurring images"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to blur images.
When we blur an image, we make the color transition from one side of an 
edge in the image to another smooth rather than sudden. The blur, or smoothing,
of an image removes "outlier" pixels that may be noise in the image. Blurring
is an example of applying a *low-pass filter* to an image. A blur
is a very common operation we need to perform before other tasks such as 
edge detection. There are several different blurring functions in OpenCV, so 
we will focus on just two here, the averaging blur and the Gaussian
blur. 

## Averaging blur

We will start with the averaging blur. Consider this image of a cat, in
particular the area of the image outlined by the white square. 

![Cat image](../fig/05-cat-snap.jpg)

Now, zoom in on the area of the cat's eye, as shown in the left image below.
When we apply a averaging blur filter, we consider each pixel in the image,
one at a time. In this example, the pixel we are applying the filter to is
highlighted in red, as shown in the right-hand image. 

![Cat eye pixels](../fig/05-cat-eye-pixels.jpg)

In an averaging blur, we consider a rectangular group of pixels surrounding
the pixel to filter. This group of pixels, called the *kernel*, moves along
with the pixel that is being filtered. So that the filter pixel is in the 
center of the kernel, the width and height of the kernel must be odd. In the 
example shown above, the kernel is square, with a dimension of seven pixels. 

To apply the filter to the current pixel, the color values of the pixels in the
kernel are averaged, on a channel-by-channel basis, and the average channel
values become the new value for the filtered pixel. Larger kernels have more
values factored into the average, and this implies that a larger
kernel will blur the image more than a smaller kernel. 

OpenCV has built-in methods to perform blurring for us. 
The following Python program shows how to use the OpenCV Average blur 
function. In this case, the program takes two command-line parameters. The 
first is the filename of the image to filter, and the second is the kernel
size, which must be odd. 

~~~
'''
 * Python script to demonstrate Average blur.
'''
import cv2, sys

# get filename and kernel size from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# apply Average blur, creating a new image
blurred = cv2.blur(img, (k, k), 0)

# display blurred image
cv2.namedWindow("blurred", cv2.WINDOW_NORMAL)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)
~~~
{: .python}

In the program, we first import the `cv2` and `sys` libraries, as we've done
before. Then, we read the two command-line arguments. The first, the filename,
should be familiar code by now. For the kernel size argument, we have to 
convert the second argument from a string, which is how all arguments are read
into the program, into an integer, which is what we will use for our kernel
size. This is done with the 

`k = int(sys.argv[2])` 

line of code. The `int()` method takes a string as its parameter, and returns 
the integer equivalent. 

Here is a constructed image to use as the input for the preceeding program.

![Original image](../fig/05-average-original.png)

When the program runs, it displays the original image, applies the filter, 
and then shows the blurred result. The following image is the result after
applying a filter with a kernel size of seven. 

![Average blurred image](../fig/05-average-blurred.png)

## Gaussian blur

The following Python program shows how to use the OpenCV Gaussian blur 
function. 

~~~
'''
 * Python script to demonstrate Gaussian blur.
'''
import cv2, sys

# get filename and kernel size from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# apply Gaussian blur, creating a new image
blurred = cv2.GaussianBlur(img, (k, k), 0)

# display blurred image
cv2.namedWindow("blurred", cv2.WINDOW_NORMAL)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)
~~~
{: .python}

![Original image](../fig/05-gaussian-original.png)

![Gaussian blurred image](../fig/05-gaussian-blurred.png)

