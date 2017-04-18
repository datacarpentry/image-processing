---
title: "Thresholding"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to apply 
thresholding to an image. Most frequently, we use thresholding as a way to 
select areas of interest of an image, while ignoring the parts we are not 
concerned with. We have already done some simple thresholding, in the 
"Manipulating pixels" section of the 
[OpenCV Images]({{ page.root }}/02-opencv-images) episode. In that case, we
used a simple NumPy array manipulation to separate the pixels belonging to the
root system of a plant from the black background. In this lesson, we will 
learn more sophisticated thresholding techniques to create masks, which can 
then be used to separate the interesting parts of an image from the background.

## Simple thresholding

Consider this image, with a series of crudely cut shapes set against a white 
background:

![Original shapes image](../fig/06-junk-before.jpg)

Now suppose we want to select only the shapes from the image. In other words,
we want to leave the pixels belonging to the shapes "on," while turning the 
rest of the pixels "off," by setting their color channel values to zeros. The
OpenCV library has several different methods of thresholding. We will start 
with the simplest version, which involves an important instance of human 
input. Specifically, in this simple, *fixed-level thresholding*, we have to 
provide a threshold value, *T*. 

The process works like this. First, we will load the original image, convert
it to grayscale, and blur it with one of the methods from the 
[Blurring]({{ page.root }}./06-blurring) episode. Then, we will use the 
`cv2.threshold()` method; *T* will be one of the parameters passed to the 
method. Any of the grayscale pixels in the image with values less than *T*
will be set to zero, while any pixels with values greater than or equal to 
*T* will be set to 255. What remains will be a mask image, with white pixels
corresponding to the things we are interested in. 

Here is a Python program to apply simple thresholding to an image. 

~~~
'''
 * Python script to demonstrate simple thresholding.
'''
import cv2, sys

# get filename, kernel size, and threshold value from command line
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# read and display the original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# blur image before thresholding
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (k, k), 0)

# perform binary thresholding 
(t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# make a mask suitable for color images
mask = cv2.merge([maskLayer, maskLayer, maskLayer])

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(img, mask)

# display the result
cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
cv2.imshow("selected", sel)
cv2.waitKey(0)
~~~
{: .python}

This program takes three command-line arguments: the filename of the image to 
manipulate, the kernel size used during the blurring step (which must be odd), 
and finally, the threshold value *T*, which should be an integer in the closed
range [0, 255]. The program takes the command-line values and stores them in 
variables named `filename`, `k`, and `t`, respectively. 

Next, the program reads the original image based on the `filename` value, and
displays it. 

Now is where the main work of the program takes place. First, we convert the 
image to grayscale and then blur it, using the `cv2.GaussianBlur()` method we
learned about in the [Blurring]({{ page.root }}./06-blurring) episode. 

The fixed-level thresholding is performed with the `cv2.threshold()` method 
call. We pass in four parameters. The first, `blur`, is our blurred grayscale
version of the image. Next is our threshold value `t`. The third parameter is
the value to be used for pixels that are turned on during the thresholding,
255. Finally, we pass in a constant telling the method what kind of 
thresholding to apply, `cv2.THRESH_BINARY_INV`. The method returns a tuple of
two items: the value used for `t` and a new, two-dimensional NumPy array 
representing the mask created by the thresholding operation. You may be 
wondering why the method returns `t`, since we passed the value in. We will 
discuss that aspect in the next section. For now, just focus on the mask 
created by the method, `maskLayer`.

Here is a visualization of the mask created by the thresholding operation.
The program used parameters of k = 7 and T = 210 to produce this mask. You can
see that the areas where the shapes were in the original area are no white, 
while the rest of the mask image is black. 

![Mask created by thresholding](../fig/06-junk-mask.jpg)

Next in the program, we convert the two-dimensional mask layer returned by 
`cv2.threshold()` into a proper image, by merging the same layer together as 
the blue, green, and red layers of the new image. This is accomplished with the
`cv2.merge()` method; we pass in a list of the three color channel layers -- 
all the same in this case -- and the method returns a single image with those
color channels. 

Finally, we can use the `cv2.bitwise_and()` method we were introduced to in the
[Drawing and Bitwise Operations]({{ page.root}}./03-drawing-bitwise) episode to
apply the mask to the original colored image. What we are left with is only the
colored shapes from the original, as shown in this image:

![Selected shapes](../fig/06-junk-selected.jpg)

## Adaptive thresholding



