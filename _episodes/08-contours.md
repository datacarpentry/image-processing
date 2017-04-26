---
title: "Contours"
teaching: 30
exercises: 0
questions:
- "What are the questions?"
objectives:
- "What are the objectives?"
keypoints:
- "What are the key points?"
---

In this episode, we will learn how to use OpenCV functions to find the 
*contours* of the objects in an image. A countour is a closed curve of points,
representing the boundaries of an object in an image. A single object in an
image may produce several associated contours, which are returned in a 
hierarchial data structure. Once we find the countours of the objects in an 
image, we can do things like determine the number of objects in an image, 
classify the shapes of the objects, or measure the size of the objects. The 
input to the contour-finding process is a binary image, which we will produce
by first applying thresholding and / or edge detection. In the binary image,
the objects we wish to detect should be white, while the background of the 
image should be black.



