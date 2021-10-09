---
layout: page
title: Setup
permalink: /setup/
---

## Setup instructions for the Image Processing workshop

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
   > {: .language-shell}
   {: .callout}

   > ## Older JupyterLab versions
   >
   > If you are using an older version of JupyterLab, you may also need
   > to install the labextensions manually, as explained in the [README
   > file](https://github.com/matplotlib/ipympl#readme) for the `ipympl`
   > package.
   {: .callout}

3. The example image files are available through Figshare. Learners
   can download the images from [FIXME
   figshare](https://figshare.com/). We recommend to create a
   directory for the Jupyter notebooks/code created during the
   lesson. The images should be located in a subfolder named `images/`.
