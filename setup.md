---
layout: page
title: Setup
permalink: /setup/
---

Before joining the workshop or following the lesson, please complete the data and software setup described in this page.


## Data

The example images used in this lesson are available on [FigShare](https://figshare.com/).
To download the data, please visit [the dataset page for this workshop][figshare-data]
and click the "Download all" button.
Unzip the downloaded file, and save the contents as a folder  called `data` somewhere you will easily find it again,
e.g. your Desktop or a folder you have created for using in this workshop.
(The name `data` is optional but recommended, as this is the name we will use to refer to the folder throughout the lesson.)

[figshare-data]: https://figshare.com/articles/dataset/Data_Carpentry_Image_Processing_Data_beta_/19260677


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

3. Open a Jupyter notebook:

   > ## Instructions for Linux & Mac
   >
   > Open a terminal and type `jupyter lab`.
   {: .solution }

   > ## Instructions for Windows
   >
   > Launch the Anaconda Prompt program and type `jupyter lab`.
   > (Running this command on the standard Command Prompt will return an error:
   > `'conda' is not recognized as an internal or external command, operable program or batch file.`)
   {: .solution }

   After Jupyter Lab has launched, click the "Python 3" button under "Notebook" in the launcher window,
   or use the "File" menu, to open a new Python 3 notebook.

4. To test your environment, run the following lines in a cell of the notebook:
   ~~~
   import skimage.io
   import matplotlib.pyplot as plt
   %matplotlib widget

   # load an image
   image = skimage.io.imread(fname='data/colonies-01.tif')

   # display the image
   fig, ax = plt.subplots()
   plt.imshow(image, cmap='gray')
   plt.show()
   ~~~
   {: .language-python}
   Upon execution of the cell, an image should be displayed in an interactive widget. When hovering over the image with the mouse pointer, the pixel coordinates and color values are displayed below the image.

   > ## Running Cells in a Notebook
   >
   >
   > ![Overview of the Jupyter Notebook graphical user interface]({{ page.root }}{% link fig/jupyter_overview.png %})
   > To run Python code in a Jupyter notebook cell, click on a cell in the notebook
   > (or add a new one by clicking the `+` button in the toolbar),
   > make sure that the cell type is set to "Code" (check the dropdown in the toolbar),
   > and add the Python code in that cell.
   > After you have added the code,
   > you can run the cell by selecting "Run" -> "Run selected cell" in the top menu,
   > or pressing <kbd>Shift</kbd>+<kbd>Enter</kbd>.
   {: .solution }
