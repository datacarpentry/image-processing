# solution to summer 2018 DIVAS colorimetric workshop challenge
#
# Mark M. Meysenburg
# 5/8/2018
import cv2
from matplotlib import pyplot as plt
import numpy as np
import sys

# video object
vid = cv2.VideoCapture(sys.argv[1])

# file object
outFile = open("titration_rgb.csv", "w")

# lists for mean color values for each channel
reds = []
greens = []
blues = []

# frame counter
i = 0

# priming read
(success, image) = vid.read()

# continue while we have frames to read
while success:
    # add average channel value to each list
    redAvg = np.mean(image[218:227, 350:359, 2])
    reds.append(redAvg)
    greenAvg = np.mean(image[218:227, 350:359, 1])
    greens.append(greenAvg)
    blueAvg = np.mean(image[218:227, 350:359, 0])
    blues.append(blueAvg)

    outFile.write('%d,%0.4f,%0.4f,%0.4f\n' % (i, redAvg, greenAvg, blueAvg))
    # move on to the next frame
    i += 1
    (success, image) = vid.read()

# close output file
outFile.close()

# configure, save, and show the plot
plt.ylim([0, 256])
plt.xlabel('Frame')
plt.ylabel('Channel Value')
plt.plot(reds, 'red')
plt.plot(greens, 'green')
plt.plot(blues, 'blue')
plt.savefig('colorimetric.png', dpi=150)
plt.show()
