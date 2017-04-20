'''
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
'''
import cv2, sys, numpy as np

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read the original image, converting to grayscale
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# blur before thresholding
blur = cv2.GaussianBlur(img, (k, k), 0)

# perform thresholding the first time to produce a mask
(t, maskLayer) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + 
	cv2.THRESH_OTSU)

# save maskLayer; first find extension beginning
dot = filename.index(".")
maskFileName = filename[:dot] + "-mask" + filename[dot:]
cv2.imwrite(maskFileName, maskLayer)

# determine root mass ratio
rootPixels = cv2.countNonZero(maskLayer)
w = maskLayer.shape[0]
h = maskLayer.shape[1]
density = rootPixels / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
