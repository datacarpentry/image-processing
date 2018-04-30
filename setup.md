---
layout: page
title: Setup
permalink: /setup/
---

## Setup instructions for the Image Processing workshop

We are using a virtual Linux machine (VM) for this workshop, since the computer vision
libraries we use can be difficult to install and configure. This allows you to run our 
"standard" computer, regardless of your specific Windows, Mac, or Linux computer. The 
files need to set up the VM are on a thumb drive, or can be downloaded from the Web 
(although the download will take a very long time). To set up the VM, follow these 
instructions.


> ## Virtual machine details
> 
> * Virtualization software: Oracle VirtualBox.
> 
> * VM operating system: 64-bit Ubuntu 16.04. 
> 
> * Login information: The machine is set to automatically log in to a user 
> account. If needed, the username is **diva** and the associated password 
> is **Diva2018**.
> 
> * Software suite: The machine is pre-configured with the following software:
> 
> | Software                    | Description                                           |
> | :-------------------------- | :-----------------------------------------------------|
> | gcc                         | C / C++ compiler                                      |
> | git                         | Source control and versioning tool                    |
> | gnuplot                     |  plotting and graphing application                    |
> | ImageJ                      | Java-based image processing application               |
> | Open JDK 1.8.0              | Java development kit                                  |
> | Python 3.6.3                | Anaconda 5.0.1 Python distribution                    |
> |                             | - includes numpy, scipy, matplotlib, and scikit-learn |
> |                             | - OpenCV 3.1.0                                        |
> |                             | - mahotas                                             |
> |                             | - Adrian Rosebrock's imutils library                  |
{: .discussion}

## Installation

1. Install VirtualBox: Mount the thumb drive, and then run one of the two VirtualBox 
installation programs, depending on what kind of computer you have:

	a. Windows: run VirtualBox-5.2.10-122406-Win.exe 

	b. Mac: run VirtualBox-5.2.10-122088-OSX.dmg

	c. Alternatively, download and install the software, via this 
	[link](https://www.virtualbox.org/wiki/Downloads "VirtualBox download")

2. Import the DIVAS VM: On your computer, start the VirtualBox application. Then,

	a. In the VirtualBox app, choose File / Import Appliance… from the File menu

	b. In the dialog that appears, browse to the thumb drive, select the 
	Divas2017.ova file, then click Next

	c. Alternatively, dowload the Divas2017.ova file from this 
	[link](https://drive.google.com/file/d/1Q-hxEQVTeoo5YkKQeMD5DYUI-TdpGRm5/view?usp=sharing "Divas2017.ova"), 
	and then browse to the download location, then click Next

	d. On the RAM section of the Appliance Settings dialog, set the amount of RAM to no 
	more than 1/2 of the total RAM on your machine. The default is 4096 MB, which is 1/2 
	of the memory on a computer with 8 GB of RAM.

	e. Click the Import button, and wait for the process to complete. Be patient, as this 
	will take a while to complete

3. Eject the thumb drive

4. Start the VM: 
	a. If the VirtualBox application is not running, start it again

	b. Highlight the Divas2017 VM in the left-hand pane of the VirtualBox application, then 
	click the Start button (the green arrow). The VM will start, and you will automatically be 
	logged in and taken to a blue desktop

5. Install Guest Additions: these will allow the VM to work more seamlessly with your computer


	a. From the VirtualBox menu, choose the Devices / Insert Guest Additions CD image… menu item. 
	The menu will be at the top of the screen, or hidden at the center bottom if the VM is in full 
	screen mode

	b. Click Run on the dialog that pops up

	c. Enter the root password, **Diva2018**, in the next dialog box, and then click Authenticate. 
	A Terminal window will show progress of the installation, which may take a while

	d. When the process is complete, hit Enter to close the Terminal window, and then right click on 
	the CD image on the launcher bar on the left side of the screen, and choose Eject

6. Configure git:

	a. Start the Terminal application 

	b. Enter the following commands, replacing Jane Smith’s information with your own. Include the 
	quotation marks.

	~~~ 
	git config --global user.name "Jane Smith" 

	git config --global user.email "jane.smith@doane.edu" 

	git config --global core.editor "gedit -s" 
	~~~
	{: .bash}

7. Clone the workshop files: 


	a. If it is not already running, start the Terminal application

	b. Enter the following commands

	~~~
	cd ~/Desktop 

	git clone https://bitbucket.org/mmeysenburg/workshops.git 
	~~~
	{: .bash}

