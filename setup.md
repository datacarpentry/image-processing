---
layout: page
title: Setup
permalink: /setup/
---

## Setup instructions for the Image Processing workshop

We are using a virtual Linux machine for this workshop, since the computer 
vision libraries we use can be difficult to install and configure. This 
allows you to run our "standard" computer, regardless of your specific 
Windows, Mac, or Linux computer. The following discussion block contains 
the details regarding our machine and its pre-installed software suite.

> ## Virtual machine details
> 
> * Virtualization software: Oracle VirtualBox.
> 
> * VM operating system: 64-bit Ubuntu 16.04. 
> 
> * Login information: The machine is set to automatically log in to a user 
> account. If needed, the username is **diva** and the associated password 
> is **DoaneDiva16**.
> 
> * Software suite: The machine is pre-configured with the following software:
> 
> | Software                    | Description                                           |
> | :-------------------------- | :-----------------------------------------------------|
> | gcc                         | C / C++ compiler                                      |
> | Geany                       | Lightweight code editor                               |
> | git                         | Source control and versioning tool                    |
> | gnuplot                     |  plotting and graphing application                    |
> | ImageJ                      | Java-based image processing application               |
> | Java JDK 8 and NetBeans IDE | Java development tools                                |
> | Python 3.6.0                | Anaconda 4.3.1 Python distribution                    |
> |                             | - includes numpy, scipy, matplotlib, and scikit-learn |
> |                             | - OpenCV 3.1.0                                        |
> |                             | - mahotas                                             |
> |                             | - Adrian Rosebrock's imutils library                  |
> | R and RStudio               | R development tools                                   | 
{: .discussion}

## Installation

1. Download and install the free Oracle VirtualBox software, via this 
[link](https://www.virtualbox.org/wiki/Downloads "VirtualBox download")

2. Download the DIVAS virtual machine image via this 
[link](https://drive.google.com/file/d/0Bx45j2TRK8WgN0hwUC1RVVQ3WlE/view?usp=sharing)
. This a 6 GB file, so the download will likely take a while.

3. Start your VirtualBox application.

4. Import the image file you downloaded, via the File / Import Appliance 
menu item. Adjust the memory for the virtual machine to be no more than 
one-half of the total memory your physical computer has.

## Running the virtual machine for the first time

1. If it is not already running, start your VirtualBox application.

2. Highlight the DIVAS virtual machine in the left-hand pane.

3. To start the virtual machine the first time, click on the Start button 
(the green arrow). After it starts, the machine will automatically log you 
in and take you to an orange desktop.

4. Install the Guest Additions, which will allow the virtual machine to 
work more seamlessly with your computer. 

	* From the VirtualBox VM Devices menu, choose the Insert Guest 
Additions CD Image... item. You will be asked if you want to run the 
additions; click Run.

	* When prompted, enter the **diva** user password, **DoaneDiva16**, 
and wait until the process is complete (when the terminal says "Press Return 
to close this window...").

	* Hit enter, then eject the CD image by right clicking on the disk 
icon on the left side launcher bar and choosing "Eject," and then restart 
the virtual machine, by clicking on the gear icon in the upper right corner 
and choosing the "Shut Down" item.

5. Set your name and email address for git

	* Open a Terminal window

	* Execute the mygit script, like this (use your own information, 
and make sure to include the quotes):

~~~
mygit "Jane Smith" "jane.smith@mail.com"
~~~
{: .bash}





