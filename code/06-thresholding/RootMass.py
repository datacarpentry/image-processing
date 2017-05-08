'''
 * Python program to determine root mass, as a ratio of pixels in the
 * root system to the number of pixels in the entire image.
 *
 * usage: python RootMass.py <filename> <kernel-size>
'''
import cv2, sys

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read the original image, converting to grayscale
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# blur before thresholding
blur = cv2.GaussianBlur(img, (k, k), 0)

# perform adaptive thresholding to produce a binary image
(t, binary) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + 
	cv2.THRESH_OTSU)

# save binary image; first find beginning of file extension
dot = filename.index(".")
binaryFileName = filename[:dot] + "-binary" + filename[dot:]
cv2.imwrite(binaryFileName, binary)

# determine root mass ratio
rootPixels = cv2.countNonZero(binary)
w = binary.shape[1]
h = binary.shape[0]
density = rootPixels / (w * h)

# output in format suitable for .csv
print(filename, density, sep=",")

