'''
 * Python script to demonstrate adaptive thresholding using Otsu's method.
 *
 * usage: python AdaptiveThreshold.py <filename> <kernel-size>
'''
import cv2, sys

# get filename and kernel size values from command line
filename = sys.argv[1]
k = int(sys.argv[2])

# read and display the original image
image = cv2.imread(filename = filename)
cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "original", mat = image)
cv2.waitKey(delay = 0)

# blur and grayscale before thresholding
blur = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(
    src = blur, 
    ksize = (k, k), 
    sigmaX = 0)

# perform adaptive thresholding 
(t, maskLayer) = cv2.threshold(src = blur, 
    thresh = 0, 
    maxval = 255, 
    type = cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# make a mask suitable for color images
mask = cv2.merge(mv = [maskLayer, maskLayer, maskLayer])

cv2.namedWindow(winname = "mask", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "mask", mat = mask)
cv2.waitKey(delay = 0)

# use the mask to select the "interesting" part of the image
sel = cv2.bitwise_and(src1 = image, src2 = mask)

# display the result
cv2.namedWindow(winname = "selected", flags = cv2.WINDOW_NORMAL)
cv2.imshow(winname = "selected", mat = sel)
cv2.waitKey(delay = 0)
