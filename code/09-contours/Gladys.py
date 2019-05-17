'''
 * Python program to use contours to count the pips on the dice faces.
 *
 * usage: python Gladys.py <filename> <threshold>
'''
import cv2, sys

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
image = cv2.imread(filename = filename)

# create binary image
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)

(t, binary) = cv2.threshold(src = blur, 
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY)

# find contours
(_, contours, hierarchy) = cv2.findContours(image = binary, 
    mode = cv2.RETR_TREE, 
    method = cv2.CHAIN_APPROX_SIMPLE)

# Count the number of pips on the dice faces.
# Iterate through hierarchy[0], first to find the indices of dice
# contours, then again to find pip contours.
# WRITE YOUR CODE HERE
