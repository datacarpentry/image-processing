---
title: "Drawing and Bitwise Operations"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

The next series of episodes covers a basic toolkit of OpenCV operators. With 
these tools, we will be able to create programs to perform simple analyses of 
images based on changes in color or shape. 

## Drawing on images

Often we wish to select only a portion of an image to analyze, and ignore the 
rest. Creating a rectangular sub-image with slicing, as we did in the 
[OpenCV Images]({{ page.root }}/02-opencv-images/) lesson is one option for
simple cases. Another option is to create another special image, of the same 
size as the original, with white pixels indicating the region to save and 
black pixels everywhere else. Such an image is called a *mask*. In preparing 
a mask, we sometimes need to be able to draw a shape -- a circle or a 
rectangle, say -- on a black image. OpenCV provides tools to do that. 

Consider this image of maize seedlings:

![Maize seedlings](../fig/03-maize-roots.jpg)

Now, suppose we want to analyze only the area of the image containing the roots
themselves; we do not care to look at the kernels themselves, or anything else 
about the roots. Further, we wish to exclude the frame of the container holding
the seedlings as well. Exploration with ImageJ could tell us that the 
upper-left coordinate of the sub-area we are interested in is *(44, 357)*,
while the lower-right coordinate is *(720, 740)*. Here is a Python program to 
create a mask to select only that area of the image:

~~~
'''
 * Python program to use OpenCV drawing tools to create a mask.
 *
'''
import cv2, numpy as np

# Load and display the original image
img = cv2.imread("maize-roots.tif")
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.waitKey(0)

# Create the basic black image 
mask = np.zeros(img.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(mask, (44, 357), (720, 740), (255, 255, 255), -1)

# Display constructed mask
cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
~~~
{: .python}

As before, we first import `cv2`. We also import the NumPy library, and give it
an alias of `np`; this is necessary when we create the initial mask image. 
Then, we load and display the initial image in the same way we have done 
before.

If you recall our discussion of the RGB color model in the 
[Image Basics]({{ page.root }}/01-image-basics) lesson, you will remember that
the color black has RGB values of *(0, 0, 0)*. It follows, then, that an image
that is all black would be a three-dimensional NumPy array containing nothing
but zeros. Luckily, the NumPy library provides a function to create just such
and array. We create the array / all black image with the 

`mask = np.zeros(img.shape, dtype = "uint8")`

function call. The first parameter to the `zeros()` function is the shape of 
the original image, so that our mask will be exactly the same size as the 
original. The second parameter, `dtype = "uint8"`, indicates that the elements
in the array should be 8-bit, unsigned integers -- i.e., numbers with values
in the range *[0, 255]*. That is exactly what we need for storing RGB values 
in 24-bit color.

Next, we draw a filled, white rectangle on the all-black mask, with the 

`cv2.rectangle(mask, (44, 357), (720, 740), (255, 255, 255), -1)`

function call. The first parameter is the image to draw the rectangle on. The
next two parameters, `(44, 357)` and `(720, 740)`, are the coordinates of the 
upper-left and lower-right corners of the rectangle. 

Have you noticed anything troubling about the coordinates of the corners? Yes,
they are specified in *(x, y*) order rather than *(y, x)*. The rule of thumb is
that if we are manipulating the elements of the underlying NumPy array 
ourselves, as we did in the [OpenCV Images]({{ page.root }}/02-opencv-images)
lesson, we specify coordinates in *(y, x)* order, but when we use OpenCV
functions such as `rectangle()`, we specify coordinates in *(x, y)* order.

> ## Check the documentation!
> 
> When using an OpenCV function for the first time -- or the fifth time -- 
> it is wise to check how the function is used, via the online 
> [OpenCV documentation](http://docs.opencv.org/master/) or via other usage
> examples on programming-related sites such as 
> [Stack Overflow](https://stackoverflow.com/). Basic information about OpenCV
> functions can be found interactively in Python, via commands like 
> `help(cv2)` or `help(cv2.rectangle)`. Take notes in your lab 
> notebook. And, it is always wise to run some test code to verify that the 
> functions your program uses are behaving in the manner you intend.
{: .callout}

The next parameter to the `rectangle()` function is the color we want the 
rectangle to be drawn in. This color is specified in *(B, G, R)* order. Here
we are using white, so all the values are 255. The final parameter, `-1`, 
specifies the thickness of the rectangle's bordering line. A negative value 
here causes the rectangle to be filled with the specified color (white in this
case). 

Here's what our constructed mask looks like:

![Maize image mask](../fig/03-maize-mask.png)

## Bitwise operations

All that remains in the task of using our mask is to apply some 
*bitwise operations* to merge the mask together with the original image,
in such a way that the areas with white pixels in the mask are shown, while
the areas with black pixels in the mask are not shown. A brief diversion
into the internal representation of numbers in a computer program is required
so we can understand how this process will work. 

Internally, numbers are represented in the *binary*, or base-two, number 
system. Humans deal with numbers in the *decimal*, or base-ten, number system.
In decimal, we have ten digits, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, and each 
digit in a number is multiplied by some power of 10. For example, the number
435 is 

4 × 10<sup>2</sup> + 3 × 10<sup>1</sup> + 5 10<sup>0</sup>, or 

4 × 100 + 3 × 10 + 5 × 1. 

In binary, we have only two values *{0, 1}*, and each *bit* in a number is 
multiplied by some power of two. The decimal number 37 is equivalent to the
binary number 100101, i.e., 

1 × 2<sup>5</sup> + 0 × 2<sup>4</sup> + 0 × 2<sup>3</sup> + 
1 × 2<sup>2</sup> + 0 × 2<sup>1</sup> + 1 × 2<sup>0</sup>, or

1 × 32 + 0 × 16 + 0 × 8 + 1 × 4 + 0 × 2 + 1 × 1. 

If we are using 24-bit color, each RGB value is represented by eight bits. 
This is what gives us the decimal range [0, 255] for each value. The smallest
eight-bit value is all zeros (00000000), and the greatist is (11111111).
This maximum value is 

1 × 2<sup>7</sup> + 1 × 2<sup>6</sup> + 1 × 2<sup>5</sup> + 
1 × 2<sup>4</sup> + 1 × 2<sup>3</sup> + 1 × 2<sup>2</sup> + 
1 × 2<sup>1</sup> + 1 × 2<sup>0</sup>,
or 

128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255. 

The reason this matters is that masks operate on these types of numbers, at a 
bit-by-bit level. The main binary operation we will need is *bitwise and*. In
this situation, we take two numbers in binary, such as 11010110 and 01001101.
From those two numbers, we produce a third number by examining each bit in
succession, performing a logical "and" on each pair to produce a bit for the
new number. 

~~~
'''
 * Python program to apply a mask to an image.
 *
'''
import cv2, numpy as np

# Load the original image
img = cv2.imread("maize-roots.tif")

# Create the basic black image 
mask = np.zeros(img.shape, dtype = "uint8")

# Draw a white, filled rectangle on the mask image
cv2.rectangle(mask, (44, 357), (720, 740), (255, 255, 255), -1)

# Apply the mask and display the result
maskedImg = cv2.bitwise_and(img, mask)
cv2.namedWindow("Masked Image", cv2.WINDOW_NORMAL)
cv2.imshow("Masked Image", maskedImg)
cv2.waitKey(0)
~~~
{: .python}
