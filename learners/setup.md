---
title: Setup
permalink: /setup/
---

Before joining the workshop or following the lesson, please complete the data and software setup described in this page.

## Data

The example images and a description of the Python environment used in this lesson are available on [FigShare](https://figshare.com/).
To download the data, please visit [the dataset page for this workshop][figshare-data]
and click the "Download all" button.
Unzip the downloaded file, and save the contents as a folder called `data` somewhere you will easily find it again,
e.g. your Desktop or a folder you have created for using in this workshop.
(The name `data` is optional but recommended, as this is the name we will use to refer to the folder throughout the lesson.)

## Software

1. Download and install the latest [Miniforge distribution of Python](https://conda-forge.org/download/) for your operating system. 
   ([See more detailed instructions from The Carpentries](https://carpentries.github.io/workshop-template/#python-1).)
   If you already have a Python 3 setup that you are happy with, you can continue to use that (we recommend that you make sure your Python version is current).
   The next step assumes that `conda` is available to manage your Python environment.
2. Set up an environment to work in during the lesson.
   In a terminal (Linux/Mac) or the MiniForge Prompt application (Windows), navigate to the location where you saved the unzipped data for the lesson and run the following command:

   ```bash
   conda env create -f environment.yml
   ```

   If prompted, allow `conda` to install the required libraries.
3. Activate the new environment you just created:

   ```bash
   conda activate dc-image
   ```

   :::::::::::::::::::::::::::::::::::::::::  callout

   ## Enabling the `ipympl` backend in Jupyter notebooks

   The `ipympl` backend can be enabled with the `%matplotlib` Jupyter
   magic. Put the following command in a cell in your notebooks
   (e.g., at the top) and execute the cell before any plotting commands.

   ```python
   %matplotlib widget
   ```

   ::::::::::::::::::::::::::::::::::::::::::::::::::

   :::::::::::::::::::::::::::::::::::::::::  callout

   ## Older JupyterLab versions

   If you are using an older version of JupyterLab, you may also need
   to install the labextensions manually, as explained in the [README
   file](https://github.com/matplotlib/ipympl#readme) for the `ipympl`
   package.


   ::::::::::::::::::::::::::::::::::::::::::::::::::

3. Open a Jupyter notebook:

   ::::::::::::::::  spoiler

   ## Instructions for Linux \& Mac

   Open a terminal and type `jupyter lab`.


   :::::::::::::::::::::::::

   ::::::::::::::::  spoiler

   ## Instructions for Windows

   Launch the Miniforge Prompt program and type `jupyter lab`.
   (Running this command on the standard Command Prompt will return an error:
   `'jupyter' is not recognized as an internal or external command, operable program or batch file.`)


   :::::::::::::::::::::::::

   After Jupyter Lab has launched, click the "Python 3" button under "Notebook" in the launcher window,
   or use the "File" menu, to open a new Python 3 notebook.

4. To test your environment, run the following lines in a cell of the notebook:

   ```python
   import imageio.v3 as iio
   import matplotlib.pyplot as plt
   import skimage as ski

   %matplotlib widget

   # load an image
   image = iio.imread(uri='data/colonies-01.tif')

   # rotate it by 45 degrees
   rotated = ski.transform.rotate(image=image, angle=45)

   # display the original image and its rotated version side by side
   fig, ax = plt.subplots(1, 2)
   ax[0].imshow(image)
   ax[1].imshow(rotated)
   ```

   Upon execution of the cell, a figure with two images should be displayed in an interactive widget. When hovering over the images with the mouse pointer, the pixel coordinates and colour values are displayed below the image.

   ::::::::::::::::  spoiler

   ## Running Cells in a Notebook

   ![](fig/jupyter_overview.png){alt='Overview of the Jupyter Notebook graphical user interface'}
   To run Python code in a Jupyter notebook cell, click on a cell in the notebook
   (or add a new one by clicking the `+` button in the toolbar),
   make sure that the cell type is set to "Code" (check the dropdown in the toolbar),
   and add the Python code in that cell.
   After you have added the code,
   you can run the cell by selecting "Run" -> "Run selected cell" in the top menu,
   or pressing <kbd>Shift</kbd>\+<kbd>Enter</kbd>.


   :::::::::::::::::::::::::

5. A small number of exercises will require you to run commands in a terminal. Windows users should 
use PowerShell for this. PowerShell is probably installed by default but if not you should
[download and install](https://apps.microsoft.com/detail/9MZ1SNWT0N5D?hl=en-eg&gl=EG) it.

[figshare-data]: https://figshare.com/articles/dataset/Data_Carpentry_Image_Processing_Data_beta_/19260677
