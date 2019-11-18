---
layout: page
title: Setup
permalink: /setup/
---

## Setup instructions for the Image Processing workshop

1. Download and install the latest [Anaconda distribution](https://www.anaconda.com/distribution/) for your operating system.
   Make sure to choose the Python 3 version (as opposed to the one with Python 2).

2. If you haven't installed git on your system, then you can do so with conda.
   a. In order to check whether git is already available on your system, open the Terminal application and type:

   ~~~
   git --version
   ~~~
   {: .bash}

   If this doesn't produce an output in the form of `git version 2.xx.x`, then install git with the following instructions.
   If git is available already, proceed to step 3.

   b. Git installation: In the Terminal application type in the following command:

   ~~~
   conda install git
   ~~~
   {: .bash}

3. Configure git:
    If you are new to git, you have to configure it:

	a. Start the Terminal application 

	b. Enter the following commands, replacing Jane Smith’s information with your own. Include the 
	quotation marks.

	~~~ 
	git config --global user.name "Jane Smith" 

	git config --global user.email "jane.smith@doane.edu" 

	git config --global core.editor "gedit -s" 
	~~~
	{: .bash}

4. Clone the workshop files: 


	a. If it is not already running, start the Terminal application

	b. Enter the following commands

	~~~
	cd ~/Desktop 

	git clone https://bitbucket.org/mmeysenburg/workshops.git 
	~~~
	{: .bash}

