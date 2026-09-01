---
title: Discussion
---

## Choice of Image Processing Library

This lesson was originally designed to use [OpenCV](https://opencv.org/)
and the [`opencv-python`](https://pypi.org/project/opencv-python/)
library ([see the last version of the lesson repository to use
OpenCV](https://github.com/datacarpentry/image-processing/tree/770a2416fb5c6bd5a4b8e728b3e338667e47b0ed)).

In 2019-2020 the lesson was adapted to use
[scikit-image](https://scikit-image.org/), as this library has proven
easier to install and enjoys more extensive documentation and support.

## Choice of Image Viewer

When the lesson was first adapted to use sckikit-image (see above),
`skimage.viewer.ImageViewer` was used to inspect images. [This viewer
is deprecated](https://scikit-image.org/docs/stable/user_guide/visualization.html)
and the lesson maintainers chose to leverage `matplotlib.pyplot.imshow`
with the pan/zoom and mouse-location tools built into the [Matplotlib
GUI](https://matplotlib.org/stable/users/interactive.html). The
[`ipympl` package](https://github.com/matplotlib/ipympl) is required
to enable the interactive features of Matplotlib in Jupyter notebooks
and in Jupyter Lab. This package is included in the setup
instructions, and the backend can be enabled using the `%matplotlib widget` magic.

The maintainers discussed the possibility of using [napari](https://napari.org/)
as an image viewer in the lesson, acknowledging its growing popularity
and some of the advantages it holds over the Matplotlib-based
approach, especially for working with image data in more than two
dimensions.  However, at the time of discussion, napari was still in
an alpha state of development, and could not be relied on for easy and
error-free installation on all operating systems, which makes it less
well-suited to use in an official Data Carpentry curriculum.

The lesson Maintainers and/or Curriculum Advisory Committee (when it
exists) will monitor the progress of napari and other image viewers,
and may opt to adopt a new platform in future.
