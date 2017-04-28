---
title: "Contours"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to find the 
*contours* of the objects in an image. A countour is a closed curve of points,
representing the boundaries of an object in an image. A single object in an
image may produce several associated contours, which are returned in a 
hierarchial data structure. Once we find the countours of the objects in an 
image, we can do things like determine the number of objects in an image, 
classify the shapes of the objects, or measure the size of the objects. The 
input to the contour-finding process is a binary image, which we will produce
by first applying thresholding and / or edge detection. In the binary image,
the objects we wish to detect should be white, while the background of the 
image should be black.

## Using contours to count objects

Consider this image of several six-sided dice on a black background. 

![Dice](../fig/08-dice.jpg)

Suppose we want to automatically count the number of dice in the image. We can
use contours to do that. We find contours with the `cv2.findContours()` method,
and then easily examine the results to count the number of objects. Our 
strategy will be this:

1. Read the input image, convert it to grayscale, and blur it slightly.

2. Use simple binary thresholding to convert the grayscale image to a binary
image.

3. Use the `cv2.findContours()` method to find contours corresponding to the 
outlines of the dice.

4. Print information on how many countours -- and thus how many objects -- were
found in the image.

5. For illustrative purposes, draw the contours in the original image so we can
visualize the results. 

Before we examine a Python program to implement this strategy, let us first 
look at the grayscale histogram for the dice image, so we can find a threshold
value that will effectively convert the image to binary. 

![Dice grayscale histogram](../fig/08-dice-histogram.png)

Since finding contours works on white objects set against a black background, 
in our thresholding we want to turn off the pixels in the background, while 
turning on the pixels associated with the face of the dice. Based on the 
histogram, a threshold value of 200 seems likely to do that. 

Here is a Python program to count the number of dice in the preceeding image
via contours. 

~~~
'''
 * Python program to use contours to count the objects in an image.
'''
import cv2, sys

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
img = cv2.imread(filename)

# create binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)

# find contours
(_, contours, _) = cv2.findContours(binary, cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

# print table of contours and sizes
print("Found %d objects." % len(contours))
for (i, c) in enumerate(contours):
    print("\tSize of contour %d: %d" % (i, len(c)))

# draw contours over original image
cv2.drawContours(img, contours, -1, (0, 0, 255), 5)

# display original image with contours
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey(0)
~~~
{: .python}

We start with familiar steps: we save the command-line arguments for the 
filename and threshold value, read the original image, convert it to 
grayscale, blur it, and convert to a binary image via `cv2.threshsold()`, with
the resulting image save in the `binary` variable. We do not display the binary
image in the program, but if we did, it would look like this, assuming a 
threshold value of 200:

![Dice binary image](../fig/08-dice-binary.jpg)

Now, we find the contours, based on the binary image of the dice. The way we 
are using `cv2.findContours()` method takes three parameters, and it returns 
three values:

~~~
(_, contours, _) = cv2.findContours(binary, cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)
~~~
{: .python}

The first parameter to the method is the binary image to find contours in. 
Remember, this image should be binary, with the objects you wish to find 
contours for in white, against a black background. Second, we pass in a 
constant indicating what kind of contours we are interested in. Since we are
interesting in counting the objects in this image, we only care about the 
contours around the outermost edges of the objects, and so we pass in the 
`cv2.RETR_EXTERNAL` parameter. The last parameter tells the method if it 
should simplify the contours or not. We pass in `cv2.CHAIN_APPROX_SIMPLE`, 
which tells the method to simplify by using line segments when it can, rather
that including all the points on what would be a straight edge. Using this
parameter saves memory and computation time in our program. 

The `cv2.findContours()` method returns three values, as a tuple; in this case,
we are choosing to ignore the first and third return value. The first parameter
is an intermediate image that is produced during the contour-finding process. 
We are not interested in that image in this application, so we effectively
discard that image by placing the underscore (`_`) in the place of the first 
return value. The second return value is a list of NumPy arrays. Each array 
holds the points for one contour in the image. So, if we have executed our 
strategy correctly, the number of contours -- the length of the `contours` list
-- will be the number of objects in the image. The final return value is a 
NumPy array that contains hierarchy information about the contours. This is not
useful to us in our object-counting program, so we also choose to discard that
return value with the `_`. 

~~~
Found 7 objects.
	Size of contour 0: 423
	Size of contour 1: 476
	Size of contour 2: 497
	Size of contour 3: 456
	Size of contour 4: 327
	Size of contour 5: 622
	Size of contour 6: 570
~~~
{: .output}

![Dice image contours](../fig/08-dice-contours.jpg)
