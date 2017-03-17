'''
 * Python program to open, display, and save an image.
 *
'''
import cv2

# read image 
img = cv2.imread("chair.jpg")

# display image and wait for keypress, using a resizable window
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)

# save a new version in .tif format
cv2.imwrite("chair.tif", img)
