---
title: Multi-dimensional data
teaching: 60
exercises: 60
---

::::::::::::::::::::::::::::::::::::::: objectives

- Learn about multi-dimensional image data such as 3D volumetric stacks and time-lapses.
- Visualize multi-dimensional data interactively using Napari.
- Learn to use the basic functionality of the Napari GUI including overlaying masks over images.
- Construct an analysis workflow to measure properties of 3D objects in a 3D volumetric image stack.
- Construct an analysis workflow to measure changes over time from a time-lapse movie.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can we scikit-image to perform image processing tasks on multi-dimensional image data?
- How can we visualise the results using Napari?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- We open access the Napari n-dimensional image viewer with `Napari.Viewer` objects.
- `Image` and `Label` layers can be added to a viewer with `Napari.Viewer.add_image`
  and `Napari.Viewer.add_label` respectively.
- Many scikit-image functions such as `skimage.filters.gaussian`, `ski.threshold.threshold_otsu`,
  `ski.measure.label` and `ski.measure.regionprops` work with 3D image data.
- Iterate through time-points to analyse time-lapse movies.

::::::::::::::::::::::::::::::::::::::::::::::::::
