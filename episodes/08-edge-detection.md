---
title: "Edge Detection"
teaching: 30
exercises: 0
questions:
- "How can we automatically detect the edges of the objects in an image?"
objectives:
- "Apply Sobel, Laplacian, and Canny edge detection to an image."
- "Explain how we can use trackbars to expedite finding appropriate parameter
values for our OpenCV method calls."
- "Create OpenCV windows with trackbars and associated callback functions."
keypoints:
- "Sobel edge detection is implemented in the `cv2.Sobel()` method. We usually
call the method twice, to find edges in the x and y dimensions."
- "The two edge images returned by two `cv2.Sobel()` calls can be merged using
the `cv2.bitwise_or()` method."
- "Edge detection methods return data that is signed instead of unsigned, so 
data types such as `cv2.CV_16S` or `cv2.CV-64F` should be used instead of
unsigned, 8-bit integers (`uint8`)."
- "The `cv2.createTrackbar()` method is used to create trackbars on windows
that have been created by our programs."
- "We use Python functions as *callbacks* when we create trackbars using 
`cv2.createTrackbar()`."
- "Use the Python `global` keyword to indicate variables referenced inside 
functions that are global variables, i.e., variables that are first declared
in other parts of the program."
---

In this episode, we will learn how to use OpenCV functions to apply *edge 
detection* to an image. In edge detection, we find the boundaries or edges of
objects in an image, by determining where the brightness of the image changes
dramatically. Edge detection can be used to extract the structure of objects in 
an image. If we are interested in the number, size, shape, or relative location
of objects in an image, edge detection allows us to focus on the parts of the 
image most helpful, while ignoring parts of the image that will not help us. 

For example, once we have found the edges of the objects in the image (or once
we have converted the image to binary using thresholding), we can 
use that information to find the image *contours*, which we will learn about in
the following [Contours]({{ page.root }}/09-contours) episode. With the 
contours, we can do things like counting the number of objects in the image,
measure the size of the objects, classify the shapes of the objects, and so on.

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

If we zoom in on the edge more closely, as in this image, we can see that the 
edge between the black and white areas of the image is not a clear-cut line.

![Black and white edge pixels](../fig/07-bw-edge-pixels.jpg)

We can learn more about the edge by examining the color values of some of the 
pixels. Imagine a short line segment, halfway down the image and straddling the 
edge between the black and white paper. This plot shows the pixel values 
(between 0 and 255, since this is a grayscale image) for forty pixels spanning 
the transition from black to white.

![Gradient near transition](../fig/07-bw-gradient.png)

It is obvious that the "edge" here is not so sudden! So, any OpenCV method to
detect edges in an image must be able to decide where the edge is, and place 
appropriately-colored pixels in that location. 

## Sobel edge detection

*Sobel edge detection* uses numerical approximations of derivatives to detect
edges in an image. Here is an example of how the process might work. If we look
at the gradient plot above, we can see that its shape roughly corresponds to
the sigmoid function, as shown by the smooth purple line in this plot:

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
we used before in the [Thresholding]({{ page.root }}/07-thresholding/) 
episode:

![Colored shapes](../fig/06-junk-before.jpg)

We are interested in finding the edges of the shapes in the image, and so the
colors are not important. Our strategy will be to read the image as grayscale,
convert it to a binary image using the techniques from the 
[Thresholding]({{ page.root }}/07-thresholding/) episode, and then apply 
Sobel edge detection. We will actually have to do the edge detection twice, 
once to examine gradient differentials in the x dimension, and then again to 
look at the differentials in the y dimension. After that, we will combine the
two results into one image, which will show the edges detected. 

~~~
'''
 * Python script to demonstrate Sobel edge detection.
 *
 * usage: python SobelEdge.py <filename> <kernel-size> <threshold>
'''
import cv2
import numpy as np
import sys

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
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# perform Sobel edge detection in x and y dimensions
edgeX = cv2.Sobel(binary, cv2.CV_16S, 1, 0)
edgeY = cv2.Sobel(binary, cv2.CV_16S, 0, 1)

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
edgeX = cv2.Sobel(binary, cv2.CV_16S, 1, 0)
edgeY = cv2.Sobel(binary, cv2.CV_16S, 0, 1)
~~~
{: .python}

As we are using it here, the `cv2.Sobel()` method takes four parameters. The 
first parameter is the input image. In this case, we are passing in the binary
image we made from the original, `binary`. 

The second parameter is the data type to be used for the color values of each
pixel in the image produced by the `cv2.Sobel()` method. Due to the way the 
method works, we must use a *signed* data type here, i.e., one that allows for
positive and negative numbers. The data type we have been using for images with
24-bit color has been `uint8`, *unsigned*, eight-bit integers, allowing for 
values in the range [0, 255]. We were first introduced to this data type in the
[Drawing and Bitwise Operations]({{ page.root }}/04-drawing-bitwise/) 
episode. If we use an unsigned type for the output data type, the `cv2.Sobel()`
method will fail to detect half of the edges in the input image. So, we specify
a signed data type, 16-bit signed integers, with the `cv2.CV_16S`
parameter. Another option would be `cv2.CV_64F`, or 64-bit, floating point 
numbers. This might provide slightly better edge detection, but it would 
require four times the memory for each pixel, and therefore our program would 
run more slowly. When performing edge detection on your own images, it is 
probably a good policy to start with the `cv2.CV_16S` data type, and then
resort to `cv2.CV_64F` if the results are unsatisfactory.

The third and fourth parameters are where we indicate the axes to perform edge
detection on. The `cv2.Sobel()` method is usually called as we have done here.
The third parameter is the derivative to use for edge detection in the x 
dimension, so the `1` in the first `cv2.Sobel()` method call tells the method 
to use the first derivative in the x dimension. The fourth parameter in the 
first call is `0`, telling the method to skip finding edges in the y dimension
for this call. In the second `cv2.Sobel()` method call, we reverse the order of
the parameters, turning off the x dimension detection and using the first 
derivative in the y dimension. 

The result of these two calls is two images, held in `edgeX` and `edgeY`, each
with some of the edges in the overall image. Both of these edge images use 16
bit signed integers for each pixel intensity value, so we will want to 
convert them back to the more usual `uint8` data type before continuing. Here 
are the two edge images produced by the preceding program on the colored shapes
image above. 

![Sobel edge detection subimages](../fig/07-junk-edge-x-y.jpg)

Now we convert the data type of the two edge images back to 8 bits per channel,
and merge them together, with these three lines of code:

~~~
edgeX = np.uint8(np.absolute(edgeX))
edgeY = np.uint8(np.absolute(edgeY))
edge = cv2.bitwise_or(edgeX, edgeY)
~~~
{: .python}

This code first takes the absolute value of each value in each of the edge 
images, with the NumPy `absolute()` method, and then truncates the values to
fit within unsigned, 8 bit integers with the NumPy `uint8()` method. We store
the resulting images back in the same variables that held the original edge 
images, `edgeX` and `edgeY`. After that, we combine the two images together 
using the `cv2.bitwise_or()` method. This means that any pixel that was turned
on in either image will be turned on in the new `edge` image; while pixels that
are black in the new image were black in both subimages. 

Finally the program displays the `edge` image, showing the edges that were 
found in the original. Here is the result, for the colored shape image above,
with blur kernel k = 3 and binary threshold value t = 210:

![Output of Sobel edge detection](../fig/07-sobel-edges.jpg)

> ## Laplacian edge detection
> 
> Another simple edge detection method in OpenCV is Laplacian edge detection.
> An advantage of the Laplacian method over Sobel edge detection is that it 
> does not require two calls to detect edges in the x and y dimensions. 
> 
> Navigate to the **Desktop/workshops/image-processing/08-edge-detection**
> directory, and modify the **LaplacianEdge.py** program to perform edge 
> detection using the `cv2.Laplacian()` method. Comments inside the program
> indicate where you should make your modifications, and tell you the 
> parameters that the `cv2.Laplacian()` method takes. 
> 
> > ## Solution
> > 
> > Here is the modified **LaplacianEdge.py** program that uses Laplacian 
> > edge detection.
> > 
> > ~~~
> > '''
> >  * Python script to demonstrate Laplacian edge detection.
> >  *
> >  * usage: python LaplacianEdge.py <filename> <kernel-size> <threshold>
> > '''
> > import cv2
> > import numpy as np
> > import sys
> > 
> > # read command-line arguments
> > filename = sys.argv[1]
> > k = int(sys.argv[2])
> > t = int(sys.argv[3])
> > 
> > # load and display original image
> > img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
> > cv2.namedWindow("original", cv2.WINDOW_NORMAL)
> > cv2.imshow("original", img)
> > cv2.waitKey(0)
> > 
> > # blur image and use simple inverse binary thresholding to create
> > # a binary image
> > blur = cv2.GaussianBlur(img, (k, k), 0)
> > (t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)
> > 
> > # WRITE YOUR CODE HERE
> > # perform Laplacian edge detection
> > # cv2.Laplacian() takes two parameters, the input image, and the data
> > # type used for the output image. Use the cv2.Laplacian() method to 
> > # detect the edges in the binary image, storing the result in an image 
> > # named edge.
> > edge = cv2.Laplacian(mask, cv2.CV_16S)
> > 
> > # WRITE YOUR CODE HERE
> > # Convert the edge image back to 8 bit unsigned integer data type.
> > edge = np.uint8(np.absolute(edge))
> > 
> > # display edges
> > cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
> > cv2.imshow("edges", edge)
> > cv2.waitKey(0)
> > ~~~
> > {: .python}
> > 
> > Here is the edge image produced by this program for the colored shapes 
> > image, using blur kernel size k = 5 and binary threshold value t = 210.
> > 
> > ![Laplacian edges](../fig/07-laplacian-edges.jpg)
> {: .solution}
{: .challenge}

## Canny edge detection and trackbars

We will introduce one more type of edge detection supported by OpenCV in this 
section, *Canny edge detection*, created by John Canny in 1986. This method 
uses a series of steps, many of which we have already discussed. The OpenCV
`cv2.Canny()` method uses the following steps:

1. A Gaussian blur, with a blur kernel of k = 5, is applied to remove noise
from the image.

2. Sobel edge detection is performed on both the x and y dimensions, to find
the intensity gradients of the edges in the image.

3. Pixels that would be highlighted, but seem too far from any edge, are 
removed. This is called *non-maximum suppression*, and the result is edge lines
that are thinner.

4. A double threshold is applied to determine potential edges. Here extraneous 
pixels caused by noise or milder color variation than desired are eliminated.
If a pixel's gradient value -- based on the Sobel differential -- is above the
high threshold value, it is considered a strong candidate for an edge. If the 
gradient is below the low threshold value, it is turned off. If the gradient is
in between, the pixel is considered a weak candidate for an edge pixel. 

5. Final detection of edges is performed using *hysteresis*. Here, weak 
candidate pixels are examined, and if they are connected to strong candidate 
pixels, they are considered to be edge pixels; the remaining, non-connected 
weak candidates are turned off.

For a user of the `cv2.Canny()` edge detection method, the two important 
parameters to pass in are the low and high threshold values used in step four
of the process. These values generally are determined empirically, based on the
contents of the image(s) to be processed. 

Here is an image of some glass beads that we can use as input into a Canny edge
detection program:

![Beads image](../fig/07-beads.jpg)

We could write a simple Python program to apply Canny edge detection to the 
image, very similar to the one using the Sobel method above. Such a program 
would take three command-line arguments: the filename, the low threshold, and
the high threshold required by the Canny method. To find acceptable values for
the thresholds, we would have to run the program over and over again, trying 
different threshold values and examining the resulting image, until we find a 
combination of parameters that works best for the image.

*Or*, we can write a Python program that uses OpenCV *trackbars*, that allow us
to vary the low and high threshold parameters while the program is running. In 
other words, we can write a program that presents us with a window like this:

![Canny UI](../fig/07-canny-ui.png)

Then, when we run the program, we can use the trackbar sliders to vary the 
values of the threshold parameters until we are satisfied with the results. 
After we have determined suitable values for the threshold parameters, we can 
write a simpler program to utilize the parameters without bothering with the 
user interface and trackbars. 

Here is a Python program that shows how to apply Canny edge detection, and how
to add trackbars to the user interface: 

~~~
'''
 * Python program to demonstrate Canny edge detection.
 *
 * usage: python CannyEdge.py <filename>
'''
import cv2
import sys

'''
 * Function to perform Canny edge detection and display the
 * result. 
'''
def cannyEdge():
	global img, minT, maxT
	edge = cv2.Canny(img, minT, maxT)
	cv2.imshow("edges", edge)

'''
 * Callback function for minimum threshold trackbar.
''' 
def adjustMinT(v):
	global minT
	minT = v
	cannyEdge()

'''
 * Callback function for maximum threshold trackbar.
'''
def adjustMaxT(v):
	global maxT
	maxT = v
	cannyEdge()
	

'''
 * Main program begins here. 
'''
# read command-line filename argument
filename = sys.argv[1]

# load original image as grayscale
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# set up display window with trackbars for minimum and maximum threshold
# values
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
minT = 30
maxT = 150
cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)

# perform Canny edge detection and display result
cannyEdge()
cv2.waitKey(0)
~~~
{: .python}

There are four parts to this program, making it a bit (but only a *bit*) more 
complicated that the programs we have looked at so far. The added complexity 
comes from three *functions* we have written. From top to bottom, the
parts are:

* The `cannyEdge()` function, 
* The `adjustMin()` function, 
* the `adjustMax()` function, and
* The main program, i.e., the code that is executed when the program runs.

We will look at the main program part first, and then return to the three 
functions. The first several lines of the main program are easily recognizable
at this point: saving the command-line argument, reading the image in 
grayscale, and creating a window. Then, the program creates two variables to
hold first guesses for the low and high threshold values, `minT` and `maxT`. 

Next comes the code where we attach two trackbars to the display window named
"edges".

~~~
cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)
~~~
{: .python}

The `cv2.createTrackbar()` method takes five parameters. First is a string 
containing the label that will be used for the trackbar when it is displayed. 
Next is a string containing the name of the window the trackbar should be 
attached to. Third is the initial value for the trackbar. Fourth is the maximum
value for the trackbar; the minimum is always 0. Finally, we pass in the name 
of a function that will be called whenever the value of the trackbar is changed
by the user. Here we pass in `adjustMinT` for the minimum threshold trackbar 
and `adjustMaxT` for the maximum threshold trackbar. 

The last two lines of our program perform the initial Canny edge detection,
by calling the `cannyEdge()` function, and then instruct OpenCV to keep the 
"edges" window open until a key is pressed. 

Now we can cover the details of the three functions in this program. First, 
consider the `cannyEdge()` function:

~~~
def cannyEdge():
	global img, minT, maxT
	edge = cv2.Canny(img, minT, maxT)
	cv2.imshow("edges", edge)
~~~
{: .python}

This function actually performs the edge detection, via a call to the 
`cv2.Canny()` method. First, however, the `global` line indicates that the 
`img`, `minT`, and `maxT` variables are *global*, that is, that they were 
created in the main program, rather than inside this function. Including this
line in functions that refer to variables that were created elsewhere makes 
sure that the variables' values are available inside the function. 

The next line calls the `cv2.Canny()` method to do edge detection. The three
parameters to the method are the variable holding the input image, the minimum
threshold value, and the maximum threshold value. The method returns the output
image, which we store in a variable named `edge`. 

After the edge detection process is complete, the edge image is displayed in 
the window named "edges." Recall that this window was already created in the 
main program. 

Now, let us examine one of the trackbar callback functions, `adjustMinT()`, in
detail.

~~~
def adjustMinT(v):
	global minT
	minT = v
	cannyEdge()
~~~
{: .python} 

This function has a single *parameter*, which we have named `v`. The parameter
is used to communicate the value of the minimum threshold trackbar when the 
function is called. For example, for the image of the user interface above, the
last time the minimum threshold trackbar was adjusted, the `adjustMinT()` 
function was called and the parameter `v` had the value 20. 

The first line in the function is a `global` statement, telling the function 
that the variable `minT` is global. Then, we change the value of `minT` to the
value contained in `v`, so that the minimum threshold variable `minT` contains 
the new value set by the trackbar. Finally, the `cannyEdge()` function is 
called again, to re-do the edge detection process and display the results in 
the "edges" window. 

The `adjustMaxT()` function is very similar. It changes the value of the `maxT`
variable based on the value of the maximum threshold trackbar. 

Here is the result of running the preceding program on the beads image, with
minimum threshold value 20 and maximum threshold value 120. 

![Beads edges](../fig/07-beads-edges.jpg)

> ## Applying Canny edge detection to another image
> 
> Now, navigate to the **Desktop/workshops/image-processing/08-edge-detection**
> directory, and run the **CannyEdge.py** program on the image of colored 
> shapes, **junk.jpg**. Adjust the minimum and maximum threshold trackbars
> to produce an edge image that looks like this:
> 
> ![Colored shape edges](../fig/07-canny-junk-edges.jpg)
> 
> What values for the minimum and maximum threshold values did you use to 
> produce an image similar to the one above? 
> 
> > ## Solution
> > 
> > The colored shape edge image above was produced with a minimum threshold
> > value of 90 and a maximum threshold value of 190. You may be able to 
> > achieve similar results with other threshold values.
> {: .solution}
{: .challenge}

> ## Using trackbars for thresholding
> 
> Now, let us apply what we know about creating trackbars to another, similar
> situation. Consider this image of a collection of maize seedlings, and 
> suppose we wish to use simple fixed-level thresholding to mask out everything 
> that is not part of one of the plants. 
> 
> ![Maize roots image](../fig/07-maize-roots.jpg)
> 
> To perform the thresholding, we could first create a histogram, then examine
> it, and select an appropriate threshold value. Here, however, let us create 
> an application with a trackbar to set the threshold value. Create a program 
> that reads in the image, displays it in a window with a trackbar, and allows
> the trackbar value to vary the threshold value used. You will find the image
> in the **Desktop/workshops/image-processing/08-edge-detection** directory, 
> under the name **maize-roots.jpg**.
> 
> > ## Solution
> > 
> > Here is a program that uses a trackbar to vary the threshold value used in 
> > a simple, fixed-level thresholding process. 
> > 
> > ~~~
> > '''
> >  * Python program to use a trackbar to control fixed-level 
> >  * thresholding value.
> >  *
> >  * usage: python TBarT.py <filename> <kernel-size>
> > '''
> > import cv2
> > import sys
> > 
> > '''
> >  * function to apply simple, fixed-level thresholding to the image
> > '''
> > def fixedThresh():
> >     global img, blur, thresh
> >     (t, mask) = cv2.threshold(blur, thresh, 255, cv2.THRESH_BINARY)
> >     sel = cv2.bitwise_and(img, mask)
> >     cv2.imshow("image", sel)
> >    
> > '''
> >  * callback function to get the value from the threshold trackbar,
> >  * and then call the fixedThresh() method
> > '''
> > def adjustThresh(v):
> >     global thresh
> >     thresh = v
> >     fixedThresh()
> >     
> > '''
> >  * Main program begins here.
> > '''
> > # read and save command-line parameters
> > filename = sys.argv[1]
> > k = int(sys.argv[2])
> > 
> > # read image as grayscale, and blur it
> > img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
> > blur = cv2.GaussianBlur(img, (k, k), 0)
> > 
> > # create the display window and the trackbar
> > cv2.namedWindow("image", cv2.WINDOW_NORMAL)
> > thresh = 128
> > cv2.createTrackbar("thresh", "image", thresh, 255, adjustThresh)
> > 
> > # perform first thresholding
> > fixedThresh()
> > cv2.waitKey(0)
> > ~~~
> > {: .python}
> > 
> > Here is the output of the program, with a blur kernel of size 7 and a 
> > threshold value of 90:
> > 
> > ![Thresholded maize roots](../fig/07-maize-roots-threshold.jpg)
> {: .solution}
{: .challenge}

Keep this trackbar technique in your image processing "toolbox." You can use 
trackbars to vary other kinds of parameters, such as blur kernel sizes, binary
thresholding values, and so on. A few minutes developing a program to tweak 
parameters like this can save you the hassle of repeatedly running a program
from the command line with different parameter values. 
