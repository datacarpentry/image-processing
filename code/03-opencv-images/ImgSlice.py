'''
 * Python script demonstrating image modification and creation via 
 * NumPy array slicing.
'''
import cv2

# load and display original image
image = cv2.imread(filename = "board.jpg")
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# extract, display, and save sub-image
clip = image[60:151, 135:481, :]
cv2.namedWindow(winname = "clip", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "clip", mat = clip)
cv2.imwrite(filename = "clip.tif", img = clip)
cv2.waitKey(delay = 0)

# replace clipped area with sampled color
c = image[330, 90]
image[60:151, 135:481] = c
cv2.namedWindow(winname = "modified", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "modified", mat = image)
cv2.waitKey(delay = 0)
