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
thresholding to an image. Thresholding is a type of *image segmentation*,
where we somehow change the pixels of an image to make the image easier to 
analyze. Most frequently, we use thresholding as a way to 
select areas of interest of an image, while ignoring the parts we are not 
concerned with. We have already done some simple thresholding, in the 
"Manipulating pixels" section of the 
[OpenCV Images]({{ page.root }}/02-opencv-images) episode. In that case, we
used a simple NumPy array manipulation to separate the pixels belonging to the
root system of a plant from the black background. In this episode, we will 
learn how to use OpenCV methods to perform thresholding. Then, we will use the
masks returned by these methods to select the parts of an image we are 
interested in. 

## Simple thresholding

Consider this image, with a series of crudely cut shapes set against a white 
background. The black outline is not part of the image.

![Original shapes image](../fig/06-junk-before.jpg)

Now suppose we want to select only the shapes from the image. In other words,
we want to leave the pixels belonging to the shapes "on," while turning the 
rest of the pixels "off," by setting their color channel values to zeros. The
OpenCV library has several different methods of thresholding. We will start 
with the simplest version, which involves an important instance of human 
input. Specifically, in this simple, *fixed-level thresholding*, we have to 
provide a threshold value, T. 

The process works like this. First, we will load the original image, convert
it to grayscale, and blur it with one of the methods from the 
[Blurring]({{ page.root }}./06-blurring) episode. Then, we will use the 
`cv2.threshold()` method; T, an integer in the closed range [0, 255],  will be
one of the parameters passed to the method. Pixels with color values on one 
side of T will be turned "on," while pixels with color values on the other side
will be turned "off." In order to use this method, we have to determine a good 
value for T. How might we do that? Well, one way is to look at a grayscale 
historgram of the image. Here is the histogram produced by the 
**GrayscaleHistogram.py** program from the 
[Creating Histograms]({{ page.root }}./04-creating-histograms) episode.

![Grayscale histogram](../fig/06-junk-histogram.png)

Since the image has a white background, most of the pixels in the image are 
white. This corresponds nicely to what we see in the histogram: there is a 
spike just past the value 250. If we want to select the shapes and not the 
background, we want to turn off the white background pixels, while leaving the
pixels for the shapes turned on. So, we should choose a value of T somewhere 
between 200 and 255, and instruct the `cv2.threshold()` method to turn pixels
below the T value on and turn the pixels above the T value off. 

Here is a Python program to apply simple thresholding to the image, to 
accomplish this task. 

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

# blur and grayscale before thresholding
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (k, k), 0)

# perform inverse binary thresholding 
(t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# make a mask suitable for color images
mask = cv2.merge([maskLayer, maskLayer, maskLayer])

# display the mask image
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
cv2.waitKey(0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(img, mask)

# display the result
cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
cv2.imshow("selected", sel)
cv2.waitKey(0)
~~~
{: .python}

This program takes three command-line arguments: the filename of the image to 
manipulate, the kernel size used during the blurring step (which, if you recall
from the [Blurring]({{ page.root }}./06-blurring) episode. must be odd), 
and finally, the threshold value T, which should be an integer in the closed
range [0, 255]. The program takes the command-line values and stores them in 
variables named `filename`, `k`, and `t`, respectively. 

Next, the program reads the original image based on the `filename` value, and
displays it. 

Now is where the main work of the program takes place. First, we convert the 
image to grayscale and then blur it, using the `cv2.GaussianBlur()` method we
learned about in the [Blurring]({{ page.root }}./06-blurring) episode. The
image passed into the thresholding method must be grayscale. 

The fixed-level thresholding is performed with the `cv2.threshold()` method 
call. We pass in four parameters. The first, `blur`, is our blurred grayscale
version of the image. Next is our threshold value `t`. The third parameter is
the value to be used for pixels that are turned on during the thresholding,
255. Finally, we pass in a constant telling the method what kind of 
thresholding to apply, `cv2.THRESH_BINARY_INV`. This instructs the method to 
turn on pixels with color values below the threshold value T and turn off
pixels with color values above T. 

The method returns a tuple of two items: the value used for `t` and a new, 
two-dimensional NumPy array representing the mask created by the thresholding 
operation. You may be wondering why the method returns `t`, since we passed the
value in. There are other ways of using the `cv2.threshold()` method in which
the threshold value is calculated automatically. For now, just focus on the 
mask created by the method, `maskLayer`.

Here is a visualization of the mask created by the thresholding operation.
The program used parameters of k = 7 and T = 210 to produce this mask. You can
see that the areas where the shapes were in the original area are now white, 
while the rest of the mask image is black. 

![Mask created by thresholding](../fig/06-junk-mask.jpg)

Next in the program, we convert the grayscale mask layer returned by 
`cv2.threshold()` into a color image, by merging the same layer together as 
the blue, green, and red layers of the new image. This is accomplished with the
`cv2.merge()` method; we pass in a list of the three color channel layers -- 
all the same in this case -- and the method returns a single image with those
color channels. 

Finally, we can use the `cv2.bitwise_and()` method we were introduced to in the
[Drawing and Bitwise Operations]({{ page.root}}./03-drawing-bitwise) episode to
apply the mask to the original colored image. What we are left with is only the
colored shapes from the original, as shown in this image:

![Selected shapes](../fig/06-junk-selected.jpg)

> ## More practice with simple thresholding
> 
> Now, it is your turn to practice. Suppose we want to use simple thresholding
> to select only the colored shapes from this image: 
> 
> ![more-junk.jpg](../fig/06-more-junk.jpg)
> 
> First, use the **GrayscaleHistogram.py** program in the 
> **Desktop/divas/04-creating-histograms** directory to examine the grayscale 
> histogram of the **more-junk.jpg** image, which you will find in the 
> **Desktop/divas/06-thresholding** directory. Via the histogram, what do you 
> think would be a good value for the threshold value, T? 
> 
> > ## Solution
> > 
> > Here is the histogram for the **more-junk.jpg** image. 
> > 
> > ![Grayscale histogram of more-junk.jpg](../fig/06-more-junk-histogram.png)
> > 
> > We can see a large spike around 75, and a smaller spike around 175. The 
> > spike near 75 represents the darker background, so it seems like a T value
> > close to 150 would be a good choice. 
> {: .solution}
> 
> Now, modify the **ThresholdPractice.py** program in the 
> **Desktop/divas/06-thresholding** directory to turn the pixels above the 
> T value on and turn the pixels below the T value off. To do this, change the
> `cv2.THRESH_BINARY_INV` parameter to `cv2.THRESH_BINARY`. Then execute the 
> program on the **more-junk.jpg** image, using a reasonable value for k and 
> the T value you obtained from the histogram. If everything works as it 
> should, your output should show only the colored shapes on a pure black 
> background. 
> 
> > ## Solution 
> > 
> > Here is the modified **ThresholdPractice.py** program.
> > 
> > ~~~
> > '''
> >  * Python script to practice simple thresholding.
> > '''
> > import cv2, sys
> > 
> > # get filename, kernel size, and threshold value from command line
> > filename = sys.argv[1]
> > k = int(sys.argv[2])
> > t = int(sys.argv[3])
> > 
> > # read and display the original image
> > img = cv2.imread(filename)
> > cv2.namedWindow("original", cv2.WINDOW_NORMAL)
> > cv2.imshow("original", img)
> > cv2.waitKey(0)
> > 
> > # blur and grayscale before thresholding
> > blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
> > blur = cv2.GaussianBlur(blur, (k, k), 0)
> > 
> > # perform inverse binary thresholding 
> > (t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)
> > 
> > # make a mask suitable for color images
> > mask = cv2.merge([maskLayer, maskLayer, maskLayer])
> > 
> > # display the mask image
> > cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
> > cv2.imshow("mask", mask)
> > cv2.waitKey(0)
> > 
> > # use the mask to select the "interesting" part of the image
> > sel = cv2.bitwise_and(img, mask)
> > 
> > # display the result
> > cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
> > cv2.imshow("selected", sel)
> > cv2.waitKey(0)
> > ~~~
> > 
> > Using a blur kernel value k = 7 and threshold T = 150, we obtain this mask:
> > 
> > ![more-junk.jpg thresholding mask](../fig/06-more-junk-mask.jpg)
> > 
> > And applying the mask results in this selection of shapes:
> > 
> > ![more-junk.jpg selected shapes](../fig/06-more-junk-selected.jpg)
> > 
> {: .solution}
{: .challenge}

## Adaptive thresholding

There are also OpenCV methods to perform *adaptive thresholding*. The chief 
advantage of adaptive thresholding is that the value of the threshold, T, is
determined automatically for us. One such method, *Otsu's method*, is 
particularly useful for situations where the grayscale histogram of an image
has two peaks. Consider this maize root system image, which we have seen 
before in the [OpenCV Images]({{ page.root }}./02-opencv-images) episode. 

![Maize root system](../fig/06-roots-original.jpg)

Now, look at the grayscale histogram of this image, as produced by our 
**GrayscaleHistogram.py** program from the 
[Creating Histograms]({{ page.root }}./02-creating-histograms) episode. 

![Maize root histogram](../fig/06-roots-histogram.png)

The histogram has a significant peak around 60, and a second, albeit smaller
peak very near 255. Thus, this image is a good candidate for thresholding with
Otsu's method. The mathematical details of how this work are complicated (see 
the [OpenCV documentation](http://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html)
if you are interested), but the outcome is that Otsu's method finds a threshold
value between the two peaks of a grayscale histogram. 

The `cv2.threshold()` method can also be used to apply thresholding via Otsu's
method, if we pass the correct parameters. You should be aware, however, that 
the current implementation of Otsu's method in the `cv2.threshold()` method 
only works with 8 bits grayscale images. 

Here is a Python program illustrating how to perform thresholding with Otsu's
method using the `cv2.threshold()` method. 

~~~
'''
 * Python script to demonstrate adaptive thresholding using Otsu's method.
'''
import cv2, sys

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display the original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# blur and grayscale before thresholding
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (k, k), 0)

# perform adaptive thresholding 
(t, maskLayer) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + 
	cv2.THRESH_OTSU)

# make a mask suitable for color images
mask = cv2.merge([maskLayer, maskLayer, maskLayer])

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
cv2.waitKey(0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(img, mask)

# display the result
cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
cv2.imshow("selected", sel)
cv2.waitKey(0)
~~~
{: .python}

The program begins with the now-familiar imports and command line parameters. 
Here we only have to get the filename and the blur kernel size from the command
line, since Otsu's method will automatically determine the thresholding value 
T. Then, the original image is read and displayed, and a blurred grayscale 
image is created.

We perform the thresholding with another call to the `cv2.threshold()` method,

~~~
(t, maskLayer) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + 
	cv2.THRESH_OTSU)
~~~
{: .python}

The parameters mostly are similar to the simple thresholding we did in the 
previous section: `blur` is the blurred grayscale image, `0` stands in for the 
threshold value T, and `255` is the value that will be used for pixels that are
turned on. 

The difference lies in the next parameter, 
`cv2.THRESH_BINARY + cv2.THRESH_OTSU`. We are adding together two `cv2` 
constants, which in this case tells the `cv2.threshold()` method to do binary
thresholding -- pixels above the threshold value will be turned on, those below
the threshold will be turned off -- *and* to use Otsu's method to automatically
determine the threshold value. 

The method returns the computed threshold value, `t`, and the grayscale mask 
layer in the `maskLayer` variable. For this root image, and a blur kernel of 
size 7, the computed threshold value is 110, and the resulting mask is:

![Root system mask](../fig/06-roots-mask.jpg)

Once we have the grayscale mask, we turn it in to a color image and apply the 
mask to the original root image, just as we did in the previous section. Here 
is the result:

![Masked root system](../fig/06-roots-sel.jpg)

## Application: measuring root mass

Let us now turn to an application where we can apply thresholding and other
techniques we have learned to this point. Consider these four maize root 
system images.

![Four root images](../fig/06-four-root-collage.jpg)

Now suppose we are interested in the amount of plant material in each image, 
and in particular how that amount changes from image to image. Perhaps the 
images represent the growth of the plant over time, or perhaps the images show
four different maize varieties at the same phase of their growth. In any case,
the question we would like to answer is, "how much root mass is in each image?"
We will construct a Python program to measure this value for a single image, 
and then create a Bash script to execute the program on each trial image in 
turn. 

Our strategy will be this:

1. Read the image, converting it to grayscale as it is read. For this 
application we do not need the color image.

2. Blur the image.

3. Use Otsu's method of thresholding to create a binary image, where the pixels
that were part of the maize plant are white, and everything else is black.

4. Save the binary image so it can be examined later.

5. Count the white pixels in the binary image, and divide by the number of 
pixels in the image. This ratio will be a measure of the root mass of the 
plant in the image.

6. Output the name of the image processed and the root mass ratio. 

~~~
'''
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
'''
import cv2, sys, numpy as np

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read the original image, converting to grayscale
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# blur before thresholding
blur = cv2.GaussianBlur(img, (k, k), 0)

# perform thresholding the first time to produce a mask
(t, maskLayer) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + 
	cv2.THRESH_OTSU)

# save maskLayer; first find extension beginning
dot = filename.index(".")
maskFileName = filename[:dot] + "-mask" + filename[dot:]
cv2.imwrite(maskFileName, maskLayer)

# determine root mass ratio
rootPixels = cv2.countNonZero(maskLayer)
w = maskLayer.shape[0]
h = maskLayer.shape[1]
density = rootPixels / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
~~~
{: .python}

~~~
#!/bin/bash
# Run the root density mass on all of the root system trail images.

# first, remove existing mask output images
rm *-mask.jpg

# then, execute the program on all the trail images
for f in trial-*.jpg
do
	python RootMass.py $f 7
done
~~~
{: .bash}

~~~
trial-016.jpg,0.04827875664893617
trial-020.jpg,0.06355651595744681
trial-216.jpg,0.1411343085106383
trial-293.jpg,0.13571126994680852
~~~
{: .output}

> ## Ignoring more of the images
> 
> You may have noticed something about the binary images produced by the 
> proceeding program. Our root mass ratios include white pixels that are not
> part of the plant in the image, do they not? The numbered labels and the 
> white circles in each image are preserved during the thresholding, and 
> therefore their pixels are included in our calculations. How might we remove
> the labels and circles before calculating the ratio, so that our results are
> more accurate? 
> 
{: .challenge}
