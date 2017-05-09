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
img = cv2.imread(filename)

# create binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)

# find contours
(_, contours, hierarchy) = cv2.findContours(binary, cv2.RETR_TREE, 
    cv2.CHAIN_APPROX_SIMPLE)

# Count the number of pips on the dice faces.
# Iterate through hierarchy[0], first to find the indices of dice
# contours, then again to find pip contours.
# WRITE YOUR CODE HERE
