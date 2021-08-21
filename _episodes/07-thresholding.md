---
title: "Thresholding"
teaching: 60
exercises: 50
questions:
- "How can we use thresholding to produce a binary image?"
objectives:
- "Explain what thresholding is and how it can be used."
- "Use histograms to determine appropriate threshold values to use for the
thresholding process."
- "Apply simple, fixed-level binary thresholding to an image."
- "Explain the difference between using the operator `>` or the operator `<` to
threshold an image represented by a numpy array."
- "Describe the shape of a binary image produced by thresholding via `>` or `<`."
- "Explain when Otsu's method of adaptive thresholding is appropriate."
- "Apply adaptive thresholding to an image using Otsu's method."
- "Use the `np.nonzero()` function to count the number of non-zero pixels
in an image."
keypoints:
- "Thresholding produces a binary image, where all pixels with intensities
above (or below) a threshold value are turned on, while all other pixels are
turned off."
- "The binary images produced by thresholding are held in two-dimensional NumPy
arrays, since they have only one color value channel. They are boolean, hence they contain
the values 0 (off) and 1 (on)."
- "Thresholding can be used to create masks that select only the interesting
parts of an image, or as the first step before
[Edge Detection]({{ page.root }}/08-edge-detection/) or finding
[Contours]({{ page.root }}/09-contours/)."
---

In this episode, we will learn how to use skimage functions to apply
thresholding to an image. Thresholding is a type of *image segmentation*,
where we change the pixels of an image to make the image easier to
analyze. In thresholding, we convert an image from color or grayscale into a
*binary image*, i.e., one that is simply black and white. Most frequently, we
use thresholding as a way to select areas of interest of an image, while
ignoring the parts we are not concerned with. We have already done some simple
thresholding, in the "Manipulating pixels" section of the
[Skimage Images]({{ page.root }}/03-skimage-images/) episode. In that case, we
used a simple NumPy array manipulation to separate the pixels belonging to the
root system of a plant from the black background. In this episode, we will
learn how to use skimage functions to perform thresholding. Then, we will use the
masks returned by these functions to select the parts of an image we are
interested in.

## Simple thresholding

Consider this image, with a series of crudely cut shapes set against a white
background. The black outline around the image is not part of the image.

![Original shapes image](../fig/06-junk-before.jpg)

Now suppose we want to select only the shapes from the image. In other words,
we want to leave the pixels belonging to the shapes "on," while turning the
rest of the pixels "off," by setting their color channel values to zeros. The

skimage library has several different methods of thresholding. We will start
with the simplest version, which involves an important step of human
input. Specifically, in this simple, *fixed-level thresholding*, we have to
provide a threshold value `t`.

The process works like this. First, we will load the original image and convert
it to grayscale.

~~~
import numpy as np
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters

# load the image
image = skimage.io.imread("../../fig/06-junk-before.jpg")

# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)
~~~
{: .language-python}

Next, we would like to apply the threshold `t`, a number in the closed range [0.0, 1.0]. Pixels with color values on one  side of `t` will be turned "on," while pixels with color values on the other side will be turned "off." To use this process, we first have to determine a "good" value for `t`. How might we do that? One way is to look at the grayscale histogram of the image and try to identify what grayscale ranges correspond to the shapes in the image or the background.

The histogram for the shapes image shown above can be produced as in the [Creating Histograms]({{ page.root }}/05-creating-histograms/) episode.

~~~
# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(gray_image, bins=256, range=(0.0, 1.0))

plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()
~~~
{: .language-python}

![Grayscale histogram](../fig/06-junk-histogram.png)

Since the image has a white background, most of the pixels in the image are white. This corresponds nicely to what we see in the histogram: there is a peak near the value of 1.0. If we want to select the shapes and not the background, we want to turn off the white background pixels, while leaving the pixels for the shapes turned on. So, we should choose a value of `t` somewhere before the large peak and turn pixels above that value "off". Let us choose `t=0.8`.

To apply the threshold `t`, we can use the numpy comparison operators to create a mask. Here, we want to turn "on" all pixels which have values smaller than the threshold, so we use the less operator `<` to compare the `blurred_image` to the threshold `t`. The operator returns a mask, that we capture in the variable `binary_mask`. It has only one channel, and each of its values is either 0 or 1. The binary mask created by the thresholding operation can be shown with `skimage.io.imshow`.

~~~
# create a mask based on the threshold
t = 0.8
binary_mask = blurred_image < t
skimage.io.imshow(binary_mask)
plt.show()
~~~
{: .language-python}

![Mask created by thresholding](../fig/06-junk-mask.png)

You can see that the areas where the shapes were in the original area are now white, while the rest of the mask image is black.

We can now apply the `binary_mask` to the original colored image as we have learned in the [Drawing and Bitwise Operations]({{ page.root}}/04-drawing/) episode. What we are left with is only the colored shapes from the original.

~~~
# use the binary_mask to select the "interesting" part of the image
selection = np.zeros_like(image)
selection[binary_mask] = image[binary_mask]

skimage.io.imshow(selection)
plt.show()
~~~
{: .language-python}

![Selected shapes](../fig/06-junk-selected.png)

> ## More practice with simple thresholding (15 min)
>
> Now, it is your turn to practice. Suppose we want to use simple thresholding
> to select only the colored shapes from this image:
>
> ![more-junk.jpg](../fig/06-more-junk.jpg)
> 
> First, plot the grayscale histogram as in **Desktop/workshops/image-processing05-creating-histograms** and examine the distribution of grayscale values in the image. What do you think would be a good value for the threshold `t`?
> 
> > ## Solution
> > 
> > The histogram for the **more-junk.jpg** image can be shown with
> >
> > ~~~
> > import numpy as np
> > import matplotlib.pyplot as plt
> > import skimage.color
> > import skimage.filters
> > import skimage.io
> >
> > image = skimage.io.imread("../../fig/06-more-junk.jpg", as_gray=True)
> > histogram, bin_edges = np.histogram(image, bins=256, range=(0.0, 1.0))
> >
> > plt.plot(bin_edges[0:-1], histogram)
> > plt.title("Graylevel histogram")
> > plt.xlabel("gray value")
> > plt.ylabel("pixel count")
> > plt.xlim(0, 1.0)
> > plt.show()
> > ~~~
> > {: .language-python}
> >
> > ![Grayscale histogram of more-junk.jpg](../fig/06-more-junk-histogram.png)
> >
> > We can see a large spike around 0.3, and a smaller spike around 0.7. The
> > spike near 0.3 represents the darker background, so it seems like a value
> > close to `t=0.5` would be a good choice.
> {: .solution}
>
> Next, create a mask to turn the pixels above the threshold `t` on and pixels below the threshold `t` off. Note that unlike the image with a white background we used above, here the peak for the background color is at a lower gray level than the shapes. Therefore, change the comparison operator less `<` to greater `>` to create the appropriate mask. Then apply the mask to the image and view the thresholded image. If everything works as it should, your output should show inly the colored shapes on a black background.
>
> > ## Solution
> >
> > Here are the commands to create and view the binary mask
> > ~~~
> > t = 0.5
> > binary_mask = image < t
> > skimage.io.imshow(binary_mask)
> > plt.show()
> > ~~~
> > {: .language-python}
> > 
> > ![more-junk.jpg thresholding mask](../fig/06-more-junk-mask.png)
> > 
> > And here are the commands to apply the mask and view the thresholded image
> > ~~~
> > selection = np.zeros_like(image)
> > selection[binary_mask] = image[binary_mask]
> > skimage.io.imshow(selection)
> > plt.show()
> > ~~~
> > {: .language-python}
> >
> > ![more-junk.jpg selected shapes](../fig/06-more-junk-selected.png)
> >
> {: .solution}
{: .challenge}

## Adaptive thresholding

The downside of the simple thresholding technique is that we have to make an educated guess about the threshold `t` by inspecting the histogram. There are also *adaptive thresholding* methods that can determine the threshold automatically for us. One such method is *[Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method)*. It is particularly useful for situations where the grayscale histogram of an image has two peaks that correspond to background and objects of interest.

> ## Denoising an image before thresholding
> In practice, it is often necessary to denoise the image before thresholding, which can be done with one of the methods from the [Blurring]({{ page.root }}/06-blurring/) episode.
{: .callout}

Consider this image of a maize root system which we have seen before in the [Skimage Images]({{ page.root }}/03-skimage-images/) episode.

![Maize root system](../fig/06-roots-original.jpg)

We use Gaussian blur with a sigma of 1.0 to denoise the root image. Let us look at the grayscale histogram of the denoised image.

~~~
image = skimage.io.imread("../../fig/06-roots-original.jpg")

# convert the image to grayscale
gray_image = skimage.color.rgb2gray(image)

# blur the image to denoise
sigma = 1.0
blurred_image = skimage.filter.gaussian(gray_image, sigma=sigma)

# show the histogram of the blurred image
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
plt.plot(bin_edges[0:-1], histogram)
plt.title("Graylevel histogram")
plt.xlabel("gray value")
plt.ylabel("pixel count")
plt.xlim(0, 1.0)
plt.show()
~~~
{: .language-python}

![Maize root histogram](../fig/06-roots-histogram.png)

The histogram has a significant peak around 0.2, and a second, smaller peak very near 1.0. Thus, this image is a good candidate for thresholding with Otsu's method. The mathematical details of how this work are complicated (see the [skimage documentation](https://scikit-image.org/docs/dev/api/skimage.filters.html#threshold-otsu) if you are interested), but the outcome is that Otsu's method finds a threshold value between the two peaks of a grayscale histogram.

The `skimage.filters.threshold_otsu()` function can be used to determine the adaptive threshold via Otsu's method. Then numpy comparison operators can be used to apply it as before. Here are the Python commands to determine the threshold `t` with Otsu's method.
~~~
# perform adaptive thresholding
t = skimage.filters.threshold_otsu(blurred_image)
print (t)
~~~
{: .language-python}

For this root image and a Gaussian blur with the chosen sigma of 1.0, the computed threshold value is 0.42. No we can create a binary mask with the comparison operator `>`. As we have seen before, pixels above the threshold value will be turned on, those below the threshold will be turned off.

~~~
# create a binary mask with the threshold found by Otsu's method
binary_mask = blurred_image > t
skimage.io.imshow(binary_mask)
plt.show()
~~~
{: .language-python}

![Root system mask](../fig/06-roots-mask.png)

Finally, we use the mask to select the foreground:

~~~
# apply the binary mask to select the foreground
selection = np.zeros_like(image)
selection[binary_mask] = image[binary_mask]

skimage.io.imshow(selection)
plt.show()
~~~
{: .language-python}

![Masked root system](../fig/06-roots-selected.png)

## Application: measuring root mass

Let us now turn to an application where we can apply thresholding and other
techniques we have learned to this point. Consider these four maize root
system images.

![Four root images](../fig/07-four-maize-roots.jpg)

Suppose we are interested in the amount of plant material in each image, and in particular how that amount changes from image to image. Perhaps the images represent the growth of the plant over time, or perhaps the images show four different maize varieties at the same phase of their growth. The question we would like to answer is, "how much root mass is in each image?"

We will first construct a Python program to measure this value for a single image. Our strategy will be this:

1. Read the image, converting it to grayscale as it is read. For this application we do not need the color image.
2. Blur the image.
3. Use Otsu's method of thresholding to create a binary image, where the pixels
that were part of the maize plant are white, and everything else is black.
4. Save the binary image so it can be examined later.
5. Count the white pixels in the binary image, and divide by the number of
pixels in the image. This ratio will be a measure of the root mass of the
plant in the image.
6. Output the name of the image processed and the root mass ratio.

Our intent is to perform these steps and produce the numeric result -- a measure of the root mass in the image -- without human intervention. Implementing the steps within a Python function will enable us to call this function for different images.

Here is a Python function that implements this root-mass-measuring strategy. Since the function is intended to produce numeric output without human interaction, it does not display any of the images. Almost all of the commands should be familiar, and in fact, it may seem simpler than the code we have worked on thus far, because we are not displaying any of the images.

~~~
import numpy as np
import skimage.io
import skimage.filters

def measure_root_mass(filename, sigma=1.0):

    # read the original image, converting to grayscale on the fly
    image = skimage.io.imread(fname=filename, as_gray=True)

    # blur before thresholding
    blurred_image = skimage.filters.gaussian(image, sigma=sigma)

    # perform adaptive thresholding to produce a binary image
    t = skimage.filters.threshold_otsu(blurred_image)
    binary_mask = blurred_image > t

    # determine root mass ratio
    rootPixels = np.count_nonzero(binary_mask)
    w = binary_mask.shape[1]
    h = binary_mask.shape[0]
    density = rootPixels / (w * h)

    return density
~~~
{: .language-python}

The function begins with reading the orignal image from the file `filename`. We use `skimage.io.imread` with the optional argument `as_gray=True` to automatically convert it to grayscale. Next, the grayscale image is blurred with a Gaussian filter with the value of `sigma` that is passed to the function. Then we determine the threshold `t` with Otsu's method and create a binary mask just as we did in the previous section. Up to this point, everything should be familiar.

The final part of the function determines the root mass ratio in the image. Recall that in the `binary_mask`, every pixel has either a value of zero (black/background) or one (white/foreground). We want to count the number of white pixels, which can be accomplished with a call to the numpy function `np.count_nonzero`. Then we determine the width and height of the image by using the the elements of `binary_mask.shape` (that is, the dimensions of the numpy array that stores the image). Finally, the density ratio is calculated by dividing the number of white pixles by the total number of pixels `w*h` in the image. The function returns then root density of the image.

We can call this function with any filename and provide a sigma value for the blurring. If no sigma value is provided, the default value 1.0 will be used. For example, for the file **trial-016.jpg** and a sigma value of 1.5, we would call the function like this:

~~~
measure_root_mass("trial-016.jpg", sigma=1.5)
~~~
{: .language-python}

The output for this particular file should be
~~~
0.0482436835106383`
~~~
{: .output}

Now we can use the function to process the series of four images shown above. In a real-world scientific situation, there might be dozens, hundreds, or even thousands of images to process. To save us the tedium of calling the function for each image by hand, we can write a loop that processes all files automatically. The following code block assumes that the files are located in the same directory and the filenames all start with the **trial-** prefix and end with the **.jpg** suffix.

~~~
import glob
all_files = glob.glob("trial-*.jpg")
for filename in all_files:
    density = measure_root_mass(filename, sigma=1.5)
    # output in format suitable for .csv
    print(filename, density, sep=",")
~~~
{: .language-python}

When executed, the loop should produce the output
~~~
trial-016.jpg,0.0482436835106383
trial-020.jpg,0.06346941489361702
trial-216.jpg,0.14073969414893617
trial-293.jpg,0.13607895611702128
~~~
{: .output}

> ## Ignoring more of the images -- brainstorming (10 min)
>
> Let us take a closer look at the binary masks produced by the `measure_root_mass` function.
> 
> ![Binary root images](../fig/07-four-maize-roots-binary.jpg)
> 
> You may have noticed in the section on adaptive thresholding that the thresholded image does include regions of the image aside of the plant root: the numbered labels and the white circles in each image are preserved during the thresholding, because their grayscale values are above the threshold. Therefore, our calculated root mass ratios include the white pixels of the label and white circle that are not part of the plant root. Those extra pixels affect how accurate the root mass calculation is!
>
> How might we remove the labels and circles before calculating the ratio, so that our results are more accurate? Think about some options given what we have learned so far.
>
> > ## Solution
> >
> > One approach we might take is to try to completely mask out a region from
> > each image, particularly, the area containing the white circle and the
> > numbered label. If we had coordinates for a rectangular area on the image
> > that contained the circle and the label, we could mask the area out easily
> > by using techniques we learned in the
> > [Drawing and Bitwise Operations]({{ page.root }}/04-drawing/)
> > episode.
> >
> > However, a closer inspection of the binary images raises some issues with
> > that approach. Since the roots are not always constrained to a certain area
> > in the image, and since the circles and labels are in different locations
> > each time, we would have difficulties coming up with a single rectangle
> > that would work for *every* image. We could create a different masking
> > rectangle for each image, but that is not a practicable approach if we have
> > hundreds or thousands of images to process.
> >
> > Another approach we could take is to apply two thresholding steps to the
> > image. Look at the graylevel histogram of the file `trial-016.jpg` shown
> > above again: Notice the peak near 1.0? Recall that a grayscale value of
> > 1.0 corresponds to white pixels: the peak corresponds to the white label
> > and circle. So, we could use simple binary thresholding to mask the white
> > circle and label from the image, and then we could use Otsu's method to
> > select the pixels in the plant portion of the image.
> >
> > Note that most of this extra work in processing the image could have been
> > avoided during the experimental design stage, with some careful consideration
> > of how the resulting images would be used. For example, all of the following
> > measures could have made the images easier to process, by helping us
> > predict and/or detect where the label is in the image and subsequently
> > mask it from further processing:
> >
> > * Using labels with a consistent size and shape
> > * Placing all the labels in the same position, relative to the sample
> > * Using a non-white label, with non-black writing
> >
> {: .solution}
{: .challenge}

> ## Ignoring more of the images -- implementation (30 min - optional, not included in timing)
>
> Implement an enhanced version of the function `measure_root_mass` that applies simple binary thresholding to remove the white circle and label from the image before applying Otsu's method.
> 
> > ## Solution 
> > 
> > We can apply a simple binary thresholding with a threshold `t=0.95` to remove the label and circle from the image. We use the binary mask to set the pixels in the blurred image to zero (black).
> >
> > ~~~
> > def enhanced_root_mass(filename, sigma):
> >
> >     # read the original image, converting to grayscale on the fly
> >     image = skimage.io.imread(fname=filename, as_gray=True)
> >
> >     # blur before thresholding
> >     blurred_image = skimage.filters.gaussian(image, sigma=sigma)
> >
> >     # perform inverse binary thresholding to mask the white label and circle
> >     binary_mask = blurred_image > 0.95
> >     # use the mask to remove the circle and label from the blurred image
> >     blurred_image[binary_mask] = 0
> >
> >     # perform adaptive thresholding to produce a binary image
> >     t = skimage.filters.threshold_otsu(blurred_image)
> >     binary_mask = blurred_image > t
> >
> >     # determine root mass ratio
> >     rootPixels = np.count_nonzero(binary_mask)
> >     w = binary_mask.shape[1]
> >     h = binary_mask.shape[0]
> >     density = rootPixels / (w * h)
> >
> >     return density
> >
> > all_files = glob.glob("trial-*.jpg")
> > for filename in all_files:
> >     density = enhanced_root_mass(filename, sigma=1.5)
> >     # output in format suitable for .csv
> >     print(filename, density, sep=",")
> > ~~~
> > {: .language-python}
> > 
> > Here are the binary images produced by this program. Note that we have not completely
> > removed the offending white pixels. Outlines still remain. However, we have
> > reduced the number of extraneous pixels, which should make the output more
> > accurate.
> >
> > ![Improved binary root images](../fig/07-four-maize-roots-binary-improved.jpg)
> >
> > The output of the improved program does illustrate that the white circles
> > and labels were skewing our root mass ratios:
> >
> > ~~~
> > trial-016.jpg,0.045935837765957444
> > trial-020.jpg,0.058800033244680854
> > trial-216.jpg,0.13705003324468085
> > trial-293.jpg,0.13164461436170213
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Thresholding a bacteria colony image (15 min)
>
> In the **../code/10-challenges/morphometrics/** directory, you will find an image named **colonies01.tif**.
>
> ![Bacteria colonies](../code/10-challenges/morphometrics/colonies01.png)
>
> This is one of the images you will be working with in the morphometric challenge at the end of the workshop.
> 1. Plot and inspect the grayscale histogram of the image to determine a good threshold value for the image.
> 2. Create a binary mask that leaves the pixels in the bacteria colonies "on" while turning the rest of the pixels in the image "off".
> 
> > ## Solution
> > Here is the code to create the grayscale histogram:
> > ~~~
> > import numpy as np
> > import matplotlib.pyplot as plt
> > import skimage.io
> > import skimage.filters
> >
> > image = skimage.io.imread("../code/10-challenges/morphometrics/colonies01.tif")
> > gray_image = skimage.color.rgb2gray(image)
> > blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
> >
> > histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
> > plt.plot(bin_edges[0:-1], histogram)
> > plt.title("Graylevel histogram")
> > plt.xlabel("gray value")
> > plt.ylabel("pixel count")
> > plt.xlim(0, 1.0)
> > plt.show()
> > ~~~
> > {: .language-python}
> >
> > ![Colonies grayscale histogram](../fig/07-colonies-histogram.png)
> >
> > The peak near one corresponds to the white image background, and the broader peak around 0.5 corresponds to the yellow/brown culture medium in the dish. The small peak near zero is what we are after: the dark bacteria colonies. A reasonable choice thus might be to leave pixels below `t=0.2` on.
> >
> > Here is the code to create and show the binarized image using the `<` operator with a threshold `t=0.2`:
> > ~~~
> > t = 0.2
> > binary_mask = blurred_image < t
> > skimage.io.imshow(binary_mask)
> > plt.show()
> > ~~~
> > {: .language-python}
> >
> > ![Colonies binary mask](../fig/07-colonies-mask.png)
> >
> > When you play around with the threshold a bit, you can see that in particular the size of the bacteria colony near the edge of the dish in the top right is affected by the choice of the threshold.
> {: .solution}
{: .challenge}
