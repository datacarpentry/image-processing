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

## On Objects

<!-- TODO: write a few sentences on objects in real live vs objects in images. -->
<!-- TODO: start off with thresholding exercise -->
<!-- TODO: Group exercise: given sheep of paper with grids of 0's and 1's, how to identify which pixels belong to an object, find a rule for each pixel to determine in which object it is  -->

## Pixel Neighborhoods

<!-- TODO: code fragments with 1's, 0's to explain neighborhood -->
<!-- TODO: multiple choice question about neighborhood -->
<!-- TODO: Callout 1, 2 jumps, 4-8 neighborhoor -->
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
