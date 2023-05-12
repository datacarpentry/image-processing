---
title: Instructor Notes
---

## Estimated Timings

This is a relatively new curriculum.
The estimated timings for each episode are based on limited experience 
and should be taken as a rough guide only.
If you teach the curriculum,
the Maintainers would be delighted to receive feedback with 
information about the time that was required
for teaching and exercises in each episode of your workshop.

Please [open an issue on the repository](https://github.com/datacarpentry/image-processing/issues/new/choose)
to share your experience with the lesson Maintainers.

## Working with Jupyter notebooks

- This lesson is designed to be taught using Jupyter notebooks. We recommend that instructors guide learners to create a new Jupyter notebook for each episode.

- Python `import` statements typically appear in the first code block near the top of each episode. In some cases, the purpose of specific libraries is briefly explained as part of the exercises.

- The possibility of executing the code cells in a notebook in arbitrary order can cause confusion. Using the "restart kernel and run all cells" feature is one way to accomplish linear execution of the notebook and may help locate and identify coding issues.

- Many episodes in this lesson load image files from disk. To avoid name clashes in episodes that load multiple image files, we have used unique variable names (instead of generic names such as `image` or `img`). When copying code snippets between exercises, the variable names may have to be changed. The maintainers are keen to receive feedback on whether this convention proves practical in workshops.

## Working with imageio and skimage

- `imageio.v3` allows to load images in different modes by passing the `mode=` argument to `imread()`. Depending on the image file and mode, the `dtype` of the resulting Numpy array can be different (e.g., `dtype('uint8')` or `dtype('float64')`. In the lesson, `skimage.util.img_as_ubyte()` and `skimage.util.img_as_float()` are used to convert the data type when necessary.

- Some `skimage` functions implicitly convert the pixel values to floating-point numbers. Several callout boxes have been added throughout the lesson to raise awareness, but this may still prompt questions from learners.

- In certain situations, `imread()` returns a read-only array. This depends on the image file type and on the backend (e.g., Pillow). If a read-only error is encountered, `image = np.array(image)` can be used to create a writable copy of the array before manipulating its pixel values.

- Be aware that learners might get surprising results in the *Keeping only low intensity pixels* exercise, if `plt.imshow` is called without the `vmax` parameter.
  A detailed explanation is given in the *Plotting single channel images (cmap, vmin, vmax)* callout box.


## Questions from Learners

### Q: Where would I find out that coordinates are `x,y` not `r,c`?

A: In an image viewer, hover your cursor over top-left (origin) the move down and see which number increases.

### Q: Why does saving the image take such a long time? (skimage-images/saving images PNG example)

A: It is a large image.

### Q: Are the coordinates represented `x,y` or `r,c` in the code (e.g. in `array.shape`)?

A: Always `r,c` with numpy arrays, unless clearly specified otherwise - only represented `x,y` when image is displayed by a viewer.
Take home is don't rely on it - always check!

### Q: What if I want to increase size? How does `skimage` upsample? (image resizing)

A: When resizing or rescaling an image, `skimage` performs interpolation to up-size or down-size the image. Technically, this is done by fitting a [spline](https://en.wikipedia.org/wiki/Spline_\(mathematics\)) function to the image data. The spline function is based on the intensity values in the original image and can be used to approximate the intensity at any given coordinate in the resized/rescaled image. Note that the intensity values in the new image are an approximation of the original values but should not be treated as the actual, observed data. `skimage.transform.resize` has a number of optional parameters that allow the user to control, e.g., the order of the spline interpolation. The [scikit-image documentation](https://scikit-image.org/docs/stable/api/skimage.transform.html#skimage.transform.resize) provides additional information on other parameters.

### Q: Why are some lines missing from the sudoku image when it is displayed inline in a Jupyter Notebook? (skimage-images/low intensity pixels exercise)

A: They are actually present in image but not shown due to interpolation.

### Q: Does blurring take values of pixels already blurred, or is blurring done on original pixel values only?

A: Blurring is done on original pixel values only.

### Q: Can you blur while retaining edges?

A: Yes, many different filters/kernels exist, some of which are designed to be edge-preserving.

## Troubleshooting

Learners reported a problem on some operating systems, that <kbd>Shift</kbd>\+<kbd>Enter</kbd> is prevented from running a cell in Jupyter when the <kbd>caps lock</kbd> key is active.


