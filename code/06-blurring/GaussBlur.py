'''
 * Python script to demonstrate Gaussian blur.
 *
 * usage: python GaussBlur.py <filename> <kernel-size> 
'''
import cv2, sys

# get filename and kernel size from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display original image
image = cv2.imread(filename = filename)
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# apply Gaussian blur, creating a new image
blurred = cv2.GaussianBlur(src = image, 
    ksize = (k, k), sigmaX = 0)

# display blurred image
cv2.namedWindow(winname = "blurred", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "blurred", mat = blurred)
cv2.waitKey(delay = 0)
