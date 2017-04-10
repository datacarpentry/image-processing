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

The following Python program shows how to use the OpenCV Average blur function.

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

![Original image](../fig/05-average-original.png)

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

