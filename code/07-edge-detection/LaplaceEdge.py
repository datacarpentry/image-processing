'''
 * Python script to demonstrate Laplace edge detection.
'''
import cv2, sys, numpy as np

# load and display original image
img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
k = int(sys.argv[2])
t = int(sys.argv[3])

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

blur = cv2.GaussianBlur(img, (k, k), 0)
(t, mask) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY_INV)

edge = cv2.Laplacian(mask, cv2.CV_64F)
edge = np.uint8(np.absolute(edge))

cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
cv2.imshow("edges", edge)
cv2.waitKey(0)
