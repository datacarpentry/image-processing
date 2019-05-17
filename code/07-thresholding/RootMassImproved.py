'''
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
 * 
 * This version applies thresholding twice, to get rid of the white 
 * circle and label from the image before performing the root mass 
 * ratio calculations. 
 *
 * usage: python RootMassImproved.py <filename> <kernel-size>
'''
import cv2, sys

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read the original image, converting to grayscale
image = cv2.imread(filename = filename, flags = cv2.IMREAD_GRAYSCALE)

# blur before thresholding
blur = cv2.GaussianBlur(src = image, 
    ksize = (k, k), 
    sigmaX = 0)

# WRITE CODE HERE
# perform inverse binary thresholding to create a mask that will remove
# the white circle and label.


# WRITE CODE HERE
# use the mask you just created to remove the circle and label from the
# blur image, saving the result back in the blur variable


# perform adaptive thresholding to produce a binary image
(t, binary) = cv2.threshold(src = blur, 
    thresh = 0, 
    maxval = 255, 
    type = cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# save binary image; first find extension beginning
dot = filename.index(".")
binaryFileName = filename[:dot] + "-binary" + filename[dot:]
cv2.imwrite(filename = binaryFileName, img = binary)

# determine root mass ratio
rootPixels = cv2.countNonZero(src = binary)
w = binary.shape[1]
h = binary.shape[0]
density = rootPixels / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")
