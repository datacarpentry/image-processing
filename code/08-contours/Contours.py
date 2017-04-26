'''
 * Python program to find the contours in an image.
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]

# read original image
img = cv2.imread(filename)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#cv2.imshow("output", img)
#cv2.waitKey(0)

# create binary image
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (5, 5), 0)
(t, binary) = cv2.threshold(blur, 210, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow("output", binary)
#cv2.waitKey(0)

# find contours
(cImg, contours, hierarchy) = cv2.findContours(binary, cv2.RETR_TREE, 
	cv2.CHAIN_APPROX_SIMPLE)

i = 0
print("Found %d contours." % len(contours))
for c in contours:
	print("\tSize of contour %d: %d" % (i, len(c)))
	i += 1

# draw contours 
for c in contours:
	if len(c) > 100:
		cv2.drawContours(img, c, -1, (0, 0, 255), 3)

cv2.imshow("output", img)
cv2.waitKey(0)
