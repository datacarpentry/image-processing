---
title: "Working with skimage"
teaching: 70
exercises: 50
questions:
- "How can the skimage Python computer vision library be used to work with images?"
objectives:
- "Read, display, and save images."
- "Resize images with skimage."
- "Perform simple image thresholding with NumPy array operations."
- "Extract sub-images using array slicing."
keypoints:
- "Images are read from disk with the `skimage.io.imread()` function."
- "We create a window that automatically scales the displayed image
with matplotlib and calling `show()` on the global figure object."
- "colour images can be transformed to grayscale using `skimage.color.rgb2gray()` or
be read as grayscale directly by passing the argument `as_gray=True` to `skimage.io.imread()`."
- "We can resize images with the `skimage.transform.resize()` function."
- "NumPy array commands, like `image[image < 128] = 0`, and be used to manipulate
the pixels of an image."
- "Array slicing can be used to extract sub-images or modify areas of
images, e.g., `clip = image[60:150, 135:480, :]`."
- "Metadata is not retained when images are loaded as skimage images."
---

We have covered much of how images are represented in computer software. In this episode we will learn some more methods
 for accessing and changing digital images.

## Reading, displaying, and saving images

Skimage provides easy-to-use functions for reading, displaying, and saving images.
All of the popular image formats, such as BMP, PNG, JPEG, and TIFF are supported,
along with several more esoteric formats.
[The skimage documentation](http://scikit-image.org/docs/stable/)
has more information about supported file formats.

Let us examine a simple Python program to load, display,
and save an image to a different format.
Here are the first few lines:

~~~
"""
 * Python program to open, display, and save an image.
 *
"""
import skimage.io

# read image
image = skimage.io.imread(fname="data/chair.jpg")
~~~
{: .language-python}

First, we import the `io` module of skimage (`skimage.io`) so
we can read and write images.
Then, we use the `skimage.io.imread()` function to read a JPEG image entitled **chair.jpg**.
Skimage reads the image, converts it from JPEG into a NumPy array,
and returns the array; we save the array in a variable named `image`.

Next, we will do something with the image:

~~~
fig, ax = plt.subplots()
plt.imshow(image)
~~~
{: .language-python}

Once we have the image in the program,
we first call `plt.subplots()` so that we will have
a fresh figure with a set of axis independent from our previous calls.
Next we call `plt.imshow()` in order to display the image.

> ## Why not use `skimage.io.imshow()`
>
> The *skimage* library has its own function to display an image,
> so you might be asking why we don't use it here.
> It is certainly something you should be aware of and
> may use as you see fit in your own code,
> but the details of what it will do to display the image are
> currently in the process of change.
> Thus, calling `imshow()` off the *matplotlib.pyplot* library at this time
> ensures participants have the experience we need across platforms for this lesson,
> so we will be doing that instead.
>
{: .callout}

Now, we will save the image in another format:

~~~
# save a new version in .tif format
skimage.io.imsave(fname="data/chair.tif", arr=image)
~~~
{: .language-python}

The final statement in the program, `skimage.io.imsave(fname="chair.tif", arr=image)`,
writes the image to a file named `chair.tif` in the `data/` directory.
The `imsave()` function automatically determines the type of the file,
based on the file extension we provide.
In this case, the `.tif` extension causes the image to be saved as a TIFF.

> ## Metadata, revisited
>
> Remember, as mentioned in the previous section, _images saved with `imsave`
> will not retain any metadata associated with the original image
> that was loaded into Python!_
> If the image metadata is important to you, be sure to **always keep an unchanged
> copy of the original image!**
{: .callout }

> ## Extensions do not always dictate file type
>
> The skimage `imsave()` function automatically uses the file type we specify in
> the file name parameter's extension.
> Note that this is not always the case.
> For example, if we are editing a document in Microsoft Word,
> and we save the document as `paper.pdf` instead of `paper.docx`,
> the file *is not* saved as a PDF document.
{: .callout}

> ## Named versus positional arguments
>
> When we call functions in Python,
> there are two ways we can specify the necessary arguments.
> We can specify the arguments *positionally*, i.e.,
> in the order the parameters appear in the function definition,
> or we can use *named arguments*.
>
> For example, the `skimage.io.imread()` function definition specifies two parameters,
> the file name to read and an optional flag value.
> So, we could load in the chair image in the sample code above
> using positional parameters like this:
>
> `image = skimage.io.imread("data/chair.jpg")`
>
> Since the function expects the first argument to be the file name,
> there is no confusion about what `"data/chair.jpg"` means.
>
> The style we will use in this workshop is to name each parameters, like this:
>
> `image = skimage.io.imsave(fname="data/chair.jpg")`
>
> This style will make it easier for you to learn how to use the variety of
> functions we will cover in this workshop.
{: .callout}


> ## Resizing an image (10 min)
>
> Add `import skimage.transform` to your list of imports.
> Using chair.jpg image located in the data folder,
> write a Python script to read your image into a variable named `image`.
> Then, resize the image to 10 percent of its current size using these lines of code:
>
> ~~~
> new_shape = (image.shape[0] // 10, image.shape[1] // 10, image.shape[2])
> small = skimage.transform.resize(image=image, output_shape=new_shape)
> small = skimage.img_as_ubyte(small)
> ~~~
> {: .language-python}
>
> As it is used here,
> the parameters to the `skimage.transform.resize()` function are
> the image to transform, `image`,
> the dimensions we want the new image to have, `new_shape`.
>
> Image files on disk are normally stored as whole numbers for space efficiency,
> but transformations and other math operations often result in
> conversion to floating point numbers.
> Using the `skimage.img_as_ubyte()` method converts it back to whole numbers
> before we save it back to disk.
> If we don't convert it before saving,
> `skimage.io.imsave()` will do so regardless and generate a
> warning that can safely be ignored in this instance.
>
> Next, write the resized image out to a new file named `resized.jpg`
> in your data directory.
> Finally, use plt.imshow() with each of your image variables to display
> both images in your notebook.
> Don't forget to use `fig, ax = plt.subplots()` so you don't overwrite
> the first image with the second.
> Images may appear the same size in jupyter,
> but you can see the size difference by comparing the scales for each.
> You can also see the differnce in file storage size on disk by
> hovering your mouse cursor over the original
> and the new file in the jupyter file browser, using `ls -l` in your shell,
> or the OS file browser if it is configured to show file sizes.
>
> > ## Solution
> >
> > Here is what your Python script might look like.
> >
> > ~~~
> > """
> >  * Python script to read an image, resize it, and save it
> >  * under a different name.
> > """
> > import skimage.io
> > import skimage.transform
> >
> > # read in image
> > image = skimage.io.imread("data/chair.jpg")
> >
> > # resize the image
> > new_shape = (image.shape[0] // 10, image.shape[1] // 10, image.shape[2])
> > small = skimage.transform.resize(image=image, output_shape=new_shape)
> > small = skimage.img_as_ubyte(small)
> >
> > # write out image
> > skimage.io.imsave(fname="data/resized.jpg", arr=small)
> >
> > # display images
> > fig, ax = plt.subplots()
> > plt.imshow(image)
> > fig, ax = plt.subplots()
> > plt.imshow(small)
> > ~~~
> > {: .language-python}
> >
> > The script resizes the `data/chair.jpg` image by a factor of 10 in both dimensions,
> > saves the result to the `data/resized.jpg` file,
> > and displays original and resized for comparision.
> {: .solution}
{: .challenge}

## Manipulating pixels

In [the _Image Basics_ episode]({{page.root}}{% link _episodes/02-image-basics.md %}),
we individually manipulated the colours of pixels by changing the numbers stored
in the image's NumPy array. Let's apply the principles learned there
along with some new principles to a real world example.

Suppose we are interested in this maize root cluster image.
We want to be able to focus our program's attention on the roots themselves,
while ignoring the black background.

![Root cluster image](../data/maize-root-cluster.jpg)

Since the image is stored as an array of numbers,
we can simply look through the array for pixel colour values that are
less than some threshold value.
This process is called *thresholding*,
and we will see more powerful methods to perform the thresholding task in
[the _Thresholding_ episode]({{ page.root }}{% link _episodes/07-thresholding.md %}).
Here, though, we will look at a simple and elegant NumPy method for thresholding.
Let us develop a program that keeps only the pixel colour values in an image
that have value greater than or equal to 128.
This will keep the pixels that are brighter than half of "full brightness",
i.e., pixels that do not belong to the black background.
We will start by reading the image and displaying it.

~~~
"""
* Python script to ignore low intensity pixels in an image.
"""
import skimage.io

# read input image
image = skimage.io.imread("data/maize-root-cluster.jpg")

# display original image
fig, ax = plt.subplots()
plt.imshow(image)
~~~
{: .language-python}


Now we can threshold the image and display the result.

~~~
# keep only high-intensity pixels
image[image < 128] = 0

# display modified image
fig, ax = plt.subplots()
plt.imshow(image)
~~~
{: .language-python}

The NumPy command to ignore all low-intensity pixels is `image[image < 128] = 0`.
Every pixel colour value in the whole 3-dimensional array with a value less
that 128 is set to zero.
In this case,
the result is an image in which the extraneous background detail has been removed.

![Thresholded root image](../fig/maize-root-cluster-threshold.jpg)


## Converting colour images to grayscale

It is often easier to work with grayscale images, which have a single channel,
instead of colour images, which have three channels.
Skimage offers the function `skimage.color.rgb2gray()` to achieve this.
This function adds up the three colour channels in a way that matches
human colour perception,
see [the skimage documentation for details](https://scikit-image.org/docs/dev/api/skimage.color.html#skimage.color.rgb2gray).
It returns a grayscale image with floating point values in the range from 0 to 1.
We can use the function `skimage.util.img_as_ubyte()` in order to convert it back to the
original data type and the data range back 0 to 255.
Note that it is often better to use image values represented by floating point values,
because using floating point numbers is numerically more stable.

> ## Colour and `color`
>
> The Carpentries generally prefers UK English spelling,
> which is why we use "colour" in the explanatory text of this lesson.
> However, `skimage` contains many modules and functions that include
> the US English spelling, `color`.
> The exact spelling matters here,
> e.g. you will encounter an error if you try to run `skimage.colour.rgb2gray()`.
> To account for this, we will use the US English spelling, `color`,
> in example Python code throughout the lesson.
> You will encounter a similar approach with "centre" and `center`.
{: .callout }

~~~
"""
* Python script to load a color image as grayscale.
"""
import skimage.io
import skimage.color

# read input image
image = skimage.io.imread(fname="data/chair.jpg")

# display original image
fig, ax = plt.subplots()
plt.imshow(image)

# convert to grayscale and display
gray_image = skimage.color.rgb2gray(image)
fig, ax = plt.subplots()
plt.imshow(gray_image, cmap="gray")
~~~
{: .language-python}

We can also load colour images as grayscale directly by
passing the argument `as_gray=True` to `skimage.io.imread()`.

~~~
"""
* Python script to load a color image as grayscale.
"""
import skimage.io
import skimage.color

# read input image, based on filename parameter
image = skimage.io.imread(fname="data/chair.jpg", as_gray=True)

# display grayscale image
fig, ax = plt.subplots()
plt.imshow(image, cmap="gray")
~~~
{: .language-python}

> ## Keeping only low intensity pixels (10 min)
>
> A little earlier, we showed how we could use Python and skimage to turn
> on only the high intensity pixels from an image, while turning all the low
> intensity pixels off.
> Now, you can practice doing the opposite - keeping all
> the low intensity pixels while changing the high intensity ones.
>
> The file `data/sudoku.png` is an RGB image of a sudoku puzzle:
>
> ![Su-Do-Ku puzzle](../data/sudoku.png)
>
> Your task is to turn all of the white pixels in the image to a light gray colour,
> say with the intensity of each formerly white pixel set to 0.75.
> The results should look like this:
>
> ![Modified Su-Do-Ku puzzle](../fig/sudoku-gray.png)
>
> _Hint: this is an instance where it is helpful to convert the image from RGB to grayscale._
>
> > ## Solution
> >
> > First, load the image file in and convert it to grayscale:
> >
> > ~~~
> > import skimage.io
> >
> > image = skimage.io.imread(fname="data/sudoku.png", as_gray=True)
> > ~~~
> > {: .language-python }
> >
> > Then, change all high intensity pixel values (> 0.75) to 0.75:
> >
> > ~~~
> > image[image > 0.75] = 0.75
> > ~~~
> > {: .language-python }
> >
> > Finally, display modified image:
> >
> > ~~~
> > fig, ax = plt.subplots()
> > plt.imshow(image, cmap="gray", vmin=0, vmax=1)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Plotting single channel images (cmap, vmin, vmax)
>
> Compared to a colour image, a grayscale image contains only a single
> intensity value per pixel. When we plot such an image with `plt.imshow`,
> matplotlib uses a colour map, to assign each intensity value a colour.
> The default colour map is called "viridis" and maps low values to purple
> and high values to yellow. We can instruct matplotlib to map low values
> to black and high values to white instead, by calling `plt.imshow` with
> `cmap="gray"`.
> [The documentation contains an overview of pre-defined colour maps](https://matplotlib.org/stable/gallery/color/colormap_reference.html).
>
> Furthermore, matplotlib determines the minimum and maximum values of
> the colour map dynamically from the image, by default. That means, that in
> an image, where the minimum is 0.25 and the maximum is 0.75, those values
> will be mapped to black and white respectively (and not dark gray and light
> gray as you might expect). If there are defined minimum and maximum vales,
> you can specify them via `vmin` and `vmax` to get the desired output.
>
> If you forget about this, it can lead to unexpected results. Try removing
> the `vmax` parameter from the sudoku challenge solution and see what happens.
{: .callout }


## Access via slicing

As noted in the previous lesson skimage images are stored as NumPy arrays,
so we can use array slicing to select rectangular areas of an image.
Then, we can save the selection as a new image, change the pixels in the image,
and so on.
It is important to
remember that coordinates are specified in *(ry, cx)* order and that colour values
are specified in *(r, g, b)* order when doing these manipulations.

Consider this image of a whiteboard, and suppose that we want to create a
sub-image with just the portion that says "odd + even = odd," along with the
red box that is drawn around the words.

![Whiteboard image](../data/board.jpg)

Using the same display technique we have used throughout this course,
we can determine the coordinates of the corners of the area we wish to extract
by hovering the mouse near the points of interest and noting the coordinates.
If we do that, we might settle on a rectangular
area with an upper-left coordinate of *(135, 60)*
and a lower-right coordinate of *(480, 150)*,
as shown in this version of the whiteboard picture:

![Whiteboard coordinates](../fig/board-coordinates.jpg)

Note that the coordinates in the preceding image are specified in *(cx, ry)* order.
Now if our entire whiteboard image is stored as an skimage image named `image`,
we can create a new image of the selected region with a statement like this:

`clip = image[60:151, 135:481, :]`

Our array slicing specifies the range of y-coordinates or rows first, `60:151`,
and then the range of x-coordinates or columns, `135:481`.
Note we go one beyond the maximum value in each dimension,
so that the entire desired area is selected.
The third part of the slice, `:`,
indicates that we want all three colour channels in our new image.

A script to create the subimage would start by loading the image:

~~~
"""
 * Python script demonstrating image modification and creation via
 * NumPy array slicing.
"""
import skimage.io

# load and display original image
image = skimage.io.imread(fname="data/board.jpg")
fig, ax = plt.subplots()
plt.imshow(image)
~~~
{: .language-python}

Then we use array slicing to
create a new image with our selected area and then display the new image.

~~~
# extract, display, and save sub-image
clip = image[60:151, 135:481, :]
fig, ax = plt.subplots()
plt.imshow(clip)
skimage.io.imsave(fname="data/clip.tif", arr=clip)
~~~
{: .language-python}

We can also change the values in an image, as shown next.

~~~
# replace clipped area with sampled color
color = image[330, 90]
image[60:151, 135:481] = color
fig, ax = plt.subplots()
plt.imshow(image)
~~~
{: .language-python}

First, we sample a single pixel's colour at a particular location of the
image, saving it in a variable named `color`,
which creates a 1 × 1 × 3 NumPy array with the blue, green, and red colour values
for the pixel located at *(ry = 330, cx = 90)*.
Then, with the `img[60:151, 135:481] = color` command,
we modify the image in the specified area.
From a NumPy perspective,
this changes all the pixel values within that range to array saved in
the `color` variable.
In this case, the command "erases" that area of the whiteboard,
replacing the words with a beige colour,
as shown in the final image produced by the program:

!["Erased" whiteboard](../fig/board-final.jpg)

> ## Practicing with slices (10 min - optional, not included in timing)
>
> Using the techniques you just learned, write a script that
> creates, displays, and saves a sub-image containing
> only the plant and its roots from "data/maize-root-cluster.jpg"
>
> > ## Solution
> >
> > Here is the completed Python program to select only the plant and roots
> > in the image.
> >
> > ~~~
> > """
> >  * Python script to extract a sub-image containing only the plant and
> >  * roots in an existing image.
> > """
> > import skimage.io
> >
> > # load and display original image
> > image = skimage.io.imread(fname="data/maize-root-cluster.jpg")
> > fig, ax = plt.subplots()
> > plt.imshow(image)
> >
> > # extract, display, and save sub-image
> > # WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:
> > clip = image[0:400, 275:550, :]
> > fig, ax = plt.subplots()
> > plt.imshow(clip)
> >
> >
> > # WRITE YOUR CODE TO SAVE clip HERE
> > skimage.io.imsave(fname="data/clip.jpg", arr=clip)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}
