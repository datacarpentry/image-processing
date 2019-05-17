'''
 * Python program to open, display, and save an image.
 *
'''
import cv2

# read image 
image = cv2.imread(filename = "chair.jpg")

# display image and wait for keypress, using a resizable window
cv2.namedWindow(winname = "image", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "image", mat = image)
cv2.waitKey(delay = 0)

# save a new version in .tif format
cv2.imwrite(filename = "chair.tif", img = image)
