---
title: "Introduction"
teaching: 5
exercises: 0
questions:
- "What sort of scientific questions can we answer with image processing /
computer vision?"
- "What are morphometric problems?"
objectives:
- "Recognize scientific questions that could be solved with image processing
 / computer vision."
- "Recognize morphometric problems (those dealing with the number, size, or
shape of the objects in an image)."
keypoints:
- "Simple Python and skimage (scikit-image) techniques can be used to solve genuine
image analysis problems."
- "Morphometric problems involve the number, shape, and / or size of the
objects in an image."
---

We can use relatively simple image processing and computer vision techniques in
Python, using [the skimage library](https://scikit-image.org/).
With careful experimental design, a digital camera or a flatbed scanner,
in conjunction with some Python code,
can be a powerful instrument in answering many different kinds of problems.
Consider the following problem that might be of interest to a scientist.

## Morphometrics

Morphometrics involves counting the number of objects in an image,
analyzing the size of the objects,
or analyzing the shape of the objects.
For example, we might be interested in automatically counting
the number of bacterial colonies growing in a Petri dish,
as shown in this image:

![Bacteria colony](../fig/colonies-01.jpg)

We could use image processing to find the colonies, count them,
and then highlight their locations on the original image,
resulting in an image like this:

![Colonies counted](../fig/colony-mask.png)

> ## Why write a program to do that?
>
> Note that you can easily manually count the number of bacteria colonies
> shown in the morphometric example above.
> Why should we learn how to write a Python program to do a task
> we could easily perform with our own eyes?
> There are at least two reasons to learn how to perform tasks like these
> with Python and skimage:
>
> 1. What if there are many more bacteria colonies in the Petri dish?
>   For example, suppose the image looked like this:
>
> 	![Bacteria colony](../fig/colonies-03.jpg)
>
> 	Manually counting the colonies in that image would present more of a challenge.
>   A Python program using skimage could count the number of colonies more accurately,
>   and much more quickly, than a human could.
>
> 2. What if you have hundreds, or thousands, of images to consider?
>   Imagine having to manually count colonies on several thousand images
>   like those above.
>   A Python program using skimage could move through all of the images in seconds;
>   how long would a graduate student require to do the task?
>   Which process would be more accurate and repeatable?
>
> As you can see, the simple image processing / computer vision techniques you
> will learn during this workshop can be very valuable tools for scientific
> research.
{: .callout}

As we move through this workshop,
we will learn image analysis methods useful for many different scientific problems.
These will be linked together and applied to a real problem in
the final end-of-workshop [capstone challenge]({{page.root}}{% link _episodes/09-challenges.md %}).

Let's get started,
by learning some basics about how images are represented and stored digitally.
