'''
 * Python script demonstrating image modification and creation via 
 * NumPy array slicing.
'''
import cv2

# load and display original image
img = cv2.imread("board.jpg")
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.waitKey(0)

# extract, display, and save sub-image
clip = img[60:150, 135:480, :]
cv2.namedWindow("clip", cv2.WINDOW_NORMAL)
cv2.imshow("clip", clip)
cv2.imwrite("clip.tif", clip)
cv2.waitKey(0)

# replace clipped area with sampled color
c = img[330, 90]
img[60:150, 135:480] = c
cv2.namedWindow("modified", cv2.WINDOW_NORMAL)
cv2.imshow("modified", img)
cv2.waitKey(0)
