---
title: "Connected Component Analysis"
teaching: ??
exercises: ??
questions:
- "How to describe objects in images in terms of numbers."
objectives:
- "Understand the term object in the context of images."
- "Learn about pixel connectivity."
- "Learn how Connected Component Analysis (CCA) works."
- "Use CCA to produce an image that highlights every object in a different color."
- "Characterize each object with numbers that describe its appearance."
keypoints:
- "`skimage.measure.label` is used to generate objects."
- "We use `skimage.measure.regionprops` to measure properties of labelled objects."
- "Color objects according to feature values."
---


## Objects

In the [thresholding episode]() we have covered dividing an image in foreground and background pixels.
In the junk example image, we considered the colored shapes as foreground _objects_ on a white background.

![Original shapes image](../fig/06-junk-before.jpg)

In thresholding we went from the original image to this version:

![Mask created by thresholding](../fig/06-junk-mask.png)

Here, we created a mask that only highlights the parts of the image that we find interesting, the _objects_.
All objects have pixel value of `True` while the background pixels are `False`.

By looking at the mask image, one can count the objects that are present in the image (7).
But how did we actually do that, how did we decide which lump of pixels constitutes a single object?

<!-- TODO: Group exercise: given sheep of paper with grids of 0's and 1's, how to identify which pixels belong to an object, find a rule for each pixel to determine in which object it is  -->

## Pixel Neighborhoods

In order to decide which pixels belong to the same object, one can exploit their neighbourhood:
pixels that are directly next to each other and belong to the foreground class can be considered to belong to the same object.

Let's consider the following mask "image" with 8 rows, and 8 columns.
Note that for brevity, `0` is used to represent `False` (background) and `1` to represent `True` (foreground).

~~~
0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0
0 1 1 0 0 0 0 0
0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0
0 0 0 0 0 0 0 0
~~~
{: .output}

The pixels are organized in a rectangular grid.

<!-- TODO: introduce jumps -->



~~~
2 1 2
1 x 1
2 1 2
~~~
{: .output}

With a single jump connectivity for each pixel, we get two resulting objects, highlighted in the image with `1`'s and `2`'s.

~~~
0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0
0 1 1 0 0 0 0 0
0 0 0 2 2 2 0 0
0 0 0 2 2 2 2 0
0 0 0 0 0 0 0 0
~~~
{: .output}

In the 1-jump version, only pixels that share a side, are considered connected.
With two jumps, however, we only get a single objects, as pixels are also considered connected along the diagonals.

~~~
0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0
0 1 1 0 0 0 0 0
0 0 0 1 1 1 0 0
0 0 0 1 1 1 1 0
0 0 0 0 0 0 0 0
~~~
{: .output}


> ## Exercise: Object counting
>
> How many objects with 1 orthogonal jump, how many with 2 orthogonal jumps?
>
> ~~~
> 0 0 0 0 0 0 0 0
> 0 1 0 0 0 1 1 0
> 0 0 1 0 0 0 0 0
> 0 1 0 1 1 1 0 0
> 0 1 0 1 1 0 0 0
> 0 0 0 0 0 0 0 0
> ~~~
> {: .output}
>
> 1 jump
>
> a) 1
> b) 5
> c) 2
>
> > ## Solution
> > b) 5
> {: .solution}
> 2 jumps
>
> a) 2
> b) 3
> c) 5
>
> > ## Solution
> > a) 2
> {: .solution}
{: .challenge}


> ## Jumps and neighborhoods
>
> We have just introduced how you can reach different neighboring pixels by performing one or more orthogonal jumps.
> There is also a different way of referring to these pixels: the 4- and 8-neighborhood.
> With a single jump you can reach four pixels from a given starting pixel.
> Hence, the one jump neighborhood corresponds to the 4-neighborhood.
> When two orthogonal jumps are allowed, eight pixels can be reached, so this corresponds to the 8-neighborhood.
{: .callout}

<!-- TODO: Callout Detection vs Segmentation -->


## Connected Component Analysis

<!-- TODO: CCA: explain what it does -->
<!-- TODO: describe a straight forward algorithm to find connected components -->
<!-- TODO: CCA Ex1: Connected component analysis of junk image - print out how many pieces of junk in image -->

## Morphometrics - Describe object properties with numbers

<!-- TODO: Morphometrics content -->
<!-- TODO: Morphometrics EX1: use `skimage.measure.regionprops` -->
<!-- TODO: Morphometrics EX2: write your own function that produces a number per object -->
<!-- TODO: produce a plot, e.g. with sizes (not so interesting on that data) -->
<!-- TODO: color-by-feature -->
