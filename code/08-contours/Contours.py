'''
 * Python program to find the contours in an image.
'''
import cv2, sys, numpy as np

# read command-line arguments
filename = sys.argv[1]

# read original image
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#cv2.imshow("output", img)
#cv2.waitKey(0)

# create binary image
blur = cv2.GaussianBlur(img, (5, 5), 0)
(t, binary) = cv2.threshold(blur, 210, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow("output", binary)
#cv2.waitKey(0)

# find contours
(cImg, contours, hierarchy) = cv2.findContours(binary, cv2.RETR_TREE, 
	cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))

# draw contours 
final = np.zeros(binary.shape, dtype = "uint8")
final = cv2.merge([final, final, final])
cv2.drawContours(final, contours, -1, (255, 0, 0), 3)

cv2.imshow("output", final)
cv2.waitKey(0)
