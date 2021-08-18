---
title: Discussion
---

## Choice of Image Processing Library

This lesson was originally written to use [OpenCV](https://opencv.org/) and the [`opencv-`](https://pypi.org/project/opencv-python/) library.
([See the last version of the lesson repository to use OpenCV](https://github.com/datacarpentry/image-processing/tree/770a2416fb5c6bd5a4b8e728b3e338667e47b0ed).)
In 2019-2020 the lesson was adapted to use [scikit-image](https://scikit-image.org/),
as this library has proven easier to install, and enjoys more extensive
documentation and support.

## Choice of Image Viewer

When the lesson was first adapted to use sckikit-image (see above),
`skimage.viewer.ImageViewer` was used to inspect images. [This viewer is deprecated](https://scikit-image.org/docs/dev/user_guide/viewer.html)
and the lesson developers chose to use the interactive inline
viewer provided by the Jupyter interface, using `matplotlib.pyplot.imshow`
and [the `% matplotlib notebook` magic]().

The developers discussed the possibility of using [napari](https://napari.org/)
as an image viewer in the lesson, acknowledging its growing popularity and
some of the advantages it holds over the `matplotlib`-based approach, especially
for working with image data in more than two dimensions.
However, at the time of discussion, napari was still in an alpha state of development,
and could not be relied on for easy and error-free installation on all operating systems,
which makes it less well-suited to use in an official Data Carpentry curriculum.

The lesson Maintainers and/or Curriculum Advisory Committee (when it exists)
will monitor the progress of napari, and other image viewers, and may opt to adopt
a new platform in future.
