'''
 * Python script to demonstrate simple thresholding.
'''
import cv2, sys

# get filename, kernel size, and threshold value from command line
filename = sys.argv[1]
k = int(sys.argv[2])
t = int(sys.argv[3])

# read and display the original image
img = cv2.imread(filename)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# blur image before thresholding
blur = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(blur, (k, k), 0)

# perform binary thresholding 
(t, maskLayer) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

# make a mask suitable for color images
mask = cv2.merge([maskLayer, maskLayer, maskLayer])

cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
cv2.waitKey(0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(img, mask)

# display the result
cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
cv2.imshow("selected", sel)
cv2.waitKey(0)
