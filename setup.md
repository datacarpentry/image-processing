---
layout: page
title: Setup
permalink: /setup/
---

Before joining the workshop or following the lesson, please complete the software and data setup described in this page.

## Software

1. Download and install the latest [Anaconda
   distribution](https://www.anaconda.com/distribution/) for your
   operating system. Make sure to choose the Python 3 version (as
   opposed to the one with Python 2).

2. This lesson uses Matplotlib features to display images, and some
   interactive features will be valuable. To enable the interactive
   tools in JupyterLab, the `ipympl` package is required. The package
   can be installed with the command

   ~~~
   conda install -c conda-forge ipympl
   ~~~
   {: .language-shell}

   > ## Enabling the `ipympl` backend in Jupyter notebooks
   >
   > The `ipympl` backend can be enabled with the `%matplotlib` Jupyter
   > magic. Put the following command in a cell in your notebooks
   > (e.g., at the top) and execute the cell before any plotting commands.
   >
   > ~~~
   > %matplotlib widget
   > ~~~
   > {: .language-python}
   {: .callout}

   > ## Older JupyterLab versions
   >
   > If you are using an older version of JupyterLab, you may also need
   > to install the labextensions manually, as explained in the [README
   > file](https://github.com/matplotlib/ipympl#readme) for the `ipympl`
   > package.
   {: .callout}

   To test your environment, open a Jupyter notebook and copy the following lines into a cell:
   ~~~
   import skimage.io
   import matplotlib.pyplot as plt
   %matplotlib widget
   
   # load an image
   image = skimage.io.imread(fname='fig/00-colonies01.jpg')
   
   # display the image
   fig, ax = plt.subplots()
   plt.imshow(image, cmap='gray')
   plt.show()
   ~~~
   {: .language-python}
   Upon execution of the cell, an image should be displayed in an interactive widget. When hovering over the image with the mouse pointer, the pixel coordinates and color values are displayed below the image.

3. The example image files are available through Figshare. Learners
   can download the images from [FIXME
   figshare](https://figshare.com/). We recommend to create a
   directory for the Jupyter notebooks/code created during the
   lesson. The images should be located in a subfolder named `images/`.


## Data

The example images used in this lesson are available on [FigShare](https://figshare.com/).
To download the data, please visit [the dataset page for this workshop][figshare-data]
and click the "Download all" button.
Unzip the downloaded file, and save the contents as a folder somewhere you will easily find it again,
e.g. your Desktop or a folder you have created for using in this workshop.

[figshare-data]: https://figshare.com/articles/dataset/Data_Carpentry_Image_Processing_Data_beta_/19260677
