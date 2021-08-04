---
title: "Instructor Notes"
---

## Image Basics

* [Presentation slides](../files/01-image-basics/01-image-basics.pdf)

## Blurring

* Take care to avoid mixing up the term "edge" to describe the edges of objects
  _within_ an image and the outer boundaries of the images themselves. Lack of a clear distinction here may be confusing for learners.

## Questions from Learners

### Q: Where would I find out that coordinates are `x,y` not `r,c`?
A: In an image viewer, hover your cursor over top-left (origin) the move down and see which number increases.

### Q: Why does saving the image take such a long time? (skimage-images/saving images PNG example)
A: It is a large image.

### Q: Are the coordinates represented `x,y` or `r,c` in the code (e.g. in `array.shape`)?
A: Always `r,c` with numpy arrays, unless clearly specified otherwise - only represented `x,y` when image is displayed by a viewer. 
Take home is don’t rely on it - always check!

### Q: What if I want to increase size? How does `skimage` upsample? (image resizing)
FIXME

### Q: Why are some lines missing from the sudoku image when it is displayed inline in a Jupyter Notebook? (skimage-images/low intensity pixels exercise) 
A: They are actually present in image but not shown due to interpolation.

### Q: Does blurring take values of pixels already blurred, or is blurring done on original pixel values only?
A: Blurring is done on original pixel values only.

### Q: Can you blur while retaining edges?
A: Yes, many different filters/kernels exist, some of which are designed to be edge-preserving.
